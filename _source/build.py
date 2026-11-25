import json, os, html, sys, re
from data import IMG, COMPANY as C, PRINCIPALS, WHY, CATEGORIES, U, PHOTOS, CAT_PHOTO, DEPARTMENTS, SERVICES, PROCESS, FAQ
CATMAP = {c['slug']: c for c in CATEGORIES}

OUT = sys.argv[1] if len(sys.argv) > 1 else "dist"
os.makedirs(OUT, exist_ok=True)
CSS = open("style.css").read()
JS = open("app.js").read()
e = html.escape

def S(d, extra=""):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" {extra}>{d}</svg>'

ICONS = {
 "pulse": '<path d="M3 12h4l2-5 4 10 2-5h6"/>',
 "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 "lungs": '<path d="M12 3v8"/><path d="M12 11c-2 0-3-2-5-2-2.5 0-4 4-4 8 0 2 1 4 3 4s4-1 6-3"/><path d="M12 11c2 0 3-2 5-2 2.5 0 4 4 4 8 0 2-1 4-3 4s-4-1-6-3"/>',
 "wind": '<path d="M3 8h11a3 3 0 1 0-3-3"/><path d="M3 12h16a3 3 0 1 1-3 3"/><path d="M3 16h7"/>',
 "lamp": '<path d="M12 2v4"/><ellipse cx="12" cy="11" rx="8" ry="4"/><path d="M8 18l-1 3M16 18l1 3M12 16v5"/>',
 "bed": '<path d="M3 18V9M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="2"/>',
 "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8L12 21l8.8-8.6a5.5 5.5 0 0 0 0-7.8z"/><path d="M7 12h2l1.5-3 3 6 1.5-3h2"/>',
 "xray": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M12 6v12M9 8h6M8.5 11h7M9 14h6"/>',
 "scan": '<path d="M3 7V5a2 2 0 0 1 2-2h2M17 3h2a2 2 0 0 1 2 2v2M21 17v2a2 2 0 0 1-2 2h-2M7 21H5a2 2 0 0 1-2-2v-2"/><circle cx="12" cy="12" r="4"/>',
 "carm": '<path d="M6 4a8 8 0 0 0 0 16"/><rect x="5" y="2" width="5" height="4" rx="1"/><rect x="5" y="18" width="5" height="4" rx="1"/><path d="M14 20h7M17 20V8"/>',
 "ear": '<path d="M6 9a6 6 0 1 1 12 0c0 3-2 4-3 6s-1 4-4 4a3 3 0 0 1-3-3"/><path d="M10 9a2 2 0 1 1 4 0c0 1.5-2 2-2 3.5"/>',
 "baby": '<circle cx="12" cy="8" r="5"/><path d="M10 7.5h.01M14 7.5h.01M10.5 10a2 2 0 0 0 3 0"/><path d="M6 21a6 6 0 0 1 12 0"/>',
 "ambulance": '<path d="M2 16V7a1 1 0 0 1 1-1h11v10M14 9h4l4 4v3h-8"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/><path d="M8 9v4M6 11h4"/>',
 "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
 "wrench": '<path d="M14.7 6.3a4 4 0 0 0 5 5L22 14l-8 8-2.3-2.3a4 4 0 0 0-5-5L2 10l8-8z" transform="scale(.9) translate(1.3 1.3)"/>',
 "refresh": '<path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
 "check": '<circle cx="12" cy="12" r="9"/><path d="m8 12 3 3 5-6"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
 "pin": '<path d="M12 22s-8-6.5-8-13a8 8 0 0 1 16 0c0 6.5-8 13-8 13z"/><circle cx="12" cy="9" r="3"/>',
 "fax": '<path d="M6 9V2h12v7"/><rect x="2" y="9" width="20" height="9" rx="2"/><path d="M6 14h12v8H6z"/>',
 "menu": '<path d="M3 6h18M3 12h18M3 18h18"/>',
 "x": '<path d="M18 6 6 18M6 6l12 12"/>',
 "up": '<path d="M12 19V5M5 12l7-7 7 7"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 "share": '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/>',
 "nav": '<path d="m3 11 19-9-9 19-2-8z"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
 "list": '<path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}
def I(n, extra=""): return S(ICONS[n], extra)

LOGO_MARK = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h4l2.5-6 4 12 2.5-6h7"/></svg>'

def img(path): return IMG + path
def nprod(c): return sum(len(g[1]) for g in c["groups"])
TOTAL = sum(nprod(c) for c in CATEGORIES)

def head(title, desc, canon='', ogimg='', ld_extra=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta name="theme-color" content="#08202c">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}"><meta property="og:image" content="{ogimg}"><meta property="og:site_name" content="Trimline Medical Systems"><meta property="og:locale" content="en_IN"><meta name="twitter:card" content="summary_large_image"><link rel="canonical" href="{canon}"><meta name="geo.region" content="IN-TN"><meta name="geo.placename" content="Chennai">
<link rel="icon" href="{IMG}favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@1&family=Manrope:wght@400;500;600;700&family=Sora:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="preconnect" href="https://images.unsplash.com">
<script type="application/ld+json">{LD}</script>{ld_extra}
<style>{CSS}</style></head><body><div class="progress"></div>'''

LD = json.dumps({"@context":"https://schema.org","@type":"MedicalBusiness","name":C["name"],"alternateName":"TMS","logo":IMG+"logo.png","description":"Medical equipment and instruments supplier",
  "telephone":"+91-44-23624880","faxNumber":"+91-44-23624881","email":C["email"],"url":"https://trimlinemedicals.com/",
  "address":{"@type":"PostalAddress","streetAddress":"Plot No. 3, Flat No. G1, Venkateshwara Street, Dhanalakshmi Colony, Vadapalani","addressLocality":"Chennai","postalCode":"600026","addressRegion":"Tamil Nadu","addressCountry":"IN"},
  "geo":{"@type":"GeoCoordinates","latitude":13.05598,"longitude":80.20752},"openingHours":"Mo-Sa 09:30-18:30","foundingDate":"2002","areaServed":"Chennai, Tamil Nadu","sameAs":C["same_as"],"hasMap":C["map_link"],"priceRange":"On request","image":U("1579684385127-1ef15d508118",1200),"brand":[{"@type":"Brand","name":n} for n,_,_ in PRINCIPALS]})

def logo():
    return f'<a href="index.html" class="logo" aria-label="Trimline Medical Systems (TMS) — home"><img src="{img("logo.png")}" alt="Trimline Medical Systems (TMS)" width="369" height="40"></a>'

def header(active=""):
    mega = "".join(f'<a href="{c["slug"]}.html"><span class="ic">{I(c["icon"])}</span><span><b>{e(c["title"])}</b><span>{e(c["short"])}</span></span></a>' for c in CATEGORIES)
    def a(href, label, key): return f'<li><a href="{href}" class="{"active" if active==key else ""}">{label}</a></li>'
    drawer_sub = "".join(f'<a href="{c["slug"]}.html">{e(c["title"])}</a>' for c in CATEGORIES)
    return f'''<div class="topbar"><div class="wrap"><div class="tb-l"><a href="tel:{C["phone_href"]}">{I("phone")}{C["phone"]}</a><a href="mailto:{C["email"]}">{I("mail")}{C["email"]}</a></div><div class="tb-r"><span class="open-now" data-open></span><span>{I("clock")}{C["hours"]}</span><span>{I("pin")}Vadapalani, Chennai</span></div></div></div>
<header class="site"><div class="wrap nav">{logo()}
<ul class="menu">{a("index.html","Home","home")}{a("about.html","About","about")}
<li class="has-mega"><button aria-expanded="false" class="{"active" if active=="products" else ""}">Products {I("chev",'class="chev"')}</button><div class="mega">{mega}<a class="all" href="products.html">Browse all {TOTAL}+ products {I("arrow",'width="16" height="16"')}</a></div></li>
{a("services.html","Services","services")}{a("principals.html","Principals","principals")}{a("contact.html","Contact","contact")}</ul>
<div class="nav-cta"><a class="btn btn-line" href="tel:{C["phone_href"]}">{I("phone")} Call us</a><a class="btn btn-primary" href="contact.html">Get a quote {I("arrow")}</a><button class="burger" data-drawer aria-label="Open menu">{I("menu")}</button></div></div></header>
<div class="drawer"><div class="drawer-panel"><div class="drawer-head">{logo()}<button class="burger" style="display:grid" data-drawer aria-label="Close menu">{I("x")}</button></div>
<nav><a href="index.html">Home</a><a href="about.html">About</a><div class="lbl">Products</div><div class="sub"><a href="products.html"><b>All products</b></a>{drawer_sub}</div><a href="services.html">Services</a><a href="principals.html">Principals</a><a href="contact.html">Contact</a></nav>
<a class="btn btn-primary" style="width:100%;justify-content:center;margin-top:24px" href="contact.html">Get a quote {I("arrow")}</a></div></div>'''

def cta(title="Planning a new OT, ICU or NICU?", sub="Tell us what you need. Our team will help you choose, install and maintain the right equipment."):
    return f'''<div class="cta"><div class="wrap"><div class="cta-box rv"><div><h2>{title}</h2><p>{sub}</p></div><div class="acts"><a class="btn btn-white" href="contact.html">Request a quote {I("arrow")}</a><a class="btn btn-ghost" href="tel:{C["phone_href"]}">{I("phone")} {C["phone"]}</a></div></div></div></div>'''

def footer():
    cats = "".join(f'<li><a href="{c["slug"]}.html">{e(c["title"])}</a></li>' for c in CATEGORIES[:7])
    cats2 = "".join(f'<li><a href="{c["slug"]}.html">{e(c["title"])}</a></li>' for c in CATEGORIES[7:])
    return f'''<footer class="site"><div class="wrap"><div class="foot">
<div>{logo()}<p>Trimline Medical Systems (TMS) — medical equipment and instruments for hospitals and clinics — supplied, installed and supported from Chennai, in partnership with leading manufacturers worldwide.</p><p style="font-size:12px;opacity:.6;margin-top:14px">Photography: Unsplash. Product images courtesy of the respective manufacturers.</p></div>
<div><h4>Products</h4><ul>{cats}</ul></div><div><h4>&nbsp;</h4><ul>{cats2}<li><a href="products.html"><b>All products →</b></a></li><li><a href="services.html">Services</a></li></ul></div>
<div><h4>Get in touch</h4><ul><li>{"<br>".join(C["address"])}</li><li><a href="tel:{C["phone_href"]}">Tel: {C["phone"]}</a></li><li>Fax: {C["fax"]}</li><li>{C["hours"]}</li><li><a href="mailto:{C["email"]}">{C["email"]}</a></li></ul></div></div>
<div class="foot-big">TMS</div>
<div class="foot-bottom"><span>© <span id="yr">2026</span> Trimline Medical Systems. All rights reserved.</span><span><a href="about.html">About</a> · <a href="principals.html">Principals</a> · <a href="contact.html">Contact</a></span></div></div></footer>
<a class="wa" href="tel:{C["phone_href"]}" aria-label="Call Trimline Medical Systems">{I("phone")}</a><nav class="mbar" aria-label="Quick actions"><a href="tel:{C["phone_href"]}">{I("phone")}<span>Call</span></a><a href="{C["map_link"]}" target="_blank" rel="noopener">{I("nav")}<span>Directions</span></a><a href="contact.html" class="mq">{I("list")}<span>Get a quote</span></a></nav><button class="to-top" aria-label="Back to top">{I("up")}</button>
<button class="qbtn" aria-label="View quote list">{I("list")} Quote list <span class="c">0</span></button>
<div class="qpanel"><div class="in"><h3>Your quote list <button data-qclose aria-label="Close">{I("x")}</button></h3><p class="sub">Add products from any page, then send them all in one enquiry.</p><div class="items"></div><a class="btn btn-primary" href="contact.html">Send enquiry {I("arrow")}</a></div></div>
<div class="toast">{I("check")}<span></span></div>'''

OGI = {"index.html": PHOTOS["hero"], "about.html": PHOTOS["lobby"], "services.html": PHOTOS["services"], "contact.html": PHOTOS["building"], "principals.html": PHOTOS["doctor"], "products.html": PHOTOS["hero2"]}
OGI.update({c["slug"] + ".html": CAT_PHOTO[c["slug"]] for c in CATEGORIES})
def page(name, title, desc, body, active="", extra_js="", ld_extra=""):
    canon = C["site"] + ("" if name == "index.html" else name)
    doc = head(title, desc, canon, U(OGI.get(name, PHOTOS["hero"]), 1200), ld_extra) + header(active) + "<main>" + body + "</main>" + footer() + (f"<script>{extra_js}</script>" if extra_js else "") + f"<script>{JS}</script></body></html>"
    open(os.path.join(OUT, name), "w").write(doc)

def page_hero(title, sub, crumbs, icon=None, meta="", photo=None):
    cr = '<a href="index.html">Home</a>' + "".join(f'<span>/</span>{x}' for x in crumbs)
    ic = f'<div class="ph-ic">{I(icon)}</div>' if icon else ""
    pcls, pbg = ("page-hero ph-photo", f'<div class="ph-bg" style="background-image:url({U(photo,1920)})"></div>') if photo else ("page-hero", "")
    return f'<section class="{pcls}">{pbg}<div class="grid-bg"></div><div class="wrap"><div class="crumbs">{cr}</div><h1>{title}</h1><p>{sub}</p>{meta}</div>{ic}</section>'

def prod_card(p, cat):
    has = bool(p.get("img"))
    media_img = f'<img loading="lazy" src="{img(p["img"])}" alt="{e(p["name"])}">' if has else ""
    brand = f'<span class="brand">{e(p["brand"])}</span>' if p.get("brand") else ""
    pts = "".join(f"<li>{e(x)}</li>" for x in p["points"])
    q = f'contact.html?product={e(p["name"]).replace(" ", "+")}&amp;category={cat["slug"]}'
    cls = "prod rv" + ("" if has else " noimg") + (" wide" if p.get("wide") else "")
    pid = re.sub(r"[^a-z0-9]+", "-", p["name"].lower()).strip("-")
    return f'''<article class="{cls}" id="{pid}"><div class="media"><button class="share" data-share="{e(p['name'])}" data-url="{cat['slug']}.html#{pid}" aria-label="Share {e(p['name'])}">{I("share")}</button>{brand}{media_img}<div class="ph" style="background-image:url({U(CAT_PHOTO[cat['slug']],800)})">{I(cat["icon"])}<b>{e(p["name"])}</b></div></div>
<div class="body"><h3>{e(p["name"])}</h3><ul>{pts}</ul><div class="acts"><button class="add" data-add="{e(p['name'])}" data-cat="{e(cat['title'])}">{I("plus")}<span>Add to quote</span></button><a class="q" href="{q}">Enquire {I("arrow")}</a></div></div></article>'''

# ---------------- HOME ----------------
marq = "".join(f'<span>{e(n)} <i>{e(cn)}</i></span>' for n, cn, _ in PRINCIPALS) * 2
why = "".join(f'<div class="rv d{i%3+1}"><span class="ic">{I(ic)}</span><h3>{t}</h3><p>{d}</p></div>' for i, (ic, t, d) in enumerate(WHY))
def dept_tiles(n=None):
    out = ""
    for i, (t, ph, d, links) in enumerate(DEPARTMENTS[:n]):
        ls = "".join(f'<a href="{l}.html">{e(CATMAP[l]["title"])}</a>' for l in links)
        big = " big" if i in (0, 3, 4) else ""
        out += f'<div class="dept rv d{i%3+1}{big}" tabindex="0"><div class="bg" style="background-image:url({U(ph,1200)})"></div><span class="no">{i+1:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p><div class="links">{ls}</div></div>'
    return out
cat_cards = "".join(f'<a href="{c["slug"]}.html" class="cat photo rv d{i%3+1}"><div class="bgp" style="background-image:url({U(CAT_PHOTO[c["slug"]],700)})"></div><span class="count">{nprod(c):02d}</span><div><span class="ic">{I(c["icon"])}</span><h3>{e(c["title"])}</h3><p>{e(c["short"])}</p></div><span class="go">View range {I("arrow")}</span></a>' for i, c in enumerate(CATEGORIES[:8]))
process = "".join(f'<div class="rv d{i%3+1}"><span class="n">{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(PROCESS))
brands = "".join(f"<span>{b}</span>" for b in ["MAQUET", "ZOLL", "Skanray", "ATMOS", "Medec", "Nice Neotech", "Magnaled"])

home = f'''
<section class="hero photo" style="padding:0"><div class="hero-photo" style="background-image:url({U(PHOTOS["hero"],2200)})"></div><div class="hero-shade"></div><div class="grid-bg"></div>
<svg class="ecg" viewBox="0 0 1400 120" preserveAspectRatio="none"><defs><linearGradient id="ecgGrad" x1="0" x2="1"><stop offset="0" stop-color="#5ff2cf" stop-opacity="0"/><stop offset=".5" stop-color="#5ff2cf"/><stop offset=".8" stop-color="#ff5a5f"/><stop offset="1" stop-color="#ff5a5f" stop-opacity="0"/></linearGradient></defs><path d="M0 70h260l20-10 20 10h60l15-50 20 95 15-45h120l20-12 20 12h170l15-50 20 95 15-45h120l20-12 20 12h170l15-50 20 95 15-45h200"/></svg>
<div class="wrap"><div>
<span class="eyebrow rv">Medical Equipments &amp; Instruments · Chennai</span>
<h1 class="rv d1">Saving lives is the <em class="s">greatest job</em> in the world.</h1>
<p class="lead rv d2">We equip the people who do it. Trimline Medical Systems plans, supplies, installs and supports critical-care, surgical, imaging and neonatal equipment from the world's most trusted manufacturers.</p>
<div class="actions rv d3"><a class="btn btn-primary" href="products.html">Explore products {I("arrow")}</a><a class="btn btn-ghost" href="contact.html">Talk to our team</a></div>
</div>
<div class="hero-panel rv d2">
<div class="glass hp-monitor"><div class="row"><div><small>HR · bpm</small><br><b class="g" id="hr">72</b></div><div style="text-align:right"><small>SpO₂ %</small><br><b>98</b></div><div style="text-align:right"><small>NIBP</small><br><b class="r" style="font-size:30px">118/76</b></div></div>
<svg class="wave" viewBox="0 0 300 56" preserveAspectRatio="none"><path d="M0 30h50l8-4 8 4h20l6-22 8 44 6-22h40l8-4 8 4h20l6-22 8 44 6-22h40l8-4 8 4h20"/></svg></div>
<div class="hp-mini"><div class="glass"><b data-count="{TOTAL}" data-suffix="+">{TOTAL}+</b><span>Models available</span></div><div class="glass"><b data-count="{len(CATEGORIES)}">{len(CATEGORIES)}</b><span>Product lines</span></div></div>
<div class="glass hp-brands"><small>Our principals</small><div>{brands}</div></div>
</div></div><div class="scroll-cue"></div></section>

<div class="marquee"><div class="label">Authorised partner of world-leading manufacturers</div><div class="track">{marq}</div></div>

<section><div class="wrap"><div class="sec-head"><div><span class="eyebrow rv">Solutions by department</span><h2 class="rv d1">Equip a whole department, <em class="s">not just a room.</em></h2></div><p class="rv d2">Pick your department to see the product lines that go into it — planned, supplied and installed by one team.</p></div>
<div class="dept-grid rail">{dept_tiles()}</div><div class="swipe-hint">Swipe to see more {I("arrow")}</div></div></section>

<section class="band"><div class="bg" style="background-image:url({U(CAT_PHOTO["anesthesia-workstation"],2000)})"></div><div class="wrap">
<span class="eyebrow rv" style="color:var(--accent-2)">Featured · MAQUET FLOW-i</span><h2 class="rv d1">ICU-grade ventilation, <em class="s">now in your OT.</em></h2>
<p class="rv d2">Built on the SERVO platform, with the VOLUME REFLECTOR® and Automatic Gas Control — in C20, C30 and ceiling-mounted C40 configurations.</p>
<div class="rv d3" style="display:flex;gap:12px;margin-top:32px;flex-wrap:wrap"><a class="btn btn-primary" href="anesthesia-workstation.html">See anaesthesia range {I("arrow")}</a><button class="btn btn-ghost" data-add="FLOW-i C20" data-cat="Anaesthesia Workstations">{I("plus")}<span>Add to quote</span></button></div></div></section>

<section><div class="wrap"><div class="sec-head"><div><span class="eyebrow rv">Our products</span><h2 class="rv d1">{len(CATEGORIES)} product lines, <em class="s">one trusted partner.</em></h2></div><a class="btn btn-line rv d2" href="products.html">View all {TOTAL}+ products {I("arrow")}</a></div>
<div class="cat-grid rail">{cat_cards}</div><div class="swipe-hint">Swipe to see more {I("arrow")}</div></div></section>

<section style="padding-top:0"><div class="wrap split">
<div class="showcase rv"><div class="ring"></div><img src="{img("c.png")}" alt="Skanray Skan-C C-arm"><span class="chip" style="right:8%;top:12%">{I("scan")} DICOM 3.0</span><span class="chip" style="left:8%;bottom:14%">{I("bolt")} 3.5 kW HF generator</span></div>
<div class="rv d2"><span class="eyebrow">Featured · Imaging</span><h2>Skan-C: a C-arm that <em class="s">keeps everyone safer.</em></h2>
<p>Low-leakage design, pulsed fluoroscopy, virtual collimation and a peripheral vascular mode with DSA and road map — ready for orthopaedics, spine, neuro, urology and vascular work.</p>
<ul class="checks"><li>{I("check")}Pulsed fluoro up to 12 mA, 2–8 pps</li><li>{I("check")}1k × 1k capture, 12–14 bit</li><li>{I("check")}SID 95 cm, free space 75 cm</li></ul>
<a class="btn btn-line" href="surgical-c-arm.html">Explore Skan-C {I("arrow")}</a></div>
</div></section>

<section style="padding-top:0"><div class="wrap"><div class="sec-head"><div><span class="eyebrow rv">How we work</span><h2 class="rv d1">From first conversation <em class="s">to years of service.</em></h2></div><a class="btn btn-line rv d2" href="services.html">Our services {I("arrow")}</a></div>
<div class="process">{process}</div></div></section>

<section class="dark"><div class="wrap"><div class="sec-head"><div><span class="eyebrow rv">What we offer</span><h2 class="rv d1">More than equipment — <em class="s">a partner for its whole life.</em></h2></div><p class="rv d2">From the first site plan to years of service, we stay with you.</p></div>
<div class="why">{why}</div></div></section>
<section style="padding-bottom:0"></section>
{cta()}'''
page("index.html", "Medical Equipment Dealer in Chennai — ICU, OT, NICU & Imaging | Trimline Medical Systems",
     "Trimline Medical Systems, Vadapalani, Chennai: patient monitors, anaesthesia workstations, ventilators, OT lights & tables, ZOLL defibrillators, X-ray, C-arm, ENT and NICU equipment from MAQUET, Skanray, ZOLL and more. Since 2002.", home, "home")

# ---------------- SERVICES ----------------
svc = "".join(f'<div class="rv d{i%3+1}"><span class="ic">{I(ic)}</span><h3>{t}</h3><p>{d}</p></div>' for i, (ic, t, d) in enumerate(SERVICES))
body = page_hero("Service that lasts as long as <em class='s'>the equipment.</em>", "Planning, installation, training, maintenance and updates — one team, from first quote to the end of the system's life.", ["Services"], photo=PHOTOS["services"])
body += f'''<section><div class="wrap"><div class="svc">{svc}</div></div></section>
<section style="padding-top:0"><div class="wrap split">
<div class="photo-split rv" style="background-image:url({U(PHOTOS["about"],1200)})"><div class="glass badge"><b>One point of contact</b><span>For every brand, every device, every department.</span></div></div>
<div class="rv d2"><span class="eyebrow">How we work</span><h2>A simple, <em class="s">proven</em> process.</h2><div class="process vert">{process}</div></div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head" style="justify-content:center;text-align:center"><div><span class="eyebrow rv">Questions</span><h2 class="rv d1">Frequently asked</h2></div></div><div class="faq">{"".join(f'<details class="rv"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)}</div></div></section>
{cta()}'''
FAQLD = '<script type="application/ld+json">' + json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}) + '</script>'
page("services.html", "Services — Trimline Medical Systems", "Medical equipment site planning, installation, training, free maintenance and updates in Chennai.", body, "services", ld_extra=FAQLD)

# ---------------- CATEGORY PAGES ----------------
side = lambda active: "".join(f'<a href="{c["slug"]}.html" class="{"active" if c["slug"]==active else ""}">{I(c["icon"])}{e(c["title"])}</a>' for c in CATEGORIES)
for c in CATEGORIES:
    brands = sorted({p.get("brand") for g in c["groups"] for p in g[1] if p.get("brand")})
    meta = '<div class="meta">' + f'<span class="pill">{nprod(c)} models</span>' + "".join(f'<span class="pill">{e(b)}</span>' for b in brands) + "</div>"
    body = page_hero(e(c["title"]), e(c["intro"]), ['<a href="products.html">Products</a>', e(c["title"])], c["icon"], meta, CAT_PHOTO[c["slug"]])
    gal = ""
    if c.get("gallery"):
        gal = '<div class="gallery">' + "".join(f'<div class="rv" data-hide-wrap><img data-hide-on-error loading="lazy" src="{img(g)}" alt="Ambulance fabricated by Trimline Medical Systems"></div>' for g in c["gallery"]) + "</div>"
    groups = "".join(f'<div class="group"><div class="group-title"><h2>{e(gt)}</h2><span></span><small>{len(ps)} {"model" if len(ps)==1 else "models"}</small></div><div class="products">{"".join(prod_card(p, c) for p in ps)}</div></div>' for gt, ps in c["groups"])
    body += f'<section style="padding-top:70px;padding-bottom:40px"><div class="wrap layout"><aside class="side"><h4>Product lines</h4>{side(c["slug"])}</aside><div>{gal}{groups}</div></div></section>'
    body += cta(f"Need help choosing {e(c['title'].lower())}?", "Share your requirements and we'll recommend the right configuration, with a detailed quotation.")
    pnames = [p["name"] for g in c["groups"] for p in g[1]]
    t = f'{c["title"]} in Chennai' + (f' — {", ".join(brands[:2])}' if brands else '') + ' | Trimline Medical Systems'
    d = f'{c["intro"]} Models: {", ".join(pnames[:5])}. Supply, installation & service in Chennai — call {C["phone"]}.'
    il = {"@context":"https://schema.org","@type":"ItemList","name":c["title"],"itemListElement":[{"@type":"ListItem","position":i+1,"item":{"@type":"Product","name":p["name"],"description":"; ".join(p["points"]),**({"brand":{"@type":"Brand","name":p["brand"]}} if p.get("brand") else {}),"url":C["site"]+c["slug"]+".html#"+re.sub(r"[^a-z0-9]+","-",p["name"].lower()).strip("-")}} for i,p in enumerate([p for g in c["groups"] for p in g[1]])]}
    bc = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":C["site"]},{"@type":"ListItem","position":2,"name":"Products","item":C["site"]+"products.html"},{"@type":"ListItem","position":3,"name":c["title"],"item":C["site"]+c["slug"]+".html"}]}
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (il, bc))
    page(f'{c["slug"]}.html', t, d, body, "products", ld_extra=ld)

# ---------------- PRODUCTS INDEX ----------------
plist = []
for c in CATEGORIES:
    for gt, ps in c["groups"]:
        for p in ps:
            plist.append({"n": p["name"], "c": c["title"], "b": p.get("brand", ""), "k": gt + " " + " ".join(p["points"]), "u": f'{c["slug"]}.html', "i": I(c["icon"])})
cards = "".join(f'<a href="{c["slug"]}.html" class="cat photo rv d{i%3+1}"><div class="bgp" style="background-image:url({U(CAT_PHOTO[c["slug"]],700)})"></div><span class="count">{nprod(c):02d}</span><div><span class="ic">{I(c["icon"])}</span><h3>{e(c["title"])}</h3><p>{e(c["short"])}</p></div><span class="go">View range {I("arrow")}</span></a>' for i, c in enumerate(CATEGORIES))
body = page_hero("Our <em class='s'>products</em>", f"{TOTAL}+ models across {len(CATEGORIES)} product lines, from {len(PRINCIPALS)} world-class manufacturers.", ["Products"], photo=PHOTOS["hero2"])
body = body.replace("</p></div>", f'</p><div class="search">{I("search")}<input id="psearch" type="search" placeholder="Search products, brands or features…" autocomplete="off" aria-label="Search products"><kbd>/</kbd></div></div>', 1)
body += f'<section style="padding-top:60px"><div class="wrap"><div id="presults" class="results"></div><div id="pcats" class="cat-grid">{cards}</div></div></section>' + cta()
page("products.html", "All Products — Trimline Medical Systems", "Browse all medical equipment supplied by Trimline Medical Systems.", body, "products", "window.PRODUCTS=" + json.dumps(plist, ensure_ascii=False) + ";")

# ---------------- ABOUT ----------------
def li(xs): return "".join(f"<li>{I('check')}{e(x)}</li>" for x in xs)
clients = "".join(f'<div class="rv" data-hide-wrap><img data-hide-on-error loading="lazy" src="{img(f"clients/logo-{i}.jpg")}" alt="Client logo"></div>' for i in range(1, 6))
body = page_hero("Equipping care teams to <em class='s'>save lives.</em>", "Trimline Medical Systems (TMS) brings world-class medical technology to hospitals and clinics — with the planning, installation and support that keeps it working.", ["About"], photo=PHOTOS["lobby"])
body += f'''<div class="wrap"><div class="stats">
<div class="stat rv"><b data-count="{len(PRINCIPALS)}">{len(PRINCIPALS)}</b><span>Global principals</span></div>
<div class="stat rv d1"><b data-count="{len(CATEGORIES)}">{len(CATEGORIES)}</b><span>Product lines</span></div>
<div class="stat rv d2"><b data-count="{TOTAL}" data-suffix="+">{TOTAL}+</b><span>Models available</span></div>
<div class="stat rv d3"><b data-count="5">5</b><span>Countries we source from</span></div></div></div>
<section><div class="wrap split">
<div class="rv"><span class="eyebrow">About company</span><h2>Planning, equipment, therapies and <em class="s">solutions</em> for safe, reliable care.</h2>
<p>Our goal is simple: saving lives. We work with hospitals to plan their departments, supply the right equipment and therapies, and deliver solutions that make care safer and more reliable — from the operating theatre to the ICU and NICU.</p>
<p style="margin-top:14px">As the Chennai partner of manufacturers including Getinge – MAQUET, ZOLL, Skanray, ATMOS, Medec and Nice Neotech, we pair global technology with local, hands-on support.</p>
<a class="btn btn-primary" style="margin-top:30px" href="principals.html">Meet our principals {I("arrow")}</a></div>
<div class="photo-split rv d2" style="background-image:url({U(PHOTOS["about"],1200)})"><div class="glass badge"><b>Saving lives is the greatest job in the world.</b><span>That's why we do what we do.</span></div></div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head"><div><span class="eyebrow rv">Where we help</span><h2 class="rv d1">Solutions for <em class="s">every department.</em></h2></div></div><div class="dept-grid">{dept_tiles()}</div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head"><div><span class="eyebrow rv">Why we are different</span><h2 class="rv d1">Complete capability, <em class="s">one point of contact.</em></h2></div></div>
<div class="tri">
<div class="rv"><span class="ic">{I("shield")}</span><h3>Why choose us</h3><ul>{li(["Complete therapeutic and monitoring capabilities","Authorised partner of global brands","Free maintenance and free updates","Documented, planned installations"])}</ul></div>
<div class="rv d1"><span class="ic">{I("heart")}</span><h3>ZOLL defibrillator monitor pacemaker</h3><ul>{li(["ECG monitoring","Semi-automatic defibrillation","Pacemaker, recorder, voice and visual prompts","PCMCIA card slots, battery packs"])}</ul></div>
<div class="rv d2"><span class="ic">{I("pulse")}</span><h3>ORION ECG machine</h3><ul>{li(["3-channel ECG machine","Rhythm lead recording","High-resolution built-in thermal recorder","Accepts Z-fold thermal paper"])}</ul></div>
</div></div></section>
<section class="dark"><div class="wrap"><div class="sec-head"><div><span class="eyebrow rv">See it in action</span><h2 class="rv d1">Our products, <em class="s">in detail.</em></h2></div></div>
<div class="video rv"><iframe src="https://www.youtube-nocookie.com/embed/0rlUheWYAEM" title="Trimline Medical Systems product video" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></div></section>
<section><div class="wrap"><div class="sec-head"><div><span class="eyebrow rv">Our happy clients</span><h2 class="rv d1">Trusted by hospitals <em class="s">across the region.</em></h2></div></div><div class="clients">{clients}</div></div></section>
{cta()}'''
page("about.html", "About — Trimline Medical Systems", "About Trimline Medical Systems, Chennai — medical equipment supply, installation and support.", body, "about")

# ---------------- PRINCIPALS ----------------
pr = "".join(f'<div class="rv d{i%3+1}"><span class="n">{i+1:02d}</span><span class="flag">{e(cn)}</span><h3>{e(n)}</h3><p>{e(d)}</p></div>' for i, (n, cn, d) in enumerate(PRINCIPALS))
body = page_hero("Our <em class='s'>principals</em>", "We represent some of the most respected names in medical technology — from Sweden, Germany, the USA, Belgium and India.", ["Principals"], "globe", photo=PHOTOS["doctor"])
body += f'<section><div class="wrap"><div class="princ">{pr}</div></div></section>' + cta("Looking for a specific brand?", "Ask us about availability, configurations and pricing across our principals' ranges.")
page("principals.html", "Principals — Trimline Medical Systems", "Manufacturers represented by Trimline Medical Systems.", body, "principals")

# ---------------- CONTACT ----------------
opts = "".join(f'<option value="{c["slug"]}">{e(c["title"])}</option>' for c in CATEGORIES)
body = page_hero("Let's <em class='s'>talk.</em>", "Tell us about your requirement — a single device or a complete department. We'll get back with recommendations and a quotation.", ["Contact"], "phone", photo=PHOTOS["building"])
body += f'''<section style="padding-top:70px"><div class="wrap"><div class="contact-grid">
<div class="info-card rv"><h2>Trimline Medical Systems</h2>
<div class="info-row"><span class="ic">{I("pin")}</span><div><small>Visit</small>{"<br>".join(C["address"])}<br><a href="{C["map_link"]}" target="_blank" rel="noopener" style="color:var(--accent-2);font-weight:700;font-size:14px">Get directions →</a></div></div>
<div class="info-row"><span class="ic">{I("phone")}</span><div><small>Call</small><a href="tel:{C["phone_href"]}">{C["phone"]}</a></div></div>
<div class="info-row"><span class="ic">{I("clock")}</span><div><small>Hours</small>{C["hours"]} <span class="open-now" data-open></span></div></div>
<div class="info-row"><span class="ic">{I("fax")}</span><div><small>Fax</small>{C["fax"]}</div></div>
<div class="info-row"><span class="ic">{I("mail")}</span><div><small>Email</small><a href="mailto:{C["email"]}" style="word-break:break-all">{C["email"]}</a></div></div></div>
<div class="form-card rv d1"><div class="form-ok hidden"><h2>Thank you! ✓</h2><p style="color:var(--muted);margin-top:10px">Your enquiry has been sent. Our team will get back to you shortly.</p></div>
<form name="enquiry" method="POST" action="contact.html?sent=1" data-netlify="true" netlify-honeypot="bot-field">
<h2>Send an enquiry</h2><p style="color:var(--muted);margin:8px 0 28px">We usually respond within one working day.</p>
<input type="hidden" name="form-name" value="enquiry"><input type="hidden" name="products"><div class="qlist-form hidden"></div><p class="hidden"><label>Leave empty <input name="bot-field"></label></p>
<div class="fgrid">
<div class="field"><label for="f-name">Full name *</label><input id="f-name" name="name" required autocomplete="name"></div>
<div class="field"><label for="f-org">Hospital / organisation</label><input id="f-org" name="organisation" autocomplete="organization"></div>
<div class="field"><label for="f-email">Email *</label><input id="f-email" type="email" name="email" required autocomplete="email"></div>
<div class="field"><label for="f-phone">Phone *</label><input id="f-phone" type="tel" name="phone" required autocomplete="tel"></div>
<div class="field full"><label for="f-cat">Product line</label><select id="f-cat" name="category"><option value="">Select a product line</option>{opts}<option value="other">Other / multiple</option></select></div>
<div class="field full"><label for="f-sub">Subject</label><input id="f-sub" name="subject"></div>
<div class="field full"><label for="f-msg">Message *</label><textarea id="f-msg" name="message" required></textarea></div></div>
<div class="form-foot"><small>Prefer to talk? Call <a href="tel:{C["phone_href"]}" style="color:var(--accent);font-weight:700">{C["phone"]}</a></small><button class="btn btn-primary" type="submit">Send enquiry {I("arrow")}</button></div></form></div></div>
<div class="map rv"><iframe src="{C["map"]}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Trimline Medical Systems on Google Maps"></iframe></div></div></section>
<section style="padding-top:0"><div class="wrap"><div class="sec-head" style="justify-content:center;text-align:center"><div><span class="eyebrow rv">Questions</span><h2 class="rv d1">Frequently asked</h2></div></div><div class="faq">{"".join(f'<details class="rv"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)}</div></div></section>'''
page("contact.html", "Contact — Trimline Medical Systems", "Contact Trimline Medical Systems, Vadapalani, Chennai — medical equipment quotes, demos and service. Tel 044 2362 4880, Mon–Sat 9:30–6:30.", body, "contact", ld_extra=FAQLD)

# ---------------- 404 ----------------
body = page_hero("Page <em class='s'>not found.</em>", "The page you're looking for has moved. Try our product range or get in touch.", ["404"])
body = body.replace("</p></div>", f'</p><div class="meta" style="margin-top:30px"><a class="btn btn-primary" href="products.html">Browse products {I("arrow")}</a><a class="btn btn-ghost" href="index.html">Home</a></div></div>', 1)
body += '<section style="padding:40px"></section>'
page("404.html", "Not found — Trimline Medical Systems", "Page not found", body)

# ---------------- Netlify config + redirects from old PHP URLs ----------------
red = ["/index.php  /  301", "/about.php  /about.html  301", "/principles.php  /principals.html  301", "/contact.php  /contact.html  301"]
red += [f'/{c["legacy"]}  /{c["slug"]}.html  301' for c in CATEGORIES]
open(os.path.join(OUT, "_redirects"), "w").write("\n".join(red) + "\n")
open(os.path.join(OUT, "robots.txt"), "w").write("User-agent: *\nAllow: /\n\nSitemap: https://trimlinemedicals.com/sitemap.xml\n")
pages = ["", "about.html", "services.html", "products.html", "principals.html", "contact.html"] + [c["slug"] + ".html" for c in CATEGORIES]
open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>https://trimlinemedicals.com/{p}</loc></url>" for p in pages) + "</urlset>")
print("built", len(os.listdir(OUT)), "files;", TOTAL, "products")
