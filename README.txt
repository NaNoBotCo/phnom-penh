PSAR PHNOM PENH · ផ្សារភ្នំពេញ

Phnom Penh near and now: 73,337 places, 20 landmarks with photographs, the
river, the sun and moon, the holidays, and a Grab ride to any of it.
English, Thai, Khmer.

Build    python3 tools/build.py        writes docs/
Look     open docs/index.html          (works from disk; no server needed)
Grab     grab/README.txt

Data on disk
  data/pp.json              Overture places (derive.py, from cache/overture)
  data/basemap.json         OSM roads and water      (importers/harvest_osm.py)
  data/basemap_core.json    OSM inner-city streets, parks, pagoda grounds
                            (importers/core_osm.py)
  data/landmarks.json       20 landmarks, names from Wikidata, words by hand
  data/soon.json            2026 public holidays, Sub-Decree 167
  data/photos/              37 Wikimedia Commons photographs + credits.json
                            (tools/commons.py; picks.json names each choice)
  cache/osrm/loop.json      the river loop, routed on OSM streets
  data/grab/places.jsonl    every place in GrabMaps' result shape

Not published.
