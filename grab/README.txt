PSAR PHNOM PENH AND GRAB

Three steps. The first is built.

1. RIDE LINKS — built, no key
   Every place and landmark has a "Ride here · Grab" button. It opens the Grab
   app with the drop-off filled in (grab://open?screenType=BOOKING, through
   Grab's grab.onelink.me link, which falls back to grab.com when the app is
   missing). Pickup is left out, so Grab starts from the phone's position:
   test this on a phone before telling anyone.
   Code: GRAB in tools/page.html.

2. GRAB'S OWN PLACES — scaffolded, needs a GrabMaps key
   maps.grab.com hands out keys without a card. With one:
       GRABMAPS_KEY=... python3 tools/grab_match.py --limit 50
   pairs our places with Grab's POIs and brings back Grab's poi_id and
   opening hours. Opening hours are what "open now" needs: Overture carries
   none for Phnom Penh.
   Our places already sit in Grab's shape: data/grab/places.jsonl
   (python3 tools/export_grab.py rebuilds it).
   Cambodia is listed for GrabMaps on Amazon Location Service; maps.grab.com
   does not name its countries.

3. PARTNER APIS — Grab's approval
   Farefeed returns a fare and a ready-made ride link per service
   (Car, TukTuk, Remorque in Phnom Penh). GrabExpress lists Cambodia.
   GrabFood and GrabMart merchant links need a partner account; until then
   the Food shelf links to food.grab.com/kh/en/.
   Apply at developer.grab.com.

Sources, checked 2026-09-29
  developer.grab.com/docs/partner-farefeed/
  developer.grab.com/docs/grab-express/
  maps.grab.com/developer/documentation
  docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html
  grab.com/kh/en/transport/   grab.com/kh/en/food/   grab.com/kh/en/mart/
