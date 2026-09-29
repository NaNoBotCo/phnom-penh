#!/usr/bin/env python3
"""Psar Phnom Penh — the whole site from the files in data/.

    python3 tools/build.py

Reads   data/pp.json (Overture places)  data/basemap.json + data/basemap_core.json (OSM)
        data/landmarks.json  data/soon.json  data/photos/  data/routes/loop.json
Writes  docs/index.html  docs/data/*.js  docs/img/  docs/card.jpg

The data files load as <script src>, not fetch(), so the page also works opened
straight from disk (file://).
"""
import gzip, json, math, os, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from shelves import SHELVES, shelf_of, public as shelves_public  # noqa: E402

DOCS = ROOT / "docs"
B36 = "0123456789abcdefghijklmnopqrstuvwxyz"
LAT0, LNG0 = 11.30, 104.60
BOX_S, BOX_W, BOX_N, BOX_E = 11.35, 104.70, 11.80, 105.10
SITE = "Psar Phnom Penh"
SITE_URL = os.environ.get("SITE_URL", "https://nanobotco.github.io/phnom-penh/")


def b36(n):
    n = int(n)
    if n <= 0:
        return "0"
    s = ""
    while n:
        s = B36[n % 36] + s
        n //= 36
    return s


def clean(s):
    # 80 rows arrive from Overture already carrying U+FFFD, a byte lost upstream.
    s = re.sub(r"[\t\n\r]+", " ", s or "").replace("�", "")
    return re.sub(r"\s{2,}", " ", s).strip(" ,.")


# A row with no category still says what it is in its name often enough to shelve.
NAME_SHELF = [
    ("wat", r"^(វត្ត|wat\s|pagoda)"),
    ("coffee", r"(កាហ្វេ|coffee|café|\bcafe\b)"),
    ("health", r"(ឱសថស្ថាន|pharmacy|មន្ទីរពេទ្យ|clinic|គ្លីនិក)"),
    ("stay", r"(សណ្ឋាគារ|ផ្ទះសំណាក់|\bhotel\b|guest ?house|hostel)"),
    ("mart", r"^(ផ្សារ|psar|phsar)|mart\b|mini ?mart|supermarket"),
    ("food", r"(ភោជនីយដ្ឋាន|restaurant|ហាងបាយ|គុយទាវ|noodle)"),
    ("spa", r"(ម៉ាស្សា|massage|\bspa\b|salon|ហាងកាត់សក់)"),
]
SHELF_IX = {s[0]: i for i, s in enumerate(SHELVES)}


def shelf_for(name, slug):
    i = shelf_of(slug)
    if i >= 0 and not (slug == "landmark_and_historical_building"):
        return i
    low = name.lower()
    for sid, rx in NAME_SHELF:
        if re.search(rx, low):
            return SHELF_IX[sid]
    return i


def check_pins(rows):
    bad = [(r[0], r[3], r[4]) for r in rows
           if not (BOX_S <= r[3] <= BOX_N and BOX_W <= r[4] <= BOX_E)]
    if bad:
        raise SystemExit(f"{len(bad)} pin(s) outside Phnom Penh or lat/lng swapped, e.g. {bad[:5]}")


def js_assign(name, obj):
    return f"window.{name}=" + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + ";\n"


# ---------- photos ----------

def photos():
    from PIL import Image
    src = ROOT / "data" / "photos"
    credits = json.loads((src / "credits.json").read_text())
    out = DOCS / "img"
    (out / "t").mkdir(parents=True, exist_ok=True)
    for slug in credits:
        f = src / f"{slug}.jpg"
        big, small = out / f"{slug}.jpg", out / "t" / f"{slug}.jpg"
        if big.exists() and small.exists() and big.stat().st_mtime > f.stat().st_mtime:
            continue
        im = Image.open(f).convert("RGB")
        a = im.copy(); a.thumbnail((1600, 1600)); a.save(big, quality=72, optimize=True, progressive=True)
        b = im.copy(); b.thumbnail((560, 560)); b.save(small, quality=70, optimize=True, progressive=True)
    for c in credits.values():
        c["author"] = re.sub(r"\s+", " ", c["author"]).strip()
        c.pop("desc", None)
    return credits


# ---------- the river loop, drawn at build time ----------

def loop_svg(landmarks, base):
    route = json.loads((ROOT / "data" / "routes" / "loop.json").read_text())["routes"][0]
    stops = ["wat-phnom", "post-office", "wat-ounalom", "national-museum", "royal-palace",
             "independence", "wat-langka", "russian-market", "central-market"]
    L = {l["id"]: l for l in landmarks}
    # Gate: each stop snapped to the road within 250 m (compound centroids sit inside their walls).
    wp = json.loads((ROOT / "data" / "routes" / "loop.json").read_text())["waypoints"]
    far = [(stops[i % len(stops)], round(w["distance"])) for i, w in enumerate(wp) if w["distance"] > 250]
    if far:
        raise SystemExit(f"loop stop(s) snapped too far from the road: {far}")
    pts = route["geometry"]["coordinates"]
    lons = [p[0] for p in pts]; lats = [p[1] for p in pts]
    pad = 0.006
    w0, e0, s0, n0 = min(lons) - pad, max(lons) + pad, min(lats) - pad, max(lats) + pad
    kx = math.cos(math.radians(11.56))
    W = 640
    sc = W / ((e0 - w0) * kx)
    H = round((n0 - s0) * sc)
    X = lambda lng: (lng - w0) * kx * sc
    Y = lambda lat: (n0 - lat) * sc

    def dec(a, lat0, lng0, q):
        out, x, y = [], 0, 0
        for i in range(0, len(a), 2):
            x += a[i]; y += a[i + 1]
            out.append((lng0 + x / q, lat0 + y / q))
        return out

    def path(pl, close):
        d = "M" + " L".join(f"{X(p[0]):.1f},{Y(p[1]):.1f}" for p in pl)
        return d + ("Z" if close else "")

    def path(pl, close, _p=path):
        # whole pixels: the street layer alone is thousands of runs
        d = "M" + " L".join(f"{X(p[0]):.0f},{Y(p[1]):.0f}" for p in pl)
        return d + ("Z" if close else "")

    def near(pl):
        return any(w0 - .004 <= p[0] <= e0 + .004 and s0 - .004 <= p[1] <= n0 + .004 for p in pl)

    q, lat0, lng0 = base["q"], base["box"][0], base["box"][1]
    water = [dec(a, lat0, lng0, q) for a in base["water"]]
    major = [dec(a, lat0, lng0, q) for a in base["major"]]
    minor = [dec(a, lat0, lng0, q) for a in base["minor"]]
    core = json.loads((ROOT / "data" / "basemap_core.json").read_text())
    streets = [dec(a, core["box"][0], core["box"][1], core["q"]) for a in core["streets"]]
    parts = [f'<svg class="loopmap" viewBox="0 0 {W} {H}" role="img" aria-labelledby="loop-h">',
             f'<defs><clipPath id="lc"><rect width="{W}" height="{H}" rx="18"/></clipPath>'
             '<filter id="glow" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="3"/></filter></defs>',
             '<g clip-path="url(#lc)"><rect class="lm-bg" width="100%" height="100%"/>',
             '<path class="lm-water" fill-rule="nonzero" d="' + "".join(path(r, True) for r in water if near(r)) + '"/>',
             '<path class="lm-street" d="' + "".join(path(l, False) for l in streets if near(l)) + '"/>',
             '<path class="lm-minor" d="' + "".join(path(l, False) for l in minor if near(l)) + '"/>',
             '<path class="lm-major" d="' + "".join(path(l, False) for l in major if near(l)) + '"/>']
    rd = path(pts, False)
    parts.append(f'<path class="lm-route-glow" d="{rd}" filter="url(#glow)"/>')
    parts.append(f'<path class="lm-route" pathLength="1000" d="{rd}"/>')
    for i, sid in enumerate(stops):
        l = L[sid]
        cx, cy = X(l["lng"]), Y(l["lat"])
        parts.append(f'<a href="#/l/{sid}" class="lm-stop"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="11"/>'
                     f'<text x="{cx:.1f}" y="{cy + 4:.1f}">{i + 1}</text><title>{l["en"]}</title></a>')
    parts.append("</g></svg>")
    legs = [{"m": round(l["distance"]), "s": round(l["duration"])} for l in route["legs"]]
    return "".join(parts), {"stops": stops, "m": round(route["distance"]), "s": round(route["duration"]), "legs": legs}


# ---------- share card ----------

def pango_png(text, font, color):
    """Khmer and Thai need real shaping, which this PIL lacks (no raqm); Pango has it."""
    import os, subprocess, tempfile
    from PIL import Image
    ttf = ROOT / "tools" / "ttf"
    with tempfile.TemporaryDirectory() as t:
        src, out = Path(t) / "t.txt", Path(t) / "t.png"
        src.write_text(text)
        conf = Path(t) / "fonts.conf"
        conf.write_text(f'<?xml version="1.0"?><fontconfig><dir>{ttf}</dir>'
                        '<include ignore_missing="yes">/opt/homebrew/etc/fonts/fonts.conf</include>'
                        f'<cachedir>{t}/fc</cachedir></fontconfig>')
        env = dict(os.environ, PANGOCAIRO_BACKEND="fc", LC_ALL="en_US.UTF-8", FONTCONFIG_FILE=str(conf))
        subprocess.run(["pango-view", f"--font={font}", "--background=transparent", f"--foreground={color}",
                        "-q", "--margin=0", "-o", str(out), str(src)], env=env, check=True)
        return Image.open(out).convert("RGBA")


def card(credits):
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    import random
    W, H = 1200, 630
    im = Image.open(ROOT / "data" / "photos" / "hero-dusk.jpg").convert("RGB")
    r = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)))
    x0 = max(0, im.width - W)          # keep the naga fountain on the right
    im = im.crop((x0, (im.height - H) // 2, x0 + W, (im.height - H) // 2 + H))
    scrim = Image.new("L", (W, H))
    d = ImageDraw.Draw(scrim)
    for x in range(W):
        d.line([(x, 0), (x, H)], fill=int(236 * max(0, 1 - x / (W * .72)) ** 1.1))
    im = Image.composite(Image.new("RGB", (W, H), (13, 11, 31)), im, scrim).convert("RGBA")
    random.seed(7)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    g = ImageDraw.Draw(glow)
    for _ in range(90):
        x, y, s = random.randint(0, W), random.randint(0, H), random.choice([1, 1, 2, 3])
        g.ellipse([x - s, y - s, x + s, y + s], fill=(255, 220, 140, random.randint(90, 220)))
    im.alpha_composite(glow.filter(ImageFilter.GaussianBlur(1.2)))
    F = ROOT / "tools" / "ttf"
    corm = ImageFont.truetype(str(F / "CormorantGaramond-SemiBold.ttf"), 66)
    small = ImageFont.truetype(str(F / "NotoSansThai-Regular.ttf"), 25)
    dr = ImageDraw.Draw(im)
    dr.ellipse([72, 70, 90, 88], fill=(240, 192, 90))
    dr.text((104, 62), "PSAR PHNOM PENH", font=small, fill=(243, 238, 226))
    wm = pango_png("ភ្នំពេញ", "Moul 84", "#f0c05a")
    im.alpha_composite(wm, (66, 118))
    dr.text((72, 118 + wm.height + 6), "Phnom Penh, near and now", font=corm, fill=(255, 255, 255))
    th = pango_png("พนมเปญ ใกล้ตัว ตอนนี้", "Noto Sans Thai SemiBold 25", "#f3eee2")
    im.alpha_composite(th, (74, 118 + wm.height + 92))
    dr.text((74, 556), "73,337 places · 20 landmarks · EN · ไทย · Khmer", font=small, fill=(210, 204, 228))
    im.convert("RGB").save(DOCS / "card.jpg", quality=86)


# ---------- trip page ----------

def trip_content_boot(TC):
    order = ["VISA", "AIR", "FLY", "STAY", "PRICE_SEC", "NAGA", "SPIRITS", "HEALTH", "EAT"]  # HEALTH id "teeth"
    secs = [getattr(TC, k) for k in order if hasattr(TC, k)]
    t = TC.t
    return {"band": "tuk-tuk-night", "rates": TC.RATES, "cities": TC.CITIES, "words": TC.WORDS,
            "prices": TC.PRICES, "picks": TC.PICKS, "sections": secs,
            "kicker": t("Chiang Mai → Phnom Penh", "เชียงใหม่ → พนมเปญ", "ឈៀងម៉ៃ → ភ្នំពេញ"),
            "title": t("Coming from Thailand", "มาจากเมืองไทย", "មកពីប្រទេសថៃ"),
            "lede": t("Visas, the new airport, flights, how long to stay, Siem Reap or not, prices against Chiang Mai, and what is not the same.",
                      "วีซ่า สนามบินใหม่ เที่ยวบิน อยู่กี่วัน ไปเสียมราฐไหม ราคาเทียบเชียงใหม่ และสิ่งที่ไม่เหมือนกัน",
                      "ទិដ្ឋាការ ព្រលានយន្តហោះថ្មី ជើងហោះ ស្នាក់ប៉ុន្មានថ្ងៃ ទៅសៀមរាបឬទេ តម្លៃធៀបឈៀងម៉ៃ និងអ្វីដែលមិនដូចគ្នា។"),
            "asof": t("Checked 29 September 2026. Rules and prices move; the links go to the sources.",
                      "ตรวจเมื่อ 29 กันยายน 2569 กฎและราคาเปลี่ยนได้ ลิงก์พาไปที่มา",
                      "ពិនិត្យថ្ងៃទី 29 កញ្ញា 2026។ ច្បាប់ និងតម្លៃអាចប្ដូរ តំណនាំទៅប្រភព។")}


# ---------- main ----------

def main():
    d = json.loads((ROOT / "data" / "pp.json").read_text())
    cats, khan, meta, rows = d["cats"], d["khan"], d["meta"], d["rows"]
    check_pins(rows)
    base = json.loads((ROOT / "data" / "basemap.json").read_text())
    core = json.loads((ROOT / "data" / "basemap_core.json").read_text())
    landmarks = json.loads((ROOT / "data" / "landmarks.json").read_text())
    soon = json.loads((ROOT / "data" / "soon.json").read_text())
    for l in landmarks:
        if not (BOX_S <= l["lat"] <= BOX_N and BOX_W <= l["lng"] <= BOX_E):
            raise SystemExit(f"landmark {l['id']} outside Phnom Penh or lat/lng swapped")

    DOCS.mkdir(exist_ok=True)
    (DOCS / "data").mkdir(exist_ok=True)
    credits = photos()
    for l in landmarks:
        if l["id"] not in credits:
            raise SystemExit(f"landmark {l['id']} has no photo in data/photos/picks.json")

    used = {e["photo"] for e in soon["items"]} | {s[6] for s in SHELVES if s[6]}
    used |= set(re.findall(r'"([a-z-]+)",\[\"', (ROOT / "tools" / "page.html").read_text()))
    missing = sorted(u for u in used if u not in credits)
    if missing:
        raise SystemExit(f"photo(s) named but not in data/photos/credits.json: {missing}")

    lines, shelf_n = [], [0] * len(SHELVES)
    for r in rows:
        name, cat, kh, lat, lng, phone, fb, addr, conf, web = r[:10]
        sh = shelf_for(name, cats[cat] if cat >= 0 else "")
        if sh >= 0:
            shelf_n[sh] += 1
        lines.append("\t".join([
            clean(name), b36(cat) if cat >= 0 else "", b36(kh) if kh >= 0 else "",
            b36(round((lat - LAT0) * 1e5)), b36(round((lng - LNG0) * 1e5)),
            phone[1:] if phone.startswith("0") else phone, fb, clean(addr), b36(conf),
            "1" if web else "", b36(sh) if sh >= 0 else ""]))
    blob = "\n".join(lines)
    (DOCS / "data" / "places.js").write_text(js_assign("PP_ROWS", blob) + js_assign("PP_CATS", cats))
    (DOCS / "data" / "base.js").write_text(js_assign("PP_BASE", base))
    (DOCS / "data" / "core.js").write_text(js_assign("PP_CORE", core))

    svg, loop = loop_svg(landmarks, base)
    shelves = shelves_public()
    for s, n in zip(shelves, shelf_n):
        s["n"] = n
    boot = {"catShelf": [shelf_of(c) for c in cats], "shelves": shelves, "khan": khan, "landmarks": landmarks, "soon": soon["items"],
            "credits": credits, "meta": meta, "loop": loop, "n": len(lines),
            "route": [[round(p[0], 5), round(p[1], 5)] for p in
                      json.loads((ROOT / "data" / "routes" / "loop.json").read_text())["routes"][0]["geometry"]["coordinates"]]}

    import trip_content as TC, region, robots_ad
    trip = trip_content_boot(TC)
    boot["trip"] = trip
    (ROOT / "data" / "trip.json").write_text(json.dumps(trip, ensure_ascii=False, indent=1))
    region_svg, _ = region.svg()
    icons = (ROOT / "tools" / "icons.svg").read_text()
    icons = icons.replace('<svg xmlns="http://www.w3.org/2000/svg">', '<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">', 1)
    tmpl = (ROOT / "tools" / "page.html").read_text()
    html = (tmpl.replace("/*__FONTS__*/", (ROOT / "tools" / "fonts.css").read_text())
                .replace("<!--__ICONS__-->", icons)
                .replace("<!--__LOOP__-->", svg)
                .replace("<!--__REGION__-->", region_svg)
                .replace("__BOOT__", json.dumps(boot, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
                .replace("__N__", "{:,}".format(len(lines)))
                .replace("__JSONLD__", robots_ad.jsonld(boot, SITE_URL))
                .replace("__SITE__", SITE_URL))
    (DOCS / "index.html").write_text(html)
    card(credits)
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n# AI assistants: {SITE_URL}llms.txt\n")
    (DOCS / "llms.txt").write_text(robots_ad.llms(boot, SITE_URL))
    (DOCS / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f'<url><loc>{SITE_URL}</loc><lastmod>{__import__("datetime").date.today()}</lastmod></url></urlset>\n')
    total = sum(f.stat().st_size for f in DOCS.rglob("*") if f.is_file())
    print(f"wrote docs/: index.html {len(html) // 1024} kB, places.js {(DOCS / 'data' / 'places.js').stat().st_size // 1024} kB "
          f"(gz {len(gzip.compress(blob.encode())) // 1024} kB), {len(credits)} photos, total {total // 1024 // 1024} MB")
    print("shelves:", {s["id"]: s["n"] for s in shelves}, "unshelved:", len(lines) - sum(shelf_n))


if __name__ == "__main__":
    main()
