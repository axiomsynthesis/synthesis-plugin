---
description: "Build a landing page from the kit: A finished landing page on a hidden preview copy of the store, every price proved against the cart, shown on a phone, a tablet and a computer"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Build a landing page from the kit

Channel: Website · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build a landing page from the kit" (id: landing-page-build, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds a paid-traffic landing page at the quality of pages that sell: the same buy box (packs with badges and crossed-out prices, a default pack, free gifts, a half-price add-on, Shop Pay, shipping and arrival lines, guarantee), the sticky phone bar, and the motion.
The person names the format and the product. Everything on the page comes from the brand's real store, claims and reviews.
It lands on an unpublished copy of the theme, then a check proves every price the page shows is the price the cart charges.

What to read: The store's products, prices and pictures, the brand's colours and approved claims, real reviews, and the format chosen
What to give me: A finished landing page on a hidden preview copy of the store, every price proved against the cart, shown on a phone, a tablet and a computer

Synthesis tools to use:
- `render_report`
- `brand_kit`
- `brand_facts`

Steps:
1. Ask which format (five_reasons, pack_picker, before_after, proof, problem_solve) and which product. Call `render_report` with `format=landing_page` and `page_format` set to it. It returns that format's playbook, section by section, and every setting. Follow the playbook.
2. Gather the real content. Products, packs, prices and pictures from the store's public product data (`/products/<handle>.js`). Colours and fonts from `brand_kit`; for an agency, the client's own kit (`client_kit`), because the page lives on the client's store. Claims only from `brand_facts`. Reviews only real, verified and dated, from the store's reviews or a file the person gives. Shipping rates as set in the store.
3. Call `render_report` with `format=landing_page` and `page` filled. If it returns problems, fix each one and call again. Read every warning.
4. In Claude Code, download the zip from `download_url`, pull the live theme, add the two theme files, and push the copy as a new unpublished theme:
```bash
shopify theme pull --store <store>.myshopify.com --live --path theme-copy
shopify theme push --store <store>.myshopify.com --unpublished --theme "Landing page preview" --path theme-copy
```
5. Open any page of the store with `?view=<view>&preview_theme_id=<new theme id>` added. That is the preview link.
6. In Claude Code, run the price check from the zip. Every line must say ok:
```bash
node lpk-check.mjs "<preview link>"
```
7. Open the preview link in a browser at phone (375 wide), tablet (768) and computer (1440) sizes. Check that the buy button shows in the first screen on a phone, nothing is wider than the screen, the sticky bar appears on scroll, and picking each pack changes the button.

Checks before answering:
- A price line that is not ok means the store has no discount charging that price. Never publish around it.
- Free gifts need a cost entered on the product in Shopify, or profit per visitor will read too high in any test.
- A store that answers "too many requests" was not checked. Wait and run the check again.
- Say what was not checked, such as shipping rates or the checkout page itself.

Output:
- The preview link first, with the format and product.
- The price check table, one line per pack and add-on.
- Phone, tablet and computer: one line each, with what was fixed.
- What was not checked, and the one step left to go live.
- Under 20 lines.

Never:
- Never push to the live theme or create the page without the person's explicit yes, in this conversation.
- Never invent a review, a rating count, a press logo or a claim.
- Never show a price the cart does not charge.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: landing-page-build". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
