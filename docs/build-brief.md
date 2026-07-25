# Build Brief: Tatiana Karelina Toppers and Wigs

This is the master specification for the standalone toppers and wigs website. Read it in full, then read AGENTS.md, CLAUDE.md, docs/keyword-map.md, docs/seo-strategy.md and docs/content-map.md before making changes. Where this brief and those docs conflict, this brief wins for structure and copy; the SEO docs win for keyword targeting and schema.

## 0. Mode: reconcile, do not rebuild from scratch

A partial build already exists in this project. Reconcile it to this brief: keep anything that already matches, rebuild only what does not. Do not bulldoze and start over. Commit per page. Keep docs/progress.md current throughout. At the end, run the production server and report what changed, page by page, for my walkthrough.

## 1. The site

A brand new STANDALONE domain: tatianakarelinatoppersandwigs.com (.com, worldwide audience). Zero starting authority. Onsite SEO and AI search readiness are the entire launch strategy. Set SITE_URL to https://tatianakarelinatoppersandwigs.com everywhere (canonicals, sitemap, JSON-LD, Open Graph). Read SITE_URL from an environment variable, never hardcode.

Business: Tatiana Karelina, premium Russian hair toppers (classic, frontal, halo), wiglets, and bespoke medical and custom human hair wigs, all made to measure. London (33 Holland Street, W8 4LX) and Manchester (505-49 Piccadilly, M1 2AP) salons. Ships worldwide. Consultations in salon or by video. 50% deposit at time of order, balance on completion. Roughly 20 years, press featured, strong Google reviews.

Scope: toppers, wiglets, medical and custom wigs, hair loss. NO extensions, NO VAT relief content, NO fashion or ready to wear wigs.

## 2. Standing rules (apply to every page)

1. Brand system is fixed: the exact TK logo, the approved TK colour tokens, Playfair Display headings and Inter body, editorial photography, white dominant with ivory as a rare accent band only. Fonts and colours never change.
2. Design freedom within the brand system: the homepage and shared components replicate the TK site's structure where a TK equivalent exists; the inner product pages use a novel, higher quality layout designed within the brand system (the TK product pages are thin, do not copy them). Impeccable and taste skills may polish, never override the brand system or locked items.
3. Replication rule: for any section or page with a tatianakarelina.co.uk equivalent, replicate its structure, section order and treatment, and change only the copy. Rewrite all copy so it is not duplicate content (Google penalises duplication across the two sites). Never invent facts; every claim traces to the source pages or confirmed facts.
4. Text and image pairing (hard layout rule): every section has a photo and a text box, and the text box is always the same height as its photo. Where two text boxes sit side by side, they must contain the same number of characters including spaces so they render identical heights. Never an orphan extra line. Copy is written to fit the box; the box is not stretched to fit the copy.
5. Keyword placement: each page's target keywords (from docs/keyword-map.md) must appear naturally in the H1, the H2 headers and the body copy. Present, never stuffed.
6. Copy rules: UK English, numerals as digits, fully justified body text with text-align justify and text-justify inter-word, hyphens none at every breakpoint (no hyphenation ever). No dividers. No bold in body copy.
7. Mobile first: every layout designed mobile first, verified at 390px. Before and afters show 4 across with horizontal scroll on desktop, 1 image with scroll on mobile.
8. Taxonomy: wiglets are a type of topper (not a third category). Medical wigs and custom or bespoke wigs are ONE product on ONE page (Medical Wigs); that page's copy naturally includes bespoke, custom and human hair wig terms so it captures those searches too.

## 3. Hero (locked, out of scope)

The hero is locked in AGENTS.md (Y=1000 crop, white TATIANA KARELINA wordmark, two line headline Russian Hair Toppers And Wigs / Made To Measure For Hair Loss, lowered text, dark gradient, fixed height). Do not touch it in this build. Known issue to revisit later: crop framing is close but not final. Leave as is.

## 4. Navigation (all caps)

TOPPERS (dropdown: CLASSIC TOPPER, FRONTAL TOPPER, HALO TOPPER), MEDICAL WIGS, PRICES, BEFORE AND AFTERS, BLOG, CONTACT, BOOK APPOINTMENT. Logo left at TK prominence, uppercase menu and black BOOK APPOINTMENT button and phone pill (+44 (0) 203 645 1761) to the right. Mobile hamburger with grouped menu. Wiglets and custom wigs are NOT in the nav (they exist as pages, linked from within content).

## 5. Homepage (11 sections, in order)

Each section follows the text and image pairing rule. Where a TK equivalent exists, replicate structure and rewrite copy.

1. Hero (locked, section 3 above).
2. Trust strip. Heading: World's Best Toppers and Medical Wigs. Then eyebrow AS FEATURED IN with the press logo row (Daily Mail, Evening Standard, Forbes, Cosmopolitan, Daily Express, PopSugar, Marie Claire, Metro) from the harvested press strip image, greyscale on white. Same position and treatment as the TK homepage.
3. Hair loss explanation (own section, own eyebrow and header, TK format). Eyebrow HAIR LOSS AND THINNING (or similar), heading, explanatory copy rewritten from the TK hair loss page: the emotional reality, that it is common, ranges from gradual (genetics, hormones, pregnancy, menopause) to sudden (stress, illness, chemotherapy), and that made to measure toppers and medical wigs restore coverage and confidence. Photo plus matched text box. Buttons to Toppers and Medical Wigs. Message: toppers and medical wigs are the solution to hair loss and thinning.
4. Toppers and wigs grid (separate section from 3, own eyebrow and header). Use the TK homepage Hair Loss section heading spirit (Rediscover your confidence, let us prove that hair loss can be managed). A four tile grid, 2 top and 2 below: Classic Topper, Frontal Topper, Halo Topper, Medical Wigs. Each tile: image, short intro line, and the bullet USPs taken from the TK homepage and reworded (Classic: bespoke coverage for thinning areas, finest Russian hair, hand blended natural colour match, lightweight discreet secure fit. Frontal: ideal for receding hairlines and temple loss, suitable for frontal fibrosing alopecia, finest Russian hair, natural discreet front hairline coverage. Halo: designed for more advanced thinning, ideal when full clips are not suitable, finest Russian hair, lightweight discreet secure fit. Medical Wig: made to measure, finest Russian hair, lightweight and breathable, discreet and secure fit). Each tile links to its page. Tiles matched to equal character counts so none is taller.
5. Our Point of Difference. Single Russian hair image plus matched text box. Eyebrow OUR POINT OF DIFFERENCE, heading Exclusive access to the world's most coveted hair. Copy rewritten from TK but framed around toppers and wigs: why Russian hair makes the most natural, undetectable toppers and wigs, sourced at source before brokers mix it with Asian hair, and the dye free colour matching (drawing from several ponytails, no dye). Russian hair plus dye free colour matching are the two headline points of difference.
6. About Us (new, hair loss and topper framed). Eyebrow ABOUT TATIANA KARELINA, heading Two decades restoring confidence through hair. Photo of Tatiana with a client or a piece, matched text box. Copy from the hair loss and topper perspective: two decades as a hair specialist, the focus on hair loss solutions, the obsession with Russian hair and bespoke craft, restoring confidence to women experiencing thinning and loss.
7. Before and Afters. Eyebrow THE ART OF CHANGE, heading See Our Before and Afters, short intro line. Carousel of topper and wig before and afters (from public/images/before-after/), 4 across with scroll on desktop, 1 with scroll on mobile, captions name / length / product (price only where available). Button: See More Real Women Real Results, to the full before and afters page.
8. Client Reviews. Eyebrow CLIENT REVIEWS, heading Real Stories of Confidence and Transformation. Display the real Google star rating and review count with the Google logo, linked to the Google reviews. Slider of 5 star reviews, prioritising topper, wig and hair loss stories, falling back to generic excellent service reviews. AggregateRating schema.
9. FAQs. Eyebrow EVERYTHING YOU WANT TO KNOW, heading Frequently Asked Questions. Curate from the real topper, hair loss and medical wig FAQs the most distinctive and citable questions (unique to the offering, e.g. hybrid vs mono vs silk bases, dye free colour matching, the 8 to 12 week process, worldwide video consultation, or strong informational intent). Answers 40 to 80 words for AI citation. FAQPage schema kept (supporting AI and entity signal, not for rich results). I approve the final selection when I see it.
10. Instagram. Minimal, static: a single photo of Tatiana (with a client or piece), the Instagram logo, and the @tatianakarelinaofficial handle linking to the profile. No live feed, no grid.
11. Footer. TK four block style, topper and wig content only. Block 1 About Tatiana Karelina: brand paragraph, both salon addresses, CALL +44 (0) 203 645 1761, WHATSAPP +44 (0) 771 439 2999. Block 2 Our Offering: Classic Topper, Frontal Topper, Halo Topper, Wiglets, Medical Wigs, Custom Wigs. Block 3 About: Prices, The Journey, Video Consultation, Before and Afters, Blog, Contact, Policies and Terms. Block 4 Quick Contact: the enquiry form with optional photo upload.

## 6. Money page template (all product pages identical structure)

Applies to Classic Topper, Frontal Topper, Halo Topper, Medical Wigs, Hair Loss. Novel, high quality layout designed within the brand system (do not copy the thin TK product pages). Same structure across all:

1. Hero: page specific image and H1 carrying the primary keyword.
2. Intro: photo plus matched text box, what it is and who it is for, keyword in the header and copy.
3. Detail sections: each a photo plus matched text box, covering specifics, bases (mono, silk, hybrid), the made to measure process, candidacy, USPs. Character matched where side by side.
4. Before and afters filtered to that type (4 across desktop scroll, 1 mobile scroll), plus Wistia videos for that category where they exist.
5. FAQ: the unique and citable questions for that page, 40 to 80 word answers, FAQPage schema.
6. Consultation CTA: Book Appointment and the enquiry form, 50% deposit at time of order noted.

Keywords in H1, H2s and body per docs/keyword-map.md. Wiglets page exists (off nav), linked from the toppers pillar and topper content. Custom or bespoke wig terms live on the Medical Wigs page copy.

## 7. Other pages

Prices: pull the real topper and medical wig tables from tatianakarelina.co.uk/prices (Toppers and Medical Wigs tabs only). Mirror them exactly, verify every figure against the live page. Add the explanatory layer (what determines price: base type, length, hair weight; why silk costs more than mono; why frontal costs less than clip in toppers; why a hand tied wig costs what it does; the 50% deposit at time of order and 8 to 12 week timeline). Mobile friendly tables. No extensions pricing, no VAT content.

The Journey / How It Works: the made to measure journey, framed as 8 to 12 weeks being a feature of bespoke craft. In salon and video routes both first class. Steps: free consultation (London, Manchester or video), assessment, recommendation of type, dye free colour match from several Russian ponytails, base selection, hair type colour and length, 50% deposit at time of order, 8 to 12 week creation, fitting and aftercare (remote clients receive the piece ready to wear, final trim by their own stylist).

Video Consultation: the remote and worldwide journey. How the video consultation works, how measurements are taken remotely, remote colour matching, the 50% deposit and 8 to 12 weeks, worldwide shipping, and that a remote client's piece arrives ready to wear (no in person cut and fit). Answers the objection: how can a bespoke piece be accurate without visiting.

Before and Afters (full page): the full topper and wig gallery, 4 across desktop scroll, 1 mobile scroll, with the Wistia video before and afters grouped by category (hair loss, toppers, wigs). Videos shown as thumbnails (Wistia poster), click to play via Wistia embed, vertical Instagram format shown as a row of vertical cards on desktop and one per screen swipeable on mobile. VideoObject schema per video. Wistia embed IDs to be supplied later; build the component with a slot per video.

London and Manchester: local pages targeting hair toppers London / Manchester and medical wigs London / Manchester. Position honestly: Manchester is the smaller location, by appointment topper and wig fittings; do not overclaim capacity. LocalBusiness schema per salon.

About: full about page expanding section 6 of the homepage.

Contact: heading Contact Us, both salon addresses, phone, WhatsApp, email, opening hours (Tue to Sat 10am to 6:30pm, closed Mon and Sun), press contact. Make an Enquiry form: Name, Telephone, Email, service dropdown (Classic Topper, Frontal Topper, Halo Topper, Wiglet, Medical Wig, Not Sure), location dropdown (London, Manchester, Video Consultation Worldwide), Message, consent checkbox, optional photo upload, UTM hidden fields. 50% deposit at time of order in any terms wording (not the TK extensions deposit).

## 8. Blog (exactly the TK blog layout)

Blog index: category filter bar across the top (black pill buttons): Hair Loss, Toppers, Medical Wigs, Russian Hair. Then a 3 across grid of article cards on desktop (1 on mobile). Each card: image on top, category tag in small caps, serif title, excerpt, READ MORE. Same brand skin.

Article template: hero image, H1, a 134 to 167 word self contained citable answer block directly under the H1 (per docs/seo-strategy.md), body with question based keyword H2s, internal links to money pages, BlogPosting schema, author byline, related articles.

18 articles at launch across the four categories, each targeting its query from docs/seo-strategy.md, each linking to at least one money page, no duplicate content, no cannibalisation of money page primary keywords. Draw from and rewrite existing TK blog content where an equivalent exists; write net new where it does not.

## 9. Images and video

Source of truth for images: my curated local assets library plus the harvested set in public/images/before-after/ and public/images/harvested/. Rules: heroes use high resolution local originals (the small harvested carousel shots at 786x586 are thumbnail only, not for heroes); before and afters and section images use the harvested and local sets; serve everything through next/image as WebP with descriptive alt text. Videos are hosted on Wistia and embedded (thumbnail plus embed), never self hosted. I confirm image placements before final.

## 10. SEO and schema

Per docs/keyword-map.md and docs/seo-strategy.md. Every page: primary and secondary keywords in H1, H2s and body; per page metadata; canonical; the citable answer block pattern for AI search; full JSON-LD (Organization, LocalBusiness x2 salons, Service, Product where relevant, BlogPosting, VideoObject, ImageObject, BreadcrumbList, AggregateRating, FAQPage) using 2026 valid types only. Generated sitemap.xml and robots.txt against SITE_URL. E-E-A-T trust signals: the As Featured In press strip and the real Google review rating. No medical disclaimer. Lead capture via the enquiry form (Formspree, endpoint supplied later, behind an env variable).

## 11. Build order

1. Shared components: nav, footer, contact and enquiry form (with photo upload behind env gate), before and after component (4 across scroll desktop, 1 mobile), Wistia video component, FAQ accordion with schema, review slider.
2. Homepage (11 sections).
3. Money pages (template applied to all).
4. Other pages (prices, journey, video consultation, before and afters, London, Manchester, about, contact).
5. Blog (index, article template, 18 articles).
6. SEO and schema pass across everything.
7. Place images (I confirm placements).
8. QA: mobile at 390px, Core Web Vitals on throttled mobile, text and image box rules, keyword presence, all links.

Commit per page. Keep docs/progress.md current. When complete, run the production server and report changes page by page for my walkthrough. Hold Wistia embed IDs, the Formspree endpoint, and final image placement confirmations for me.
