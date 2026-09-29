#!/usr/bin/env python3
"""Turn the Overture cache into the compact payload the page reads.

The shape is mot-dang's: a record is a place, not a link, so the row carries
the phone, the district and the point. Everything is kept — a low-confidence
row is shown with its number, never dropped, because the reader filters, not
the builder.
"""
import gzip, json, re, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "cache" / "overture" / "pp.jsonl.gz"

# Confirmed against the data twice: locality naming a khan, and khan names
# written into the address. 1213 (Boeng Keng Kang) and 1214 (Kamboul) were
# carved out of 1201 and 1209 in 2019 and the rows still carry the parent
# code, so they are not separable here and are not claimed.
KHAN = [
    ("1201", "ចំការមន",       "Chamkar Mon"),
    ("1202", "ដូនពេញ",        "Daun Penh"),
    ("1203", "ប្រាំពីរមករា",  "Prampi Makara"),
    ("1204", "ទួលគោក",        "Tuol Kouk"),
    ("1205", "ដង្កោ",         "Dangkao"),
    ("1206", "មានជ័យ",        "Mean Chey"),
    ("1207", "ឫស្សីកែវ",      "Russey Keo"),
    ("1208", "សែនសុខ",        "Sen Sok"),
    ("1209", "ពោធិ៍សែនជ័យ",   "Pou Senchey"),
    ("1210", "ជ្រោយចង្វារ",   "Chroy Changvar"),
    ("1211", "ព្រែកព្នៅ",     "Prek Pnov"),
    ("1212", "ច្បារអំពៅ",     "Chbar Ampov"),
]
KHAN_BY_PC = {pc: i for i, (pc, _, _) in enumerate(KHAN)}

# Overture's category slugs, given a Khmer and an English label. Only the ones
# the city actually carries get a shelf; the rest fall to their parent word.
def label(slug):
    return slug.replace("_", " ")

def khmer_re(s):
    return bool(re.search(r"[ក-៿]", s or ""))

def fb_id(socials):
    for s in socials or []:
        m = re.search(r"facebook\.com/(?:profile\.php\?id=)?([0-9A-Za-z.\-_]+)", s)
        if m:
            return m.group(1)
    return ""

def local_phone(p):
    if not p:
        return ""
    p = re.sub(r"[^\d+]", "", p)
    if p.startswith("+855"):
        return "0" + p[4:]
    if p.startswith("855") and len(p) > 9:
        return "0" + p[3:]
    return p

def clean_addr(a):
    if not a:
        return ""
    a = re.sub(r"\s+", " ", a).strip(" ,")
    # Meta pads with the city and country over and over; the reader is in the
    # city already.
    for junk in ("Phnom Penh, Cambodia", "Phnom Penh", "Cambodia", "cambobia",
                 "ភ្នំពេញ", "កម្ពុជា"):
        a = re.sub(r"(?i),?\s*" + re.escape(junk) + r"\s*,?", ", ", a)
    a = re.sub(r"[\s,]+", " ", a).strip(" ,")
    if len(a) < 3 or a.isdigit():
        return ""
    return a[:70]

def main():
    rows = [json.loads(l) for l in gzip.open(SRC, "rt", encoding="utf-8")]
    cats = collections.Counter(r["cat"] for r in rows if r.get("cat"))
    catlist = [c for c, _ in cats.most_common()]
    cat_ix = {c: i for i, c in enumerate(catlist)}

    out, seen = [], set()
    for r in rows:
        name = (r.get("name") or "").strip()
        if not name:
            continue
        key = (name.lower(), round(r["lat"], 4), round(r["lng"], 4))
        if key in seen:                       # Meta ships the same shop twice
            continue
        seen.add(key)
        pc = str(r.get("postcode") or "")[:4]
        out.append([
            name,
            cat_ix.get(r.get("cat"), -1),
            KHAN_BY_PC.get(pc, -1),
            round(r["lat"], 5),
            round(r["lng"], 5),
            local_phone(r.get("phone")),
            fb_id(r.get("socials")),
            clean_addr(r.get("address")),
            int(round((r.get("confidence") or 0) * 100)),
            1 if r.get("website") else 0,
            r["id"],                          # Overture GERS id: the join key for a Grab POI match
        ])
    out.sort(key=lambda x: -x[8])
    print("records", len(out), "of", len(rows), "( %d duplicates dropped )" % (len(rows) - len(out)))
    print("khmer-named", sum(1 for o in out if khmer_re(o[0])))
    print("with phone", sum(1 for o in out if o[5]))
    print("with fb", sum(1 for o in out if o[6]))
    print("with district", sum(1 for o in out if o[2] >= 0))
    print("with address", sum(1 for o in out if o[7]))
    print("categories", len(catlist))
    payload = {
        "cats": catlist,
        "khan": [[k[1], k[2]] for k in KHAN],
        "rows": out,
        "meta": json.loads((ROOT / "cache" / "overture" / "manifest.json").read_text()),
    }
    p = ROOT / "data" / "pp.json"
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
    print("payload", p.stat().st_size // 1024, "kB")

if __name__ == "__main__":
    main()
