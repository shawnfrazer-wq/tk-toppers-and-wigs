# Impeccable audit — Tatiana Karelina Toppers & Wigs

**Mode**: audit and report only. No code changes. Shawn picks which findings to apply, we do them in approved batches.

**Loaded references**: `.agents/skills/impeccable/SKILL.md` (v3.9.1) + `reference/brand.md` (design IS the product). Ran `context.mjs` — `NO_PRODUCT_MD` (proceeded using code as context per SKILL rule; not blocking).

**Out of scope per AGENTS.md and this brief** (findings against these are noted but not proposed for change):
- Hero (`HomeHero` in `src/components/home.tsx`) — banner, wordmark, 2-line headline, dark gradient treatment, fixed container height
- Nav (`src/components/Nav.tsx`)
- Price tables (`src/app/prices/page.tsx` — the `TopperPriceTable` and wig table markup, not the surrounding sections)
- FAQ block (`src/components/Faq.tsx`)
- Hero headline text
- Content rules (UK English, justify, hyphens: none, no VAT, ivory once, no bordered cards)

**Severities** — **H** high (visibly wrong, ships bad), **M** medium (real polish debt, no urgency), **L** low (nice-to-have).

---

## Executive summary

Top 10 findings across the site, ranked by ship-blocker weight.

| # | Sev | Page(s) | Finding | Proposed fix |
|---|---|---|---|---|
| 1 | **H** | All money pages | `Hero` right-column image is a small tall 4:5 panel next to the text — reads as a shrunken thumbnail, not a hero. Undersells the craft on 8 pages. | Full-bleed photograph hero at ~55vh (below nav), text overlaid or beneath. Keep the two-column pattern only where text is the point (Prices, Video consultation). |
| 2 | **H** | Home | `ReviewsBand` renders "TODO CONFIRM" placeholders as real reviews with 5-star rows. Anyone loading the page now sees three review slots that say TODO. | Either replace with real reviews (needs Shawn) OR hide the whole section behind an env flag until data arrives. Never ship TODOs to a real user. |
| 3 | **H** | Home | `Carousel` (offer sections) uses `.85` white transparency on the arrow buttons — arrow glyph `←` in ink is fine on that, but there's no focus-visible ring anywhere on the button. Keyboard users can't tell which arrow they're on. | Add `focus-visible:ring-2 focus-visible:ring-ink` on Carousel and BeforeAftersCarousel controls. |
| 4 | **H** | Nav (flag, locked) | Desktop dropdown opens on `group-hover` only — no `focus-within` variant. Keyboard tab through nav skips dropdown children entirely. | Locked per AGENTS.md — flagging for the record. If ever unlocked, add `group-focus-within:visible group-focus-within:opacity-100`. |
| 5 | **M** | Home | `HairLossSection` and `PointOfDifference` both use the same 2-col text+image at the same rhythm — the page has two visually identical rows back-to-back. Third occurrence in `OfferSection` compounds it. | Break rhythm: give one of them a full-bleed image treatment, or invert dominance so text is the wider column, or swap one image position side. |
| 6 | **M** | Toppers pillar | The 4-up "Three topper types — only at TK" row is 4 columns of nearly identical text density — reads as a spec sheet, not editorial. | Give one card more prose or an image, or drop to 3 columns and pair each with a small representative thumbnail. |
| 7 | **M** | Journey, Video consultation | Numbered step lists (01-09 and 01-06) use serif numerals + border-t + prose in one repeated pattern — 9 identical rows on Journey. | Vary rhythm: alternating image-and-text rows, or step-into-image reveals, or a horizontal timeline for the first 3 steps and prose for the deeper ones. |
| 8 | **M** | Contact | Enquiry form now has no visual containment (border removed correctly), but the salon addresses on the left and the form fields on the right are floating on the same page with no anchoring rhythm. | Anchor with typography scale (form heading > address city headings) and give the two columns different top margins so they don't align at the same line. |
| 9 | **M** | Blog | Blog index is a plain `<ul>` of 3 title/description pairs — no imagery, no dates, no cluster labels. Reads like a stub. | Add a hero image per post (`hero` frontmatter exists) + published date + cluster tag; consider a magazine 2-col layout. |
| 10 | **L** | Site-wide | Zero motion anywhere below the hero. Skill's brand register says "One well-orchestrated page-load beats scattered micro-interactions"; we currently ship neither. | Add one deliberate motion moment on the homepage (recommend a subtle stagger on the OfferSection carousel image swap, or a fade-in on the Before/Afters row on scroll — respect `prefers-reduced-motion`). |

---

## Global findings (cross-page)

### Spacing and rhythm — **M**
- `Section` component uses `py-16 sm:py-20` at every breakpoint. That's 64px → 80px. On desktop above 1280 the page reads flat because breathing room stops scaling. **Fix**: fluid clamp `paddingBlock: clamp(3.5rem, 5vw + 2rem, 6.5rem)`.
- `mx-auto max-w-6xl` (72rem = 1152px) is the container everywhere. Every page has the same width feel. **Fix**: allow the hero-adjacent editorial sections to breathe wider (max-w-7xl) and prose blocks tighter (max-w-2xl), varying by content.
- `ContentSection` inner `max-w-3xl` (48rem) with body 16px → ~96 characters per line at the widest. Brand register cap is 65–75ch. **Fix**: reduce to `max-w-2xl` or `max-w-prose` on `ContentSection`, and also on the numbered step list bodies (Journey, Video consultation).

### Typography — **M**
- Headings sit at `line-height: 1.12` and `letter-spacing: -0.01em`. Tight display letter-spacing is fine; line-height 1.12 on a two-line h2 can look cramped at mobile. **Fix**: `line-height: 1.15` on h2/h3, keep 1.1 on the display h1.
- No `text-wrap: balance` on h1–h3 or `text-wrap: pretty` on p. Ragged single-word last lines show up on Journey, About, Hair loss. **Fix**: add both to the base layer in `globals.css`.
- Base body font-size is browser default (16px). At 16px justified with 96ch line length, prose reads dense. **Fix**: bump body to 17px on ≥768px viewports OR combine with the max-w-2xl fix above.
- The `Eyebrow` component (small uppercase tracked label) appears above nearly every section on nearly every page. Impeccable's brand register calls this the saturated AI grammar — "if you're not using it as a deliberate named brand system, choose a different cadence." **The main site uses eyebrows too, so identity-preservation wins per the skill's own rule.** Flagging without proposing a change — noting only that our eyebrow density is at the ceiling.

### Colour and contrast — **M**
- `--color-slate: #686e77` on `--color-paper: #ffffff` is ~5.4:1 — passes AA body (4.5:1). But `text-slate` is also used inside `bg-ivory` (#f7f5e7) — the actual contrast on ivory is ~5.2:1, still fine.
- `text-slate` on `bg-line-2/50` (#f5f5f580) — where GallerySection uses it — is closer to ~4.4:1, right at the AA edge. **Fix**: use `text-body` (#333) for the empty-state paragraph instead of `text-slate`.
- `text-slate/60` variants (in Footer copyright band, ConsultationCTA subtitle) drop below 3:1 on their backgrounds in places. **Fix**: audit every `/60` and `/70` and either raise to `/80` or switch to the paired ink.

### Accessibility — **H / M**
- **Focus states**: no `focus-visible:` styles anywhere on interactive elements. Buttons, links, form fields all default to browser outline (varies by OS). Keyboard-only users can't reliably track focus on primary CTAs, nav items, filter buttons or dropdown items. **[H] Fix**: add a single `focus-visible:ring-2 focus-visible:ring-ink focus-visible:ring-offset-2` treatment to `.btn`, all `<Link>` that render as CTAs, all `<button>`s (Gallery filters, Carousel arrows, mobile hamburger, FAQ summaries), and form inputs.
- **Nav dropdown keyboard** — covered above under Executive summary #4 (locked).
- **Alt text**: gallery `alt` strings are descriptive and good ("20 inch mono based topper", etc.). No decorative images without alt — clean. No finding.
- **Colour-only signalling**: none found. Buttons use both colour and structure.
- **Reduced motion**: nothing to enforce today (no motion), but the future motion pass needs `@media (prefers-reduced-motion: reduce)` alternatives from day one.

### Semantic HTML — **L**
- Every page uses `<main>` (good), but landmarks below vary. `Nav` is a `<header>`, `Footer` is a `<footer>` — good. Sections use `<section>` — good. Some inner divs could become `<article>` on the blog index and Before & Afters figures, but not required.
- Home page has multiple `<h2>` per section (correct) but the `Eyebrow` `<p>` reads before the `<h2>` — screen-reader users hear the label before the heading, which is fine for context but breaks the "heading first" scanning pattern if they use heading navigation.

### Imagery density — **M**
- Money pages have exactly one image (the right-column Hero thumbnail) plus the GallerySection carousel + a "coming soon" VideoSlot. Between those, hundreds of words of prose with no visual anchor. Brand register: image-led briefs must ship imagery.
- Hair loss, Journey, Video consultation, About, Contact, London, Manchester, Prices, Before-and-afters index — either no hero image at all or one thumb. **Fix**: allow selected sections to break to full-bleed imagery. Give About a portrait of Tatiana. Give Journey a process image mid-page. Give Hair loss an editorial visual for the causes band. Give the location pages a photo of each salon.

---

## Per-page findings

### `/` — Home

| Sev | Finding | One-line fix |
|---|---|---|
| **H** | Reviews section ships TODO placeholders visibly. | Hide the section behind env flag or replace with real reviews. |
| **M** | Two consecutive text+image rows (HairLossSection then OfferSection wig row then PointOfDifference) share the same rhythm — page reads as a stack of identical rows. | Break the middle row into a full-bleed treatment or invert dominance. |
| **M** | `AboutBand` and `EditorialSeo` are both centred paragraphs at `max-w-3xl` — same width and centre — ivory band and paper section have the same silhouette. | Left-align `EditorialSeo` (it's editorial, not manifesto), reserve centred for the About band. |
| **M** | `BeforeAftersCarousel` "See more" black CTA sits far-right of the back/next controls; on mobile the button wraps under the arrows breaking the row. | Move "See more" beneath the carousel, full-width on mobile, right-aligned above the fold on desktop. |
| **L** | The homepage has 8 major sections stacked vertically without any anchor moment. No motion, no full-bleed break, no changed layout logic. | Add one full-bleed image band mid-page (a colour-blending studio close-up would suit). |
| **L** | Star rows in ReviewsBand use `★★★★★` as text characters — differs in width across fonts. | Use an SVG star icon at fixed width. Only if the reviews section itself survives (see H finding). |

### `/toppers` — Toppers pillar

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | 4-up "Three topper types — only at TK" grid is text-only with an arrow. Undersells the pieces. | Add a small representative image to each of the four cards (classic / frontal / halo / wiglet). |
| **M** | Hero image thumb (right column of `Hero`) is one topper on a stand — same visual language repeats in the SignatureApproach and the topper-types grid without variation. | Use a wider studio hero (or none) so the topper thumbs downstream carry the visual specificity. |
| **L** | "Explore →" glyph is a plain arrow — decorative, no motion. | Optional: animate the arrow shift on hover (transform: translateX). |

### `/toppers/classic-topper`, `/toppers/frontal-topper`, `/toppers/halo-topper`

Same structure, same findings for each:

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | Same `Hero` two-col pattern with a small right-column image. Underweighting the page's product. | Consider a small-photo-strip band (3 images) below the ContentSection for visual weight. |
| **M** | `GallerySection` is `bg="line-2"` — grey tint separates it from paper, but the tint is very close to paper and reads as a rendering artefact on some screens. | Either raise the tint (line-2 → line) or drop the bg entirely and separate with whitespace. |
| **L** | No structural difference between the three topper pages other than copy. Visitor bouncing between them sees the same 6 sections in the same order. | Vary one section per page: classic gets a colour-blending panel, frontal gets a hairline detail image, halo gets a comfort/wearability angle. |

### `/wiglets`

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | Identical structure to the topper detail pages — no reason a visitor lands here as their own page vs. a section on the classic topper page. Wiglets are "a compact topper", per the copy itself. | Consider whether Wiglets needs to remain a full money page or become a section under `/toppers`. If it stays, differentiate the visual treatment. |
| **L** | Copy says "essentially a compact topper" — same-day-fittings and pricing bundling implied but not linked to Prices page. | Add an inline link to the wiglets price line in `/prices`. |

### `/wigs/medical-wigs`

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | Sensitive-audience page — the tone is right in copy, but the visual treatment is identical to the topper pages (same Hero pattern, same SignatureApproach ivory band, same carousel). The register the page speaks in is different from the register it looks in. | Give this page a quieter visual treatment: no ivory accent band, more whitespace, single image with respectful alt text and caption. |
| **M** | Cross-link at the bottom to `custom-human-hair-wigs` is a paragraph at `text-sm text-slate` — hard to see. | Promote the cross-link to a proper CTA row or an in-content link at higher weight. |

### `/wigs/custom-human-hair-wigs`

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | Mirror image of medical-wigs page. Same finding as above regarding differentiation. | Give this page a lifestyle / occasion visual treatment (colour, occasion, freedom) to contrast the clinical restraint of medical-wigs. |
| **L** | Cross-link to medical-wigs at bottom has same visibility issue as medical-wigs → custom link. | Same fix pair. |

### `/hair-loss`

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | Causes grid (6 items in a 3×2 ivory band) with hairline separators — reads as a spec table. Sensitive topic deserves a warmer treatment. | Convert to a 6-row prose list with a lead paragraph per cause, no grid. Or drop to 3 causes with room to explain each. |
| **M** | Two `ContentSection` blocks (Causes intro + "The immediate solution") sandwich the grid — the page has three prose rhythms in a row. | Consolidate into a single ContentSection with a lead + inline cause list. |
| **L** | Page ends with FAQ then ConsultationCTA — the reader is emotionally primed by the causes reading, and the closer is a black band asking them to book. Consider whether an editorial "you are not alone" moment sits between. | Add a soft transitional section (client testimonial, quote from Tatiana, or a founding-story link) before the CTA. |

### `/journey`

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | 9 numbered steps as a single vertical list — reads as a checklist, not a journey. | Break into visual arcs: three steps as an image-and-text alternation, six steps as compact numbered rows, or add a horizontal timeline scrubber for desktop. |
| **M** | "In salon" vs "By video" panels (post-border-removal) now float side-by-side with hairline separators — but visually indistinguishable from the SignatureApproach 3-column pattern used elsewhere. | Add an icon or a small visual (salon door photo / laptop shot) to each panel to differentiate them from generic pillar rows. |
| **L** | Step 07 "50% deposit" and step 08 "8 to 12 weeks of craftsmanship" are the crux of the value proposition but visually identical to the other steps. | Emphasise one — e.g. pull "8 to 12 weeks" out as a display-scale statement between step 07 and step 09. |

### `/prices` (price tables locked; sections around them in scope)

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | Three tables (topper 1, topper 2, wig) stacked in an ivory band followed by a paper band followed by a line-2 band. Same rhythm three times. | Consolidate visually: one long section with tables separated by whitespace not backgrounds. |
| **M** | "Wiglets" callout at bottom of Toppers section is a bordered-left blockquote (`border-l-2 border-taupe`) — the ONLY border-left in the codebase. Stands out inconsistently. | Convert to an inline paragraph inside the Toppers intro, or a small hairline-topped panel matching the SignatureApproach pattern. |
| **L** | Prices transcription date ("11 July 2026") sits at bottom in slate — small print in the right place, but pointing at a specific date that will age. | Make it a variable in `SITE` config so it's easy to update; or express as "current at time of publication" without a date. |

### `/before-and-afters`

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | Page has no ConsultationCTA — visitor scrolls through beautiful transformations and hits the footer with no next-step invitation. | Add a ConsultationCTA at the bottom. |
| **M** | Filter buttons are outlined boxes with borders — the ONLY borders on any interactive control in the site (all CTAs use bg-black, all links have no chrome). | Restyle filters as text-only with an active underline; or accept the borders as the deliberate exception and note it in the design system. |
| **L** | Gallery grid images hover with `scale-105` — the only hover-transform in the site. Micro-interaction. Feels good, keep. | No fix — noting for consistency. |

### `/about`

| Sev | Finding | One-line fix |
|---|---|---|
| **H** | No image of Tatiana anywhere on the About page. On a personal-brand page this is a miss — visitor comes here specifically to know who she is. | Add a portrait of Tatiana in the top section (existing photograph from the Kensington salon or a portrait if one exists). |
| **M** | Two `ContentSection` prose blocks + one ivory band = three centred columns of text stacked. No visual anchor. | Give one block a photograph beside it (2-col layout) to break the vertical rhythm. |

### `/contact`

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | Salon addresses (left column) and enquiry form (right column) don't share a visual heading rhythm — the form's `<h2>` is bigger than the "London" salon `<h2>`, but they're semantically peers. | Bring both column headings to the same scale; or promote the intro line to h1 and demote all four to h2. |
| **M** | Salon cards are two blocks of address text with no map, no phone, no opening hours, no photo. | Add per-salon phone + opening hours (already in `SALONS` config?) + photo (or Google Maps embed link). |
| **L** | The form's success state is a centred "Thank you" — no confirmation number, no next-step context ("we reply within 48 hours"). | Add a next-step line under the success message. |

### `/london` and `/manchester`

Same LocationPage component; same findings:

| Sev | Finding | One-line fix |
|---|---|---|
| **H** | No photo of the salon exterior/interior. Location page's primary job is "you can find this real place" — text alone doesn't do that. | Add a full-bleed exterior photo (or interior with the branding visible) as a page hero, or an image band mid-page. |
| **M** | "What we make" ivory band lists two things (toppers + wigs) as border-t hairline columns — same pattern as SignatureApproach on money pages. Repetition. | Vary the visual: e.g. a 3-image band (topper on stand / wig on stand / colour-blending) with captions. |
| **M** | No map, no directions, no transport info. | Add a Google Maps iframe (or static image with a link) below the address. |
| **M** | ConsultationCTA at bottom uses default copy — should be salon-scoped ("book at our London salon"). | The prop is passed already — verify it renders. Otherwise, done. |

### `/video-consultation`

| Sev | Finding | One-line fix |
|---|---|---|
| **M** | 6 numbered steps in an ivory band — identical rhythm to the Journey page's 9 steps. Two pages, same visual grammar. | Differentiate: e.g. video-consultation gets image-and-text pair per step; Journey stays numbered list. |
| **M** | Copy is strong but no visual proof — no screenshot of a video call, no photo of a wig arriving in a client's home. | Add one photo of a client fitting or a courier / packaging shot to prove the remote route is real. |
| **L** | No FAQ specific to video ordering above the remoteOrdering FAQ items — but the whole page IS the answer to "how does this work". Fine. | No fix. |

### `/blog`

| Sev | Finding | One-line fix |
|---|---|---|
| **H** | Only 3 posts. Sparse index reads as an under-development section, not a live journal. | Either commission more posts (out of my scope) or hide `/blog` from nav and sitemap until 8+ posts. |
| **M** | Index is title + description only — no hero image, no date, no cluster. The MDX frontmatter has `hero` and `cluster` fields already. | Add a hero thumbnail per post, publish date, and cluster tag; consider a 2-column magazine layout. |
| **L** | No pagination, no cluster filter, no read time estimate. Deferred until there are more posts. | Deferred. |

---

## Motion opportunities

Zero motion below the hero currently. Brand register: "One well-orchestrated page-load beats scattered micro-interactions." Recommend picking **one** of these and shipping it well rather than scattering:

- **Homepage first-load choreography** — TATIANA / KARELINA wordmark fade+slight-scale from ~0.98 → 1.0, then headline lines stagger 60ms apart, then CTAs. 400ms total. Respect `prefers-reduced-motion` with an instant fade.
- **BeforeAftersCarousel scroll reveal** — each figure fades + rises 12px into place as it enters the viewport (IntersectionObserver, `once: true`). Same reduced-motion opt-out.
- **OfferSection carousel image swap** — currently instant `src` change on arrow click; add 300ms opacity crossfade.

Pick one. Two is too many for this brand.

---

## Accessibility summary

| # | Sev | Item | Fix |
|---|---|---|---|
| A1 | **H** | No `focus-visible:` styles anywhere on interactive elements | Add site-wide `focus-visible:ring-2 focus-visible:ring-ink focus-visible:ring-offset-2` on buttons, CTAs, form fields, gallery filters, carousel arrows, FAQ summaries |
| A2 | **H** | Nav dropdown keyboard-inaccessible (locked; flagging) | If unlocked: add `group-focus-within:visible group-focus-within:opacity-100` |
| A3 | **M** | `text-slate` on `bg-line-2/50` at ~4.4:1 (right on AA edge) | Use `text-body` on that background |
| A4 | **M** | `/60` and `/70` opacity slate text drops below 3:1 in places | Raise to `/80` or paired ink |
| A5 | **L** | FAQ summaries have no explicit `aria-expanded` — native `<details>` handles it, but SR announcement could be clearer | Leave; native details is fine |
| A6 | **L** | No skip-to-content link | Add `<a href="#main">Skip to content</a>` visually-hidden until focused; useful for keyboard users on every page |

---

## Consistency summary

Patterns that repeat and where they're consistent vs. drift:

| Pattern | Occurrences | Consistency |
|---|---|---|
| `Hero` two-col text+image | 13 money pages | Consistent, but the pattern itself is weak (finding #1) |
| `SignatureApproach` ivory band | Every topper + wig page | Consistent — good |
| Numbered step list (border-t + serif numeral) | Journey (9), Video consultation (6), also implicit in some grids | Consistent — good |
| `Eyebrow` above every section | ~40+ occurrences | Consistent but at saturation ceiling (see Global typography) |
| `Section` `py-16 sm:py-20` | Every content section | Consistent but static (see Global spacing) |
| `ConsultationCTA` black band | Every money page except `/before-and-afters` | One missing (see B&A findings) |
| `text-slate` for muted body | Various | Mostly consistent, one contrast edge case (see A3) |

---

## Out of scope (per locked list) — findings noted but not for action

- Hero composition (H, M, L findings do not exist here — Shawn has explicitly locked)
- Nav dropdown keyboard access (A2 above — noted for record)
- Price tables' internal markup — tables themselves are fine; my findings are all about the surrounding sections
- FAQ block — component is well-built (proper TODO CONFIRM guarding, semantic details, good hierarchy)
- Hero headline text — locked
- Content rules — I proposed nothing that breaks them (justify preserved, no VAT introduced, no bordered cards, ivory-once respected)

---

## Recommended batches

If you want to sequence the applies:

**Batch A — accessibility (H)**: focus-visible everywhere (A1), Reviews TODO handling (Exec #2), Carousel focus states (Exec #3). Small, all high-severity, no visual risk.

**Batch B — money page hero + About + Locations imagery (H)**: About portrait, London/Manchester salon photos, and a decision on the money-page `Hero` treatment. Needs source images from Shawn.

**Batch C — spacing/rhythm/typography (M)**: fluid section padding, prose line-length cap, `text-wrap` on headings/paragraphs, line-height nudge. Global, low visual risk, big legibility win.

**Batch D — page-specific rhythm breaks (M)**: Home middle-row differentiation, Toppers pillar cards with thumbs, Journey timeline arc, Hair loss causes as prose, Contact salon cards enriched, Blog index redesign.

**Batch E — motion (L, optional)**: pick ONE choreography moment and ship it.

Batches A + C are the cheapest high-value combination if you want a fast win.
