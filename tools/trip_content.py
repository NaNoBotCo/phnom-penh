# -*- coding: utf-8 -*-
"""Words for the trip page (#/trip): coming from Thailand. Each string EN/TH/KM.
Figures carry their source URL; checked 2026-09-29. build.py writes data/trip.json from this."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
def t(en, th, km, **kw): return dict(en=en, th=th, km=km, **kw)

EVISA = "https://www.evisa.gov.kh/information/tourist_visa/4"
TOURISM = "https://www.tourismcambodia.com/tripplanner/essential-information/visa-passport.htm"
ARRIVAL = "https://arrival.gov.kh/"
TDAC = "https://th.usembassy.gov/notice-thailand-digital-arrival-card-system-set-to-launch-on-1-may-2025/"
EXEMPT = "https://visasnews.com/en/thailand-introduces-new-visa-free-and-visa-on-arrival-rules-on-september-15-2026/"
MFA = "https://image.mfa.go.th/mfa/0/wdW3FTtVMc/2026-05-22/%E0%B8%95%E0%B8%B2%E0%B8%A3%E0%B8%B2%E0%B8%87%E0%B8%97%E0%B8%9A%E0%B8%97%E0%B8%A7%E0%B8%99%E0%B8%A1%E0%B8%B2%E0%B8%95%E0%B8%A3%E0%B8%81%E0%B8%B2%E0%B8%A3_ver._eng.pdf"
REENTRY = "https://bangkok.immigration.go.th/en/re-entry-permit/"
DTV = "https://www.thaievisa.go.th/visa/dtv-visa"
THAI7 = "https://www.khmertimeskh.com/501696759/in-response-to-thai-ruling-cambodia-limits-thai-nationals-to-7-days-of-entry-into-cambodia/"
BORDER = "https://www.nationthailand.com/news/politics/40068852"
BUSES = "https://www.nationthailand.com/news/asean/40050993"
KTI_BUS = "https://www.techoairport.com.kh/transportation/public"
KTI_OPEN = "https://en.wikipedia.org/wiki/Techo_International_Airport"
WING = "https://www.wingbank.com.kh/en/news/wing-atms-now-at-techo-international-airport"
SAI = "https://www.siemreap.net/guides/travel/siem-reap-angkor-international-airport/"
PG = "https://www.bangkokair.com/flightdeals/view/siem-reap"
KR = "https://www.aeroroutes.com/eng/260617-krjun26sai"
IBIS = "https://www.giantibis.com/routes/phnom-penh-to-siem-reap"
ANGKOR = "https://www.siemreap.net/guides/angkor/hours-admission/"
ADVISORY = "https://kh.usembassy.gov/security-alert-cambodia-thailand-border/"
ARC = "https://www.aupptechcenter.com/what-is-arc-start-up-accelerator/"
ARC_LAUNCH = "https://thebettercambodia.com/launching-arc-start-up-accelerator-a-new-era-for-cambodian-entrepreneurs/"
ARC_CONF = "https://mptc.gov.kh/en/2025/10/secretary-of-state-so-visothy-presided-over-the-arc-startup-accelerator-conference-2025/"

VISA = dict(id="visa", icon="i-document", h=t("Visas", "วีซ่า", "ទិដ្ឋាការ"), blocks=[
  dict(t="p", **t("The land border between Thailand and Cambodia has been shut since June 2025. Every trip from Chiang Mai goes by air, through Bangkok.",
                  "ด่านพรมแดนไทย–กัมพูชาปิดมาตั้งแต่มิถุนายน 2568 จากเชียงใหม่ต้องบินอย่างเดียว ต่อเครื่องที่กรุงเทพฯ",
                  "ព្រំដែនគោករវាងថៃ និងកម្ពុជាបិទតាំងពីខែមិថុនា ឆ្នាំ 2025។ ពីឈៀងម៉ៃ ត្រូវជិះយន្តហោះ ឆ្លងកាត់បាងកក។", src=[BORDER, BUSES])),
  dict(t="cards", cards=[
    dict(k=t("US passport", "พาสปอร์ตอเมริกา", "លិខិតឆ្លងដែនអាមេរិក"), h=t("Visa needed: $30, 30 days", "ต้องมีวีซ่า 30 ดอลลาร์ อยู่ได้ 30 วัน", "ត្រូវការទិដ្ឋាការ៖ $30 ស្នាក់បាន 30 ថ្ងៃ"),
         p=t("Buy the e-Visa online (about 3 working days) or get it on arrival. Six months left on the passport, one blank page.",
             "ซื้อ e-Visa ออนไลน์ (ราว 3 วันทำการ) หรือทำที่สนามบิน พาสปอร์ตต้องเหลืออายุ 6 เดือน มีหน้าว่าง 1 หน้า",
             "ទិញ e-Visa តាមអនឡាញ (ប្រហែល 3 ថ្ងៃធ្វើការ) ឬសុំពេលមកដល់។ លិខិតឆ្លងដែននៅសល់ 6 ខែ និងទំព័រទំនេរ 1។"), src=[EVISA, TOURISM]),
    dict(k=t("Thai passport", "พาสปอร์ตไทย", "លិខិតឆ្លងដែនថៃ"), h=t("No visa, but check the days", "ไม่ต้องใช้วีซ่า แต่เช็กจำนวนวัน", "មិនត្រូវការទិដ្ឋាការ តែពិនិត្យចំនួនថ្ងៃ"),
         p=t("The old free stay was 14 days. In June 2025 Cambodia cut it to 7 days for Thais. We found nothing saying it has changed back.",
             "เดิมอยู่ฟรีได้ 14 วัน มิถุนายน 2568 กัมพูชาลดเหลือ 7 วันสำหรับคนไทย ยังไม่พบข่าวว่ากลับเป็นเหมือนเดิม",
             "ពីមុនស្នាក់បាន 14 ថ្ងៃ។ ខែមិថុនា ឆ្នាំ 2025 កម្ពុជាកាត់មកត្រឹម 7 ថ្ងៃសម្រាប់ជនជាតិថៃ។ មិនទាន់ឃើញព័ត៌មានថាប្ដូរវិញទេ។"), src=THAI7),
    dict(k=t("Everyone flying in", "ทุกคนที่บินเข้า", "អ្នកជិះយន្តហោះទាំងអស់"), h=t("e-Arrival card, free", "บัตรขาเข้าออนไลน์ ฟรี", "ប័ណ្ណមកដល់អេឡិចត្រូនិក ឥតគិតថ្លៃ"),
         p=t("Fill it in at arrival.gov.kh within 7 days before you land. Only that address.",
             "กรอกที่ arrival.gov.kh ภายใน 7 วันก่อนเครื่องลง ใช้เว็บนี้เท่านั้น",
             "បំពេញនៅ arrival.gov.kh ក្នុងរយៈពេល 7 ថ្ងៃមុនចុះចត។ តែគេហទំព័រនេះប៉ុណ្ណោះ។"), src=ARRIVAL, hot=True),
  ]),
  dict(t="h", **t("Coming back into Thailand", "ขากลับเข้าไทย", "ត្រឡប់ចូលថៃវិញ")),
  dict(t="cards", cards=[
    dict(k=t("US passport, no visa", "พาสปอร์ตอเมริกา ไม่มีวีซ่า", "គ្មានទិដ្ឋាការ"), h=t("30 days now, not 60", "ตอนนี้ 30 วัน ไม่ใช่ 60", "ឥឡូវ 30 ថ្ងៃ មិនមែន 60"),
         p=t("From 15 September 2026 the visa-free stay is 30 days, with one extension of up to 30 more at immigration's say.",
             "ตั้งแต่ 15 กันยายน 2569 อยู่ได้ 30 วัน ต่อได้อีกครั้งไม่เกิน 30 วัน แล้วแต่ ตม.",
             "ចាប់ពីថ្ងៃទី 15 កញ្ញា 2026 ស្នាក់បាន 30 ថ្ងៃ បន្តបានម្ដងទៀតរហូតដល់ 30 ថ្ងៃ តាមការសម្រេចរបស់អន្តោប្រវេសន៍។"), src=[EXEMPT, MFA], hot=True),
    dict(k=t("DTV", "DTV", "DTV"), h=t("A fresh 180 days", "ได้ 180 วันใหม่", "បាន 180 ថ្ងៃថ្មី"),
         p=t("Each entry on a Destination Thailand Visa gives 180 days. An extension you were granted ends when you leave.",
             "เข้าประเทศแต่ละครั้งด้วยวีซ่า DTV ได้ 180 วัน ถ้าเคยต่ออายุไว้ การต่อนั้นสิ้นสุดเมื่อออกนอกประเทศ",
             "ចូលម្ដងៗដោយ DTV បាន 180 ថ្ងៃ។ ការបន្តដែលបានទទួល នឹងបញ្ចប់ពេលអ្នកចេញ។"), src=DTV),
    dict(k=t("Non-O, retirement, marriage", "Non-O เกษียณ แต่งงาน", "Non-O ចូលនិវត្តន៍ រៀបការ"), h=t("Re-entry permit first", "ทำรีเอ็นทรีก่อน", "ធ្វើលិខិតចូលវិញមុន"),
         p=t("Leave on an extension of stay without a re-entry permit and the stay ends. Single ฿1,000, multiple ฿3,800, at immigration or the airport.",
             "ถ้าออกนอกประเทศโดยไม่มีรีเอ็นทรี การอยู่ต่อจะสิ้นสุด ครั้งเดียว 1,000 บาท หลายครั้ง 3,800 บาท ทำที่ ตม. หรือสนามบิน",
             "បើចេញដោយគ្មានលិខិតចូលវិញ ការស្នាក់នៅនឹងបញ្ចប់។ ម្ដង ฿1,000 ច្រើនដង ฿3,800 នៅអន្តោប្រវេសន៍ ឬព្រលានយន្តហោះ។"), src=REENTRY, hot=True),
    dict(k=t("Everyone", "ทุกคน", "គ្រប់គ្នា"), h=t("TDAC within 3 days", "TDAC ภายใน 3 วัน", "TDAC ក្នុង 3 ថ្ងៃ"),
         p=t("The Thailand Digital Arrival Card, free at tdac.immigration.go.th, in the 3 days before you land.",
             "บัตรขาเข้าดิจิทัลของไทย ฟรีที่ tdac.immigration.go.th ภายใน 3 วันก่อนถึง",
             "ប័ណ្ណមកដល់ឌីជីថលថៃ ឥតគិតថ្លៃ នៅ tdac.immigration.go.th ក្នុង 3 ថ្ងៃមុនមកដល់។"), src=TDAC),
  ]),
  dict(t="p", **t("Staying longer in Cambodia: a visitor visa (type T) extends once, by a month; a business (E) visa extends up to a year. Overstay is $10 a day.",
                  "อยู่กัมพูชานานขึ้น วีซ่าท่องเที่ยวต่อได้ครั้งเดียว 1 เดือน วีซ่าธุรกิจ (E) ต่อได้ถึง 1 ปี อยู่เกินวันละ 10 ดอลลาร์",
                  "ស្នាក់នៅយូរជាងនេះ៖ ទិដ្ឋាការទេសចរណ៍បន្តបានម្ដង 1 ខែ។ ទិដ្ឋាការអាជីវកម្ម (E) បន្តបានដល់ 1 ឆ្នាំ។ ស្នាក់លើស $10 ក្នុងមួយថ្ងៃ។", src=TOURISM)),
  dict(t="p", **t("The US Embassy asks travellers to stay more than 50 km from the Thai–Cambodian border. Phnom Penh and Siem Reap town are well outside it.",
                  "สถานทูตสหรัฐฯ แนะนำให้อยู่ห่างแนวชายแดนไทย–กัมพูชาเกิน 50 กม. พนมเปญและตัวเมืองเสียมราฐอยู่นอกระยะนั้น",
                  "ស្ថានទូតអាមេរិកស្នើឱ្យនៅឆ្ងាយពីព្រំដែនថៃ–កម្ពុជាលើសពី 50 គ.ម។ ភ្នំពេញ និងទីក្រុងសៀមរាបនៅក្រៅចម្ងាយនោះ។", src=ADVISORY)),
])

AIR = dict(id="air", icon="i-plane", h=t("The airport", "สนามบิน", "ព្រលានយន្តហោះ"), blocks=[
  dict(t="p", **t("Phnom Penh's airport is new and far out. Techo International (code KTI, not the old PNH) opened on 9 September 2025, about 20 km south of the city; our road route to Central Market is 27 km.",
                  "สนามบินพนมเปญเป็นสนามบินใหม่และอยู่ไกลเมือง เตโช (รหัส KTI ไม่ใช่ PNH แบบเดิม) เปิด 9 กันยายน 2568 อยู่ใต้เมืองราว 20 กม. ตามถนนถึงตลาดกลาง 27 กม.",
                  "ព្រលានយន្តហោះភ្នំពេញថ្មី ហើយនៅឆ្ងាយ។ អាកាសយានដ្ឋានតេជោ (កូដ KTI មិនមែន PNH ចាស់) បើកថ្ងៃទី 9 កញ្ញា 2025 ប្រហែល 20 គ.ម ខាងត្បូងទីក្រុង។ តាមផ្លូវទៅផ្សារធំថ្មី 27 គ.ម។", src=KTI_OPEN)),
  dict(t="facts", rows=[
    dict(k=t("Airport bus", "รถบัสสนามบิน", "ឡានក្រុងព្រលាន"), v=t("05:30–23:30 daily, via the railway station (Canadia Garden) and Monivong Blvd. Fare reported as 1,500 riel.",
          "ทุกวัน 05:30–23:30 ผ่านสถานีรถไฟและถนนมุนีวงศ์ ค่าโดยสารราว 1,500 เรียล", "រៀងរាល់ថ្ងៃ 05:30–23:30 តាមស្ថានីយ៍រថភ្លើង និងមហាវិថីព្រះមុនីវង្ស។ តម្លៃប្រហែល 1,500 រៀល។"), src=KTI_BUS),
    dict(k=t("Grab or taxi", "Grab หรือแท็กซี่", "Grab ឬតាក់ស៊ី"), v=t("About $10–21 to the centre, 30–60 minutes by traffic.", "ราว 10–21 ดอลลาร์ถึงใจกลางเมือง 30–60 นาที แล้วแต่รถติด", "ប្រហែល $10–21 ទៅកណ្ដាលក្រុង 30–60 នាទី អាស្រ័យលើចរាចរណ៍។"), src="https://cambopedia.com/how-to-get-from-techo-international-airport-to-phnom-penh/"),
    dict(k=t("On landing", "ลงเครื่องแล้ว", "ពេលចុះ"), v=t("SIM counters (Cellcard, Smart, Metfone) after baggage; bank ATMs in arrivals. Dollars work everywhere; riel is the change.",
          "เคาน์เตอร์ซิม (Cellcard, Smart, Metfone) หลังรับกระเป๋า มีตู้ ATM ที่ขาเข้า ใช้ดอลลาร์ได้ทุกที่ ทอนเป็นเรียล",
          "តូបស៊ីម (Cellcard, Smart, Metfone) ក្រោយយកឥវ៉ាន់ និង ATM នៅច្រកមកដល់។ ប្រើដុល្លារបានគ្រប់កន្លែង ប្រាក់អាប់ជារៀល។"), src=WING),
    dict(k=t("Siem Reap (SAI)", "เสียมราฐ (SAI)", "សៀមរាប (SAI)"), v=t("Also new (2023), about 50 km from town. Shuttle $8, car $35.", "ใหม่เหมือนกัน (2566) ห่างเมืองราว 50 กม. รถรับส่ง 8 ดอลลาร์ รถเหมา 35 ดอลลาร์", "ថ្មីដូចគ្នា (2023) ប្រហែល 50 គ.ម ពីទីក្រុង។ ឡានដឹក $8 ឡានឯកជន $35។"), src=SAI),
  ]),
  dict(t="ride", lat=11.362917, lng=104.916611, name="Techo International Airport"),
])

FLY = dict(id="fly", icon="i-route", h=t("Flying in and out", "บินไป บินกลับ", "ហោះទៅ ហោះមក"), blocks=[
  dict(t="region"),
  dict(t="p", **t("No airline flies Chiang Mai or Chiang Rai to Cambodia nonstop. Change in Bangkok: Suvarnabhumi (Thai, Bangkok Airways, Air Cambodia and others) or Don Mueang (Thai AirAsia). Bangkok to Phnom Penh is about 1 h 10.",
                  "ไม่มีเที่ยวบินตรงจากเชียงใหม่หรือเชียงรายไปกัมพูชา ต่อเครื่องที่กรุงเทพฯ สุวรรณภูมิ (การบินไทย บางกอกแอร์เวย์ส แอร์กัมพูชา ฯลฯ) หรือดอนเมือง (ไทยแอร์เอเชีย) กรุงเทพฯ–พนมเปญราว 1 ชม. 10 นาที",
                  "គ្មានជើងហោះត្រង់ពីឈៀងម៉ៃ ឬឈៀងរ៉ាយទៅកម្ពុជាទេ។ ប្ដូរយន្តហោះនៅបាងកក៖ សុវណ្ណភូមិ ឬដុនមឿង។ បាងកកទៅភ្នំពេញប្រហែល 1 ម៉ោង 10 នាទី។", src="https://en.wikipedia.org/wiki/Chiang_Mai_International_Airport")),
  dict(t="p", **t("Siem Reap flies straight to Bangkok: Bangkok Airways three times a day (07:40, 10:55, 17:35, about 1 h 20), Thai AirAsia to Don Mueang, Thai, and from 15 September 2026 Cambodia Airways.",
                  "เสียมราฐบินตรงกรุงเทพฯ ได้ บางกอกแอร์เวย์สวันละ 3 เที่ยว (07:40, 10:55, 17:35 ราว 1 ชม. 20 นาที) ไทยแอร์เอเชียไปดอนเมือง การบินไทย และแคมโบเดียแอร์เวย์สตั้งแต่ 15 ก.ย. 2569",
                  "សៀមរាបហោះត្រង់ទៅបាងកក៖ Bangkok Airways 3 ដងក្នុងមួយថ្ងៃ (07:40, 10:55, 17:35 ប្រហែល 1 ម៉ោង 20 នាទី) Thai AirAsia ទៅដុនមឿង និង Cambodia Airways ចាប់ពី 15 កញ្ញា 2026។", src=[PG, "https://www.aeroroutes.com/eng/260901-krsep26sai"])),
  dict(t="facts", rows=[
    dict(k=t("Phnom Penh → Siem Reap by bus", "พนมเปญ → เสียมราฐ รถบัส", "ភ្នំពេញ → សៀមរាប ឡានក្រុង"), v=t("About 6 h, from about $10 (Giant Ibis from the Night Market, Larryta, night buses with bunks). 313 km by road; no expressway yet.",
          "ราว 6 ชม. เริ่มราว 10 ดอลลาร์ (Giant Ibis จากตลาดกลางคืน, Larryta, รถนอน) ถนน 313 กม. ยังไม่มีทางด่วน", "ប្រហែល 6 ម៉ោង ចាប់ពីប្រហែល $10 (Giant Ibis ពីផ្សាររាត្រី, Larryta, ឡានយប់មានគ្រែ)។ ផ្លូវ 313 គ.ម មិនទាន់មានផ្លូវល្បឿនលឿនទេ។"), src=IBIS),
    dict(k=t("Phnom Penh → Siem Reap by air", "พนมเปญ → เสียมราฐ เครื่องบิน", "ភ្នំពេញ → សៀមរាប យន្តហោះ"), v=t("About 55 minutes (Air Cambodia, AirAsia Cambodia, Cambodia Airways 09:00 and 12:50).",
          "ราว 55 นาที (แอร์กัมพูชา แอร์เอเชียกัมพูชา แคมโบเดียแอร์เวย์ส 09:00 และ 12:50)", "ប្រហែល 55 នាទី (Air Cambodia, AirAsia Cambodia, Cambodia Airways ម៉ោង 09:00 និង 12:50)។"), src=KR),
  ]),
])

STAY = dict(id="stay", icon="i-cal", h=t("How long, and Siem Reap?", "อยู่กี่วัน ไปเสียมราฐดีไหม", "ស្នាក់ប៉ុន្មានថ្ងៃ ទៅសៀមរាបឬទេ?"), blocks=[
  dict(t="cards", cards=[
    dict(k=t("3 nights", "3 คืน", "3 យប់"), h=t("Phnom Penh only", "พนมเปญอย่างเดียว", "តែភ្នំពេញ"),
         p=t("Day one the palace, the museum and the river loop; day two the markets and a spa; day three Wat Phnom at dawn and whatever you missed. Fly in and out of KTI.",
             "วันแรกพระราชวัง พิพิธภัณฑ์ และวนริมน้ำ วันที่สองตลาดกับสปา วันที่สามวัดพนมตอนเช้าและที่ยังไม่ได้ไป เข้าออกทาง KTI",
             "ថ្ងៃទី1 វាំង សារមន្ទីរ និងដំណើរមាត់ទន្លេ។ ថ្ងៃទី2 ផ្សារ និងស្ប៉ា។ ថ្ងៃទី3 វត្តភ្នំពេលព្រឹក។ ចេញចូលតាម KTI។")),
    dict(k=t("5 nights · half a leg", "5 คืน · ครึ่งขา", "5 យប់ · ពាក់កណ្ដាលជើង"), h=t("In by Phnom Penh, out by Siem Reap", "เข้าพนมเปญ ออกเสียมราฐ", "ចូលតាមភ្នំពេញ ចេញតាមសៀមរាប"), hot=True,
         p=t("Three nights in Phnom Penh, bus or fly north, two nights in Siem Reap, then fly SAI straight to Bangkok. No backtracking. Buy a one-day Angkor pass ($37) dated for your full day: it lets you in from 16:45 the afternoon before, so you get a sunset and a sunrise.",
             "พนมเปญ 3 คืน นั่งรถหรือบินขึ้นเหนือ เสียมราฐ 2 คืน แล้วบินจาก SAI ตรงกรุงเทพฯ ไม่ต้องย้อนกลับ ซื้อบัตรนครวัด 1 วัน (37 ดอลลาร์) ลงวันที่ของวันเที่ยวเต็มวัน เข้าได้ตั้งแต่ 16:45 ของวันก่อน ได้ทั้งตะวันตกและตะวันขึ้น",
             "ភ្នំពេញ 3 យប់ ជិះឡានក្រុង ឬហោះទៅខាងជើង សៀមរាប 2 យប់ រួចហោះពី SAI ត្រង់ទៅបាងកក។ មិនបាច់ត្រឡប់ក្រោយ។ ទិញសំបុត្រអង្គរ 1 ថ្ងៃ ($37) សម្រាប់ថ្ងៃពេញ៖ ចូលបានពីម៉ោង 16:45 ល្ងាចមុន ឃើញទាំងថ្ងៃលិច និងថ្ងៃរះ។"), src=[ANGKOR, PG]),
    dict(k=t("6–7 nights · the whole leg", "6–7 คืน · เต็มขา", "6–7 យប់ · ពេញជើង"), h=t("Three and three", "สามคืนกับสามคืน", "បីយប់ និងបីយប់"),
         p=t("Three nights each, the three-day Angkor pass ($62, use within 7 days). Worth it if the temples are why you came; the far ones (Banteay Srei, Beng Mealea) need the extra day.",
             "เมืองละ 3 คืน บัตรนครวัด 3 วัน (62 ดอลลาร์ ใช้ภายใน 7 วัน) คุ้มถ้ามาเพราะปราสาท ปราสาทไกลๆ (บันทายศรี เบงเมเลีย) ต้องใช้วันเพิ่ม",
             "ក្រុងនីមួយៗ 3 យប់ សំបុត្រអង្គរ 3 ថ្ងៃ ($62 ប្រើក្នុង 7 ថ្ងៃ)។ សមនឹងទៅបើអ្នកមកដើម្បីប្រាសាទ។"), src=ANGKOR),
  ]),
  dict(t="p", **t("Our pick for a first trip from Chiang Mai: the half leg. It costs one domestic hop or a $10 bus, and saves the flight back through Phnom Penh.",
                  "ถ้ามาครั้งแรกจากเชียงใหม่ เราเลือกแบบครึ่งขา เพิ่มแค่เที่ยวบินในประเทศหรือรถบัส 10 ดอลลาร์ และไม่ต้องบินย้อนผ่านพนมเปญ",
                  "ការជ្រើសរើសរបស់យើងសម្រាប់ដំណើរដំបូងពីឈៀងម៉ៃ៖ ពាក់កណ្ដាលជើង។ ចំណាយតែជើងហោះក្នុងស្រុក ឬឡានក្រុង $10 ហើយមិនបាច់ហោះត្រឡប់តាមភ្នំពេញ។")),
])

EAT = dict(id="eat", icon="i-food", h=t("Picked", "ร้านที่เลือกไว้", "ជ្រើសរើស"), blocks=[dict(t="picks", ids=["dos-besos", "amaze-burger", "brooklyn-pizza", "arc"])])

PICKS = [
  dict(id="dos-besos", name="Dos Besos", icon="i-food", color="#f06a2c", lat=11.53709, lng=104.90694, phone="+85577977016", fb="160251091170950",
       what=t("Mexican restaurant · Street 105B, Toul Tompoung", "ร้านอาหารเม็กซิกัน · ถนน 105B ตวลทุมปูง", "ភោជនីយដ្ឋានម៉ិកស៊ិក · ផ្លូវ 105B ទួលទំពូង")),
  dict(id="amaze-burger", name="Amaze Burger", icon="i-food", color="#e2458b", lat=11.53709, lng=104.90694, phone="+85570920460", fb="617349715435101",
       what=t("Burgers · same address as Dos Besos, #13 Street 105B", "เบอร์เกอร์ · ที่อยู่เดียวกับ Dos Besos เลขที่ 13 ถนน 105B", "ប៊ឺហ្គឺ · អាសយដ្ឋានដូច Dos Besos លេខ 13 ផ្លូវ 105B")),
  dict(id="brooklyn-pizza", name="Brooklyn Pizza and Bistro", icon="i-food", color="#d99a06", lat=11.54121, lng=104.91733, phone="+85511871504", fb="564527970262271",
       what=t("Pizza · Street 123, by the Russian Market", "พิซซ่า · ถนน 123 ใกล้ตลาดรัสเซีย", "ភីហ្សា · ផ្លូវ 123 ជិតផ្សារទួលទំពូង")),
  dict(id="arc", name="ARC Start-up Accelerator", icon="i-sparkle", color="#6574ff", lat=11.61593, lng=104.90117, url=ARC,
       what=t("Start-ups · AUPP Technology Center, 4th floor, Km 6", "สตาร์ทอัพ · ศูนย์เทคโนโลยี AUPP ชั้น 4 กม. 6", "ស្តាតអាប់ · មជ្ឈមណ្ឌលបច្ចេកវិទ្យា AUPP ជាន់ទី 4 គ.ម 6"),
       line=t("Zia Bharwani's accelerator, co-founded with ChainsAtlas at the American University of Phnom Penh: three months of mentoring for Cambodian start-ups, for 5% equity.",
              "ศูนย์บ่มเพาะของ Zia Bharwani ก่อตั้งร่วมกับ ChainsAtlas ที่มหาวิทยาลัยอเมริกันแห่งพนมเปญ ให้คำปรึกษาสตาร์ทอัพกัมพูชา 3 เดือน แลกหุ้น 5%",
              "កម្មវិធីបណ្ដុះរបស់ Zia Bharwani សហការជាមួយ ChainsAtlas នៅសាកលវិទ្យាល័យអាមេរិកាំងភ្នំពេញ៖ ការណែនាំ 3 ខែ សម្រាប់ស្តាតអាប់កម្ពុជា ដោយយកភាគហ៊ុន 5%។")),
]

GAUDES = "https://asianethnology.org/article/148920-kaundinya-preah-thaong-and-the-nagi-soma-some-aspects-of-a-cambodian-legend.pdf"
PHAN = "http://www.asianscholarship.org/asf/ejourn/articles/Phan%20Anh%20Tu3.pdf"
UDANA = "https://www.accesstoinsight.org/tipitaka/kn/ud/ud.2.01.irel.html"
SMART = "https://smarthistory.org/angkor-thom/"
NATION_NAGA = "https://www.nationthailand.com/thailand/general/40021635"
OKPHANSA = "https://thailandfoundation.or.th/ok-phansa-the-end-of-buddhist-lent/"
WORK = "https://www.tandfonline.com/doi/abs/10.1080/14442213.2018.1553205"
EFEO = "https://collection.efeo.fr/ws/web/app/collection/record/218309"
NAGAWORLD = "https://www.nagaworld.com/nagaworld/"

def pair(k, kh, th, src=None):
    return dict(k=k, h=kh, p=th, src=src)

NAGA = dict(id="naga", icon="i-water", h=t("Nagas: Khmer and Thai", "นาค เขมรกับไทย", "នាគ ខ្មែរ និងថៃ"), blocks=[
  dict(t="photo", slug="wat-phnom", **t("The naga stair at Wat Phnom", "บันไดนาควัดพนม", "ជណ្ដើរនាគវត្តភ្នំ")),
  dict(t="p", **t("Both countries keep the naga at the water, the stair and the door. The stories they tell about it are different, and so is the body.",
                  "ทั้งสองประเทศมีนาคอยู่ที่น้ำ ที่บันได ที่ประตู แต่เรื่องเล่าต่างกัน รูปร่างก็ต่างกัน",
                  "ប្រទេសទាំងពីរមាននាគនៅទឹក នៅជណ្ដើរ និងនៅទ្វារ។ តែរឿងនិទាន និងរូបរាងខុសគ្នា។")),
  dict(t="h", **t("Where the naga comes from", "นาคมาจากไหน", "នាគមកពីណា")),
  dict(t="cards", cards=[
    dict(k=t("Khmer", "เขมร", "ខ្មែរ"), h=t("The naga is family", "นาคคือญาติ", "នាគជាញាតិ"), hot=True,
         p=t("Preah Thong, a prince from over the sea, marries Neang Neak, the naga king's daughter. The naga king drinks the sea to make land for them: Kampuchea. Khmer read themselves as the children of that marriage.",
             "พระทอง เจ้าชายจากโพ้นทะเล แต่งงานกับนางนาค ธิดาพญานาค พญานาคดื่มน้ำทะเลจนเกิดแผ่นดินให้ทั้งสอง คือกัมพูชา ชาวเขมรถือว่าตนเป็นลูกหลานของการแต่งงานครั้งนั้น",
             "ព្រះថោង ជាព្រះរាជបុត្រមកពីក្រៅសមុទ្រ រៀបការជាមួយនាងនាគ បុត្រីស្ដេចនាគ។ ស្ដេចនាគផឹកទឹកសមុទ្រ ធ្វើជាដីឱ្យពួកគេ៖ កម្ពុជា។ ខ្មែរចាត់ទុកខ្លួនជាកូនចៅនៃអាពាហ៍ពិពាហ៍នោះ។"), src=GAUDES),
    dict(k=t("Thai and Lanna", "ไทยและล้านนา", "ថៃ និងឡាន់ណា"), h=t("The naga is a guardian", "นาคคือผู้พิทักษ์", "នាគជាអ្នកការពារ"),
         p=t("Mucalinda coils seven times around the Buddha and spreads his hood through a seven-day storm. In the north, a naga drowns the city of Yonok after its people eat a great white eel from the Mekong.",
             "พญามุจลินท์ขดเจ็ดรอบองค์พระพุทธเจ้า แผ่พังพานกันพายุเจ็ดวัน ทางเหนือ พญานาคถล่มเมืองโยนกให้จมน้ำ หลังชาวเมืองกินปลาไหลเผือกตัวใหญ่จากแม่น้ำโขง",
             "មុចលិន្ទនាគរាជ ព័ទ្ធព្រះពុទ្ធ 7 ជុំ ហើយបាំងពពែកការពារព្យុះ 7 ថ្ងៃ។ នៅភាគខាងជើង នាគបានលិចក្រុងយោនក ក្រោយអ្នកក្រុងស៊ីអន្ទង់សដ៏ធំពីទន្លេមេគង្គ។"), src=[UDANA, PHAN]),
  ]),
  dict(t="h", **t("What it looks like", "หน้าตาเป็นอย่างไร", "រូបរាងយ៉ាងដូចម្ដេច")),
  dict(t="cards", cards=[
    dict(k=t("Khmer", "เขมร", "ខ្មែរ"), h=t("A fan of heads, in stone", "หัวแผ่เป็นพัด ทำด้วยหิน", "ក្បាលលាតដូចផ្លិត ធ្វើពីថ្ម"),
         p=t("Five, seven or nine heads open like a hood, the body laid flat along a causeway. The stone naga balustrade starts in Khmer temples, first at Bakong in the 9th century. At Angkor Thom gods and demons pull the naga to churn the sea of milk.",
             "หัวห้า เจ็ด หรือเก้าหัวแผ่เป็นพังพาน ตัววางยาวตามทางเดิน ราวบันไดนาคหินเริ่มที่ปราสาทเขมร ครั้งแรกที่บากองในศตวรรษที่ 9 ที่นครธม เทวดากับอสูรดึงนาคกวนเกษียรสมุทร",
             "ក្បាល 5 7 ឬ 9 លាតដូចពពែក ខ្លួនដេកលាតតាមផ្លូវ។ បង្កាន់ដៃនាគថ្មចាប់ផ្ដើមនៅប្រាសាទខ្មែរ ដំបូងនៅបាគង សតវត្សទី 9។ នៅអង្គរធំ ទេវតា និងអសុរទាញនាគកូរសមុទ្រទឹកដោះ។"), src=["https://www.ncpedia.org/media/seven-headed-serpent-forming", SMART]),
    dict(k=t("Thai", "ไทย", "ថៃ"), h=t("Out of the makara's mouth", "ออกมาจากปากมกร", "ចេញពីមាត់មករ"),
         p=t("On temple stairs the naga pours from the jaws of a makara, a water beast. The roof itself is naga: the bargeboards ripple like its body and end in a raised head.",
             "ที่บันไดวัด นาคพุ่งออกจากปากมกร สัตว์น้ำในตำนาน หลังคาก็เป็นนาค ลำยองพลิ้วเหมือนตัวนาค ปลายเป็นหางหงส์ชูหัวขึ้น",
             "នៅជណ្ដើរវត្ត នាគចេញពីមាត់មករ សត្វទឹក។ ដំបូលក៏ជានាគដែរ៖ ក្ដារគែមរលកដូចខ្លួននាគ ចុងជាក្បាលលើក។"), src=PHAN),
    dict(k=t("Lanna", "ล้านนา", "ឡាន់ណា"), h=t("Crests, and sometimes wings", "มีหงอน บางตัวมีปีก", "មានក្បាំង ពេលខ្លះមានស្លាប"),
         p=t("Doi Suthep's long stair is two many-headed nagas spilling from makara. Northern roofs also carry the tua luang, a winged serpent that never comes out of a makara.",
             "บันไดยาวดอยสุเทพคือนาคหลายเศียรสองตัวที่ออกจากปากมกร หลังคาทางเหนือยังมี “ตัวลวง” งูมีปีกที่ไม่เคยออกจากปากมกร",
             "ជណ្ដើរវែងនៅដូយសុទេព គឺនាគច្រើនក្បាលពីរ ចេញពីមាត់មករ។ ដំបូលខាងជើងមាន “តួលួង” ពស់មានស្លាប ដែលមិនចេញពីមករ។"), src=[PHAN, "https://blog.bangkokair.com/en/wat-phra-that-doi-suthep-chiang-mai/"]),
  ]),
  dict(t="h", **t("What people do with it", "คนทำอะไรกับนาค", "មនុស្សធ្វើអ្វីជាមួយនាគ")),
  dict(t="cards", cards=[
    dict(k=t("Khmer", "เขมร", "ខ្មែរ"), h=t("A wedding re-told", "งานแต่งเล่าเรื่องซ้ำ", "ពិធីរៀបការនិទានឡើងវិញ"),
         p=t("At a Khmer wedding the groom holds the bride's sash and follows her, as Preah Thong followed Neang Neak down into the naga realm. Neak ta, the land spirits, are a different word and a different being.",
             "ในงานแต่งเขมร เจ้าบ่าวจับผ้าสไบเจ้าสาวเดินตาม เหมือนพระทองตามนางนาคลงสู่เมืองนาค ส่วน “เนียะตา” ผีเจ้าที่ เป็นคนละคำ คนละตน",
             "នៅពិធីរៀបការខ្មែរ កូនកំលោះកាន់ស្បៃកូនក្រមុំដើរតាម ដូចព្រះថោងតាមនាងនាគចុះទៅនគរនាគ។ អ្នកតា ជាពាក្យផ្សេង និងជាអង្គផ្សេង។"), src=[GAUDES, WORK]),
    dict(k=t("Thai", "ไทย", "ថៃ"), h=t("Fireballs, lottery, ordination", "บั้งไฟ หวย บวช", "បាល់ភ្លើង ឆ្នោត បួស"),
         p=t("At the end of Buddhist Lent the Mekong sends up the naga's fireballs. People ask Phaya Nak for lottery numbers. A man waiting to be ordained is called nak, after the naga who once took human form to become a monk. Since 2022 the naga is Thailand's national mythical creature.",
             "วันออกพรรษามีบั้งไฟพญานาคขึ้นจากแม่น้ำโขง คนขอหวยจากพญานาค ผู้ที่รอบวชเรียกว่า “นาค” ตามนาคที่แปลงเป็นคนมาขอบวช ตั้งแต่ปี 2565 นาคเป็นสัตว์ในตำนานประจำชาติไทย",
             "ថ្ងៃចេញព្រះវស្សា ទន្លេមេគង្គបញ្ចេញបាល់ភ្លើងនាគ។ មនុស្សសុំលេខឆ្នោតពីនាគ។ អ្នករង់ចាំបួសហៅថា “នាគ” តាមនាគដែលប្រែជាមនុស្សមកបួស។ ចាប់ពីឆ្នាំ 2022 នាគជាសត្វទេវកថាជាតិថៃ។"), src=[OKPHANSA, NATION_NAGA]),
  ]),
  dict(t="h", **t("Nagas in Phnom Penh", "นาคในพนมเปญ", "នាគនៅភ្នំពេញ")),
  dict(t="p", **t("The east stair of Wat Phnom; the naga heads on the five tiers of the Independence Monument; the Naga Fountain in the garden beside it. In 1892 a Naga Bridge crossed the canal south of Wat Phnom; the canal is gone. NagaWorld takes its name from a seven-headed naga the company says guards the rivers of the city.",
                  "บันไดทิศตะวันออกของวัดพนม หัวนาคบนห้าชั้นของอนุสาวรีย์เอกราช น้ำพุนาคในสวนข้างๆ ปี 1892 มีสะพานนาคข้ามคลองทางใต้วัดพนม ตอนนี้คลองไม่มีแล้ว ส่วนนาคาเวิลด์ตั้งชื่อตามนาคเจ็ดเศียรที่บริษัทบอกว่าเฝ้าแม่น้ำของเมือง",
                  "ជណ្ដើរខាងកើតវត្តភ្នំ ក្បាលនាគលើថ្នាក់ទាំង 5 នៃវិមានឯករាជ្យ និងទឹកពុលនាគក្នុងសួនក្បែរនោះ។ ឆ្នាំ 1892 មានស្ពាននាគឆ្លងព្រែកខាងត្បូងវត្តភ្នំ ព្រែកនោះលែងមានហើយ។ NagaWorld យកឈ្មោះតាមនាគ 7 ក្បាល ដែលក្រុមហ៊ុននិយាយថាការពារទន្លេរបស់ទីក្រុង។",
                  src=["https://en.wikipedia.org/wiki/Independence_Monument_(Cambodia)", EFEO, NAGAWORLD])),
  dict(t="photo", slug="hero-dusk", **t("The Naga Fountain garden at dusk", "สวนน้ำพุนาคยามเย็น", "សួនទឹកពុលនាគពេលល្ងាច")),
])

NUMBEO = ["https://www.numbeo.com/cost-of-living/in/Phnom-Penh", "https://www.numbeo.com/cost-of-living/in/Chiang-Mai"]
RATES = dict(thb=33.57, khr=4056, date="2026-09-29",
             src=["https://www.nbc.gov.kh/english/economic_research/exchange_rate.php", "https://api.frankfurter.dev/v1/latest?base=USD&symbols=THB"])
CITIES = dict(pp=t("Phnom Penh", "พนมเปญ", "ភ្នំពេញ"), cm=t("Chiang Mai", "เชียงใหม่", "ឈៀងម៉ៃ"))
WORDS = dict(same=t("about the same", "พอๆ กัน", "ប្រហាក់ប្រហែល"), cheaper=t("cheaper", "ถูกกว่า", "ថោកជាង"))

def pr(icon, item, pp, cm, unit=None, note=None, src=NUMBEO):
    return dict(icon=icon, item=item, pp=pp, cm=cm, unit=unit, note=note, src=src)

PRICES = [
  pr("i-food", t("Cheap meal", "อาหารจานถูก", "អាហារថោក"), 4.00, 2.09),
  pr("i-food", t("Dinner for two", "มื้อค่ำสองคน", "អាហារពេលល្ងាចពីរនាក់"), 39.80, 19.36, t("mid-range", "ร้านระดับกลาง", "កម្រិតមធ្យម")),
  pr("i-coffee", t("Cappuccino", "คาปูชิโน", "កាពូឈីណូ"), 2.95, 1.73),
  pr("i-beer", t("Draught beer", "เบียร์สด", "ស្រាបៀរស្រស់"), 1.25, 2.38, t("0.5 L, local", "0.5 ลิตร ยี่ห้อในประเทศ", "0.5 លីត្រ ក្នុងស្រុក")),
  pr("i-beer", t("Imported beer", "เบียร์นอก", "ស្រាបៀរនាំចូល"), 3.00, 3.80, t("0.33 L", "0.33 ลิตร", "0.33 លីត្រ")),
  pr("i-basket", t("Water", "น้ำดื่ม", "ទឹក"), 0.75, 0.52, t("1.5 L", "1.5 ลิตร", "1.5 លីត្រ")),
  pr("i-basket", t("Eggs", "ไข่", "ពង"), 1.72, 2.21, t("12", "12 ฟอง", "12 គ្រាប់")),
  pr("i-basket", t("Chicken", "ไก่", "សាច់មាន់"), 4.17, 2.83, t("1 kg fillet", "อก 1 กก.", "1 គ.ក")),
  pr("i-basket", t("Bananas", "กล้วย", "ចេក"), 1.74, 1.07, t("1 kg", "1 กก.", "1 គ.ក")),
  pr("i-tag", t("Marlboro", "มาร์ลโบโร", "ម៉ាលបូរ៉ូ"), 1.89, 4.25, t("20", "1 ซอง", "1 កញ្ចប់")),
  pr("i-home2", t("One-bedroom flat", "ห้องหนึ่งห้องนอน", "ផ្ទះមួយបន្ទប់គេង"), 630, 476, t("city centre, a month", "ใจกลางเมือง ต่อเดือน", "កណ្ដាលក្រុង ក្នុងមួយខែ")),
  pr("i-fit", t("Gym", "ฟิตเนส", "កន្លែងហាត់ប្រាណ"), 40.62, 39.05, t("a month", "ต่อเดือน", "ក្នុងមួយខែ")),
  pr("i-fuel", t("Petrol", "น้ำมันเบนซิน", "សាំង"), 1.29, 1.21, t("a litre", "ต่อลิตร", "ក្នុងមួយលីត្រ"),
     t("Cambodia's Gasoline 92 ceiling for 21 Sep–1 Oct 2026 against PTT Gasohol 95 in Chiang Mai, 24 Sep.", "เพดานราคาเบนซิน 92 ของกัมพูชา 21 ก.ย.–1 ต.ค. 2569 เทียบแก๊สโซฮอล์ 95 ของ ปตท. เชียงใหม่ 24 ก.ย.", "តម្លៃពិដានសាំង 92 កម្ពុជា 21 កញ្ញា–1 តុលា 2026 ធៀបនឹង Gasohol 95 PTT ឈៀងម៉ៃ 24 កញ្ញា។"),
     ["https://data.mef.gov.kh/api/v1/public-datasets/pd_681d89b4dbc953000126f5e7/json", "https://www.pttor.com/en/oil_price"]),
  pr("i-fuel", t("Diesel", "ดีเซล", "ម៉ាស៊ូត"), 1.50, 1.26, t("a litre", "ต่อลิตร", "ក្នុងមួយលីត្រ"), None,
     ["https://data.mef.gov.kh/api/v1/public-datasets/pd_681d89b4dbc953000126f5e7/json", "https://www.pttor.com/en/oil_price"]),
  pr("i-ride", t("5 km on Grab", "Grab 5 กม.", "Grab 5 គ.ម"), 2.76, 2.53, None,
     t("GrabTukTuk in Phnom Penh against GrabCar Economy in Chiang Mai.", "GrabTukTuk ในพนมเปญ เทียบ GrabCar Economy ในเชียงใหม่", "GrabTukTuk នៅភ្នំពេញ ធៀបនឹង GrabCar Economy នៅឈៀងម៉ៃ។"),
     ["https://asiatoday.co/2026/04/27/tuk-tuk-drivers-protest-in-phnom-penh-over-grab-fare-cuts/", "https://www.taxifarefinder.com/main.php?city=GrabCar-Economy-Chiang-Mai-Thailand"]),
  pr("i-phone", t("Visitor SIM, 30 days", "ซิมนักท่องเที่ยว 30 วัน", "ស៊ីមទេសចរ 30 ថ្ងៃ"), 20, 35.72, None,
     t("Cellcard 30 GB against True unlimited 5G. Cellcard's ordinary prepaid plan is $6 for 90 GB.", "Cellcard 30 GB เทียบ True ไม่จำกัด 5G แพ็กเติมเงินปกติของ Cellcard 6 ดอลลาร์ ได้ 90 GB", "Cellcard 30 GB ធៀប True គ្មានដែនកំណត់ 5G។ គម្រោងធម្មតា Cellcard $6 បាន 90 GB។"),
     ["https://www.cellcard.com.kh/", "https://www.true.th/en/prepaid/sim/tourist"]),  # stylecheck: allow (URL)
  pr("i-atm", t("ATM, foreign card", "กดเงิน บัตรต่างประเทศ", "ដកប្រាក់ កាតបរទេស"), 5, 7.45, t("per withdrawal", "ต่อครั้ง", "ក្នុងមួយដង"),
     t("About $5 at ACLEDA or Canadia; Krungsri charges ฿250 for Visa and ฿350 for Mastercard since March 2026.", "ราว 5 ดอลลาร์ที่ ACLEDA หรือ Canadia กรุงศรีคิด 250 บาทสำหรับวีซ่า 350 บาทสำหรับมาสเตอร์การ์ด ตั้งแต่มีนาคม 2569", "ប្រហែល $5 នៅ ACLEDA ឬ Canadia។ Krungsri គិត ฿250 សម្រាប់ Visa និង ฿350 សម្រាប់ Mastercard ចាប់ពីខែមីនា 2026។"),
     ["https://www.you.co/sg/blog/cambodia-atm-withdrawal-guide/", "https://www.krungsri.com/getmedia/546f2617-8522-47b8-9b06-6c2cb49f32d0/fee-withdrawal-via-atm-for-international-card-11032026-en"]),
]

PRICE_SEC = dict(id="prices", icon="i-coin", h=t("Prices: Phnom Penh and Chiang Mai", "ราคา พนมเปญกับเชียงใหม่", "តម្លៃ ភ្នំពេញ និងឈៀងម៉ៃ"), blocks=[
  dict(t="p", **t("Phnom Penh prices in dollars, Chiang Mai in baht, both turned into one currency at the 29 September rate ($1 = ฿33.57 = 4,056 riel). Food and rent come from Numbeo, which people fill in themselves.",
                  "พนมเปญคิดเป็นดอลลาร์ เชียงใหม่เป็นบาท แปลงเป็นสกุลเดียวที่อัตรา 29 กันยายน (1 ดอลลาร์ = 33.57 บาท = 4,056 เรียล) ราคาอาหารและค่าเช่ามาจาก Numbeo ที่ผู้ใช้กรอกเอง",
                  "តម្លៃភ្នំពេញជាដុល្លារ ឈៀងម៉ៃជាបាត ប្ដូរជារូបិយប័ណ្ណតែមួយតាមអត្រា 29 កញ្ញា ($1 = ฿33.57 = 4,056 រៀល)។ តម្លៃម្ហូប និងជួលផ្ទះមកពី Numbeo ដែលអ្នកប្រើបំពេញខ្លួនឯង។", src=RATES["src"] + NUMBEO)),
  dict(t="cards", cards=[
    dict(k=t("Cheaper in Chiang Mai", "ถูกกว่าที่เชียงใหม่", "ថោកជាងនៅឈៀងម៉ៃ"), h=t("Food, coffee, fuel, rent", "อาหาร กาแฟ น้ำมัน ค่าเช่า", "ម្ហូប កាហ្វេ សាំង ជួលផ្ទះ"), hot=True,
         p=t("A cheap meal costs about half, a cappuccino 40% less. Diesel is cheaper in Thailand. A central one-bedroom rents for less in Chiang Mai than in Phnom Penh.",
             "อาหารจานถูกราคาราวครึ่งเดียว คาปูชิโนถูกกว่า 40% ดีเซลไทยถูกกว่า ห้องหนึ่งห้องนอนกลางเมืองเชียงใหม่ถูกกว่าพนมเปญ",
             "អាហារថោកតម្លៃប្រហែលពាក់កណ្ដាល កាពូឈីណូថោកជាង 40%។ ម៉ាស៊ូតនៅថៃថោកជាង។ ផ្ទះមួយបន្ទប់កណ្ដាលក្រុងឈៀងម៉ៃថោកជាងភ្នំពេញ។")),
    dict(k=t("Cheaper in Phnom Penh", "ถูกกว่าที่พนมเปญ", "ថោកជាងនៅភ្នំពេញ"), h=t("Draught beer, cigarettes, cash", "เบียร์สด บุหรี่ กดเงิน", "ស្រាបៀរស្រស់ បារី ដកប្រាក់"),
         p=t("Draught beer is about half the Chiang Mai price and a pack of Marlboro less than half. A foreign-card ATM withdrawal costs less than at a Thai bank.",
             "เบียร์สดราคาราวครึ่งหนึ่งของเชียงใหม่ มาร์ลโบโรไม่ถึงครึ่ง กดเงินด้วยบัตรต่างประเทศถูกกว่าตู้ธนาคารไทย",
             "ស្រាបៀរស្រស់តម្លៃប្រហែលពាក់កណ្ដាលនៃឈៀងម៉ៃ ម៉ាលបូរ៉ូតិចជាងពាក់កណ្ដាល។ ដកប្រាក់ដោយកាតបរទេសថោកជាងធនាគារថៃ។")),
    dict(k=t("Dollars", "ดอลลาร์", "ដុល្លារ"), h=t("Priced in dollars, changed in riel", "ตั้งราคาเป็นดอลลาร์ ทอนเป็นเรียล", "តម្លៃជាដុល្លារ អាប់ជារៀល"),
         p=t("Restaurants, visas, SIMs and the Angkor pass are priced in US dollars. Fuel, electricity and Grab tuk-tuks run in riel.",
             "ร้านอาหาร วีซ่า ซิม และบัตรนครวัดตั้งราคาเป็นดอลลาร์ น้ำมัน ไฟฟ้า และตุ๊กตุ๊ก Grab คิดเป็นเรียล",
             "ភោជនីយដ្ឋាន ទិដ្ឋាការ ស៊ីម និងសំបុត្រអង្គរ គិតជាដុល្លារ។ សាំង អគ្គិសនី និងរ៉ឺម៉ក Grab គិតជារៀល។")),
  ]),
  dict(t="prices"),
])

KENT = "https://www.newmandala.org/the-desertion-of-cambodias-spirits/"
ANG = "https://www.aefek.fr/wa_files/angchoulean1.pdf"
CMAG = "https://www.cambodgemag.com/en/post/cambodia-tradition-cambodian-spirit-houses"
SANPHUM = "https://th.wikipedia.org/wiki/%E0%B8%A8%E0%B8%B2%E0%B8%A5%E0%B8%9E%E0%B8%A3%E0%B8%B0%E0%B8%A0%E0%B8%B9%E0%B8%A1%E0%B8%B4"
BAAN = "https://baanlaesuan.com/279892/maintenance/spirit-house-difference"
LPRU = "https://culture.lpru.ac.th/WebCulture2553/CultureKnowledge/file/06-01.pdf"

SPIRITS = dict(id="spirits", icon="i-home2", h=t("Spirit houses: why the Khmer ones look empty", "ศาลพระภูมิ ทำไมศาลเขมรดูว่างเปล่า", "ផ្ទះអ្នកតា ហេតុអ្វីរបស់ខ្មែរមើលទៅទទេ"), blocks=[
  dict(t="p", **t("In Thailand you buy a spirit house with its people: a guardian figure, servants, dancers, an elephant and a horse. In Cambodia the little house by the gate often holds only incense, fruit and a garland. The two houses are built for different beings.",
                  "ในไทย ซื้อศาลพระภูมิมาพร้อมตุ๊กตา เจ้าที่ คนรับใช้ นางรำ ช้าง ม้า ในกัมพูชา ศาลเล็กๆ ข้างประตูมักมีแค่ธูป ผลไม้ และพวงมาลัย เพราะศาลสองแบบสร้างให้คนละตน",
                  "នៅថៃ គេទិញផ្ទះព្រះភូមិមកជាមួយរូបតុក្កតា៖ អ្នកការពារ អ្នកបម្រើ អ្នករាំ ដំរី និងសេះ។ នៅកម្ពុជា ផ្ទះតូចក្បែរទ្វារច្រើនតែមានធូប ផ្លែឈើ និងកម្រងផ្កា។ ផ្ទះទាំងពីរសាងសង់សម្រាប់អង្គផ្សេងគ្នា។")),
  dict(t="cards", cards=[
    dict(k=t("Thai", "ไทย", "ថៃ"), h=t("A named god, with a court", "เทพมีชื่อ มีบริวาร", "ទេវតាមានឈ្មោះ មានបរិវារ"), hot=True,
         p=t("The san phra phum, on one post, houses Phra Phum, one of nine sons a king sent to guard the land; Phra Chaimongkhon keeps houses and shops. He is shown as an image, so he gets servants, soldiers, elephants and horses. The lower san chao thi on four or more posts is for the ancestors and earlier owners of the land.",
             "ศาลพระภูมิเสาเดียวเป็นที่สถิตของพระภูมิ หนึ่งในโอรสเก้าองค์ที่ท้าวทศราชส่งไปเฝ้าแผ่นดิน พระชัยมงคลดูแลบ้านและร้านค้า ท่านมีรูป จึงมีบริวาร ทหาร ช้าง ม้า ส่วนศาลเจ้าที่ที่เตี้ยกว่า มีสี่เสาขึ้นไป เป็นที่อยู่ของบรรพบุรุษและเจ้าของที่เดิม",
             "ផ្ទះព្រះភូមិលើសសរមួយ ជាទីគង់របស់ព្រះភូមិ ជាបុត្រមួយក្នុងចំណោមប្រាំបួនដែលស្ដេចបញ្ជូនឱ្យការពារដី។ លោកមានរូប ដូច្នេះមានអ្នកបម្រើ ទាហាន ដំរី និងសេះ។ ផ្ទះទាបលើសសរ 4 ឬច្រើន សម្រាប់ដូនតា និងម្ចាស់ដីមុន។"), src=[SANPHUM, BAAN]),
    dict(k=t("Khmer", "เขมร", "ខ្មែរ"), h=t("The spirit is already there", "ผีอยู่ที่นั่นอยู่แล้ว", "អ្នកតានៅទីនោះរួចហើយ"),
         p=t("Neak ta, the owners of the land and water, live in a tree, a rock, a termite mound, an old piece of sculpture, or in no visible form. The hut shelters that place or receives the offerings; there is no image to put inside. A village keeps its neak ta a hut, often to the northeast; a household honours its tevoda with offerings in front.",
             "เนียะตา เจ้าของแผ่นดินและน้ำ อยู่ในต้นไม้ ก้อนหิน จอมปลวก ชิ้นประติมากรรมเก่า หรือไม่มีรูปให้เห็น ศาลมีไว้คุ้มที่นั้นหรือรับเครื่องเซ่น ไม่มีรูปให้ใส่ หมู่บ้านสร้างศาลให้เนียะตา มักทางทิศตะวันออกเฉียงเหนือ ในบ้านบูชาเทวดาโดยวางของไหว้ไว้ข้างหน้า",
             "អ្នកតា ជាម្ចាស់ដី និងទឹក នៅក្នុងដើមឈើ ថ្ម ដំបូក បំណែករូបចម្លាក់ចាស់ ឬគ្មានរូបមើលឃើញ។ ខ្ទមការពារកន្លែងនោះ ឬទទួលតង្វាយ គ្មានរូបដាក់ខាងក្នុងទេ។ ភូមិធ្វើខ្ទមអ្នកតា ច្រើននៅទិសឦសាន។ ក្នុងផ្ទះ គេគោរពទេវតាដោយដាក់តង្វាយពីមុខ។"), src=[KENT, ANG, CMAG]),
    dict(k=t("Lanna", "ล้านนา", "ឡាន់ណា"), h=t("Closer to the Khmer way", "ใกล้แบบเขมร", "ជិតនឹងរបៀបខ្មែរ"),
         p=t("The san phra phum came late to the north. A northern house keeps a plain ho phi pu ya for its ancestors, facing east or north: a place to meet them, since they live in the upper realm, not a home to fill.",
             "ศาลพระภูมิมาถึงภาคเหนือทีหลัง บ้านล้านนามีหอผีปู่ย่าเรียบๆ หันทิศตะวันออกหรือทิศเหนือ เป็นที่พบบรรพบุรุษ เพราะท่านอยู่เมืองบน ไม่ใช่บ้านที่ต้องใส่ของให้เต็ม",
             "ផ្ទះព្រះភូមិមកដល់ភាគខាងជើងយឺត។ ផ្ទះនៅឡាន់ណាមានហោផីពូយ៉ាសាមញ្ញសម្រាប់ដូនតា បែរទៅទិសកើត ឬជើង៖ ជាកន្លែងជួប ព្រោះដូនតានៅស្ថានលើ មិនមែនជាផ្ទះដែលត្រូវដាក់ឱ្យពេញ។"), src=[LPRU, SANPHUM]),
  ]),
  dict(t="photo", slug="spirit-thai", **t("A san phra phum and a san chao thi, Bangkok", "ศาลพระภูมิและศาลเจ้าที่ กรุงเทพฯ", "ផ្ទះព្រះភូមិ និងផ្ទះអ្នកតា បាងកក")),
  dict(t="photo", slug="spirit-khmer", **t("The spirit house at Phnom Nham Lea", "ศาลที่พนมญำเลีย", "ខ្ទមអ្នកតា នៅ Phnom Nham Lea")),
])

ROOMCHANG = "https://www.roomchang.com/en"
USEMB_MED = "https://kh.usembassy.gov/medical-assistance/"
AUEMB = "https://cambodia.embassy.gov.au/penh/MedicalServiceProviders.html"
SDC = "https://www.sittiporndental.com/en/prices/"
KITCHA = "https://www.kitchadentalclinic.com/prices/"
COUNCIL = "https://data.opendevelopmentcambodia.net/laws_record/royal-decree-on-the-establishment-of-dental-council"
CDAILY = "https://english.cambodiadaily.com/2008/06/18/dentists-must-register-or-risk-closure-govt/"
CDC_V = "https://www.cdc.gov/vibrio/prevention/index.html"
FSANZ = "https://www.foodstandards.gov.au/sites/default/files/2023-11/Bivalve%20molluscs%20and%20Hepatitis%20A.pdf"
TOPAZ = "https://www.cambodgemag.com/en/post/topaz-brings-marennes-ol%C3%A9ron-oysters-to-norodom-boulevard"
SOFITEL = "https://www.sofitel-phnompenh-phokeethra.com/restaurants-bars/la-coupole/"
PNTD = "https://journals.plos.org/plosntds/article?id=10.1371%2Fjournal.pntd.0014353"

HEALTH = dict(id="teeth", icon="i-health", h=t("Teeth and oysters", "ทำฟันกับหอยนางรม", "ធ្មេញ និងងាវ"), blocks=[
  dict(t="h", **t("Is Phnom Penh good for dentistry?", "พนมเปญทำฟันดีไหม", "ភ្នំពេញល្អសម្រាប់ព្យាបាលធ្មេញទេ?")),
  dict(t="p", **t("Patients fly in for it, mostly from Australia, Japan and Singapore. From Chiang Mai the saving mostly disappears: cleanings, fillings and root canals cost about the same, zirconia crowns were cheaper on Chiang Mai clinics' published lists, and a top-brand implant with its crown runs close to the same in both cities.",
                  "มีคนบินมาทำฟัน ส่วนใหญ่จากออสเตรเลีย ญี่ปุ่น สิงคโปร์ แต่ถ้ามาจากเชียงใหม่ แทบไม่ประหยัด ขูดหินปูน อุดฟัน รักษารากฟันราคาพอๆ กัน ครอบฟันเซอร์โคเนียตามราคาที่คลินิกเชียงใหม่ประกาศถูกกว่า รากเทียมยี่ห้อดีพร้อมครอบราคาใกล้กัน",
                  "មានអ្នកជំងឺហោះមក ភាគច្រើនពីអូស្ត្រាលី ជប៉ុន សិង្ហបុរី។ ពីឈៀងម៉ៃ ការសន្សំស្ទើរតែគ្មាន៖ សម្អាត បំពេញ ព្យាបាលឫស តម្លៃប្រហាក់ប្រហែល ក្រោនហ្ស៊ីកូនៀថោកជាងនៅឈៀងម៉ៃ ហើយឫសធ្មេញសិប្បនិម្មិតម៉ាកល្អ តម្លៃជិតគ្នា។", src=[ROOMCHANG, SDC, KITCHA])),
  dict(t="facts", rows=[
    dict(k=t("Crown", "ครอบฟัน", "ក្រោន"), v=t("Phnom Penh $512–600 · Chiang Mai zirconia from $357", "พนมเปญ 512–600 ดอลลาร์ · เชียงใหม่ เซอร์โคเนีย เริ่ม 357 ดอลลาร์", "ភ្នំពេញ $512–600 · ឈៀងម៉ៃ ហ្ស៊ីកូនៀ ចាប់ពី $357"), src=[ROOMCHANG, SDC]),
    dict(k=t("Implant with crown", "รากเทียมพร้อมครอบ", "ឫសសិប្បនិម្មិត និងក្រោន"), v=t("Phnom Penh about $2,400 · Chiang Mai $1,220–2,232 by brand. Ask for the price in writing.", "พนมเปญราว 2,400 ดอลลาร์ · เชียงใหม่ 1,220–2,232 ดอลลาร์ แล้วแต่ยี่ห้อ ขอใบเสนอราคาเป็นลายลักษณ์อักษร", "ភ្នំពេញប្រហែល $2,400 · ឈៀងម៉ៃ $1,220–2,232 តាមម៉ាក។ សុំតម្លៃជាលាយលក្ខណ៍អក្សរ។"), src=[ROOMCHANG, SDC, KITCHA]),
    dict(k=t("Who is licensed", "ใครมีใบอนุญาต", "អ្នកណាមានអាជ្ញាប័ណ្ណ"), v=t("Cambodia has had a Dental Council since 2006. In 2008 the Ministry of Health said most dental offices were unregistered. The US and Australian embassies both list Roomchang and the European Dental Clinic.",
          "กัมพูชามีสภาทันตแพทย์ตั้งแต่ปี 2549 ปี 2551 กระทรวงสาธารณสุขบอกว่าร้านทำฟันส่วนใหญ่ไม่ได้จดทะเบียน สถานทูตสหรัฐฯ และออสเตรเลียต่างก็มีชื่อรูมชางและ European Dental Clinic",
          "កម្ពុជាមានក្រុមប្រឹក្សាទន្តសាស្ត្រតាំងពីឆ្នាំ 2006។ ឆ្នាំ 2008 ក្រសួងសុខាភិបាលថា ភាគច្រើនមិនបានចុះបញ្ជី។ ស្ថានទូតអាមេរិក និងអូស្ត្រាលីដាក់ឈ្មោះ Roomchang និង European Dental Clinic។"), src=[COUNCIL, CDAILY, USEMB_MED, AUEMB]),
  ]),
  dict(t="ride", lat=11.56321, lng=104.92554, name="Roomchang Dental Hospital"),
  dict(t="h", **t("Raw oysters in a good restaurant?", "กินหอยนางรมดิบในร้านหรูได้ไหม", "ញ៉ាំងាវឆៅនៅភោជនីយដ្ឋានល្អបានទេ?")),
  dict(t="p", **t("The places that serve them fly them in from France: Marennes-Oléron and Fines de Claire. Topaz on Norodom Boulevard brought in Marennes-Oléron oysters this September, served gratinéed; Sofitel's La Coupole puts French oysters on its Sunday brunch.",
                  "ร้านที่มีขายนำเข้าจากฝรั่งเศส เช่น Marennes-Oléron และ Fines de Claire ร้าน Topaz ถนนนโรดมนำเข้า Marennes-Oléron เมื่อกันยายนนี้ เสิร์ฟแบบอบชีส La Coupole ของโซฟิเทลมีหอยนางรมฝรั่งเศสในบุฟเฟต์บรันช์วันอาทิตย์",
                  "កន្លែងដែលលក់ នាំចូលពីបារាំង៖ Marennes-Oléron និង Fines de Claire។ Topaz នៅមហាវិថីព្រះនរោត្តម នាំចូលក្នុងខែកញ្ញានេះ ហើយដុតឱ្យឆ្អិន។ La Coupole របស់ Sofitel មានងាវបារាំងក្នុងអាហារថ្ងៃអាទិត្យ។", src=[TOPAZ, SOFITEL])),
  dict(t="p", **t("What an expensive room cannot change: cold does not kill hepatitis A in an oyster, and heat does (90 °C for 90 seconds). The US CDC advises against raw or undercooked oysters because of Vibrio, which is most dangerous to people with liver disease, diabetes, cancer or weak immunity. A 2026 study from eastern Thailand's coast found raw oysters there widely contaminated.",
                  "สิ่งที่ร้านแพงเปลี่ยนไม่ได้ ความเย็นไม่ฆ่าไวรัสตับอักเสบเอในหอย ความร้อนฆ่าได้ (90 องศา 90 วินาที) CDC สหรัฐฯ แนะนำไม่ให้กินหอยนางรมดิบหรือไม่สุก เพราะเชื้อวิบริโอ อันตรายที่สุดกับคนเป็นโรคตับ เบาหวาน มะเร็ง หรือภูมิคุ้มกันต่ำ งานวิจัยปี 2569 จากชายฝั่งภาคตะวันออกของไทยพบหอยนางรมดิบปนเปื้อนมาก",
                  "អ្វីដែលភោជនីយដ្ឋានថ្លៃមិនអាចប្ដូរ៖ ភាពត្រជាក់មិនសម្លាប់ជំងឺរលាកថ្លើម A ក្នុងងាវទេ តែកម្ដៅសម្លាប់បាន (90 °C រយៈពេល 90 វិនាទី)។ CDC អាមេរិកណែនាំកុំញ៉ាំងាវឆៅ ដោយសារ Vibrio ដែលគ្រោះថ្នាក់បំផុតចំពោះអ្នកមានជំងឺថ្លើម ទឹកនោមផ្អែម មហារីក ឬភាពស៊ាំខ្សោយ។ ការសិក្សាឆ្នាំ 2026 នៅឆ្នេរភាគខាងកើតថៃ រកឃើញងាវឆៅមានមេរោគច្រើន។", src=[FSANZ, CDC_V, PNTD])),
  dict(t="ride", lat=11.54846, lng=104.92849, name="Topaz Restaurant"),
])
