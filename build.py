#!/usr/bin/env python3
"""Emit docs/index.html — one self-contained file, payload and all."""
import json, re, gzip
from pathlib import Path

ROOT = Path(__file__).resolve().parent
B36 = "0123456789abcdefghijklmnopqrstuvwxyz"
LAT0, LNG0 = 11.30, 104.60
TAB = "\t"


def b36(n):
    n = int(n)
    if n == 0:
        return "0"
    s = ""
    while n:
        s = B36[n % 36] + s
        n //= 36
    return s


def clean(s):
    # 80 rows arrive from Overture already carrying U+FFFD — a byte Meta lost
    # upstream, not a character. It says nothing, so it goes.
    s = re.sub(r"[\t\n\r]+", " ", s or "").replace("\ufffd", "")
    return re.sub(r"\s{2,}", " ", s).strip(" ,.")


# The harvest box (importers/harvest_overture.py BBOX). Latitude 11 and
# longitude 104 cannot trade places inside it, so a swapped pair fails here too.
# The south-west corner must also sit north-east of LAT0/LNG0: offsets are
# unsigned base-36.
BOX_S, BOX_W, BOX_N, BOX_E = 11.35, 104.70, 11.80, 105.10
assert LAT0 <= BOX_S and LNG0 <= BOX_W


def check_pins(rows):
    bad = [(r[0], r[3], r[4]) for r in rows
           if not (BOX_S <= r[3] <= BOX_N and BOX_W <= r[4] <= BOX_E)]
    if bad:
        raise SystemExit(f"{len(bad)} pin(s) outside Phnom Penh or lat/lng swapped, e.g. {bad[:5]}")


def check_basemap(bm):
    s, w, n, e = bm["box"]
    if not (BOX_S - 0.1 <= s < n <= BOX_N + 0.1 and BOX_W - 0.1 <= w < e <= BOX_E + 0.1):
        raise SystemExit(f"basemap box {bm['box']} is not Phnom Penh (s, w, n, e)")
    if not bm["water"] or not bm["major"]:
        raise SystemExit("basemap has no water or no major roads: rerun importers/harvest_osm.py")


def main():
    d = json.loads((ROOT / "data" / "pp.json").read_text())
    cats, khan, meta = d["cats"], d["khan"], d["meta"]
    check_pins(d["rows"])
    bm = json.loads((ROOT / "data" / "basemap.json").read_text())
    check_basemap(bm)
    lines = []
    for name, cat, kh, lat, lng, phone, fb, addr, conf, web in d["rows"]:
        lines.append(TAB.join([
            clean(name),
            b36(cat) if cat >= 0 else "",
            b36(kh) if kh >= 0 else "",
            b36(round((lat - LAT0) * 1e5)),
            b36(round((lng - LNG0) * 1e5)),
            phone[1:] if phone.startswith("0") else phone,
            fb,
            clean(addr),
            b36(conf),
            "1" if web else "",
        ]))
    blob = "\n".join(lines)
    # The payload rides in a text/plain script tag, so the one sequence that
    # would end it early must not be in the data.
    assert "</script" not in blob.lower(), "a name would close the script tag"

    tmpl = (ROOT / "page.html").read_text()
    html = (tmpl
            .replace("__CATS__", json.dumps(cats, ensure_ascii=False, separators=(",", ":")))
            .replace("__KHAN__", json.dumps(khan, ensure_ascii=False, separators=(",", ":")))
            .replace("__META__", json.dumps(meta, ensure_ascii=False, separators=(",", ":")))
            .replace("__BASEMAP__", json.dumps(bm, separators=(",", ":")))
            .replace("__N__", "{:,}".format(len(lines)))
            .replace("__BLOB__", blob))
    out = ROOT / "docs" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html)
    print("wrote", out, out.stat().st_size // 1024, "kB",
          "| gzipped", len(gzip.compress(html.encode())) // 1024, "kB")


if __name__ == "__main__":
    main()
