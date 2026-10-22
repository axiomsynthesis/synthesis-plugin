---
description: "Profit per order after ads, page by page: What each landing page keeps per order after product, warehouse and Meta costs, profit per visitor against your target, and the moves ranked by dollars a week"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Profit per order after ads, page by page

Channel: Website · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Profit per order after ads, page by page" (id: website-page-profit-after-ads, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Answers one question per landing page: after product, warehouse and Meta costs, does an order make money?
It builds profit kept per order from each page's pack mix and real per-item costs, takes off what Meta paid per sale to that page, and ranks the moves that close the gap.

What to read: Meta spend and sales by landing page, visits per page, pack mix per page, product and warehouse costs per item
What to give me: What each landing page keeps per order after product, warehouse and Meta costs, profit per visitor against your target, and the moves ranked by dollars a week

Synthesis tools to use:
- `cost_rules for=website-page-profit-after-ads`
- `recall_decisions`
- `meta_metric metric=ad_returns`
- `meta_metric metric=ad_destinations days=7`
- `ga4_metric metric=landing_pages days=7`
- `shopify_metric metric=profit`
- `shopify_metric metric=daily_revenue days=7`
- `shopify_metric metric=order_tags months=1`
- `operator_inputs section=cogs`
- `first_order_contribution_margin`

Steps:
1. Call `recall_decisions` for a saved profit per visitor target and keep line. Ask in one message: which pages (default every page Meta spends on), the week (default the last 7 closed days), and any target not saved. None given: grade against break-even, never another brand's number. Say if the week crosses a big sale (Prime days, Black Friday).
2. Call `meta_metric` with `metric=ad_returns` for website spend and sales by ad set, then `metric=ad_destinations` with `days=7` for each ad's page. It lists the top 40 ads only, and ad returns can leave ad sets out: add both, and list ad sets found in only one and ads with no page. Group by page, links stripped of tags.
3. Call `ga4_metric` with `metric=landing_pages` and `days=7` for visits per page. If not connected, use Shopify's sessions report and say so.
4. Pack mix per page. No tool splits orders by landing page. Ask for Shopify's orders export with landing page. Without it, call `shopify_metric` with `metric=profit` for this month: store profit before ads / store orders is the stand-in profit kept per order, labelled so. Never use top products for a week: it is all-time.
5. Costs per pack. Call `operator_inputs` with `section=cogs`. Call `shopify_metric` with `metric=profit` for shipping and warehouse cost per order. If the warehouse charges per item, ask for its price list (pick fee per item, box, postage) and use it. Call `first_order_contribution_margin` per pack with `price`, `cogs`, `misc` for warehouse, postage and gifts, and `referral_fee_pct=2.9` for card fees.
6. Per page: profit kept per order = each pack's share x its profit, or the stand-in. Minus Meta cost per sale to that page = profit per order after ads. Times orders = dollars a week. Divided by visits = profit per visitor.
7. The keep line per page is its profit kept per order. If the ad returns read carries a different keep line, show both and say which this answer uses. List ads over it with their spend.
8. Rank moves by dollars a week: switch off ads over the keep line (single ads, never an ad set that also holds an ad under it), lift order size (bigger default pack, add-on), change the default pack. Each move: dollars, low case, its assumption, and the test that proves it (/splittest or /pagetest).

Checks before answering:
- Meta counts sales it touched. If Meta's sales to a page exceed the store's orders from it, use the store's.
- Fees the profit read marks not connected (card or payment fees): show profit kept per order with them as the low case.
- A pack or gift with no cost: ask. Never fill one in.
- A flat warehouse cost per order hides that bigger packs cost more to ship. Say which was used.
- Repeat orders are not counted. Say a losing first order may still pay back later, and that this does not measure it.
- Only propose moves that make money in their low case.

Rounds (relook before you answer):
1. **Real costs.** Re-read each pack's cost lines. Fails when: a pack or gift has no cost, or a flat warehouse cost is used while the warehouse charges per item. Fix: ask, recompute.
2. **Spend matched.** Fails when: under 90% of website spend in the ad returns read is matched to a page. Fix: list the unmatched ads and ad sets and match by link.
3. **Second week.** Re-run on the week before. Fails when: a page flips between profit and loss after ads, or the top move changes. Fix: say it is not settled.
4. **Stand-in mix.** Fails when: a page uses the store-wide mix and a move depends on that mix. Fix: say so and ask for the export.
5. **Meta over-count.** Call `shopify_metric` with `metric=daily_revenue` for the week and `metric=order_tags` for renewals. Fails when: Meta's website sales exceed the store's orders less subscription renewals and email-credited orders. Fix: scale every page's Meta orders down by that ratio, so cost per sale rises.
6. **Low case.** Fails when: a move's take rate or lift has no source, or it loses money in its low case. Fix: drop it or mark it a test.

Output:
- First line: the worst page, its profit or loss per order after ads, and dollars a week.
- Table per page: orders, profit kept per order, Meta cost per sale, after ads per order, profit per visitor against target.
- Moves ranked by dollars a week, each with its low case and test.

Never:
- Never use another brand's target or keep line.
- Never change budgets, prices or pages. A person does that, or the do shortcuts after a yes.
- Never count a cost as zero because it is missing.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-page-profit-after-ads". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
