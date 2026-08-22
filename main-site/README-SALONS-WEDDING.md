# TK Homepage + Salon Pages + Wedding Hair — Handover Notes

## What this is
Four page designs for tatianakarelina.co.uk, same design system as the main
11 page package (css/tk-main.css is included and is identical).

| File | URL |
|---|---|
| homepage.html | replaces the homepage at / |
| london.html | replaces /london-best-hair-extension-salon/ |
| manchester.html | replaces /manchester-best-hair-extension-salon/ |
| wedding-hair-extensions.html | NEW page, create at /wedding-hair-extensions/ |

## The homepage
It keeps the live homepage structure section for section: hero, As Featured
In, the services carousel (one service per slide, text one side and photo the
other, with the arrows on the photo), About Us, the before and after
carousel, Point of Difference, the hair loss carousel, client reviews,
Instagram, FAQ and Ready to Transform with the dark London map.

On top of that structure these repositioning changes are applied:
- H1 is "London's Leading Russian Hair Extensions Salon" (was "World's Best
  Hair Extensions in London"), and the floating tagline above it is gone.
- A trust strip sits under the hero: 20 years / two salons / six natural
  textures / 100% Russian hair.
- Every service and hair loss method opens with an outcome line above the
  body copy, e.g. "Undetectable, everyday confidence" over micro rings.
- Kathryn Forde's Google review about her chemotherapy wig sits under the
  hair loss carousel as a pull quote, with a "Take the First Step Back to
  Yourself" button to /hair-loss/.
- The hero button reads "Start Your Transformation".
- The reviews slider opens with three curated reviews (Daisy Slavkova,
  Veronica Heague, Ruth Morgan) before the rest.
- 20 years is used consistently everywhere. The live typos are fixed:
  "standby strand" to "strand by strand", "fast becoming popular way" to
  "fast becoming a popular way", "Our, medical wigs" to "Our medical wigs".
- Services carousel order: micro rings, micro bonds, tapes, clip ins, wefts,
  braids and ponytails. Hair loss order: classic, frontal, halo, medical wigs.
- Both carousels loop continuously and move a whole slide at a time.

Homepage notes for the build:
- The Ready to Transform map in this preview is a captured image. Use the
  Elementor Google Maps widget with the existing dark style, as on the live
  page, linked to 33 Holland Street, London W8 4LX.
- The Instagram section photo is images/home/instagram-salon.webp (supplied
  by Shawn); the Follow Us button is centred beneath the copy.
- Homepage meta: title "The Best Extensions in the World - Tatiana Karelina",
  canonical https://tatianakarelina.co.uk/, and the Organization JSON-LD in
  the head nests both salons with their addresses and phone numbers.

Live previews:
https://shawnfrazer-wq.github.io/tk-toppers-and-wigs/main/london.html
https://shawnfrazer-wq.github.io/tk-toppers-and-wigs/main/manchester.html
https://shawnfrazer-wq.github.io/tk-toppers-and-wigs/main/wedding-hair-extensions.html

## Meta data (port into Rank Math/Yoast, exact values in each file's head)

- london: title "Hair Extension Salon in London, Kensington | Tatiana Karelina",
  canonical /london-best-hair-extension-salon/ (slug must not change).
- manchester: title "Hair Extension Salon in Manchester, Northern Quarter |
  Tatiana Karelina", canonical /manchester-best-hair-extension-salon/.
- wedding: title "Wedding Hair Extensions in London & Manchester | Tatiana
  Karelina", canonical /wedding-hair-extensions/ (new slug, exactly this).

Meta descriptions are in each file's `<meta name="description">` tag, written
to length. Copy verbatim.

## Structured data (JSON-LD, in each head, port as is)
- Both salon pages: HairSalon (LocalBusiness) with the full address, phone,
  email, opening hours and price range, plus BreadcrumbList and FAQPage.
  This is the schema that feeds Google Business/local results, so port it
  carefully and keep it in sync with the on page details.
- Wedding page: BreadcrumbList + FAQPage. The FAQ text in the schema matches
  the on page FAQ exactly and must stay in sync.

## Facts baked into the pages (verify before launch)
- London: 33 Holland Street W8 4LX, Tue to Sat 10am to 6.30pm,
  +44 (0) 203 645 1761, info@tatianakarelina.co.uk.
- Manchester: Salon 505, 5th floor, 49 Piccadilly M1 2AP, open since 2010,
  +44 (0) 161 236 4467, manchester@tatianakarelina.co.uk, free parking at
  1 Port Street (confirm at booking), meter parking on Port Street, Hilton
  Street and Newton Street.
- Manchester's services list deliberately omits micro bonds (matches the live
  page) and says every clip in is handmade in the Manchester salon.
- Wedding page: fittings possible as little as 3 hours before the day,
  fitted methods booked a few weeks ahead for a trial style.

## Images
- images/salons/ — the two salon heroes. SAME filenames as the WordPress
  media library (2025/10): Hero-Mobile-355x768-7-2.webp (London),
  Hero-Mobile-355x768-8.webp (Manchester). Reuse the media library versions.
- images/weddings/Blog-68.webp — the bridal hero, already in the media
  library (2025/09, used on the wedding blog post). Reuse it.

## Navigation
- Salon pages live under the SALONS menu item, as on the live site.
- Wedding hair: link it from the footer (Explore column) and, if wanted, as a
  child of Hair Extensions in the menu. Both salon pages' wedding sections
  already link to it.
- Internal links in these previews point at .html files; on WordPress point
  them at the live URLs.

## Design rules
Identical to the main package README (README-FOR-DAMJAN.md): white
backgrounds, boxed hero with translucent band, trust strip of four facts,
justified body copy with no dashes, black buttons, brand question first in
every FAQ, CTA paragraph exactly as wide as its heading, single column below
900px.
