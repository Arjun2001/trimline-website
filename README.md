# Trimline Medical Systems — website (v2)

A fast, fully static site (no PHP, no database): Home, About, Services, Products (with live search), 13 product-line pages, Principals, Contact with FAQ, and a 404 page.

## Highlights
- Full-bleed photography throughout (hero, departments, every product-line page)
- **Solutions by department:** OT, ICU, NICU, Emergency, Imaging and ENT, each linking to the right product lines
- **Quote list:** visitors tap "Add to quote" on any product, build a list across pages, then send it all in one enquiry
- Enquiry form (Netlify Forms) that arrives pre-filled with the chosen products
- Services page with a 5-step process and FAQ
- Google-friendly: structured business data, a sitemap, and old `.php` links redirected to the new pages

## 1. Make every image local (one time, before going live)
```bash
bash fetch-images.sh
```
This downloads the product photos from the old site and the Unsplash photography into `images/`, then points every page at the local copies.

## 2. Go live on Netlify (free)
- **Quickest:** drag this folder onto https://app.netlify.com/drop, then sign up (free) to keep the site.
- **Better:** push the folder to GitHub, then in Netlify choose *Add new site → Import from Git*. There's no build command, and the publish directory is `.`.

## 3. Connect trimlinemedicals.com
Go to *Netlify → Domain management → Add a domain* and update the DNS at your registrar. HTTPS is set up automatically.

## 4. Enquiries
Submissions appear under *Netlify → Forms → enquiry*. Turn on email notifications there to get each enquiry in your inbox.

Photography is from Unsplash (free for commercial use, no attribution required). Product images belong to their manufacturers.
