"""All site content, extracted from trimlinemedicals.com (Nov 2026) and cleaned up."""

IMG = "https://trimlinemedicals.com/images/"  # change to "images/" after running fetch-images.sh

COMPANY = {
    "name": "Trimline Medical Systems",
    "tagline": "Medical Equipments & Instruments",
    "address": ["Plot No. 3, Flat No. G1, Venkateshwara Street", "Dhanalakshmi Colony, Vadapalani", "Chennai – 600 026"],
    "phone": "044 2362 4880",
    "phone_href": "+914423624880",
    "fax": "044 2362 4881",
    "email": "contact@trimlinemedicalsystems.com",
    "map": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3886.6807694492563!2d80.20752361482289!3d13.055980490800568!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a52675e3b4c8771%3A0xbdd06def426e3952!2sTrimline+Medical+Systems!5e0!3m2!1sen!2sin!4v1524649924188",
    "map_link": "https://www.google.com/maps/search/?api=1&query=Trimline+Medical+Systems+Vadapalani+Chennai",
}

PRINCIPALS = [
    ("Skanray Technologies", "India", "Patient monitoring, surgical diathermy, X-ray & C-arm"),
    ("Getinge – MAQUET Medical", "Sweden", "Anaesthesia, ventilation, OR lights & tables"),
    ("ATMOS", "Germany", "ENT workstations"),
    ("ZOLL Medical", "USA", "Defibrillators & resuscitation"),
    ("Magnatek Enterprises", "India", "Magnaled surgical lights"),
    ("Nice Neotech Medical Systems", "India", "Neonatal warmers, incubators & phototherapy"),
    ("Medec Benelux NV", "Belgium", "Anaesthesia workstations"),
]

WHY = [
    ("doc", "Well documented", "Every installation is handed over with clear documentation, so your team knows the equipment from day one."),
    ("wrench", "Free maintenance", "Preventive maintenance included, keeping critical equipment ready when it matters."),
    ("refresh", "Free updates", "Software and firmware updates at no extra cost, through the life of the system."),
    ("shield", "Solid support", "A responsive service team in Chennai, backed directly by our global principals."),
    ("bolt", "Simple installation", "Planned, installed and commissioned by trained engineers with minimal disruption."),
    ("check", "Genuine equipment", "Authorised partner of world-leading manufacturers from Sweden, Germany, USA, Belgium and India."),
]

# Each category: slug, title, short, icon, legacy php path, intro, groups[(group title, [products])]
# Product: dict(name, img (optional), points [..], brand (optional))
CATEGORIES = [
    {
        "slug": "patient-monitoring", "title": "Patient Monitoring", "icon": "pulse", "legacy": "patient-monitoring.php",
        "short": "Pulse oximeters, multipara monitors and central stations.",
        "intro": "From a bedside pulse oximeter to a 16-bed central nursing station — Skanray monitoring that scales from ward to ICU and OT.",
        "groups": [
            ("Pulse Oximeter", [
                dict(name="Comet Plus", brand="Skanray", img="cp.png", points=["Nellcor pulse oximetry with plethysmograph", "Online SpO₂ and pulse-rate trend graphs", "Alarm system with SatSeconds", "Adult, paediatric and neonatal use"]),
            ]),
            ("Basic Multipara Monitors", [
                dict(name="Planet 45", brand="Skanray", img="p45.png", points=["4-channel, 10.4\" backlit LED display", "ECG, Resp, NIBP, SpO₂ (Oxyskan), Temp", "ST-segment analysis & arrhythmia detection", "Advanced alarm system"]),
                dict(name="Planet 60", brand="Skanray", img="p60.png", points=["6-channel, 10.4\" backlit LED display", "ECG, Resp, NIBP, SpO₂ (Nellcor), Temp", "ST analysis, arrhythmia detection, SatSeconds", "Optional Wi-Fi to central nursing station"]),
            ]),
            ("Pre-configured Multipara Monitors", [
                dict(name="Star 60", brand="Skanray", img="s60.png", points=["6-channel, 10.4\" backlit LED display", "ECG, Resp, dual Temp, NIBP, SpO₂ (Nellcor), IBP", "Upgradeable to Microstream EtCO₂ with IPI", "ST analysis & arrhythmia detection"]),
                dict(name="Star 65", brand="Skanray", img="s65.png", points=["8-channel modular, 12.1\" XGA touchscreen", "Plug-in EtCO₂, IBP, cardiac output, anaesthetic gas", "Optional 2-channel thermal printer", "USB, HDMI, Ethernet and Wi-Fi"]),
                dict(name="Star 90", brand="Skanray", img="s90.png", points=["10-channel, 15\" colour touchscreen", "Built-in rack for external modules", "CO, NiCCO, EtCO₂ with IPI options", "Wired / wireless to Skanray central station"]),
            ]),
            ("Central Monitoring", [
                dict(name="Skyline 55", brand="Skanray", img="skyline01.png", points=["Windows-based central station for 8 or 16 beds", "Wired and wireless monitor connectivity", "Multi-parameter, multi-bed views", "Up to 72 hours of waveform review"]),
                dict(name="Skyview", brand="Skanray", img="skyview.png", points=["Remote monitoring over LAN or web", "Secure access to patient data", "30-day waveform review & alarm recall", "SMS alerts"]),
            ]),
            ("Anaesthesia Gas Monitor", [
                dict(name="AGM 55", brand="Skanray", img="agm55.png", points=["Gas module for Star 90 and Star 55", "Detects 5 agents and 3 gases", "Auto-identifies primary & secondary agent", "Measures and displays MAC"]),
            ]),
        ],
    },
    {
        "slug": "surgical-diathermy", "title": "Surgical Diathermy", "icon": "bolt", "legacy": "surgical-diathermy.php",
        "short": "Electrosurgical units with smart impedance feedback.",
        "intro": "Microprocessor-controlled electrosurgical generators with impedance-based feedback for clean, consistent cutting and coagulation.",
        "groups": [
            ("Electrosurgical Units", [
                dict(name="Maestro Seal Plus", brand="Skanray", img="msp.png", points=["Impedance-based smart feedback", "Monopolar cut & coagulation", "Clamp mode for bipolar vessel sealing", "Optional split patient plate with indicator"]),
                dict(name="SurgiSkan 200", brand="Skanray", img="SurgiSkan-200.png", points=["3 monopolar cut, 4 coag and 3 bipolar modes", "Dual monopolar outputs for simultaneous coag", "6 preset + 4 user-defined programs", "Bipolar auto-start; TUR as standard"]),
                dict(name="Maestro Plus 100", brand="Skanray", img="mp100.png", points=["Smart feedback for consistent results", "Monopolar cut/coag plus bipolar cut with coag", "Patient-plate connectivity indicator", "Dual-generator output version available"]),
                dict(name="Octave", brand="Skanray", img="oct.png", points=["400 W output", "\"Supercut\" mode for TUR surgery", "Monopolar cut & coag, bipolar coag", "Impedance-based smart feedback"]),
            ]),
        ],
    },
    {
        "slug": "anesthesia-workstation", "title": "Anaesthesia Workstations", "icon": "lungs", "legacy": "anesthesia-delivery-systems.php",
        "short": "Medec and MAQUET FLOW-i anaesthesia delivery.",
        "intro": "Years of experience meeting the challenges anaesthetists face — compact workstations to fully modular, ICU-grade anaesthesia delivery.",
        "groups": [
            ("MAQUET FLOW-i", [
                dict(name="FLOW-i C20", brand="Getinge · MAQUET", img="Anesthesia-Systems/flow-i-c20-primary.jpg", points=["ICU ventilator performance in an anaesthesia system", "Built on the SERVO ventilation platform", "VOLUME REFLECTOR® replaces the bag-in-bottle", "One lockable drawer standard, 2–3 optional"]),
                dict(name="FLOW-i C30", brand="Getinge · MAQUET", img="Anesthesia-Systems/flow-i-c30-us_primary.jpg", points=["Height-adjustable ergonomic unit", "Rotatable screen arm, tiltable screens", "Rails for auxiliary equipment", "Modular and upgradeable"]),
                dict(name="FLOW-i C40", brand="Getinge · MAQUET", img="Anesthesia-Systems/flow-i_c20_inline-new--jpg-224.0x0.0.jpg", points=["Ceiling-mounted for a clear floor", "Two-part circulating radius, wide working range", "Integrated gas, electrical & comms connections", "Automatic Gas Control (AGC) for efficiency"]),
            ]),
            ("Medec", [
                dict(name="Caelus", brand="Medec", points=["40 years of Medec ventilator development", "Bag-in-bottle: neonates (~1 kg) to bariatric", "VoluProtect® & BaroProtect® safety", "18.5\" capacitive touchscreen, free software updates"]),
                dict(name="Caelus Lite", brand="Medec", points=["Compact footprint, integrated work surface", "PureTouch® interface, 18.5\" touchscreen", "Optional PRVC and VVV modes", "Gas analysis & qCON–qNOX depth monitoring"]),
                dict(name="Neptune", brand="Medec", points=["Medec's most compact anaesthesia ventilator", "Neonates, infants, adults and bariatric", "VoluProtect® & BaroProtect® safety", "Lifetime warranty on the flow sensor"]),
            ]),
        ],
    },
    {
        "slug": "critical-care-ventilators", "title": "Critical Care Ventilators", "icon": "wind", "legacy": "criticalcare-ventilator.php",
        "short": "The MAQUET SERVO family for every ICU.",
        "intro": "The SERVO family from Getinge – MAQUET: proven ventilation from intermediate care to the most demanding ICU.",
        "groups": [
            ("SERVO Ventilators", [
                dict(name="SERVO-U®", brand="Getinge · MAQUET", points=["Makes lung-protective ventilation easier", "Tailor therapy to each patient", "Controlled, supported, NIV and SBT phases", "Intuitive, guided user interface"]),
                dict(name="SERVO-i®", brand="Getinge · MAQUET", points=["Invasive, non-invasive & NAVA ventilation", "Infant, Adult and Universal configurations", "MR and HBO editions available", "Add features and upgrades as needs change"]),
                dict(name="SERVO-air™", brand="Getinge · MAQUET", points=["Independent of wall gas supply", "Easy to learn, use and own", "ICU to intermediate care", "Invasive and non-invasive"]),
                dict(name="SERVO-s®", brand="Getinge · MAQUET", points=["Proven SERVO technology", "Sensitive, reliable and simple to operate", "Adult and paediatric patients", "Suits many hospital settings"]),
            ]),
        ],
    },
    {
        "slug": "ot-lights", "title": "OT Lights", "icon": "lamp", "legacy": "operating-room.php",
        "short": "LED surgical lights from MAQUET and Magnaled.",
        "intro": "Shadow-free, colour-true LED illumination — from the modular MAQUET VOLISTA range to the Magnaled family.",
        "groups": [
            ("MAQUET", [
                dict(name="VOLISTA Access", brand="Getinge · MAQUET", points=["Lighting, suspension & multimedia via Quick Lock", "Constant illumination with natural colours", "Green ambient mode for a calmer OR", "Designed for safety and surgeon comfort"]),
                dict(name="Lucea LED 50–100", brand="Getinge · MAQUET", points=["Brings LED technology to any operating room", "Innovative design, functional shape", "Efficient for the surgical team", "Low maintenance LED source"]),
                dict(name="H LED Surgical Light", brand="Getinge · MAQUET", points=["Long-lasting LED", "Comfort and cost savings", "HD image integration", "Sustainable, efficient operation"]),
            ]),
            ("Magnaled", [
                dict(name="Magnaled Sleek Plus 500/500", brand="Magnatek", points=["Twin-dome surgical light", "LED illumination", "For major OTs"]),
                dict(name="Magnaled Sphere 620/620", brand="Magnatek", points=["Twin-dome surgical light", "LED illumination", "For major OTs"]),
                dict(name="Magnaled Sphere 700/500", brand="Magnatek", points=["Twin-dome, mixed sizes", "LED illumination", "For major OTs"]),
                dict(name="Magnaled Sleek 4 + 3", brand="Magnatek", points=["Twin-dome surgical light", "LED illumination", "Versatile for general OTs"]),
            ]),
        ],
    },
    {
        "slug": "ot-tables", "title": "OT Tables", "icon": "bed", "legacy": "operating-room1.php",
        "short": "Operating tables for every specialty.",
        "intro": "Operating tables for general surgery, bariatrics, cardiac, laparoscopy and paediatrics — including heavy-load MAQUET platforms.",
        "groups": [
            ("Operating Tables", [
                dict(name="Alpha Classic Pro", brand="Getinge · MAQUET", img="alpha.png", points=["Heavy-load table built with physician input", "Up to 450 kg (1000 lbs)", "Modular frame adapts to patient size", "Height, longitudinal shift, lateral tilt"]),
                dict(name="Meera", img="meera.png", points=["One table, forty-five positions", "Compact concave base", "Double-layer foam, PU cover", "Optional motor drive with Sensor Drive control"]),
                dict(name="Multistar 4S", img="multistar-4s.png", points=["Multi-purpose operating table"]),
                dict(name="Multistar 3S", img="multistar-3s.png", points=["Multi-purpose operating table"]),
                dict(name="Bariatrics", img="bariatrics.png", points=["For bariatric surgery"]),
                dict(name="Cardiomatic", img="cardiomatic.png", points=["For cardiac surgery"]),
                dict(name="Laparostar", img="laprostar.png", points=["For laparoscopic procedures"]),
                dict(name="Babystar", img="baby-star.png", points=["For paediatric surgery"]),
            ]),
        ],
    },
    {
        "slug": "defibrillators", "title": "Defibrillators", "icon": "heart", "legacy": "defibrillators.php",
        "short": "ZOLL defibrillators, AEDs and AutoPulse.",
        "intro": "ZOLL resuscitation — from public-access AEDs to transport monitors and automated CPR.",
        "groups": [
            ("Monitor / Defibrillators", [
                dict(name="R Series", brand="ZOLL", img="r-series.png", points=["CPR Dashboard with Real CPR Help®", "See-Thru CPR® reduces pause time", "High-current defibrillation", "R Series Plus and ALS variants"]),
                dict(name="X Series", brand="ZOLL", img="x-series1.png", points=["Under 12 lb, neonate to adult", "Defib, real-time CPR feedback, pacing", "Capnography, SpO₂, 3 IBP, 2 Temp, NIBP", "For EMS and hospital transport"]),
                dict(name="M2", brand="ZOLL", img="m2.png", points=["Monitoring and resuscitation", "CPR support", "Compact and portable"]),
            ]),
            ("Automated CPR", [
                dict(name="AutoPulse®", brand="ZOLL", img="auto1.png", points=["Battery-powered, full-chest compressions", "Automatically sizes to the patient", "Fewer interruptions during transport", "Supports in-hospital code teams"]),
            ]),
            ("AEDs", [
                dict(name="AED Plus®", brand="ZOLL", img="aed1.png", points=["Real CPR Help® rate & depth feedback", "5-year battery and electrodes", "Optional PlusTrac program management"]),
                dict(name="AED Pro®", brand="ZOLL", img="aed2.png", points=["Real CPR Help® and See-Thru CPR®", "3-lead ECG monitoring", "USB data transfer at the scene"]),
                dict(name="AED 3™", brand="ZOLL", img="aed3.png", points=["Next-generation ZOLL AED", "CPR feedback", "Built for public access"]),
            ]),
        ],
    },
    {
        "slug": "x-ray-systems", "title": "X-Ray Systems", "icon": "xray", "legacy": "X-ray-Systems.php",
        "short": "Mobile, RAD, CR and DR X-ray systems.",
        "intro": "Mobile, classical RAD, CR and DR systems for hospitals and small clinics, with SkanSHIELD® low-leakage technology. Wireless, cordless Microskan models suit ICUs and rural centres.",
        "groups": [
            ("Mobile X-Ray", [
                dict(name="Ultra-light Mobile HF X-Ray", brand="Skanray", points=["Under 55 kg · 2.8 kW · 200 kHz · 60 mA", "APR, hand-held unit & integrated console", "±90° collimator, rotating tube head", "NICU, ICU, trauma, ortho, ambulance"]),
                dict(name="Battery-operated Mobile HF X-Ray", brand="Skanray", points=["Under 110 kg · 2.8 kW · 200 kHz · 60 mA", "Up to 100 exposures per charge", "APR with integrated console", "Cordless — ideal for wards & ICU"]),
                dict(name="Mobile HF X-Ray with DR", brand="Skanray", points=["CsI flat panel, 2304 × 2880 px, 150 µm", "~1–8 s wired / ~11 s wireless cycle", "Wi-Fi 802.11n, 5.2 GHz", "3.5 kg detector, ~3 h recharge"]),
                dict(name="4 kW Mobile HF X-Ray", brand="Skanray", points=["200 kHz · 100 mA · mains powered", "Under 85 kg", "Negligible leakage radiation", "NICU, ICU, trauma, ortho"]),
                dict(name="4 kW Mobile HF X-Ray with CR", brand="Skanray", points=["Flat scan path, large touchscreen", "PACS-ready DICOM", "200,000+ artefact-free images", "NICU, ICU, trauma, ortho, wards"]),
            ]),
            ("Fixed Radiography", [
                dict(name="45 kW HF Fixed RAD", brand="Skanray", points=["40–125 kV · 10–600 mA", "Dual-focus rotating anode, fail-safe brake", "4-way floating table, under-table bucky", "Motorised tube head synced with chest stand"]),
                dict(name="45–80 kW Flat-panel DR", brand="Skanray", points=["50–150 kV · 160–1000 mA", "16-bit CsI detector, 16×16\" or 17×17\"", "Intelligent anti-collision", "Fully motorised with auto-positioning"]),
            ]),
        ],
    },
    {
        "slug": "radiology", "title": "Radiology Products", "icon": "scan", "legacy": "radiology-products.php",
        "short": "Mobile and fixed radiography solutions.",
        "intro": "High-frequency mobile and fixed radiography for every department — plus transport monitoring for imaging workflows.",
        "groups": [
            ("Radiology", [
                dict(name="Ultra-light Mobile HF X-Ray", brand="Skanray", points=["Under 55 kg · 2.8 kW · 200 kHz · 60 mA", "Hand-held unit with integrated console", "±90° collimator, rotating tube head", "NICU, ICU, trauma, ortho, ambulance"]),
                dict(name="Mobile HF X-Ray 4 kW", brand="Skanray", points=["200 kHz · 100 mA · mains powered", "Under 85 kg", "Negligible leakage radiation", "NICU, ICU, trauma, ortho"]),
                dict(name="45 kW Fixed Radiography", brand="Skanray", points=["40–125 kVp · 10–600 mA", "Dual focal-spot rotating anode", "4-way floating table, independent bucky", "Software-controlled generator & exposure"]),
                dict(name="45–80 kW Flat-panel DR Platform", brand="Skanray", points=["50–150 kVp · 160–1000 mA", "16-bit, 16×16\" or 17×17\" CsI detector", "Anti-collision, motorised all axes", "Integrated auto-positioning"]),
                dict(name="X Series Transport Monitor", brand="ZOLL", img="x-series2.png", points=["Monitoring + defibrillation + CPR feedback", "Under 12 lb, neonate to adult", "Pacing, EtCO₂, SpO₂, 3 IBP, 2 Temp, NIBP"]),
            ]),
        ],
    },
    {
        "slug": "surgical-c-arm", "title": "Surgical C-Arm", "icon": "carm", "legacy": "surgical-crm.php",
        "short": "Skan-C mobile C-arm for the OT.",
        "intro": "Skan-C — a compact, low-leakage mobile C-arm for orthopaedics, spine, neuro, urology, GI and vascular procedures.",
        "groups": [
            ("C-Arm", [
                dict(name="Skan-C", brand="Skanray", img="c.png", wide=True, points=[
                    "Low-leakage design — among the safest C-arms in its class",
                    "Compact 3.5 kW, 80–250 kHz HF generator",
                    "40–110 kV in 1 kV steps; 0.2–8 mA fluoroscopy",
                    "SnapShot up to 10 mA; pulsed fluoro up to 12 mA (2/4/6/8 pps)",
                    "1k × 1k capture, 12–14 bit",
                    "9\" image intensifier — 9\", 6\", 4.5\" fields",
                    "Virtual collimation & ROI without continuous fluoro",
                    "Peripheral vascular mode: DSA, trace, road map",
                    "SID 95 cm, free space 75 cm · DICOM 3.0",
                ]),
            ]),
        ],
    },
    {
        "slug": "ent-workstation", "title": "ENT Workstations", "icon": "ear", "legacy": "ent-workstation.php",
        "short": "ATMOS ENT treatment units from Germany.",
        "intro": "German-engineered ATMOS ENT workstations — modular, hygienic and built around the way you examine and treat.",
        "groups": [
            ("ATMOS", [
                dict(name="ATMOS S 61", brand="ATMOS", points=["Modern design, choice of colours, ample storage", "Modular — upgradable later on site", "Integrated devices with automatic switching", "Separate clean/contaminated areas, endoscope management"]),
                dict(name="ATMOS C 21 / C 31", brand="ATMOS", points=["Ergonomic workstation with rotatable chair (C 31)", "Ear irrigation with instruments in reach", "Sprayers & suction activate on lift", "Microscope lights up when grasped"]),
                dict(name="ATMOS C 11 Systema", brand="ATMOS", points=["Designed around patient & doctor workflow", "Small footprint — start small, expand later", "Metal construction, LED illumination", "Autoclavable ear-irrigation module"]),
            ]),
        ],
    },
    {
        "slug": "neonatal-care", "title": "Radiant Warmer & Phototherapy", "icon": "baby", "legacy": "radiant-warmer-phototheraphy.php",
        "short": "Incubators, infant warmers and LED phototherapy.",
        "intro": "Nice Neotech neonatal care — incubators, radiant warmers and LED phototherapy for NICUs and labour rooms.",
        "groups": [
            ("Baby Incubators", [
                dict(name="Nice 3010 H", brand="Nice Neotech", points=["Microprocessor control; skin, air & set temp display", "Electric height adjustment", "Built-in humidity chamber & O₂ flow meter", "Trendelenburg / Fowler tilt; optional scale"]),
                dict(name="Nice 3010", brand="Nice Neotech", points=["As 3010 H, without electric height adjustment", "Centrifugal blower for fresh air, lower CO₂", "Withdrawable tray, elbow-operated ports", "Optional double-wall canopy"]),
            ]),
            ("Infant Warmers", [
                dict(name="Nice 5000", brand="Nice Neotech", points=["Servo skin, servo air and manual modes", "Touch panel, large display, alarms", "Heater pivots 90° for X-ray", "Optional built-in weighing scale"]),
                dict(name="Nice 2007 SCFL", brand="Nice Neotech", points=["Servo skin & manual modes, APGAR timer", "Built-in underside CFL phototherapy", "Tilting bed, pivoting heater", "O₂ mount, pump pole, X-ray tray options"]),
                dict(name="Nice 2007 S", brand="Nice Neotech", points=["As 2007 SCFL, without phototherapy", "APGAR timer, keypad lock", "Removable side panels for cleaning"]),
            ]),
            ("LED Phototherapy", [
                dict(name="Nice 4000 LED", brand="Nice Neotech", points=["9 high-power LEDs, no UV / IR", "Adjustable height, tilting source", "Treatment timer with auto cut-off", "20,000+ hour lamp life"]),
                dict(name="Nice 4000 SPOT", brand="Nice Neotech", points=["24 high-power LEDs", "Lamp-hour monitoring & alerts", "20,000+ hour lamp life"]),
                dict(name="Nice 4005 SPOT", brand="Nice Neotech", points=["24 high-power LEDs", "Under-surface light module", "Trolley mounted, 20,000+ hour life"]),
            ]),
        ],
    },
    {
        "slug": "ambulance-fabrication", "title": "Ambulance Fabrication", "icon": "ambulance", "legacy": "ambulance-fabrication.php",
        "short": "Custom-fitted ambulances, ready to save lives.",
        "intro": "Complete ambulance fabrication — interiors, fittings and life-support equipment integrated into a vehicle that's ready for the road.",
        "gallery": ["ambulance1.png", "ambulance2.png", "ambulance3.png"],
        "groups": [
            ("What we build", [
                dict(name="Patient Transport Ambulance", points=["Custom interior fit-out", "Stretcher and seating layout", "Lighting, storage and oxygen"]),
                dict(name="Basic Life Support (BLS)", points=["Oxygen and suction systems", "Monitoring and first-response kit", "Ergonomic crew workspace"]),
                dict(name="Advanced Life Support (ALS)", points=["Defibrillator / monitor integration", "Ventilator and infusion mounting", "Full critical-care transport setup"]),
            ]),
        ],
    },
]

# ---- Photography (Unsplash, free for commercial use) ----
def U(pid, w=1600): return f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w={w}&q=80"

PHOTOS = {
    "hero": "1579684385127-1ef15d508118",       # surgeons under OT light
    "hero2": "1551076805-e1869033e561",         # operating room
    "about": "1504813184591-01572f98c85f",      # medical professionals
    "lobby": "1519494026892-80bbd2d6fd0d",      # hospital lobby
    "building": "1586773860418-d37222d8fce3",   # hospital building
    "doctor": "1519494026892-80bbd2d6fd0d",     # doctor with tablet
    "monitor": "1513224502586-d1e602410265",    # vital signs monitor
    "services": "1579684453423-f84349ef60b0",   # clinician + laptop
}
CAT_PHOTO = {
    "patient-monitoring": "1513224502586-d1e602410265",
    "surgical-diathermy": "1579684453423-f84349ef60b0",
    "anesthesia-workstation": "1551601651-2a8555f1a136",
    "critical-care-ventilators": "1712232415633-095dc9e03c5d",
    "ot-lights": "1516549655169-df83a0774514",
    "ot-tables": "1551076805-e1869033e561",
    "defibrillators": "1755549746563-a7c0a391af36",
    "x-ray-systems": "1516069677018-378515003435",
    "radiology": "1616012480717-fd9867059ca0",
    "surgical-c-arm": "1571772996211-2f02c9727629",
    "ent-workstation": "1576091160550-2173dba999ef",
    "neonatal-care": "1560306580-9e204fe45f3e",
    "ambulance-fabrication": "1579037005241-a79202c7e9fd",
}
DEPARTMENTS = [
    ("Operating Theatre", "1516549655169-df83a0774514", "Lights, tables, anaesthesia, diathermy and C-arm for a complete, modern OT.",
        ["ot-lights", "ot-tables", "anesthesia-workstation", "surgical-diathermy", "surgical-c-arm"]),
    ("ICU & Critical Care", "1712232415633-095dc9e03c5d", "Ventilation, multipara monitoring and central stations for every bed.",
        ["critical-care-ventilators", "patient-monitoring", "defibrillators"]),
    ("NICU & Labour Room", "1560306580-9e204fe45f3e", "Warmers, incubators and LED phototherapy for the most fragile patients.",
        ["neonatal-care", "patient-monitoring"]),
    ("Emergency & Transport", "1579037005241-a79202c7e9fd", "Defibrillators, AutoPulse and fully fitted ambulances, ready to respond.",
        ["defibrillators", "ambulance-fabrication"]),
    ("Imaging & Radiology", "1516069677018-378515003435", "Mobile, fixed, CR and DR X-ray — built for wards, ICUs and rural centres.",
        ["x-ray-systems", "radiology", "surgical-c-arm"]),
    ("ENT & Specialty Clinics", "1576091160550-2173dba999ef", "ATMOS ENT workstations designed around how you examine and treat.",
        ["ent-workstation"]),
]
SERVICES = [
    ("pin", "Site planning", "We help plan the department — layout, utilities and the right mix of equipment for your caseload and budget."),
    ("bolt", "Installation & commissioning", "Engineers install, calibrate and commission every system, so it's ready for patients on day one."),
    ("doc", "Documentation & training", "Every installation is well documented, and your clinical and biomedical teams are trained on the equipment."),
    ("wrench", "Free maintenance", "Preventive maintenance keeps critical equipment ready when it matters."),
    ("refresh", "Free updates", "Software and firmware updates as manufacturers release them."),
    ("shield", "Solid support", "A responsive Chennai service team, backed directly by our global principals."),
]
PROCESS = [
    ("Consult", "Tell us about your department, caseload and goals."),
    ("Recommend", "We propose the right configuration and a clear quotation."),
    ("Install", "Delivery, installation and commissioning by trained engineers."),
    ("Train", "Hands-on training and documentation for your team."),
    ("Support", "Maintenance, updates and service for the life of the system."),
]
FAQ = [
    ("Do you handle installation?", "Yes. Every system we supply is installed and commissioned by our engineers, with documentation and training for your team."),
    ("Is maintenance included?", "We offer free maintenance and free updates on the equipment we supply. Ask us for the exact terms for the product you're considering."),
    ("Can you equip a complete OT, ICU or NICU?", "Yes. Our range covers lights, tables, anaesthesia, ventilation, monitoring, imaging and neonatal care, so we can plan and supply a whole department."),
    ("Can I see a demo?", "Many products can be demonstrated. Send an enquiry with the product name and we'll arrange it."),
    ("How do I get a quotation?", "Use 'Add to quote' on any product to build a list, then send it from the Contact page — or call us on 044 2362 4880."),
]
