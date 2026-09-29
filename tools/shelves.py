# -*- coding: utf-8 -*-
"""The shelves, in the order of the tiles on the front page.

Overture's 806 category slugs fold into these by pattern; a slug matches the
first shelf whose pattern it hits. Anything unmatched stays searchable under
"More". The first four follow Grab's own verticals (Transport, Food, Mart,
Hotels) so a shelf can later hand off to the matching Grab service.
"""
import re

SHELVES = [
 # id, icon, en, th, km, grab vertical, photo, pattern
 ("food", "i-food", "Food", "อาหาร", "ម្ហូប", "food", "amok",
  r"restaurant|^food$|food_delivery|eat_and_drink|bakery|dessert|ice_cream|food_truck|noodle|soup|barbecue|buffet|cupcake|caterer|bistro|diner|food_court|street_vendor|deli$|sandwich|pizza|burger|chicken|hot_pot|dim_sum|brunch"),
 ("coffee", "i-coffee", "Coffee & tea", "กาแฟ ชา", "កាហ្វេ តែ", "food", "hero-dawn",
  r"coffee|^cafe$|bubble_tea|tea_room|juice|smoothie"),
 ("mart", "i-basket", "Mart", "ของใช้ ตลาด", "ផ្សារ ម៉ាត", "mart", "fruit",
  r"grocery|convenience|supermarket|fruits_and_vegetables|farmers_market|liquor|health_food|organic|wholesale_store|market$|butcher|seafood_market|meat_shop|beverage_store|wine|water_store|rice"),
 ("stay", "i-bed", "Stay", "ที่พัก", "ស្នាក់នៅ", "hotels", "le-royal",
  r"hotel|accommodation|hostel|guest_house|service_apartments|resort|bed_and_breakfast|motel|holiday_rental|inn$"),
 ("spa", "i-spa", "Spa & beauty", "สปา ความงาม", "ស្ប៉ា សម្ផស្ស", None, "apsara",
  r"^spas$|_spa$|^day_spa|beauty_salon|skin_care|hair_salon|nail_salon|barber|massage|tattoo|eyelash|waxing|makeup|hair_removal"),
 ("health", "i-health", "Health", "สุขภาพ", "សុខភាព", None, None,
  r"pharmacy|hospital|dentist|health_and_medical|medical|diagnostic|dermatolog|physical_therap|womens_health|optician|eyewear|clinic|doctor|laboratory_testing|maternity|pediatric|surgeon|vitamins"),
 ("wat", "i-wat", "Pagodas & worship", "วัด ศาสนสถาน", "វត្ត ទីសក្ការៈ", None, "wat-phnom-gold",
  r"buddhist_temple|temple|pagoda|church|mosque|religious|shrine|monastery|place_of_worship"),
 ("sights", "i-museum", "Sights", "ที่เที่ยว", "កន្លែងកម្សាន្ត", None, "independence",
  r"landmark|monument|museum|art_gallery|park$|tours|attraction|arts_and_entertainment|cinema|zoo|garden|sculpture|memorial|historical"),
 ("night", "i-beer", "Night", "กลางคืน", "ពេលយប់", None, "hero-night",
  r"^bar$|pub|lounge|cocktail|dance_club|karaoke|music_venue|beer|wine_bar|night|casino|jazz"),
 ("shop", "i-shop", "Shops", "ร้านค้า", "ហាង", "mart", "central-market",
  r"clothing|shoe|jewel|fashion|electronics|mobile_phone|shopping|cosmetic|souvenir|bookstore|toy|gift|flowers|luggage|accessor|lingerie|sporting_goods|department|boutique|watch|bag|computer_store|furniture|home_goods|fabric|arts_and_crafts|market_stall"),
 ("money", "i-atm", "Money", "เงิน", "លុយ", None, None,
  r"bank|atm|financial_service|currency|money_transfer|pawn|exchange|microfinance|installment_loans"),
 ("ride", "i-ride", "Ride & fix", "เดินทาง ซ่อมรถ", "ធ្វើដំណើរ ជួសជុល", "transport", "tuk-tuk",
  r"gas_station|fuel|car_rental|taxi|transportation|bus_station|motorcycle_repair|motorcycle_dealer|automotive|tire|car_wash|motorcycle_rental|bike_rental|parking|travel_services|oil_change|auto_detailing|bicycle"),
]

_RX = [(s[0], re.compile(s[7])) for s in SHELVES]


def shelf_of(slug):
    if not slug:
        return -1
    for i, (_, rx) in enumerate(_RX):
        if rx.search(slug):
            return i
    return -1


def public():
    return [{"id": s[0], "icon": s[1], "en": s[2], "th": s[3], "km": s[4], "grab": s[5], "photo": s[6]}
            for s in SHELVES]
