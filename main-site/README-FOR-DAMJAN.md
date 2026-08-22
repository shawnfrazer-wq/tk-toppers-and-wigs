# TK Main Site Redesign — Complete Handover (11 pages)

## What this is
Eleven finished page designs for tatianakarelina.co.uk, built as plain standalone
HTML for conversion into the existing WordPress/Elementor site. Open any file in
a browser to view it (all assets are relative, no server needed). Live previews
at https://shawnfrazer-wq.github.io/tk-toppers-and-wigs/main/{filename}

| File | Replaces the live page at |
|---|---|
| hair-loss.html | /hair-loss/ |
| hair-toppers.html | /clip-in-toppers-and-wiglets/ |
| medical-wigs.html | /medical-wigs/ |
| topper-giveaway.html | /topper-giveaway/ (new page) |
| micro-rings-hair-extensions.html | /micro-rings-hair-extensions/ |
| micro-bonds.html | /micro-bonds/ |
| tape-hair-extensions.html | /tape-hair-extensions/ |
| wefts-hair-extensions.html | /wefts-hair-extensions/ |
| clip-in-extensions.html | /clip-in-extensions/ |
| hair-extensions-braids-ponytails.html | /hair-extensions-braids-ponytails/ |
| prices.html | /prices/ |

URL slugs must NOT change. index.html is only a preview hub for review and is
not to be built in WordPress.

## Meta data — port ALL of this into WordPress (Rank Math or Yoast)

Each HTML head already contains the exact meta title, meta description and
canonical URL. They are repeated here so nothing is missed. Character counts
are within Google's display limits.

| Page | Meta title | Canonical |
|---|---|---|
| hair-loss | Hair Loss Solutions for Women \| Tatiana Karelina | /hair-loss/ |
| hair-toppers | Russian Hair Toppers & Wiglets for Women \| Tatiana Karelina | /clip-in-toppers-and-wiglets/ |
| medical-wigs | Medical Wigs Made to Measure \| Tatiana Karelina | /medical-wigs/ |
| topper-giveaway | Monthly Topper Giveaway for Women with Hair Loss \| Tatiana Karelina | /topper-giveaway/ |
| micro-rings | Micro Ring Hair Extensions in London & Manchester \| Tatiana Karelina | /micro-rings-hair-extensions/ |
| micro-bonds | Micro Bond Hair Extensions in London & Manchester \| Tatiana Karelina | /micro-bonds/ |
| tapes | Tape Hair Extensions in London & Manchester \| Tatiana Karelina | /tape-hair-extensions/ |
| wefts | Weft Hair Extensions in London & Manchester \| Tatiana Karelina | /wefts-hair-extensions/ |
| clip-ins | Clip In Hair Extensions in London & Manchester \| Tatiana Karelina | /clip-in-extensions/ |
| braids | Clip In Braids & Ponytails in London & Manchester \| Tatiana Karelina | /hair-extensions-braids-ponytails/ |
| prices | Hair Extension, Topper & Medical Wig Prices \| Tatiana Karelina | /prices/ |

Meta descriptions: copy them verbatim from each file's
`<meta name="description">` tag — they are written to length (130 to 166
characters) and contain the price anchors deliberately.

### Structured data (JSON-LD)
Every page carries JSON-LD in the head. Port it as-is (SEO plugin schema
feature, or a code block in the page):

- All pages: BreadcrumbList.
- All six extension pages + toppers + wigs: Product with AggregateOffer
  (real price ranges, GBP). If prices ever change, update page copy AND
  schema together.
- hair-loss, medical-wigs, prices and all six extension pages: FAQPage.
  The FAQ text in the schema matches the on-page FAQ text exactly and must
  stay in sync if either is ever edited.
- topper-giveaway: BreadcrumbList only, deliberately (a recurring giveaway is
  better without Product/Offer schema).

### Open Graph / Twitter tags
Deliberately NOT included in the static files — let Rank Math/Yoast generate
them from the meta title, description and featured image, as it does today.
One request: set og:locale to en_GB (the live site currently outputs en_US,
which is the wrong signal for a UK business).

### Other SEO notes
- One H1 per page, keyword-first. Do not add extra H1s in Elementor (its
  heading widgets default to H2 — keep it that way).
- Every image has a written alt attribute. Please carry the alt text across
  when rebuilding, they are keyword-bearing and descriptive.
- Internal links in the previews point at .html files so the preview can be
  browsed offline. In WordPress they must point at the live URLs (the mapping
  is the table above; "See Prices" buttons go to /prices/).
- No em dashes or hyphens are used anywhere in the copy. Please keep it that
  way when transcribing.

## Fonts
Headings: Butler, already self hosted on the live site at
/wp-content/uploads/2025/07/Butler.woff (see the @font-face in css/tk-main.css).
Playfair Display is only a preview fallback and is not needed on the domain.
Body: Poppins (300/400/600). Nav: Montserrat. Both via Google Fonts.

## Images — all in the images/ folder
- images/ba/ — before and after photos. SAME filenames as the existing
  WordPress media library uploads (2025/09). Reuse the media library versions,
  no re-upload needed.
- images/extensions/Divider-*.webp, images/toppers/Divider-*.webp,
  images/wigs/Divider-*.webp — these are the section photos from the live
  service pages (media library uploads 2025/10, same filenames). Reuse the
  media library versions. They are bundled here only because the preview
  cannot hotlink them.
- Other files in images/hair-loss/, images/toppers/, images/wigs/,
  images/extensions/, images/giveaway/ are new exports named by page, slot
  and content — upload these to the media library.
- Some heroes and before/after carousels hotlink the live domain directly in
  the preview; in WordPress simply select the same file from the media
  library (the filename in the src tells you which).

## Design rules to preserve (apply to every page)
- All white backgrounds, no grey section bands anywhere. The closing call to
  action section is white too (black button, black serif heading), and its
  paragraph is fully justified and exactly as wide as its heading.
- Hero: boxed within the page margin (not full bleed), translucent white band
  (#FFFFFF8A) sitting flush on the bottom edge of the photo, H1 centred in it.
- On mobile the first section after the hero shows its TEXT first, photo below
  (.split--intro). Later sections keep photo first when they stack.
- Trust strip: slim band of exactly four facts between thin rules. Same strip
  on desktop and mobile; on mobile it wraps to two columns, each block centred.
- Eyebrow labels: centred, uppercase, short centred 1px rule below.
- Body text: Poppins 300, justified.
- Buttons: black fill, 3px radius, uppercase.
- Before and after carousel: square thumbnails, 4 across on desktop, 3 on
  tablet, 1 on mobile, 20px gaps, centred BACK / NEXT below. Identical
  component on every page that has one. Before/after photos NEVER appear as
  static section photos, and hair-loss.html has no carousel on purpose.
- Every service page: intro photo and journey photo are the two photos from
  that page's own live version (signature approach photo and what to expect
  photo). No photo is reused across pages.
- FAQ: large serif question, thin divider rows, circled plus that becomes a
  minus when open. The brand question ("Why ... Tatiana Karelina ...") is
  always FIRST in every FAQ.
- Mobile first: everything stacks to a single column below 900px.

## Page-specific behaviour to rebuild

### prices.html
- One shared grid: every table's first column (Length) and last column line
  up across ALL charts (fixed table layout, first col 26%, last col 18%;
  2-column tables carry an empty spacer middle column).
- Categories are accordions and EXCLUSIVE: opening one closes the previous,
  and the opened section scrolls to the top under the sticky jump bar.
- The jump bar buttons must not push browser history (the preview uses
  history.replaceState) so the back button leaves the page rather than
  stepping back through charts. In Elementor, wire the accordion with the
  same behaviour (the JS at the bottom of prices.html is small and portable).
- All price content is plain HTML so Google indexes every price.
- Deposit £200, cancellation 24 hours, removal £80/hour, Exclusive = double
  drawn, maintenance at half price — the practical details section matches
  the live Before You Book copy.

### topper-giveaway.html
- The form is a styled static mock: rebuild with Elementor Forms (fields:
  name, email, nearest salon, story, three required consent checkboxes) and
  add reCAPTCHA. Entries go wherever Shawn specifies.
- Countdown JS targets the 25th of each month 23:59 (first target
  25 September 2026), recipient announced on the 30th. The JS is at the
  bottom of the file and is portable.
- Past recipients cards are placeholders — swap photos/names monthly.
- Navigation: the giveaway page does NOT join the main nav. If it must live
  somewhere, it is a child of Hair Loss.

### Carousels
The before/after carousel is plain scroll-snap CSS plus a few lines of JS
(BACK/NEXT scroll one viewport). An Elementor image carousel with 4/3/1
slides per view and 20px spacing reproduces it exactly — that is what the
live site already uses.

## Copy details worth knowing
- Wording is trichologist (not dermatologist) in the hair loss diagnosis FAQ.
- Wiglets no longer have their own section on the toppers page; passing
  mentions and the from £615 price remain on purpose for SEO.
- Timing is 8 to 12 weeks for custom pieces everywhere. Toppers £615 to
  £1,950, wigs £2,600 to £3,725, and the extension page price anchors match
  the price charts exactly.
- The company describes 18 years of experience — use 18 consistently (the
  live site mixes 18, almost 20, and two decades; we standardised on 18).
