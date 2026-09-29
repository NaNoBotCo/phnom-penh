#!/usr/bin/env python3
"""Overture Maps Places for Phnom Penh — the fetch half.

Lifted from mot-dang/importers/harvest_overture.py, which is the same fetch
pointed at Chiang Mai. Only the box and the province test differ: Cambodia
uses 6-digit postcodes (12xxxx = Phnom Penh capital) but most rows carry no
postcode at all, so `country = KH` inside the box plus a region/locality
naming Phnom Penh is what keeps a row.

CDLA-Permissive-2.0. Use it, publish it, attribute it. It does NOT clear a
contribution back to OpenStreetMap — Meta's and Foursquare's rows are in here.

    python3 importers/harvest_overture.py
    python3 importers/harvest_overture.py --check
"""
import argparse
import gzip
import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache" / "overture"
OUT = CACHE / "pp.jsonl.gz"
MANIFEST = CACHE / "manifest.json"

BUCKET = "s3://overturemaps-us-west-2/release"
LICENCE = "CDLA-Permissive-2.0"
ATTRIBUTION = "© Overture Maps Foundation"

# Phnom Penh capital plus a margin: the box also catches Kandal, which rings
# the city on three sides, so the box is a first cut and the country/region
# test below is what actually keeps a row.
BBOX = (104.70, 11.35, 105.10, 11.80)

FIELDS = """
  id,
  names.primary AS name,
  names.common AS names_common,
  categories.primary AS cat,
  categories.alternate AS cat_alt,
  confidence,
  operating_status,
  phones[1] AS phone,
  websites[1] AS website,
  socials AS socials,
  emails[1] AS email,
  addresses[1].freeform AS address,
  addresses[1].locality AS locality,
  addresses[1].postcode AS postcode,
  addresses[1].region AS region,
  addresses[1].country AS country,
  brand.names.primary AS brand,
  sources[1].dataset AS dataset,
  sources[1].update_time AS updated,
  (bbox.xmin + bbox.xmax) / 2 AS lng,
  (bbox.ymin + bbox.ymax) / 2 AS lat
"""


def latest_release(con):
    try:
        rows = con.execute(
            f"SELECT file FROM glob('{BUCKET}/*/theme=places/type=place/*.parquet')"
        ).fetchall()
    except Exception as e:
        print(f"could not list releases: {e}", file=sys.stderr)
        return None
    rel = sorted({f[0].split("/release/")[1].split("/")[0] for f in rows})
    return rel[-1] if rel else None


def harvest(release=None, out=OUT):
    try:
        import duckdb
    except ImportError:
        sys.exit("needs duckdb: python3 -m pip install duckdb")
    con = duckdb.connect()
    con.execute("INSTALL httpfs; LOAD httpfs; SET s3_region='us-west-2';")
    release = release or latest_release(con)
    if not release:
        sys.exit("no Overture release found; pass --release")
    src = f"{BUCKET}/{release}/theme=places/type=place/*"
    x0, y0, x1, y1 = BBOX
    print(f"overture {release}: reading the box …", flush=True)
    con.execute(f"""
        CREATE TABLE box AS SELECT {FIELDS}
        FROM read_parquet('{src}', hive_partitioning=1)
        WHERE bbox.xmin BETWEEN {x0} AND {x1}
          AND bbox.ymin BETWEEN {y0} AND {y1}
    """)
    print("in the box:", con.execute("SELECT count(*) FROM box").fetchone()[0], flush=True)
    # What the rows actually say, before any filter — so the filter is chosen
    # from the data and not from what Cambodia is supposed to look like.
    for label, q in (
        ("country", "SELECT country, count(*) c FROM box GROUP BY 1 ORDER BY c DESC LIMIT 8"),
        ("region", "SELECT region, count(*) c FROM box GROUP BY 1 ORDER BY c DESC LIMIT 12"),
        ("locality", "SELECT locality, count(*) c FROM box GROUP BY 1 ORDER BY c DESC LIMIT 12"),
        ("postcode", "SELECT postcode, count(*) c FROM box GROUP BY 1 ORDER BY c DESC LIMIT 8"),
    ):
        print(f"-- {label}")
        for r in con.execute(q).fetchall():
            print("   ", r)
    return con


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--release")
    a = ap.parse_args()
    harvest(a.release)
