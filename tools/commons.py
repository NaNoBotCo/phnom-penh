# -*- coding: utf-8 -*-
"""commons.py — Wikimedia Commons pictures for the site, picked by hand.

    python3 tools/commons.py search   -> cache/commons/_triage.json + contact sheets in cache/commons/sheets/
    python3 tools/commons.py fetch    -> data/photos/<slug>.jpg (1800px) for data/photos/picks.json,
                                         credits in data/photos/credits.json

Lifted from laila-chiang-rai/tools/commons.py. Free licences only: CC0, PD, CC BY, CC BY-SA.
"""
import io, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache" / "commons"
OUT = ROOT / "data" / "photos"
UA = "phnom-penh-build/0.2 (https://motdang.net; nan@motdang.net) python-urllib"
API = "https://commons.wikimedia.org/w/api.php"
FREE = re.compile(r"^(cc0|pd|public.domain|cc.by(.sa)?(.[1-4]\.[0-9])?)", re.I)

TOPICS = {
 # landmarks
 "royal-palace": "Royal Palace Phnom Penh",
 "throne-hall": "Throne Hall Phnom Penh",
 "silver-pagoda": "Silver Pagoda Phnom Penh",
 "national-museum": "National Museum of Cambodia",
 "wat-phnom": "Wat Phnom",
 "independence": "Independence Monument Phnom Penh",
 "central-market": "Phsar Thmei Central Market Phnom Penh",
 "russian-market": "Russian Market Phnom Penh",
 "wat-ounalom": "Wat Ounalom",
 "wat-langka": "Wat Langka Phnom Penh",
 "wat-botum": "Wat Botum Phnom Penh",
 "riverside": "Sisowath Quay Phnom Penh",
 "koh-pich": "Koh Pich Phnom Penh",
 "chroy-changvar": "Chroy Changvar bridge Phnom Penh",
 "olympic": "Olympic Stadium Phnom Penh Vann Molyvann",
 "railway": "Phnom Penh railway station",
 "post-office": "Phnom Penh post office",
 "le-royal": "Hotel Le Royal Phnom Penh",
 "mosque": "Nur ul-Ihsan mosque Phnom Penh",
 "chaktomuk": "Chaktomuk Phnom Penh",
 "sihanouk-memorial": "Norodom Sihanouk statue Phnom Penh",
 "wat-moha-montrey": "Wat Moha Montrey",
 "orussey": "Orussey market",
 "night-market": "Phnom Penh night market",
 # life
 "tuk-tuk": "tuk-tuk Phnom Penh",
 "remork": "remork Phnom Penh",
 "skyline": "Phnom Penh skyline",
 "skyline-night": "Phnom Penh night",
 "sunset": "Phnom Penh sunset",
 "mekong": "Mekong Phnom Penh",
 "tonle-sap": "Tonle Sap river Phnom Penh",
 "water-festival": "Bon Om Touk Phnom Penh",
 "boat-race": "Water Festival boat race Phnom Penh",
 "monks": "monks Phnom Penh",
 "apsara": "Apsara dance Phnom Penh",
 "lotus": "lotus Cambodia",
 "amok": "fish amok",
 "khmer-food": "Cambodian cuisine",
 "num-banh-chok": "Num banh chok",
 "street-food": "street food Phnom Penh",
 "coffee": "Cambodian iced coffee",
 "fruit": "fruit market Phnom Penh",
 "pharmacy": "pharmacy Phnom Penh",
 "market-stall": "market Phnom Penh",
 "spa": "Cambodia massage",
 "gold": "gold shop Phnom Penh",
 "motorbike": "motorbike Phnom Penh street",
 "boulevard": "Norodom Boulevard Phnom Penh",
 "buddha": "Buddha Phnom Penh pagoda",
 "naga": "naga Phnom Penh",
 "hotel": "hotel Phnom Penh",
 "bar": "bar Phnom Penh",
 "cyclo": "cyclo Phnom Penh",
}


def api(params):
    params = dict(params, format="json")
    req = urllib.request.Request(API, data=urllib.parse.urlencode(params).encode(), headers={"User-Agent": UA})
    err = None
    for i in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except Exception as e:
            err = e; time.sleep(2 + 3 * i)
    raise RuntimeError(err)


def strip(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()


def info(titles, width):
    out = []
    for i in range(0, len(titles), 20):
        d = api({"action": "query", "prop": "imageinfo", "iiprop": "url|size|extmetadata|mime",
                 "iiurlwidth": width, "titles": "|".join(titles[i:i + 20])})
        for p in d.get("query", {}).get("pages", {}).values():
            ii = (p.get("imageinfo") or [{}])[0]; m = ii.get("extmetadata", {})
            out.append({"title": p.get("title"), "w": ii.get("width"), "h": ii.get("height"),
                        "mime": ii.get("mime"), "thumb": ii.get("thumburl"), "page": ii.get("descriptionurl"),
                        "licence": (m.get("LicenseShortName", {}).get("value") or ""),
                        "licence_url": m.get("LicenseUrl", {}).get("value", ""),
                        "author": strip(m.get("Artist", {}).get("value"))[:120],
                        "desc": strip(m.get("ImageDescription", {}).get("value"))[:200]})
    return out


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    for i in range(4):
        try:
            return urllib.request.urlopen(req, timeout=120).read()
        except Exception:
            time.sleep(3 + 5 * i)
    raise RuntimeError(url)


def sheet(slug, rows):
    from PIL import Image, ImageDraw
    W, H, C = 300, 200, 4
    n = len(rows)
    if not n:
        return
    im = Image.new("RGB", (W * C, (H + 18) * ((n + C - 1) // C)), "white")
    dr = ImageDraw.Draw(im)
    for i, r in enumerate(rows):
        try:
            t = Image.open(io.BytesIO(get(r["small"]))).convert("RGB")
        except Exception:
            continue
        t.thumbnail((W, H))
        x, y = (i % C) * W, (i // C) * (H + 18)
        im.paste(t, (x, y))
        dr.text((x + 3, y + H + 2), f"{i} {r['licence'][:14]}", fill="black")
        time.sleep(0.2)
    (CACHE / "sheets").mkdir(parents=True, exist_ok=True)
    im.save(CACHE / "sheets" / f"{slug}.jpg", quality=80)


def one(k, q):
        d = api({"action": "query", "list": "search", "srnamespace": 6, "srsearch": q, "srlimit": 40})
        titles = [x["title"] for x in d.get("query", {}).get("search", [])]
        rows = [r for r in info(titles, 300) if r["mime"] == "image/jpeg"
                and FREE.match(r["licence"].replace(" ", "-"))
                and (r["w"] or 0) >= 1400 and (r["w"] or 0) >= (r["h"] or 1) * 1.15][:16]
        for r in rows:
            r["small"] = r.pop("thumb")
        (CACHE / "triage").mkdir(parents=True, exist_ok=True)
        (CACHE / "triage" / f"{k}.json").write_text(json.dumps(rows, ensure_ascii=False, indent=1))
        print(k, len(titles), len(rows), file=sys.stderr, flush=True)
        sheet(k, rows)


def search(only=None):
    from concurrent.futures import ThreadPoolExecutor
    todo = [(k, q) for k, q in TOPICS.items()
            if (k in only if only else not (CACHE / "sheets" / f"{k}.jpg").exists())]
    with ThreadPoolExecutor(5) as ex:
        def safe(kq):
            try:
                one(*kq)
            except Exception as e:
                print(kq[0], "failed:", e, file=sys.stderr, flush=True)
        list(ex.map(safe, todo))


def load_triage():
    return {f.stem: json.loads(f.read_text()) for f in (CACHE / "triage").glob("*.json")}


def fetch():
    picks = json.loads((OUT / "picks.json").read_text())
    tri = load_triage()
    credits = {}
    for slug, (topic, i) in picks.items():
        r = tri[topic][i]
        f = OUT / f"{slug}.jpg"
        if not f.exists():
            big = info([r["title"]], 1800)[0]
            f.write_bytes(get(big["thumb"]))
            time.sleep(0.4)
        credits[slug] = {k: r[k] for k in ("title", "page", "licence", "licence_url", "author", "desc")}
    (OUT / "credits.json").write_text(json.dumps(credits, ensure_ascii=False, indent=1))
    print(len(credits), "photos")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "search":
        search(set(sys.argv[2:]) or None)
    else:
        fetch()
