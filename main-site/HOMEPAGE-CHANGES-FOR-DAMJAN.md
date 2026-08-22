# Homepage — Changes for Damjan

## The approach
Do NOT rebuild the homepage. Keep the existing live homepage exactly as it is,
section for section, and make only the changes below in Elementor. The preview
at https://shawnfrazer-wq.github.io/tk-toppers-and-wigs/main/homepage.html
shows these changes applied in the new design language and is the visual
reference, but the live page's own structure and carousels stay.

## 1. Typography, SITE WIDE (this is what makes everything match)
- Headings: switch from Butler to Playfair Display, weight 400, via Google
  Fonts. This applies across the whole site, including pages not being
  rebuilt yet. Butler is retired.
- Body: Poppins 300, justified text.
- Nav and small labels: Montserrat.
- Sizes to match the new pages: H2 40px desktop / 30px mobile, body 14px with
  25px line height (see css/tk-main.css in the page packages for the tokens).

## 2. Hero
- H1 becomes: "London's Leading Russian Hair Extensions Salon"
- DELETE the floating tagline above the H1 ("Russian Hair Extensions For
  Today's Empowered Women"). Nothing floats over the hero except the H1.
- Keep the existing hero photo and the Book Appointment button.

## 3. Add the trust strip directly under the hero
The slim band of exactly four facts between thin rules (same component as on
every redesigned page, see the preview):
- 20 years / Of Russian hair mastery
- Two salons / London, Manchester and video calls
- Six natural textures / Including naturally curly hair
- 100% Russian hair / Colour matched without dye

## 4. One number everywhere: 20 years
Replace on the homepage (and anywhere else it appears):
- About Us: "as it was 18 years ago" -> "as it was 20 years ago"
- Point of Difference: "Over the past 18 years" -> "Over the past 20 years"
- FAQ: "over 18 years" -> "over 20 years"; "almost 20 years" -> "20 years"
- Ready to Transform: "almost two decades" -> "20 years"

## 5. Typo fixes in live copy
- Weft card: "standby strand" -> "strand by strand"
- Medical wigs card: "Our, medical wigs" -> "Our medical wigs"

## 6. About Us section
- Add a photo beside the About text: media library file
  Hero-Mobile-355x768-7-1.webp (2025/10, the auburn haired model).
- Promote the empowerment line to the section heading: "Through Hair We
  Empower Women. And When Women Empower Women, Great Things Happen."
- "Step Into the World of Tatiana Karelina" becomes the bold lead of the
  first paragraph. Keep the rest of the About copy as is (with 20 years).
- Add at the end: "Every month we also fit one woman experiencing hair loss
  with a custom Russian hair topper, free of charge." with an outline button
  "Discover the Monthly Topper Giveaway" linking to /topper-giveaway/.

## 7. Point of Difference section
- The section's image (Our-Point-of-Difference.png) is broken on the live
  server and does not render. Replace it with the media library file
  tatiana-karelina-london-salon-russian-hair.webp (2026/04, Tatiana holding
  two Russian hair ponytails). Keep the copy (with 20 years).

## 8. Hair Loss section
- Keep the four cards exactly as they are.
- ADD beneath the carousel a centred serif pull quote:
  "After losing my hair during chemotherapy, I turned to the salon for a wig
  that would look just like my natural, pre chemo hair. The wig they created
  for me is incredible. They sourced hair that perfectly matches my natural
  colour, length and texture." — Kathryn Forde, Google review
- Add a black button under it: "Discover Our Hair Loss Solutions"
  linking to /hair-loss/.

## 9. Client Reviews
- Keep the Google review slider, but PIN these three reviews first, in this
  order (one confidence story, one hair loss story, one wedding story):
  1. Daisy Slavkova  2. Veronica Heague  3. Ruth Morgan
- Keep the "EXCELLENT ... 157 reviews" widget above the slider.

## 10. FAQ
- DELETE the second question ("Why choose Tatiana Karelina for hair
  extensions in London?") — it duplicates the first. All other questions stay.
- The brand question ("Why is Tatiana Karelina the best for hair extensions
  in the UK?") stays FIRST.
- Update the numbers per item 4.
- Add FAQPage JSON-LD matching the on page FAQ exactly. A ready made block
  covering the kept questions is in the head of homepage.html in the preview
  package; regenerate it if any answer is edited.

## 11. Meta (Rank Math)
- Title: Russian Hair Extensions London | Tatiana Karelina
- Description: Genuine Russian hair extensions, toppers and medical wigs in
  London and Manchester. Micro rings, bonds, tapes, clip ins and wefts,
  colour matched without dye.
- Canonical stays https://tatianakarelina.co.uk/
- Set og:locale to en_GB (currently en_US).
- Add the Organization JSON-LD from the preview homepage.html head (it nests
  both salons with addresses and phone numbers).

## What does NOT change
The hero photo, the As Featured In logos, the six service cards and their
carousel, the before and after carousel and its See More link, the hair loss
cards, the Instagram block, the footer, and every URL.
