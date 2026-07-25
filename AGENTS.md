<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

# Tatiana Karelina — Toppers & Wigs

SEO site for TK's topper/wig business. Same brand as tatianakarelina.co.uk, separate site.

## Hard rules
- **NO VAT relief content anywhere** — no page, FAQ, or mention (accounting decision; overrides the brief).
- **Scope**: toppers (classic/frontal/halo), wiglets, medical & custom human-hair wigs. No fashion / ready-to-wear wigs.
- **Domain is never hardcoded.** Read the origin from `SITE_URL` (via `@/lib/site` → `SITE_URL` / `absoluteUrl()`). Used by canonicals, sitemap, robots, JSON-LD, OG. Set in Vercel; changing the subdomain is a one-line switch. Do not touch `hairloss.tatianakarelina.co.uk`.
- **UK English throughout; numbers as numerals.**
- **Prices**: indicative ranges only, clearly marked TODO until Shawn supplies them.
- **The homepage hero is LOCKED AND FINAL — do not redesign, do not "polish", do not regenerate under any skill or audit pass.** The composition is:
  - **Banner**: deep 1.8:1 crop of `../Assets /Toppers/Photo 01-02-2023, 15 28 29.jpg` at **Y=900** (source is 3024×4032 portrait after EXIF-orientation; crop is 3024×1680, so source rows 900..2580 of 4032; ceiling max Y = 2352; outputs `public/images/hero/salon-banner-deep-{2400,1200}.webp`). Topper stands dominate the frame; Tatiana's head sits higher in the composition. **If ever changing Y**: kill and restart `next dev` after cutting new webps — a `.next/cache/images` wipe alone does NOT clear Next's cached image optimizations; only `rm -rf .next` + dev restart forces re-optimization.
  - **Wordmark**: `public/brand/tk-wordmark-white.png` (white variant), centred at `top-[10%] lg:top-[12%]`, sized `w-[62vw] max-w-[440px] sm:w-[46vw] sm:max-w-[520px] lg:w-[32vw] lg:max-w-[560px]`.
  - **Headline + CTAs**: two-line nowrap Playfair headline anchored to the base at `pb-6 lg:pb-8` (firmly in the lower third with a comfortable ~33px margin above the bottom edge). CTA pair beneath the headline, grouped.
  - **Gradients**: dark top-fade `rgba(0,0,0,0.55)→transparent` covering top 42%; dark bottom-fade `rgba(0,0,0,0.88)→transparent` covering bottom 62%.
  - **Container**: `h-[68vh] min-h-[440px] lg:h-[calc(100vh-7rem)]`.
  
  Do not touch the crop Y offset, the wordmark position/scale/colour, the headline padding, the gradient opacities, the container height, or the composition order. If any future pass reverts one of these values, restore them from this rule. `HomeHero` in `src/components/home.tsx` is a fixed surface.

## Spacing density — never default to airy (standing rule)

The default failure mode across passes has been over-spacing: too much
padding, too much gap, too many line-heights of breathing room. TK's
site is tighter than what a "modern editorial" reflex produces.
Correct posture:

1. **Read TK's rendered spacing before choosing our own.** For any
   shared surface with a TK equivalent (footer, contact, section
   headings, forms, dropdowns), fetch its CSS (`.elementor-element-*`
   rules in the SiteGround combined stylesheet) and match the exact
   padding / margin / gap / line-height / font-size values. Do not
   invent generous defaults.
2. **When exact TK values aren't available**, err on the tight side.
   TK body text is 12px, footer link gap is ~6px, section padding is
   ~40-72px block. Our tokens are tuned to that band, not to a
   Stripe-white-airy scale.
3. **Recorded reference values** (from the TK Elementor CSS,
   2026-07-17 scrape):
   - Footer outer container padding: 50px top / 30px bottom desktop;
     40px top / 30px bottom mobile.
   - Footer body text: 12px Montserrat.
   - Footer `h4` heading: 1.25em (=15px) at font-weight 600.
   - Content section padding sits ~40-72px block (matches our
     `--section-pad-y` clamp).

## Desktop layout standard (density and rhythm)

Homepage and all pages, applied from the homepage layout pass onward. The
current build has too much white on desktop; this is the fix.

1. **Max content width 1200–1280px.** Use `max-w-7xl` (1280px) for content
   containers, not `max-w-6xl` (1152px). No narrow centre column with big
   empty side margins.
2. **Section vertical padding: generous but controlled.** Aim ~72–96px
   desktop, ~48–64px mobile. Tighten the current cavernous gaps.
3. **Full-bleed (edge to edge)** for: hero, trust strip, before-and-afters,
   and any section using a background band (ivory About, black
   ConsultationCTA). **Contained width** (max-w-7xl) for text-and-photo
   sections.
4. **Paired photos are large; copy fills the matched photo-height box.**
   Thin copy next to a tall photo is the main white-space generator, so
   every paired text box carries substantial copy that fills its box. Copy
   is written to fit the box; the box is not stretched to fit the copy.
5. **Every section carries real, substantial visible content.** This is a
   zero-authority SEO site — visible content depth is the strategy.
   Prefer fuller sections over sparse ones.
6. **Elegant, not busy.** The richness comes from content and imagery.
   The premium feel comes from Playfair Display + Inter typography,
   photography and colour restraint — not from empty space.

Rule of thumb: if a desktop viewport shows a paired section where the
photo is >30% taller than the text box beside it, the text box is
underwritten. Rewrite until the two match.

## Design system (replicate the main site)
- **Replicate tatianakarelina.co.uk's design language exactly.** Fonts are the only permitted difference (Playfair Display + Inter here; the main site's stack is different). Everything else — spacing rhythm, typographic scale, section patterns, colour tokens, hero pattern, CTA styles, nav, footer — matches the main site 1:1.
- **White dominant.** The base canvas is `paper` (near-white). Ivory is used **once per page at most** as a single accent band (typically the About band).
- **No bordered cards.** No panels with borders, no drop shadows on content blocks, no boxed callouts. Editorial layout — sections separated by whitespace and typography, never by borders.
- **Justification standard.** All body copy is fully justified. Every paragraph, every breakpoint, every page: `text-align: justify`, inter-word spacing only, `hyphens: none`. Never hyphenate. This is a universal rule — apply it to the base prose class in `globals.css` so it holds everywhere by default, and never override.
- **Comparison artefacts.** Any before/after or design-review screenshot must show the live main site next to ours at the same scale (same viewport width, same crop). Never present our page alone as "matches the reference".

## Stack & conventions
- Next.js 16 App Router, TypeScript, Tailwind v4 (CSS-first `@theme` in `src/app/globals.css`), static generation, Vercel (scope `shawnfrazer-wq`).
- Type: Playfair Display (serif headings, `font-serif`) + Inter (body, `font-sans`), self-hosted via `next/font` in `layout.tsx`.
- Brand colours: exact from the main site, defined as tokens in `globals.css` (`ink`, `body`, `paper`, `ivory`, `navy`, `taupe`, `slate`, `line`…). Monochrome editorial — black/white + ivory + neutrals.
- **Money pages** = hand-built routes under `src/app`. **Blog** = MDX in `content/blog` (frontmatter: title, slug, description, cluster, hero, faq) rendered via `next-mdx-remote/rsc` at `/blog/[slug]`; pipeline in `@/lib/blog`.
- Shared nav/footer = single components (never duplicated per page) — built in the components stage.
- SEO helpers: `@/lib/seo` (`buildMetadata`, `rootMetadata`), `@/lib/schema` (JSON-LD builders), `@/components/JsonLd`. Route registry: `@/lib/routes` (drives sitemap + nav).
- Images: source assets in `../Assets ` (sibling folder, note trailing space, capital A). Convert to WebP, serve via `next/image`. Videos hosted externally (Mux/Cloudflare) behind one host-agnostic `VideoEmbed`; keep raw video out of the repo.
- Galleries driven by a TS manifest so swaps are one-line.
- Lead capture: Formspree (endpoint TBD), one shared enquiry-form component.

## Working practice
- **End every working session by writing to `docs/progress.md`.** Two sections: `## Current state` (what is done and signed off, what is in progress and where it is up to) and `## Next steps` (the ordered list of what happens when the next session opens). Overwrite the file each time — it is a live status doc, not a log. This survives session loss.
- **Commit at every stage completion.** Clear message. No `git add -A` sweeps.

## Build stages (check in with Shawn at the end of each)
scaffold → shared components → money pages → blog. Brief lives at `docs/content-map.md`.
