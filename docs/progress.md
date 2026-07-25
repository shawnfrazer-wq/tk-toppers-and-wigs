# Progress

## Current state

Static HTML build — wave 1 (foundation) and wave 2 (homepage) shipped

Foundation
- `src-html/` authoring source, `dist/` deliverable, `build.py` zero-dep include-processor.
- `site.css` — TK-matched brand tokens, self-hosted Playfair + Inter (Latin subsets), typography (headings 400 weight not 500, matching TK Butler), eyebrow (13/12/11px stack with 38px hairline rule, matching TK Elementor CSS values), buttons, nav + dropdown, footer, forms (light + dark themes), hero, section patterns.
- `partials/head.html` `nav.html` `footer.html` `foot.html`.
- Footer tightened to TK exact spacing (50/30px padding, 15px @600 headings, 12px body, ~6px link gap) after reading its Elementor CSS.

Homepage (11 sections)
1. **Hero** — LOCKED per AGENTS.md (Y=1000 crop, white wordmark, lowered text, dark top+bottom fades).
2. **Trust strip** — "World's Best Toppers and Medical Wigs" + AS FEATURED IN eyebrow + greyscale press strip.
3. **Hair loss explanation** — 2-col image+text, buttons to Toppers and Medical Wigs.
4. **4-tile grid** — Classic / Frontal / Halo / Medical Wigs with image + intro + 3-USP bullets each.
5. **Our Point of Difference** — ivory band, 2-col Russian hair image+text (reverse).
6. **About Us** — 2-col Tatiana photo+text, "Read Tatiana's story" CTA.
7. **Before and Afters** — 6-card horizontal-scroll row, "See More Real Women Real Results" CTA.
8. **Client Reviews** — Google star band (5.0, 157 reviews placeholder), review slider with 3 TODO CONFIRM placeholders rendered italic.
9. **FAQs** — 6 curated distinctive questions with 40–80 word answers, native details/summary.
10. **Instagram** — single Tatiana photo + @tatianakarelinaofficial handle + IG glyph.
11. **Footer** — TK black band (shared partial).

AGENTS.md carries new **Spacing density standing rule** — never default to airy; read TK's Elementor CSS before choosing values; err tight when exact values unavailable.

Local preview: **http://localhost:8080/**

Held for Shawn
- Real Google review count + star + reviews (currently 5.0/157 placeholder + 3 italic TODO reviews).
- Real Instagram photo for section 10 (currently Tatiana-with-ponytails placeholder).
- Real hair-loss section image (currently `hair-loss-page-hero.webp` from harvest).
- 4-tile grid uses harvested carousel thumbnails (786×586) — small; Shawn to confirm or supply larger crops for these tiles.
- All image placements per section (brief §10 rule).

## Site build — COMPLETE (18/18 pages)

All pages below are written and rebuild-verified (`python3 src-html/build.py` → "built 18 pages, 201 images, 3 brand assets, 3 root files"):

1. `/` — Homepage (pre-existing, real trust-strip press image swapped in).
2. `/toppers/` — Toppers pillar. Product-type grid, before/afters, Wistia video slot, 7-item FAQ + FAQPage schema, VideoObject schema.
3. `/toppers/classic-topper.html` — Product schema (£1,050–£1,900), FAQ, VideoObject.
4. `/toppers/frontal-topper.html` — Product schema (£615–£1,335), FAQ, VideoObject.
5. `/toppers/halo-topper.html` — Product schema (£1,100–£1,950), FAQ, VideoObject.
6. `/wiglets.html` — Smaller off-nav page, 2 before/afters, FAQ, VideoObject.
7. `/wigs/medical-wigs.html` — Product schema (£2,600–£3,725), chemo-focused FAQ, 3 before/afters (image paths corrected to real filenames), VideoObject.
8. `/hair-loss.html` — Causes grid, solution pairing, 3-tile recap.
9. `/journey.html` — In-salon/by-video route cards, 9-step process.
10. `/video-consultation.html` — Remote 6-step process, FAQ + schema.
11. `/prices.html` — 4 full pricing tables (Classic/Frontal/Halo/Full Wig) from salvaged-copy §6, what's-included checklist.
12. `/before-and-afters.html` — All 20 real before/after pairs, filterable gallery (6 pills), 3 Wistia video placeholders + VideoObject schema (@graph).
13. `/london.html` — LocalBusiness schema, Google Maps embed.
14. `/manchester.html` — LocalBusiness schema, Google Maps embed.
15. `/about.html` — Organization schema.
16. `/contact.html` — Two-panel layout: info panel (both salons, hours, press contact) + dark enquiry form (Formspree placeholder action, honeypot, UTM fields, photo upload, consent).
17. `/blog/` — Filterable journal index. 2 real article titles/excerpts shown as "Coming Soon" metadata-only cards (full bodies held per sign-off requirement — see `docs/salvaged-copy.md` §7.1/7.2) + 1 scaffold card (§7.3). No dead links to unpublished articles.
18. `/blog/article-template.html` — Reusable scaffold template (hero/body/FAQ/CTA structure) for when article bodies are approved. Excluded from sitemap.xml and disallowed in robots.txt (not for indexing yet).

## SEO / technical pass — COMPLETE

- `sitemap.xml` and `robots.txt` added at site root (`public/`), now copied into `dist/` by `build.py` (root-file copy step added).
- `favicon.ico` generated (TK monogram, navy `#112337` background, Playfair Display, multi-size ICO 16/32/48/64) — was previously missing (0 pages had it).
- **VideoObject schema** added to all 7 pages with a Wistia video-slot placeholder (toppers pillar, classic/frontal/halo toppers, wiglets, medical wigs, before-and-afters ×3 via `@graph`).
- All JSON-LD blocks across all 18 pages validated — 0 parse errors.
- Full link/asset audit run on the built `dist/` output — 0 broken internal links, 0 missing images (fixed 3 wrong before/after filenames on medical-wigs.html, corrected 2160×2160 dimensions for Margaret/Tulsi images).
- Schema coverage now: Organization (about), LocalBusiness ×2 (london/manchester), Product ×4 (classic/frontal/halo toppers, medical wigs), FAQPage (toppers pillar, classic/frontal/halo, wiglets, medical wigs, video-consultation), BreadcrumbList (all 18 pages), VideoObject (7 pages), AggregateRating (homepage). ImageObject and BlogPosting intentionally not added — no article bodies or per-image licensing data exist yet to support them accurately.

## Remaining / held items (not blockers — flagged for Shawn)

- **Blog article bodies** — 2 real articles + 1 scaffold have titles/excerpts live on `/blog/`, but full bodies are withheld pending sign-off (per governing instruction). `article-template.html` is ready to receive them.
- **Wistia embeds** — 10 video placeholders across the site (`data-wistia-placeholder` attributes) need real embed codes once videos are on Wistia; never self-hosted/compressed per standing rule.
- **Formspree endpoint** — contact form currently posts to a placeholder action; needs the real Formspree form ID.
- **TODO CONFIRM items** — 2 international-shipping/remote-fitting FAQ items (salvaged-copy §5.2) remain unpublished pending Shawn's confirmation.
- Full 390px-width Playwright screenshot QA and side-by-side vs. tatianakarelina.co.uk comparison were not completed this pass (local static QA — link/schema/asset validation — was done instead); recommend a follow-up visual QA pass before go-live.

## 2026-07-17 late night — file:// portability fix + Toppers page redesign

- **Site-wide link fix (all 18 pages):** `build.py` now runs a `relativize_links()` post-process pass after every build. It rewrites every root-absolute `href="/..."` / `src="/..."` / `action="/..."` into a path relative to each page's depth in `dist/`, and expands bare directory links (`/`, `/toppers/`) to their `index.html`. Result: **`dist/index.html` can now be double-clicked and browsed via `file://` with zero server** — every internal link, stylesheet, font, and image resolves correctly at any depth. Verified with a headless-browser click-through: home → Toppers nav → Classic Topper tile → logo home, all resolved to the correct `file://` paths. Confirmed 0 remaining absolute-root links anywhere in `dist/` after rebuild. External URLs (canonical tags, og:url, JSON-LD, schema.org `https://...`), `tel:`, `mailto:`, and `#anchors` are untouched.
- **Toppers pillar page (`/toppers/`) — visual refresh, scoped to this page only:** added a page-scoped `<style>` block (does not touch `css/site.css`, so no other page is affected) inspired by the structural polish of the TK Academy site reference, but recoloured to strict black/white/grey and kept TK's real font stack (Playfair Display serif + Montserrat sans + Poppins accent):
  - Eyebrows now flanked by short rules on both sides (`.eyebrow--flanked`) instead of the single hairline below, echoing Academy's symmetrical eyebrow treatment.
  - One word per major heading gets an italic serif accent (`.accent` — italic, same black ink, no colour change) for a touch of editorial flourish, e.g. "Hair *Toppers*", "Coverage exactly where you need *it*".
  - Topper-type tiles now have a thin border, rounded corners, and a lift + shadow on hover (previously borderless/flat).
  - "Signature approach" feature grid switched from a top-hairline to an editorial vertical rule on desktop (top rule preserved on mobile).
  - Before/after cards get the same lift-on-hover treatment as the tiles.
  - No content, copy, images, FAQ, or schema were changed — only the visual treatment layer, per the "polish never override brand system" rule. Assumption flagged: this page intentionally deviates from the html-build-brief.md "replicate tatianakarelina.co.uk EXACTLY" golden rule, per Shawn's explicit request to follow the Academy site's structure for this page specifically — the other 17 pages are untouched and still follow the original TK-clone treatment.
  - Verified via headless-browser screenshots at desktop (1280px) and mobile (390px) — no overflow, no wrapping issues, cards and eyebrows render cleanly at both sizes.
- Not yet propagated to Classic/Frontal/Halo topper pages (same "money page template" family) — only the pillar page (`/toppers/`) was redesigned this pass, per the literal request ("the topper page").

### 2026-07-18 — Toppers page v2: real structural redesign (v1 was rejected)

Shawn rejected the pass above as decorative-only ("this is exactly the same thing Claude did, nothing has changed"), correctly diagnosing that it kept the same underlying TK page template (full-bleed photo hero, tile-grid cards, symmetric sections) and only added surface polish. Pulled the real Academy reference (`Acadaemy Website  WIP/index.html`) and screenshotted it to compare structurally rather than decoratively. v2 changes the actual markup/layout, not just CSS:

- **Hero rebuilt as an asymmetric split**, not full-bleed photo-behind-text: eyebrow + big serif H1 (up to ~68px) + lead paragraph + two CTAs (filled "Book a Consultation" + outline "See the Three Types") on the left, framed portrait image on the right. Mirrors Academy's hero exactly (text block left, image right, dual CTAs).
- **Added a full-bleed black stat band** (new section, mirrors Academy's 4-column white-on-black stat band) using only verified facts already published elsewhere on the TK site — nothing invented: "18 Years / Russian Hair Expertise" (from about.html), "3 Types / Classic, Frontal & Halo" (from the toppers page's own "only UK company" claim), "Dye-Free / Hand-Blended Colour" (from about.html and this page), "London & Manchester / Plus Video Consultations" (from about.html's CTA copy). No client-count or other numeric stat was fabricated — none exists in the source content.
- **"Three topper types" section rebuilt from a 4-tile card grid into a numbered list with horizontal-rule dividers** (01 Classic / 02 Frontal / 03 Halo / 04 Wiglets), paired with a single feature image — directly mirrors Academy's "Who This Class Is For" numbered-list pattern instead of the old tile-grid.
- **"Signature approach" section rebuilt from a 3-column feature grid into a stacked left-border (blockquote-style) list**, paired with an image — directly mirrors Academy's "What You Will Learn" left-border block pattern instead of the old vertical-rule columns.
- **Alternating image position** across sections (hero image right → topper-types image left → signature-approach image right) for the asymmetric rhythm Academy uses, instead of the old site's consistent centred/symmetric sections.
- Bumped section-heading (`h2`) type scale bigger (up to ~48px) for more editorial presence, matching Academy's larger headline sizing.
- Kept from v1 (still valid, not decorative-only on their own once paired with the structural changes above): flanked-eyebrow style, italic accent word, before/after card hover-lift.
- Colour stayed strict black/white/grey (TK tokens), fonts stayed TK's real stack (Playfair Display + Montserrat + Poppins) — only Academy's layout architecture was borrowed, not its champagne palette or its fonts.
- No content, copy, images, FAQ or schema changed beyond what's listed above (same rule as v1) — this remains a structural/visual redesign only.
- Verified via headless-browser screenshots at desktop (1280px) and mobile (390/375px), and by direct visual comparison against the Academy reference screenshots — confirmed the numbered-list, left-border, split-hero and stat-band patterns are genuinely present, not just re-skinned tiles.
- Re-verified 0 remaining absolute-root links after rebuild (file:// portability fix still holds).

### 2026-07-18 — Toppers page v2.1: fixed the text/photo equal-height rule

Shawn flagged that the v2 structural redesign broke a documented hard layout rule from `build-brief.md`/`html-build-brief.md`: "every section has a photo and a text box, and the text box is always the same height as its photo ... Copy is written to fit the box; the box is not stretched to fit the copy." Measured the three new `.pair` sections and confirmed real mismatches (intro: image 679px vs text 263px; topper-types: 781 vs 838; signature-approach: 679 vs 506).

First attempt (rejected on my own visual QA before showing Shawn): tried CSS `justify-content: space-between` to spread existing copy across the photo's fixed height — this left ugly, unprofessional dead gaps between paragraphs/list items. That is exactly the anti-pattern the brief warns against ("the box is not stretched to fit the copy").

Correct fix implemented: reversed the relationship so the **photo crops to match the text's natural height**, never the other way round:
- Added one extra genuine sentence to the intro section (Russian hair, hand-blended colour, London/Manchester or by video — all facts already established elsewhere on the site, nothing invented) so its natural copy length is reasonable.
- Removed the fixed `aspect-ratio: 4/5` on `.pair__image` for this page at 900px and up.
- Made the `<img>` `position: absolute; inset: 0; object-fit: cover;` inside a `position: relative` container — this removes the image from the grid's auto-sizing pass entirely (an img with HTML `width`/`height` attributes otherwise leaks its own intrinsic aspect ratio into the row's auto height, which was the root cause of the mismatch even after `align-items: stretch`).
- Result: the grid row height is now driven purely by the text column's real content height, and the photo stretches/crops to fill exactly that height — verified via Playwright measurement that `pair__body` height, `pair__image` height, and the actual list content's bottom edge are all pixel-identical (diff = 0) for all three sections, with no dead space and no artificial spacing.
- Scoped entirely to this page's `<style>` block (`main .pair`, `main .pair__image`) — does not touch the shared `.pair` component in `site.css`, so no other page is affected.
- Re-verified on both desktop (1280px) and mobile (390px) screenshots; mobile is unaffected since the fix only applies at the 900px+ breakpoint where the two-column pair layout exists.

## Standing rules

- Commit per page.
- Refresh this file at each check-in.
- Hero locked (AGENTS.md hero rule).
- Never default to airy — read TK Elementor CSS and match (AGENTS.md spacing density rule).
- Never let macOS ` 2.*` duplicates back into any directory.

## 2026-07-23 — Wave 1: Academy layout rollout, sitewide (homepage + toppers + 4 product pages)

Shawn's governing corrections this session (now standing rules, recorded in `css/site.css` §25):

1. **Photos are STANDARD SIZE, never zoomed.** The v2.1 crop-photo-to-text-height rule is retired — it was the cause of the zoomed-in photos. Every paired photo now sits in the shared 4:5 frame (`.pair__image`), uniform 584px tall at 1280px desktop, sources chosen at 0.71–0.80 aspect so the crop is near zero.
2. **Copy balances the photo, not the reverse.** Each pair carries 1–2+ substantial paragraphs (measured 419–508px vs the 584px photo, centred); no stretched boxes, no dead gaps.
3. **Where tatianakarelina.co.uk has a working component, clone it exactly.** Before/after rows are now a true carousel: desktop EXACTLY 4 identical-size thumbnails per view with prev/next arrows (verified via Playwright: 4 per view, one-card step, arrows disable at ends), mobile 1 per view swipeable. Shared enhancer in `partials/foot.html` auto-upgrades every `.ba-row` site-wide.
4. **Photo curation** — no photo repeats within a page (old homepage used tatiana-with-ponytails 3×; now hero/PoD/About/IG all distinct). Contact sheets of the full image pool generated for Shawn's review.

Approved by Shawn before the pass: **Academy split hero replaces the locked full-bleed hero** (AGENTS.md hero-lock superseded), rollout in waves with check-ins.

Redesigned this wave (Academy architecture, strict black/white/grey, TK font stack):
- `/` — split hero (salon-made-to-measure-portrait), black stat band (20 Years / Russian Hair / Dye-Free / London & Manchester), trust strip kept TK-exact, hair-loss pair (toppers-03), offering rebuilt from 4-tile grid → numbered list + feature photo (toppers-04), PoD (wigs-18), About (tatiana-with-ponytails) + press-mention paragraph, 8-card before/after carousel, reviews/FAQ/IG restyled with flanked eyebrows + accent words. Organization + FAQPage + Breadcrumb JSON-LD added (homepage previously had none in src).
- `/toppers/` — photos re-fixed to standard frames (types image → new-toppers-24; hero shows full composition), intro copy extended, gallery → carousel (6 cards).
- `/toppers/classic-topper.html`, `frontal-topper.html`, `halo-topper.html`, `/wigs/medical-wigs.html` — full-bleed photo heroes → split heroes with standard-frame product shots, flanked eyebrows + accent words throughout, thin single-paragraph sections expanded (facts already established on-site only), candidacy sections given intro paragraphs, galleries → 4-card carousels, medical-wigs intro photo deduplicated (wigs-02 → wigs-16, hero keeps wigs-01).

Shared system changes: `css/site.css` §25 (Academy components promoted from the toppers page: flanked eyebrows, accent, split-hero, stat-band, numbered-list, border-list, tile/card polish, bigger editorial h2s) + §26 (ba-carousel) + pair balance tuning (0.8fr/1.2fr columns). `partials/foot.html` carries the carousel JS.

QA: rebuild clean (18 pages), 0 broken internal links/assets, 0 JS errors, carousel behaviour verified headless, desktop 1280px + mobile 390px screenshots reviewed for all 6 redesigned pages.

## Next steps

- Shawn reviews Wave 1 (homepage, toppers pillar, classic/frontal/halo, medical wigs).
- Wave 2 on approval: hair-loss.html, wiglets.html, prices, journey, video-consultation, before-and-afters, london, manchester, about, contact, blog index — same treatment.
- Still held: real Google review count/text, Wistia embeds, Formspree endpoint, blog article bodies.

## 2026-07-23 — Round 2: TK-parity fixes (per Shawn's screenshot review vs live site)

1. **Before/afters cleaned to match TK originals.** All 20 harvested before/after webps had a caption strip baked into the image ("X achieved this look with... £N"); strips detected and cropped programmatically (105px/1152 and 197px/2160). The BEFORE/AFTER badge overlay and the sub-captions were also removed across every page — TK shows clean photos only. Captions live on in alt text for SEO.
2. **FAQ resized to TK treatment.** Full-container-width rows (was 44rem), serif questions at clamp 1.15–1.5rem (was 1.05rem), 1.5rem row padding, circled-plus icon (30px ring) matching TK's ⊕.
3. **Press strip enlarged to TK scale.** Height cap removed; strip now renders at up to 66rem wide at natural aspect (two large logo rows), matching the live site's proportion.
4. **Client reviews rebuilt as the exact TK component.** "EXCELLENT ★★★★★ 157 reviews Google" band (amber stars, coloured Google wordmark) + card slider: white shadowed cards with speech-bubble tail, grey quote mark, black stars + verified tick, italic grey excerpt with Read more → Google, G logo bottom-right, reviewer name in caps below. Populated with 3 real Google reviews shown on the live TK site (Antonia Moss, Lisa Robinson, Jennifer Solomon). NOTE for Shawn: these are extension-era reviews — swap in topper/wig-specific ones when chosen.
5. **Contact page rebuilt as the exact TK replica** (scraped tatianakarelina.co.uk/contact-us/): grey "Contact us" panel (icon lines: both addresses, phone, WhatsApp, email; full 7-day hours table Monday Closed → Sunday Closed; press contact Denise Palmer at Borne Media) beside black "Make an Enquiry" panel (First/Last Name, Telephone/Email, service + location dropdowns with our six services and Video Worldwide, Message, consent with terms links, optional photo upload, full-width white SUBMIT). Below: "Before You Order" small print with the 50%-deposit / 8-12 week wording, then a full-width Google map band (33 Holland Street). Formspree ID still placeholder.

## 2026-07-23 — Round 3: inner pages rebuilt to the Academy instructor.html template

Per Shawn: instructor.html is the inner-page reference; text must MATCH photo height with fuller SEO copy (build-brief golden rule — copy written to fill the box).

- H1 scale corrected first: Academy hero H1 is clamp(44px, 4.4vw, 60px), lh 1.05, ls -0.02em (42px mobile) — applied to all heroes/page intros; H2 cap brought to Academy's 44px.
- **Inner-page template** (classic/frontal/halo/medical wigs): centred page intro (flanked eyebrow → 60px serif H1 with accent word → centred lead → dual CTAs) → photo + FULL-HEIGHT text pair (H2, italic serif pull-quote with left rule, 3 substantial paragraphs) → ivory "The detail, in brief" band with two character-matched text columns (H3 + 2 paragraphs each) → candidacy pair (reversed) with intro para + check-list + closing para → carousel/video/FAQ/CTA unchanged. All copy expanded for SEO from established facts only (bases, 8-12 weeks, 50% deposit, dye-free blending, video worldwide, care guidance, cross-links between topper types).
- Pair balance measured (Playwright, 1280px): photo 584px vs text 554-619px on all rebuilt pairs (lists taller by design) — no thin-text sections remain.
- Homepage + toppers pillar pairs given Academy pull-quotes and extra copy; toppers signature list gained a 4th item (made to measure, in salon or by video).
- 0 broken refs after rebuild.

## 2026-07-23 — Round 4: approved copy live, no dash rule, blog launched (18 articles)

Shawn approvals applied: hero H1 option C (unchanged wording), NO medical disclaimer, reviews held as placeholders in the exact TK card format, unverified figures (7,000 fittings, £910 to £1,725, 12 to 14 weeks) NOT used; site standardises on 8 to 12 weeks and the on site product schema price ranges.

- Approved Draft 1 copy applied sitewide: new hero lead and eyebrow, stat band (3 Topper Types, The Only Company in the UK), rewritten Point of Difference around all USPs (heading: Nothing off the shelf. Everything made around you), 4 paragraph hair loss section with GP line, offering descriptions, toppers pillar rewrite with The Topper Journey section and upgraded 8 question FAQ, wiglets intro, prices explainer, about addition, hair-loss.html fully rebuilt (page intro, answer block, causes two col band, coverage pair, causes FAQ + schema).
- NO HYPHENS OR DASHES ANYWHERE: automated sweep across all pages, partials, META blocks, alt text and JSON-LD; em and en dashes rewritten, compounds unhyphenated (made to measure, dye free, hand tied, colour matched, full lace, clip free, sulphate free...). Audit: 0 dash occurrences in rendered text. Addresses and URLs untouched.
- All body text fully justified (main p/li), hyphenation disabled at every breakpoint; labels, buttons and centred headings excepted.
- Photos sized to text boxes: pair image column widened to 0.85fr (photo 620px at 1280) and copy topped up; measured 620/595 to 621/669 across pages, lists taller by design, centring absorbs the rest.
- TKA H1 scale (clamp 44 to 60px) now also applied to page hero variants (journey, prices, video consultation, before and afters, london, manchester); articles use 36 to 48px.
- Before/after carousel (TK exact: 4 desktop, 1 mobile, arrows) added to every inner page: hair loss, journey, video consultation, prices, about, london, manchester; wiglets topped to 4 cards.
- BLOG LAUNCHED: 18 net new SEO articles per docs/seo-strategy.md (15 launch titles + base types, dye free colour matching, do toppers damage your hair). Every article: 134 to 167 word citable answer block naming the entity with a number, question H2s, internal money page links, Tatiana byline, BlogPosting + FAQPage + BreadcrumbList schema, no dashes, justified. Categories: Hair Loss 5, Toppers 7, Medical Wigs 3, Russian Hair 3.
- Blog index rebuilt to the TK blog pattern: pill filter bar (All, Hair Loss, Toppers, Medical Wigs, Russian Hair) + 3 across cards (image, small caps tag, serif title, excerpt, READ MORE).
- sitemap.xml extended with all 18 article URLs. QA: 0 broken refs, 0 JSON-LD errors, 0 JS errors, 36 pages build clean.

Held for Shawn: 3 Google review picks (placeholders in correct format), Wistia embeds, Formspree ID.
