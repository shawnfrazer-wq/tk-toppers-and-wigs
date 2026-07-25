# HTML Build Brief: Tatiana Karelina Toppers and Wigs

Master specification for a STATIC HTML website. The deliverable is a clean, complete multi-page HTML site (HTML + CSS + optimised images + inline schema) that a third party (Pontifex) will convert to WordPress. Build for that: clean semantic HTML, well organised CSS, no framework, no build step required to view.

Read this brief in full, plus AGENTS.md, docs/keyword-map.md, docs/seo-strategy.md, docs/content-map.md and docs/salvaged-copy.md, before building.

## 0. Build target and the golden rule

Static HTML, one file per page, shared nav and footer markup repeated consistently (or via a simple include pattern that still produces standalone HTML). Plain CSS in one stylesheet (or a small set). Images as optimised files (WebP with jpg fallback) with proper width/height and alt text. Schema as inline JSON-LD in each page head. No React, no Next.js, no MDX, no bundler.

GOLDEN RULE, the top priority on this build: replicate the tatianakarelina.co.uk visual treatment EXACTLY. Match its colour blocking (black footer, grey-and-black contact panels, ivory accent bands, white dominant), its fonts, its eyebrow style, its section anatomy. NEVER substitute a cleaner all-white redesign. When a TK equivalent exists, fetch it, read its rendered styles, and match them. Do not redesign what TK already does; replicate it and change only the copy.

## 1. The site

Standalone domain: tatianakarelinatoppersandwigs.com. Set every canonical, sitemap entry, schema URL and Open Graph tag to https://tatianakarelinatoppersandwigs.com. Zero starting authority, so onsite SEO and AI-search readiness are the whole strategy.

Business: Tatiana Karelina, premium Russian hair toppers (classic, frontal, halo), wiglets, bespoke medical and custom wigs, all made to measure. London (33 Holland Street, W8 4LX) and Manchester (505-49 Piccadilly, M1 2AP). Ships worldwide. Consultations in salon or by video. 50% deposit at time of order, balance on completion. About 20 years, press featured, strong Google reviews. Scope: toppers, wiglets, medical and custom wigs, hair loss. NO extensions, NO VAT content, NO fashion wigs.

## 2. Brand and style system (fixed)

1. Logo: the exact TK logo.
2. Fonts: Playfair Display for headings, Inter for body. Self-hosted.
3. Colours: the TK colour tokens. White dominant, ivory as an accent band only, BLACK for the footer and the contact enquiry panel, grey for the contact info panel. Match TK's exact hex values (fetch and read them).
4. Eyebrows: every section heading is preceded by an eyebrow, small letter-spaced CAPS, centred, with a short horizontal rule beneath it, exactly as TK does (for example OUR POINT OF DIFFERENCE, THE ART OF CHANGE, AS FEATURED IN). Consistent placement and style across all sections.
5. Magazine editorial style: Playfair serif headings, letter-spaced caps eyebrows, full-bleed photography, alternating photo-and-text sections, substantial copy, TK colour blocking. Richer magazine feel, elegant and content-rich, not sparse-white and not busy. The richness comes from content and imagery; the premium feel from type and restraint.

## 3. Layout rules (hard)

1. Every section pairs a photo with a text box, and the text box is the same height as its photo. Where two text boxes sit side by side, they carry the same character count (including spaces) so they render identical heights. Never an orphan line. Copy is written to fill the box.
2. Desktop: max content width around 1200 to 1280px, using the screen, no narrow centre column with big empty margins. Controlled section padding, generous but not cavernous. Full-bleed (edge to edge) for hero, trust strip, before-and-afters and any background band. Contained width for text-and-photo sections. Paired photos are large and copy fills the matched box (thin copy next to a tall photo is the main white-space generator, avoid it).
3. Mobile first, verified at 390px. Before and afters: 4 across with horizontal scroll on desktop, 1 image with scroll on mobile.
4. Copy: UK English, numerals as digits, fully justified body text (text-align justify, text-justify inter-word), NO hyphenation at any breakpoint, no dividers, no bold in body.
5. Keywords: each page's target keywords (docs/keyword-map.md) appear naturally in the H1, the H2s and the body. Present, not stuffed.
6. Taxonomy: wiglets are a topper. Medical and custom/bespoke wigs are ONE product on ONE page (Medical Wigs), whose copy naturally includes bespoke, custom and human hair wig terms.

## 4. Navigation (all caps)

TOPPERS (dropdown: CLASSIC TOPPER, FRONTAL TOPPER, HALO TOPPER), MEDICAL WIGS, PRICES, BEFORE AND AFTERS, BLOG, CONTACT, BOOK APPOINTMENT. Logo left at TK prominence; uppercase menu, black BOOK APPOINTMENT button and phone pill (+44 (0) 203 645 1761) right. Dropdown: clean white panel, NO heavy top border, ALL CAPS items, small light font, narrow box sized to content, CENTRED under the TOPPERS label. Mobile hamburger with grouped menu. Wiglets and custom wigs are pages but NOT in the nav (linked from content).

## 5. Hero (TK style, rebuilt clean)

Full-bleed background image (the salon measuring photo, Photo 01-02-2023). The TATIANA KARELINA wordmark in white, centred over the upper image. Two-line serif headline lower on the image: Russian Hair Toppers And Wigs / Made To Measure For Hair Loss. Two CTA buttons beneath: Book a Consultation, See Before & Afters. Subtle gradient so text is legible over the photo. Match the TK homepage hero treatment (wordmark over image, headline low, CTAs beneath). Full viewport-height feel as TK.

## 6. Homepage (11 sections in order)

Each section: eyebrow, heading, photo-and-text per the layout rules, TK treatment. Where a TK equivalent exists, replicate structure and rewrite copy (not duplicate).

1. Hero (section 5).
2. Trust strip. Heading World's Best Toppers and Medical Wigs, then eyebrow AS FEATURED IN with the press logo row (Daily Mail, Evening Standard, Forbes, Cosmopolitan, Daily Express, PopSugar, Marie Claire, Metro) greyscale on white. TK position and treatment.
3. Hair loss explanation (own eyebrow and heading). Copy rewritten from the TK hair loss page: hair loss is common, ranges from gradual (genetics, hormones, pregnancy, menopause) to sudden (stress, illness, chemotherapy), and toppers and medical wigs restore coverage and confidence. Photo plus matched text box. Buttons to Toppers and Medical Wigs.
4. Toppers and wigs grid (separate section, own eyebrow and heading; use the TK Rediscover your confidence spirit). Four tiles, 2 top 2 below: Classic Topper, Frontal Topper, Halo Topper, Medical Wigs. Each tile: image, short intro, bullet USPs (reworded from TK homepage: Classic, bespoke coverage for thinning areas, finest Russian hair, hand blended natural colour match, lightweight discreet secure fit; Frontal, ideal for receding hairlines and temple loss, suitable for frontal fibrosing alopecia, finest Russian hair, natural discreet front hairline coverage; Halo, designed for more advanced thinning, ideal when full clips are not suitable, finest Russian hair, lightweight discreet secure fit; Medical Wig, made to measure, finest Russian hair, lightweight and breathable, discreet and secure fit). Each links to its page. Character matched so tiles are equal height.
5. Our Point of Difference. Single Russian hair image plus matched text box. Eyebrow OUR POINT OF DIFFERENCE, heading Exclusive access to the world's most coveted hair. Copy rewritten from TK, framed around toppers and wigs: Russian hair sourced at source, and dye free colour matching from several ponytails.
6. About Us (hair loss and topper framed). Eyebrow ABOUT TATIANA KARELINA, heading Two decades restoring confidence through hair. Photo of Tatiana, matched text box. Copy: two decades as a hair specialist, the hair loss focus, the Russian hair and bespoke craft, restoring confidence.
7. Before and Afters. Eyebrow THE ART OF CHANGE, heading See Our Before and Afters, short intro. Topper and wig before-and-afters (public/images/before-after/), 4 across scroll desktop, 1 scroll mobile, captions name / length / product. Button See More Real Women Real Results to the full page.
8. Client Reviews. Eyebrow CLIENT REVIEWS, heading Real Stories of Confidence and Transformation. Real Google star rating and count with Google logo, linked to Google reviews. Slider of 5 star reviews, topper and wig and hair loss stories first. AggregateRating schema.
9. FAQs. Eyebrow EVERYTHING YOU WANT TO KNOW, heading Frequently Asked Questions. Curate the most distinctive and citable questions from the topper, hair loss and medical wig FAQs (hybrid vs mono vs silk bases, dye free colour matching, 8 to 12 week process, worldwide video consultation, etc). Answers 40 to 80 words. FAQPage schema.
10. Instagram. Static: one photo of Tatiana, the Instagram logo, and @tatianakarelinaofficial linking to the profile.
11. Footer. TK BLACK band, white text, tight aligned columns (match the TK footer exactly). Block 1 About Tatiana Karelina, brand paragraph, both addresses, CALL and WHATSAPP. Block 2 Our Offering: Classic Topper, Frontal Topper, Halo Topper, Wiglets, Medical Wigs. Block 3 About: Prices, The Journey, Video Consultation, Before and Afters, Blog, Contact, Policies and Terms. Block 4 Quick Contact: enquiry form. Bottom: copyright and the worldwide strapline.

## 7. Money page template (all product pages identical)

Classic Topper, Frontal Topper, Halo Topper, Medical Wigs, Hair Loss. Same structure, magazine editorial style, TK treatment:
1. Hero: page image and H1 with the primary keyword.
2. Intro: photo plus matched text box, what it is and who for, keyword in header and copy.
3. Detail sections: photo plus matched text box, specifics, bases (mono, silk, hybrid), the made to measure process, candidacy, USPs.
4. Before and afters filtered to that type, plus Wistia videos for that category where they exist.
5. FAQ: unique citable questions, 40 to 80 word answers, FAQPage schema.
6. Consultation CTA: Book Appointment and the enquiry form, 50% deposit at time of order noted.
Keywords in H1, H2s, body. Wiglets page exists off nav, linked from toppers content. Custom and bespoke wig terms on the Medical Wigs page.

## 8. Other pages

Prices: mirror the real topper and medical wig tables from tatianakarelina.co.uk/prices (Toppers and Medical Wigs tabs), verify every figure. Add the explanatory layer (what determines price, silk vs mono, frontal vs clip in, hand tied wig, 50% deposit at time of order, 8 to 12 weeks). Mobile friendly.

The Journey: the made to measure journey, 8 to 12 weeks framed as bespoke craft. In salon and video routes both. Steps: free consultation, assessment, recommendation, dye free colour match, base selection, hair choices, 50% deposit at order, 8 to 12 week creation, fitting and aftercare (remote clients receive the piece ready to wear, trim by own stylist).

Video Consultation: the remote and worldwide journey, how the video consultation works, remote measurements, remote colour matching, 50% deposit, 8 to 12 weeks, worldwide shipping, piece arrives ready to wear.

Before and Afters (full page): full topper and wig gallery, 4 across scroll desktop, 1 scroll mobile, plus Wistia video before-and-afters grouped by hair loss, toppers, wigs. Videos as thumbnails (Wistia poster) click to play via Wistia embed, vertical Instagram format as a row of vertical cards on desktop, one per screen swipeable on mobile. VideoObject schema. Wistia embed IDs supplied later; build the slots.

London and Manchester: local pages, hair toppers and medical wigs London / Manchester. Manchester positioned honestly as the smaller location, by appointment fittings. LocalBusiness schema per salon.

About: full page expanding the homepage About section.

Contact: EXACT replica of the TK contact page (tatianakarelina.co.uk/contact-us/). Two panels: LEFT light grey with heading Contact us, address pins (both salons), phone, WhatsApp, email, full opening hours table (Mon Closed, Tue to Sat 10AM-6:30PM, Sun Closed), press contact. RIGHT BLACK with heading Make an Enquiry in white, white-bordered fields: First Name / Last Name, Telephone / Email, service dropdown / location dropdown, Message, consent, SUBMIT. Match TK exactly. Only changes: service dropdown lists Classic Topper, Frontal Topper, Halo Topper, Wiglet, Medical Wig, Not Sure; location adds Video Worldwide; any deposit wording is 50% at time of order; add optional photo upload.

## 9. Blog (exact TK blog layout)

Index: category filter bar across the top (black pill buttons): Hair Loss, Toppers, Medical Wigs, Russian Hair. Then a 3-across card grid on desktop, 1 on mobile. Each card: image on top, category tag small caps, serif title, excerpt, READ MORE. TK style.

Article template: hero image, H1, a 134 to 167 word self-contained citable answer block under the H1, body with question-based keyword H2s, internal links to money pages, BlogPosting schema inline, byline, related articles.

18 articles at launch across the four categories (per docs/seo-strategy.md), each targeting its query, each linking to a money page, no duplicate content, no cannibalisation. Build the blog structure and article template now; hold article writing for my content sign-off.

## 10. Images and video

Images from the curated local assets plus public/images/before-after/ and public/images/harvested/. Heroes use high-resolution originals (small 786x586 carousel shots are thumbnails only). Optimise to WebP with width/height and descriptive alt text. Videos hosted on Wistia, embedded (thumbnail plus embed code), never self-hosted. I confirm image placements before final.

## 11. SEO and schema (inline)

Per docs/keyword-map.md and docs/seo-strategy.md. Every page: primary and secondary keywords in H1, H2s and body; per-page title and meta description; canonical; the citable answer-block pattern; inline JSON-LD (Organization, LocalBusiness x2 salons, Service, Product where relevant, BlogPosting, VideoObject, ImageObject, BreadcrumbList, AggregateRating, FAQPage) using 2026 valid types only. A sitemap.xml and robots.txt against the domain. E-E-A-T: the As Featured In press strip and the real Google review rating. No medical disclaimer. Enquiry form posts to Formspree (endpoint supplied later; use a placeholder action).

## 12. Build order

1. Foundation: the stylesheet (brand tokens, fonts, eyebrow style, colour blocking, layout rules), and the shared nav and footer markup.
2. Homepage (11 sections).
3. Money pages (template applied).
4. Other pages (prices, journey, video consultation, before and afters, London, Manchester, about, contact).
5. Blog (index and article template; hold articles for sign-off).
6. SEO and schema pass (inline per page), sitemap, robots.
7. Place images (I confirm).
8. QA: mobile at 390px, box rules, keyword presence, all links, and a final side-by-side of every page against its TK equivalent to confirm the treatment matches.

Deliverable: a clean, self-contained HTML site folder ready to hand to Pontifex for WordPress conversion. Commit per page. Keep docs/progress.md current. Hold the Wistia embed IDs, the Formspree endpoint, image placement confirmations and blog article writing for me. Run a local preview (a simple static server) and give me the URL at each check-in so I can walk it.

Reminder of the golden rule: replicate the TK visual treatment exactly, match the reference, never substitute a white redesign.
