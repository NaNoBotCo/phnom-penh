#!/usr/bin/env python3
"""Pair each place with Grab's own POI through the GrabMaps nearby search.

    GRABMAPS_KEY=... python3 tools/grab_match.py --limit 50     # a trial batch
    python3 tools/grab_match.py --dry-run --limit 3             # print the requests, send nothing

Needs a GrabMaps API key (maps.grab.com, self-serve). Not yet run: no key is on this
machine. For each row it asks for Grab places within 60 m and keeps the best name match,
writing poi_id, opening_hours and Grab's categories into data/grab/matched.jsonl.
Responses are cached in cache/grab/ so a rerun costs nothing.

Endpoint and fields are as documented at maps.grab.com/developer/documentation on
2026-09-29 (search-nearby: location "lat,lng", radius in km, bearer key). Check them
against the live docs before the first real batch.
"""
import argparse, difflib, hashlib, json, os, subprocess, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "grab" / "places.jsonl"
OUT = ROOT / "data" / "grab" / "matched.jsonl"
CACHE = ROOT / "cache" / "grab"
URL = "https://maps.grab.com/api/v1/search-nearby"


def ask(row, key, dry):
    loc = f'{row["location"]["latitude"]},{row["location"]["longitude"]}'
    q = f"{URL}?location={loc}&radius=0.06&keyword={row['name'][:60]}"
    if dry:
        print("GET", q)
        return None
    f = CACHE / (hashlib.sha1(q.encode()).hexdigest() + ".json")
    if f.exists():
        return json.loads(f.read_text())
    r = subprocess.run(["curl", "-sf", "-G", URL, "-H", f"Authorization: Bearer {key}",
                        "--data-urlencode", f"location={loc}", "--data-urlencode", "radius=0.06",
                        "--data-urlencode", f"keyword={row['name'][:60]}"], capture_output=True)
    if r.returncode:
        print("request failed", r.returncode, file=sys.stderr)
        return None
    CACHE.mkdir(parents=True, exist_ok=True)
    f.write_bytes(r.stdout)
    time.sleep(0.2)
    return json.loads(r.stdout)


def best(row, res):
    cands = (res or {}).get("places") or (res or {}).get("results") or []
    score = lambda c: difflib.SequenceMatcher(None, row["name"].lower(), (c.get("name") or "").lower()).ratio()
    cands = sorted(cands, key=score, reverse=True)
    return cands[0] if cands and score(cands[0]) >= 0.6 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=50)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    key = os.environ.get("GRABMAPS_KEY", "")
    if not key and not a.dry_run:
        sys.exit("set GRABMAPS_KEY (maps.grab.com) or pass --dry-run")
    rows = [json.loads(l) for l in SRC.open()][: a.limit]
    hits = 0
    with OUT.open("a") as f:
        for row in rows:
            c = best(row, ask(row, key, a.dry_run))
            if not c:
                continue
            hits += 1
            row.update(poi_id=c.get("poi_id", ""), opening_hours=c.get("opening_hours"),
                       grab_categories=c.get("categories"), grab_name=c.get("name"))
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"{hits} of {len(rows)} matched")


if __name__ == "__main__":
    main()
