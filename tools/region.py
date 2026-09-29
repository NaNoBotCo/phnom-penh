# -*- coding: utf-8 -*-
"""The region map for the trip page: Thailand to Cambodia, drawn at build time.

Countries, lakes, rivers: Natural Earth 1:50m (public domain), clipped to the region in data/ne_region.json.
Road legs: OSRM on OpenStreetMap, cached in data/routes/. Flights are drawn as
arcs and labelled as flights; they follow no road.
"""
import json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W0, E0, S0, N0 = 97.4, 108.2, 9.6, 20.6
KX = math.cos(math.radians(15))
WIDTH = 640
SC = WIDTH / ((E0 - W0) * KX)
HEIGHT = round((N0 - S0) * SC)
X = lambda o: (o - W0) * KX * SC
Y = lambda a: (N0 - a) * SC

AIRPORTS = {  # Wikidata P625, checked 2026-09-29
    "CNX": (98.9625, 18.766667, "Chiang Mai", "เชียงใหม่", "ឈៀងម៉ៃ"),
    "CEI": (99.882778, 19.952222, "Chiang Rai", "เชียงราย", "ឈៀងរ៉ាយ"),
    "BKK": (100.747222, 13.681111, "Bangkok", "กรุงเทพฯ", "បាងកក"),
    "KTI": (104.916611, 11.362917, "Phnom Penh", "พนมเปญ", "ភ្នំពេញ"),
    "SAI": (104.223056, 13.369167, "Siem Reap", "เสียมราฐ", "សៀមរាប"),
}
FLIGHTS = [("CNX", "BKK"), ("CEI", "BKK"), ("BKK", "KTI"), ("BKK", "SAI"), ("KTI", "SAI")]
SHOW = {"THA": "Thailand", "KHM": "Cambodia", "LAO": "Laos", "VNM": "Vietnam", "MMR": "Myanmar"}


def rings(geom):
    polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
    for poly in polys:
        for ring in poly:
            yield ring


def path(pts, close=True, step=1):
    pts = pts[::step] or pts
    d = "M" + " L".join(f"{X(o):.1f},{Y(a):.1f}" for o, a in pts)
    return d + ("Z" if close else "")


def arc(a, b, bend=0.18):
    (x1, y1), (x2, y2) = (X(a[0]), Y(a[1])), (X(b[0]), Y(b[1]))
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    cx, cy = mx - dy * bend, my + dx * bend
    return f"M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}"


def svg():
    NE = json.loads((ROOT / "data" / "ne_region.json").read_text())
    ne = NE["admin0_50m"]
    out = [f'<svg class="regionmap" viewBox="0 0 {WIDTH} {HEIGHT}" role="img" aria-label="Chiang Mai, Bangkok, Phnom Penh and Siem Reap">',
           f'<defs><clipPath id="rc"><rect width="{WIDTH}" height="{HEIGHT}" rx="18"/></clipPath></defs><g clip-path="url(#rc)">',
           '<rect class="rm-sea" width="100%" height="100%"/>']
    labels = {"THA": (100.2, 16.2), "KHM": (104.6, 12.6), "LAO": (103.4, 18.9), "VNM": (106.9, 14.6), "MMR": (98.6, 20.3)}
    for f in ne["features"]:
        iso = f["properties"].get("ADM0_A3")
        if iso not in SHOW:
            continue
        cls = "rm-kh" if iso == "KHM" else "rm-th" if iso == "THA" else "rm-land"
        d = "".join(path(r) for r in rings(f["geometry"]))
        out.append(f'<path class="{cls}" d="{d}"/>')
    for iso, (o, a) in labels.items():
        out.append(f'<text class="rm-cty" x="{X(o):.0f}" y="{Y(a):.0f}">{SHOW[iso]}</text>')
    inbox = lambda pts: any(W0 <= o <= E0 and S0 <= a <= N0 for o, a in pts)
    lakes = NE["ne_50m_lakes"]
    d = "".join(path(r) for f in lakes["features"] for r in rings(f["geometry"]) if inbox(r))
    out.append(f'<path class="rm-water" d="{d}"/>')
    rivers = NE["ne_50m_rivers_lake_centerlines"]
    d = ""
    for f in rivers["features"]:
        g = f["geometry"]
        lines = g["coordinates"] if g["type"] == "MultiLineString" else [g["coordinates"]]
        d += "".join(path(l, False) for l in lines if inbox(l))
    out.append(f'<path class="rm-river" d="{d}"/>')
    road = json.loads((ROOT / "data" / "routes" / "pp_sr.json").read_text())["routes"][0]
    out.append(f'<path class="rm-road" d="{path(road["geometry"]["coordinates"], False)}"/>')
    for a, b in FLIGHTS:
        pa, pb = AIRPORTS[a], AIRPORTS[b]
        out.append(f'<path class="rm-fly rm-{a}-{b}" d="{arc(pa, pb)}"/>')
    for code, (o, a, en, th, km) in AIRPORTS.items():
        right = True
        tx = X(o) + (10 if right else -10)
        out.append(f'<g class="rm-ap"><circle cx="{X(o):.1f}" cy="{Y(a):.1f}" r="6"/>'
                   f'<text x="{tx:.0f}" y="{Y(a) + 4:.0f}" text-anchor="{"start" if right else "end"}">'
                   f'<tspan class="rm-code">{code}</tspan> <tspan data-en="{en}" data-th="{th}" data-km="{km}">{en}</tspan></text></g>')
    out.append("</g></svg>")
    return "".join(out), {k: round(road["distance"] / 1000) for k in ["pp_sr"]}


if __name__ == "__main__":
    s, info = svg()
    print(len(s), info)
