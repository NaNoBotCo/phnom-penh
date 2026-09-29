#!/usr/bin/env python3
"""OpenStreetMap streets and water for the map view — fetched once, cached.

The box is the middle 98% of the pins (the extent page.html fits the map to)
plus a margin for a canvas wider or taller than the city. Roads: motorway to
tertiary. Water: natural=water and waterway=riverbank, which in Phnom Penh is
the Mekong, the Tonlé Sap, the Bassac and the lakes.

ODbL 1.0 — © OpenStreetMap contributors. The page credits it.

    python3 importers/harvest_osm.py            fetch if not cached, then write data/basemap.json
    python3 importers/harvest_osm.py --refetch  fetch again

System Python 3.9's LibreSSL fails TLS to Overpass, so the fetch goes through curl.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache" / "osm" / "overpass.json"
OUT = ROOT / "data" / "basemap.json"
MIRRORS = ["https://overpass-api.de/api/interpreter",
           "https://overpass.private.coffee/api/interpreter"]
PAD = 0.1           # degrees past the pin extent, ~11 km: covers a 2:1 canvas
Q = 1e4             # grid: 1e-4 degree, ~11 m
TOL = 1.5           # Douglas-Peucker tolerance, grid units (~16 m)
MIN_AREA = 40       # water rings smaller than this (grid units², ~0.5 ha) drop
ROADS = "motorway|trunk|primary|secondary|tertiary"
MAJOR = {"motorway", "trunk", "primary"}


def pin_box():
    rows = json.loads((ROOT / "data" / "pp.json").read_text())["rows"]
    la = sorted(r[3] for r in rows)
    lo = sorted(r[4] for r in rows)
    n = len(rows)
    return (round(la[n // 100] - PAD, 3), round(lo[n // 100] - PAD, 3),
            round(la[n * 99 // 100] + PAD, 3), round(lo[n * 99 // 100] + PAD, 3))


def fetch(box):
    b = ",".join(map(str, box))
    q = (f'[out:json][timeout:120];('
         f'way["highway"~"^({ROADS})(_link)?$"]({b});'
         f'way["natural"="water"]({b});way["waterway"="riverbank"]({b});'
         f'relation["natural"="water"]({b});relation["waterway"="riverbank"]({b});'
         f');out geom;')
    for url in MIRRORS:
        print("overpass:", url, flush=True)
        r = subprocess.run(["curl", "-sf", "--max-time", "180",
                            "-H", "User-Agent: phnom-penh-basemap/1 (local build)",
                            "--data-urlencode", "data=" + q, url],
                           capture_output=True)
        if r.returncode == 0 and r.stdout.lstrip().startswith(b"{"):
            CACHE.parent.mkdir(parents=True, exist_ok=True)
            CACHE.write_bytes(r.stdout)
            return
        print(f"  failed (curl {r.returncode})", file=sys.stderr)
    sys.exit("every Overpass mirror failed")


def dp(pts, tol):
    """Douglas-Peucker on a list of (x, y)."""
    if len(pts) < 3:
        return pts
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        (ax, ay), (bx, by) = pts[a], pts[b]
        dx, dy = bx - ax, by - ay
        L = (dx * dx + dy * dy) ** 0.5 or 1e-12
        best, bi = -1.0, -1
        for i in range(a + 1, b):
            px, py = pts[i]
            d = abs(dy * (px - ax) - dx * (py - ay)) / L
            if d > best:
                best, bi = d, i
        if best > tol:
            keep[bi] = True
            stack += [(a, bi), (bi, b)]
    return [p for p, k in zip(pts, keep) if k]


def dp_ring(ring, tol):
    """Douglas-Peucker on an open ring: split at the point farthest from the
    first, since a closed run has no chord to measure against."""
    if len(ring) < 4:
        return ring
    x, y = ring[0]
    k = max(range(len(ring)), key=lambda i: (ring[i][0] - x) ** 2 + (ring[i][1] - y) ** 2)
    return dp(ring[:k + 1], tol)[:-1] + dp(ring[k:] + [ring[0]], tol)[:-1]


def clip_ring(ring, x0, y0, x1, y1):
    """Sutherland-Hodgman against the box."""
    def cut(pts, inside, meet):
        out = []
        for i, cur in enumerate(pts):
            prev = pts[i - 1]
            if inside(cur):
                if not inside(prev):
                    out.append(meet(prev, cur))
                out.append(cur)
            elif inside(prev):
                out.append(meet(prev, cur))
        return out

    def at_x(x):
        return lambda p, q: (x, p[1] + (q[1] - p[1]) * (x - p[0]) / (q[0] - p[0]))

    def at_y(y):
        return lambda p, q: (p[0] + (q[0] - p[0]) * (y - p[1]) / (q[1] - p[1]), y)

    for inside, meet in ((lambda p: p[0] >= x0, at_x(x0)), (lambda p: p[0] <= x1, at_x(x1)),
                         (lambda p: p[1] >= y0, at_y(y0)), (lambda p: p[1] <= y1, at_y(y1))):
        if not ring:
            break
        ring = cut(ring, inside, meet)
    return ring


def clip_line(line, x0, y0, x1, y1):
    """Split a polyline into the runs inside the box (segment ends clipped)."""
    def ins(p):
        return x0 <= p[0] <= x1 and y0 <= p[1] <= y1

    def seg(p, q):  # Liang-Barsky
        t0, t1 = 0.0, 1.0
        dx, dy = q[0] - p[0], q[1] - p[1]
        for pp, qq in ((-dx, p[0] - x0), (dx, x1 - p[0]), (-dy, p[1] - y0), (dy, y1 - p[1])):
            if pp == 0:
                if qq < 0:
                    return None
            else:
                t = qq / pp
                if pp < 0:
                    t0 = max(t0, t)
                else:
                    t1 = min(t1, t)
        if t0 > t1:
            return None
        return (p[0] + t0 * dx, p[1] + t0 * dy), (p[0] + t1 * dx, p[1] + t1 * dy)

    runs, cur = [], []
    for p, q in zip(line, line[1:]):
        s = seg(p, q)
        if s is None:
            if cur:
                runs.append(cur)
                cur = []
            continue
        a, b = s
        if not cur:
            cur = [a]
        cur.append(b)
        if not ins(q):
            runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return [r for r in runs if len(r) > 1]


def stitch(ways):
    """Join member ways end to end into closed rings."""
    ways = [list(w) for w in ways if len(w) > 1]
    rings = []
    while ways:
        ring = ways.pop()
        grew = True
        while ring[0] != ring[-1] and grew:
            grew = False
            for i, w in enumerate(ways):
                if w[0] == ring[-1]:
                    ring += w[1:]
                elif w[-1] == ring[-1]:
                    ring += w[-2::-1]
                elif w[-1] == ring[0]:
                    ring = w[:-1] + ring
                elif w[0] == ring[0]:
                    ring = w[:0:-1] + ring
                else:
                    continue
                ways.pop(i)
                grew = True
                break
        if ring[0] == ring[-1] and len(ring) > 3:
            rings.append(ring)
    return rings


def area(r):
    return sum(r[i - 1][0] * r[i][1] - r[i][0] * r[i - 1][1] for i in range(len(r))) / 2


def encode(pts, ox, oy):
    """Grid ints, first point absolute, the rest as deltas; repeats drop."""
    out, px, py = [], None, None
    for x, y in pts:
        gx, gy = round((x - ox) * Q), round((y - oy) * Q)
        if (gx, gy) == (px, py):
            continue
        out += [gx, gy] if px is None else [gx - px, gy - py]
        px, py = gx, gy
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--refetch", action="store_true")
    args = ap.parse_args()
    s, w, n, e = pin_box()
    if args.refetch or not CACHE.exists():
        fetch((s, w, n, e))
    els = json.loads(CACHE.read_text())["elements"]

    def xy(geom):  # lon/lat in grid units, so DP tolerance is in grid units
        return [(g["lon"] * Q, g["lat"] * Q) for g in geom if g]

    bx = (w * Q, s * Q, e * Q, n * Q)
    major, minor, water = [], [], []
    for el in els:
        tags = el.get("tags", {})
        hw = tags.get("highway", "").replace("_link", "")
        if el["type"] == "way" and hw:
            for run in clip_line(xy(el["geometry"]), *bx):
                (major if hw in MAJOR else minor).append(dp(run, TOL))
            continue
        if el["type"] == "way":
            rings = [(xy(el["geometry"]), "outer")]
        else:
            by_role = {"outer": [], "inner": []}
            for m in el.get("members", []):
                if m["type"] == "way" and m.get("geometry"):
                    by_role["inner" if m.get("role") == "inner" else "outer"].append(xy(m["geometry"]))
            rings = [(r, role) for role, ws in by_role.items() for r in stitch(ws)]
        for r, role in rings:
            if len(r) < 4 or r[0] != r[-1]:
                continue
            c = clip_ring(r[:-1], *bx)
            if len(c) < 3:
                continue
            c = dp_ring(c, TOL)
            a = area(c)
            if len(c) < 3 or abs(a) < MIN_AREA:
                continue
            # nonzero fill: outer rings counter-clockwise, holes clockwise
            if (a < 0) == (role == "outer"):
                c.reverse()
            water.append(c)

    ox, oy = w, s
    unq = lambda pts: [(x / Q, y / Q) for x, y in pts]
    doc = {
        "box": [s, w, n, e],
        "q": Q,
        "credit": "© OpenStreetMap contributors, ODbL 1.0",
        "water": [encode(unq(r), ox, oy) for r in water],
        "major": [encode(unq(l), ox, oy) for l in major],
        "minor": [encode(unq(l), ox, oy) for l in minor],
    }
    OUT.write_text(json.dumps(doc, separators=(",", ":")))
    print(f"wrote {OUT.relative_to(ROOT)}: box {s},{w} to {n},{e}; "
          f"{len(water)} water rings, {len(major)} major + {len(minor)} minor road runs; "
          f"{OUT.stat().st_size // 1024} kB")


if __name__ == "__main__":
    main()
