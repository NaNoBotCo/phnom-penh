#!/usr/bin/env python3
"""Write data/grab/places.jsonl: every place in the shape of a GrabMaps place result.

    python3 tools/export_grab.py

Field names follow the GrabMaps search response (maps.grab.com/developer/documentation):
poi_id, name, formatted_address, location{latitude,longitude}, country_code, city,
administrative_areas, categories[{category_name}], business_type. poi_id stays empty
until tools/grab_match.py has paired the row with Grab's own POI; ovt_id is the
Overture GERS id that pairing keys on. Extra fields (phone, facebook, shelf,
confidence, source) are ours.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from build import shelf_for, SHELVES  # noqa: E402


def main():
    d = json.loads((ROOT / "data" / "pp.json").read_text())
    cats, khan = d["cats"], d["khan"]
    out = ROOT / "data" / "grab" / "places.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with out.open("w") as f:
        for name, cat, kh, lat, lng, phone, fb, addr, conf, web, ovt in d["rows"]:
            slug = cats[cat] if cat >= 0 else ""
            sh = shelf_for(name, slug)
            f.write(json.dumps({
                "poi_id": "",
                "ovt_id": ovt,
                "name": name,
                "formatted_address": addr,
                "location": {"latitude": lat, "longitude": lng},
                "country_code": "KHM",
                "city": "Phnom Penh",
                "administrative_areas": [{"type": "khan", "name": khan[kh][1], "name_km": khan[kh][0]}] if kh >= 0 else [],
                "categories": [{"category_name": slug.replace("_", " ")}] if slug else [],
                "business_type": SHELVES[sh][0] if sh >= 0 else "",
                "phone": ("+855" + phone[1:]) if phone.startswith("0") else phone,
                "facebook": fb,
                "confidence": conf / 100,
                "source": "overture " + d["meta"]["release"],
            }, ensure_ascii=False) + "\n")
            n += 1
    print(f"wrote {out.relative_to(ROOT)}: {n} places, {out.stat().st_size // 1024} kB")


if __name__ == "__main__":
    main()
