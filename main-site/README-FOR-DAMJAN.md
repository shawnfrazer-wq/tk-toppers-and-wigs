# TK Main Site Redesign, Handover Notes

## What this is
Three finished page designs for tatianakarelina.co.uk, built as plain standalone
HTML for conversion into the existing WordPress/Elementor site:

- hair-loss.html      -> replaces the page at /hair-loss/
- hair-toppers.html   -> replaces the page at /clip-in-toppers-and-wiglets/
- medical-wigs.html   -> replaces the page at /medical-wigs/

Open any file in a browser to view it (all assets are relative, no server needed).
Live previews:
https://shawnfrazer-wq.github.io/tk-toppers-and-wigs/main/hair-loss.html
https://shawnfrazer-wq.github.io/tk-toppers-and-wigs/main/hair-toppers.html
https://shawnfrazer-wq.github.io/tk-toppers-and-wigs/main/medical-wigs.html

## URLs, titles and meta tags
Each HTML head contains, per page: the meta title, meta description and the
canonical URL (the existing live URL, which must not change), plus JSON-LD
structured data:

- hair-loss.html:     BreadcrumbList + FAQPage
- hair-toppers.html:  BreadcrumbList + Product (offers £615 to £1,950)
- medical-wigs.html:  BreadcrumbList + FAQPage + Product (offers £2,600 to £3,725)

Please port all of these into WordPress (Rank Math or Yoast for title,
description and canonical; the JSON-LD can go into the page as a code block or
via the SEO plugin's schema feature). The FAQ text in each FAQPage schema
matches the FAQ text on the page exactly and must stay in sync if either is
ever edited.

## Fonts
Headings: Butler, already self hosted on the live site at
/wp-content/uploads/2025/07/Butler.woff (see the @font-face in css/tk-main.css).
Playfair Display is only a preview fallback and is not needed on the domain.
Body: Poppins (300/400/600). Nav: Montserrat. Both via Google Fonts.

## Images, all in the images/ folder
- images/ba/            Before and afters (toppers and wigs pages only, none on
                        hair loss). These use the SAME filenames as the existing
                        WordPress media library uploads (2025/09), e.g. 15.webp,
                        BA-21.webp, Copy-of-22.webp. Reuse the media library
                        versions, no re-upload needed.
- images/hair-loss/, images/toppers/, images/wigs/  page photos, named by page,
                        slot number and content so placement is obvious. These
                        are new exports, upload them to the media library.

### Two image swaps for you to make
1. Hair toppers hero: the package currently shows a placeholder. Keep the
   page's EXISTING live hero, which is already in the media library:
   /wp-content/uploads/2025/10/Hero-Mobile-355x768-7.webp
2. Halo topper photo (the before and after in "The Halo Topper" section,
   images/toppers/04-halo-topper-before-after.webp): replace it with the file
   Halo.png that Shawn has in the shared Photos folder, exported to webp at
   1200 wide. Ask Shawn for the file if you do not have access.

## Design rules to preserve
- All white backgrounds, no grey section bands anywhere. The closing call to
  action section is white too (black button, black serif heading).
- Hero: boxed within the page margin (not full bleed), translucent white band
  (#FFFFFF8A) sitting flush on the bottom edge of the photo, H1 centred in it.
- On mobile the first section after the hero shows its TEXT first, photo below
  (handled by the .split--intro class in the CSS). Later sections keep photo
  first when they stack.
- Trust strip: the slim band of four facts between thin rules (replaces the
  old facts card graphics). Same strip on desktop and mobile; on mobile it
  wraps to two columns. On the toppers page it sits directly before the
  "Our signature approach" section, on the wigs page directly after the intro.
- Eyebrow labels: centred, uppercase, with a short centred 1px rule below.
- Body text: Poppins 300, justified, no hyphens or dashes anywhere in copy.
- Buttons: black fill, 3px radius, uppercase, centred under their sections.
- Before and afters: 4 across on desktop, 1 across on mobile, swipe or the
  centred BACK / NEXT arrows below, identical component on both pages.
- FAQ: large serif question, thin divider rows, circled plus that becomes a
  minus when open. The brand question ("Why ... Tatiana Karelina ...") is
  always FIRST in every FAQ.
- Mobile first: everything stacks to a single column below 900px.

## Copy details worth knowing
- Wording is trichologist (not dermatologist) in the hair loss diagnosis FAQ.
- Wiglets no longer have their own section or anchor button on the toppers
  page (a wiglet is just another name for a topper); passing mentions and the
  from £615 price remain on purpose for SEO on /clip-in-toppers-and-wiglets/.
- Timing everywhere is 8 to 12 weeks, toppers £615 to £1,950, wigs £2,600 to
  £3,725. If any of these figures change, update page copy AND schema together.
