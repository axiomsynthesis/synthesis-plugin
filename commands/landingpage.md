---
description: "Build a landing page from the kit: A landing page on a hidden copy of the store, default pack picked for profit, every price proved against the cart, and a test plan"
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
Builds a paid-traffic landing page with packs, gifts, an add-on, a guarantee and a sticky phone bar.
It picks the format and default pack from the brand's numbers, builds on a hidden theme copy, proves every price against the cart, and plans the test.

What to read: Landing page results, the store's products, prices and pictures, pack costs, the brand's colours and approved claims, real reviews
What to give me: A landing page on a hidden copy of the store, default pack picked for profit, every price proved against the cart, and a test plan

Synthesis tools to use:
- `cost_rules for=landing-page-build`
- `ga4_metric metric=landing_pages days=28`
- `meta_metric metric=ad_destinations days=28`
- `render_report`
- `brand_kit`
- `brand_facts`
- `first_order_contribution_margin`
- `breakeven_roas`
- `web_fetch`

Steps:
1. Call `ga4_metric` with `metric=landing_pages` and `days=28`, and `meta_metric` with `metric=ad_destinations` and `days=28`. Find the best current page by sales per visitor, and the ads that will feed the new one. Propose a format (five_reasons, pack_picker, before_after, proof, problem_solve): cold traffic gets a problem or proof page, warm traffic a pack page. Confirm with the person. Call `render_report` with `format=landing_page` and `page_format` set to it, and follow its playbook.
2. Call `brand_kit`. A colour or font in state house is our default, not the brand's. Read the store's homepage with `web_fetch` or ask the person for the brand's colours. Show both before building.
3. Offer maths. For each pack, gift and add-on, get the product cost. Call `first_order_contribution_margin` and `breakeven_roas` with the pack price and cost passed by hand. Add gift, shipping and payment costs. Show profit per order and the most to pay per sale. Default to the pack with the highest profit times expected take rate.
4. Prices and pictures from the store's product data. Claims only from `brand_facts`. Reviews only real and dated.
5. Call `render_report` with `format=landing_page` and `page` filled, with the store's address. Fix every problem and call again.
6. In Claude Code, download the zip from `download_url`, unzip it, and run the preview there. It checks every price and four screen sizes:
```bash
node lpk.mjs preview --store <store>.myshopify.com
```
7. Stop at the first FAIL, fix it, run again. Show the preview link and `lpk-shots/`.
8. Only after an explicit yes in this conversation, go live (it backs up first), create the page with template `lpk-<name>`, and check it:
```bash
node lpk.mjs live --store <store>.myshopify.com --page <any page handle> --confirm
node lpk.mjs check "<new page link>"
```
9. Test plan: control = the page from step 1. Metric: profit per visitor. Visitors a side = 16 x p x (1 - p) divided by d squared, p the current conversion rate, d the lift to detect. At least 2 full weeks. Give the read date.

Checks before answering:
- A price line not ok means no discount charges that price. Never publish around it.
- A gift or pack with no cost fails step 3. Ask for it. A pack that loses money needs the person to call it a loss leader.
- Every claim must match a `brand_facts` entry. Cut a health claim with no proof and a review with no date.
- A crossed-out price must be a real earlier price. The cart check cannot prove this. Ask, and say so.
- This cannot read the test out yet. Say who pulls the results on the read date.
- Say what was not checked: shipping, tax, checkout.

Output:
- First line: format, product, default pack, and the page it must beat.
- The preview link. Offer table: pack, price, profit per order, most to pay per sale.
- Price check, one line per pack. The test plan. What was not checked. Under 20 lines.

Never:
- Never go live without an explicit yes in this conversation.
- Never invent a review, a rating count, a press logo or a claim.
- Never show a price the cart does not charge, or ship a page in our default colours.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: landing-page-build". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
