---
description: "Build a landing page from the kit: A five-reasons landing page on a hidden copy of the store, each reason answering a real complaint, every price proved against the cart, and a test plan"
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
Builds a paid-traffic landing page, usually "5 reasons to switch", with packs, a guarantee and a sticky phone bar.
Reasons come from real review complaints and searches. Claims are approved and prices proved against the cart.

What to read: Landing page results, review complaints, what shoppers search for, store and marketplace prices, pack costs, brand colours and approved claims
What to give me: A five-reasons landing page on a hidden copy of the store, each reason answering a real complaint, every price proved against the cart, and a test plan

Synthesis tools to use:
- `cost_rules for=landing-page-build`
- `ga4_metric metric=landing_pages days=28`
- `meta_metric metric=ad_destinations days=28`
- `amazon_metric metric=review_voice limit=12`
- `amazon_metric metric=search_query_performance grain=month scope=nonbranded`
- `amazon_metric metric=listing_details`
- `render_report`
- `brand_kit`
- `brand_facts`
- `first_order_contribution_margin`
- `breakeven_roas`
- `web_fetch`

Steps:
1. Call `ga4_metric` with `metric=landing_pages` and `days=28`, and `meta_metric` with `metric=ad_destinations` and `days=28`. Find the best page by sales per visitor and the ads that will feed the new one. Start from it and any rival pages the person names. Format: five_reasons unless the person picks pack_picker, before_after, proof or problem_solve. Call `render_report` with `format=landing_page` and `page_format` set to it, and follow its playbook.
2. Reasons. Call `amazon_metric` with `metric=review_voice`, `sentiment=negative` and `limit=12`, then `sentiment=positive`. Each of the top 3 complaints gets a reason that answers it head on. Top praise becomes proof. No marketplace sales: ask for the store's reviews.
3. Angle. Call `amazon_metric` with `metric=search_query_performance`, `grain=month` and `scope=nonbranded`. Lead with the pain shoppers search most that the product answers, not the feature the brand likes best. On one live brand a pain searched about 34,000 times a month beat a feature searched 2,500.
4. Call `brand_kit`. A colour or font in state house is our default, not the brand's. Read the homepage with `web_fetch` or ask. Show both before building.
5. Offer maths. For each pack, gift and add-on, get the cost. Call `first_order_contribution_margin` and `breakeven_roas` with price and cost passed by hand, plus gift, shipping and payment costs. Show profit per order and the most to pay per sale. Default to the pack with the highest profit times expected take.
6. Price gap: call `amazon_metric` with `metric=listing_details` and `asin=<the product's marketplace code>`. A page price above it needs a stated reason, such as a gift, a bigger pack or free shipping.
7. Claims only from `brand_facts`. Watch every creator clip to the end for words on screen or said aloud. Proof numbers are real counts rounded down. Reviews real and dated.
8. Section order: offer bar, hero with buy box, press, reasons with a buy button after reasons 1 and 4, reviews and creator clips, timeline, FAQ, final buy box, sticky phone bar.
9. Call `render_report` with `format=landing_page` and `page` filled, with the store's address. Fix every problem and call again.
10. In Claude Code, download the zip from `download_url`, unzip it, and run the preview there. It checks every price and four screen sizes. Stop at the first FAIL, fix, run again. Show the preview link and `lpk-shots/`.
```bash
node lpk.mjs preview --store <store>.myshopify.com
```
11. Only after an explicit yes in this conversation, go live (it backs up first), create the page with template `lpk-<name>`, and check it:
```bash
node lpk.mjs live --store <store>.myshopify.com --page <any page handle> --confirm
node lpk.mjs check "<new page link>"
```
12. Test plan: control = the page from step 1, never on its own template. Metric: profit per visitor. Visitors a side = 16 x p x (1 - p) divided by d squared. At least 2 full weeks. Give the read date.

Checks before answering:
- A price line not ok means no discount charges that price. Never publish around it.
- A gift or pack with no cost fails step 5. A losing pack needs the person to call it a loss leader.
- A crossed-out price must be a real earlier price. The cart check cannot prove this. Ask.
- Say who reads the test on the read date, and what was not checked: shipping, tax, checkout.

Rounds (relook before you answer):
1. **Complaints answered.** Re-read step 2. Fails when: one of the top 3 complaints has no reason answering it, or a reason answers a complaint nobody wrote. Fix: rewrite that reason.
2. **Angle beats the alternatives.** Re-read step 3. Fails when: another pain the product answers has twice the monthly searches of the headline's. Fix: swap the headline and reason 1.
3. **Claim sweep.** Check every sentence, image word and clip caption against `brand_facts`. Fails when: one claim has no matching entry, a disease claim appears, or a rival is named. Fix: cut or reword it.
4. **Price proof.** Re-run the preview check and step 6. Fails when: any pack's cart price is 1 cent off the page, or the page price beats the marketplace price with no stated reason. Fix: correct the price or add the reason.
5. **Profit bar.** Compare the default pack's most to pay per sale with what the feeding ads cost per sale from step 1. Fails when: the ads cost more than the pack can pay. Fix: lead with a bigger pack or add an add-on.
6. **Phone first screen.** Open `lpk-shots/` at 360 wide. Fails when: the buy button is not on the first screen, a sideways scroll shows, or the sticky bar is missing. Fix: move the buy box up.

Output:
- First line: format, product, headline angle, default pack, and the page it must beat.
- The preview link. Offer table: pack, price, profit per order, most to pay per sale.
- Reasons, one line each with the complaint or search it answers.
- Price check, one line per pack. The test plan. What was not checked. Under 25 lines.

Never:
- Never go live without an explicit yes in this conversation.
- Never invent a review, a rating count, a press logo, a claim or a proof number.
- Never show a price the cart does not charge, or ship a page in our default colours.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: landing-page-build". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
