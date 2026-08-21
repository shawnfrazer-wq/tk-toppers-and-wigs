# TK Main Site Redesign, Handover Notes

## What this is
Three finished page designs for tatianakarelina.co.uk, built as plain standalone
HTML for conversion into the existing WordPress/Elementor site:

- hair-loss.html      -> replaces the page at /hair-loss/
- hair-toppers.html   -> replaces the page at /clip-in-toppers-and-wiglets/
- medical-wigs.html   -> replaces the page at /medical-wigs/

Open any file in a browser to view it (all assets are relative, no server needed).
Live previews: https://shawnfrazer-wq.github.io/tk-toppers-and-wigs/main/hair-loss.html

## URLs, titles and meta tags
Each HTML head contains, per page: the meta title, meta description and the
canonical URL (the existing live URL, which must not change), plus JSON-LD
structured data (BreadcrumbList, FAQPage, and Product where relevant).
Please port all of these into WordPress (Rank Math or Yoast for title,
description and canonical; the JSON-LD can go into the page as a code block
or via the SEO plugin's schema feature). The FAQ text in the schema matches
the FAQ text on the page exactly and must stay in sync.

## Fonts
Headings: Butler, already self hosted on the live site at
/wp-content/uploads/2025/07/Butler.woff (see the @font-face in css/tk-main.css).
Playfair Display is only a preview fallback and is not needed on the domain.
Body: Poppins (300/400/600). Nav: Montserrat. Both via Google Fonts.

## Images, all in the images/ folder
- images/ba/            Before and afters. These use the SAME filenames as the
                        existing WordPress media library uploads (2025/09), e.g.
                        15.webp, BA-21.webp, Copy-of-22.webp. Reuse the media
                        library versions, no re-upload needed.
- images/toppers/card-topper-facts-*.png and images/wigs/card-wig-facts-*.png
                        are the existing Divider facts cards from the media
                        library (desktop and mobile versions).
- images/hair-loss/, images/toppers/, images/wigs/  page photos, named by
                        page, slot number and content so placement is obvious.
- Heroes are the pages' existing live hero images, exported at 1920px wide.

## Design rules to preserve
- All white backgrounds, no grey section bands anywhere.
- Hero: boxed within the page margin (not full bleed), translucent white band
  (#FFFFFF8A) sitting flush on the bottom edge of the photo, H1 centred in it.
- Eyebrow labels: centred, uppercase, with a short centred 1px rule below.
- Body text: Poppins 300, justified, no hyphens or dashes anywhere in copy.
- Buttons: black fill, 3px radius, uppercase, centred under their sections.
- Before and afters: 4 across on desktop, 1 across on mobile, swipe or the
  centred BACK / NEXT arrows below, identical component on all three pages.
- FAQ: large serif question, thin divider rows, circled plus that becomes a
  minus when open.
- Mobile first: everything stacks to a single column below 900px; the facts
  cards swap to their mobile versions below 768px.
