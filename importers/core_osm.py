#!/usr/bin/env python3
"""Inner-city OpenStreetMap detail for the zoomed-in map: residential streets,
parks and pagoda grounds, 11.515–11.605 N, 104.875–104.950 E. Cached in
cache/osm/core.json (fetched 2026-09-29 through Overpass); written to
data/basemap_core.json in the same delta-grid encoding as data/basemap.json.

ODbL 1.0 — © OpenStreetMap contributors.
"""
import json
from pathlib import Path
from harvest_osm import dp, dp_ring, clip_line, clip_ring, area, encode, Q, TOL, MIN_AREA

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache" / "osm" / "core.json"
OUT = ROOT / "data" / "basemap_core.json"
S, W, N, E = 11.515, 104.875, 11.605, 104.950


def main():
    els = json.loads(CACHE.read_text())["elements"]
    xy = lambda g: [(p["lon"] * Q, p["lat"] * Q) for p in g if p]
    bx = (W * Q, S * Q, E * Q, N * Q)
    streets, parks, wats = [], [], []
    for el in els:
        t = el.get("tags", {})
        g = xy(el.get("geometry", []))
        if t.get("highway"):
            for run in clip_line(g, *bx):
                streets.append(dp(run, TOL * 0.7))
            continue
        if len(g) < 4 or g[0] != g[-1]:
            continue
        c = clip_ring(g[:-1], *bx)
        if len(c) < 3:
            continue
        c = dp_ring(c, TOL * 0.7)
        a = area(c)
        if len(c) < 3 or abs(a) < MIN_AREA / 4:
            continue
        if a < 0:
            c.reverse()
        (parks if t.get("leisure") == "park" else wats).append(c)
    unq = lambda pts: [(x / Q, y / Q) for x, y in pts]
    doc = {"box": [S, W, N, E], "q": Q, "credit": "© OpenStreetMap contributors, ODbL 1.0",
           "streets": [encode(unq(l), W, S) for l in streets],
           "parks": [encode(unq(r), W, S) for r in parks],
           "wats": [encode(unq(r), W, S) for r in wats]}
    OUT.write_text(json.dumps(doc, separators=(",", ":")))
    print(f"wrote {OUT.name}: {len(streets)} streets, {len(parks)} parks, {len(wats)} worship grounds, "
          f"{OUT.stat().st_size // 1024} kB")


if __name__ == "__main__":
    main()
