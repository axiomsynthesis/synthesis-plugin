---
description: "How fast does a new customer pay back?: Months to earn back a new website customer's cost from profit after product cost, shipping and fees"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# How fast does a new customer pay back?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How fast does a new customer pay back?" (id: grw-cac-payback, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Divides ad spend that sends shoppers to the website by the new website customers it won, over the same three closed months. It then follows earlier customers to see how many months their profit, after product cost, shipping and card fees, takes to pay that cost back.

What to read: Ad spend that sends shoppers to the website, new website customers and their cumulative value by acquisition month
What to give me: Months to earn back a new website customer's cost from profit after product cost, shipping and fees

Synthesis tools to use:
- `cost_rules for=grw-cac-payback`
- `meta_metric metric=weekly_trend weeks=13`
- `meta_metric metric=ad_destinations days=90`
- `google_ads_metric metric=efficiency_trend weeks=13`
- `tiktok_metric metric=spend_trend months=4`
- `new_customers_dtc month=<YYYY-MM>`
- `shopify_metric metric=cohort_ltv_censor_safe basis=contribution`
- `shopify_metric metric=profit month=YYYY-MM`
- `first_order_contribution_margin`

Steps:
1. Use the last three closed months for every spend and count.
2. Call `meta_metric metric=weekly_trend weeks=13`. Add the spend of weeks that start inside the three months, minus each week's `amazon_bound_spend`. Then call `meta_metric metric=ad_destinations days=90` only to split the rest into website, Walmart and no known destination. Top ads only.
3. Call `google_ads_metric metric=efficiency_trend weeks=13`. Same weeks, minus each week's `amazon_bound_spend`.
4. Call `tiktok_metric metric=spend_trend months=4`. Keep `auction_spend` for the three months as a destination unknown line. Leave shop ad spend out. It sells inside TikTok Shop.
5. Call `new_customers_dtc` for each of the three months and add them.
6. Cost per new customer = website spend over new customers. Low figure: known website spend only. High figure: add no known destination and TikTok auction spend.
7. Call `shopify_metric metric=cohort_ltv_censor_safe basis=contribution`. Each point carries `cumulative_contribution_per_customer`, what a customer kept after product cost, fees, refunds and shipping.
8. Payback month = first month a cohort's `cumulative_contribution_per_customer` passes the cost. If `contribution_basis.keep_per_sales_dollar` is missing, give `contribution_basis.why` and no payback month. Never use a margin.
9. Call `shopify_metric metric=profit` for the latest month. Average order value is `own_store` sales over `orders`. Shipping per order is `contribution_basis.shipping_per_order`.
10. Call `first_order_contribution_margin` with `price=` the average order value, `cogs=` its product cost, `misc=` shipping per order and `cac=` the cost per new customer.

Checks before answering:
- If a customer tool returns gated, do not state the number. Give its refusal reason.
- Weeks do not match months to the day. Say so.
- Young cohorts are unfinished. Leave immature cells blank, never read them as low.
- New means first website order. A long-time Amazon buyer counts as new, so cost per new customer reads low. Say so.
- Never add Amazon-bound or TikTok Shop spend to the website cost. Say how much was left out.
- Use website cohorts only. Brand-wide cohort tables are built from Amazon orders.
- Costs in `contribution_basis.not_counted` are not taken off, so payback reads fast. Name them.
- One month's rates are applied to every cohort. Say so.
- Email and retention spend on repeat orders is not taken off yet, so payback reads a little fast.

Rounds (relook before you answer):
1. **Censored cohorts.** Re-read each payback month. Fails when: a payback month is read from a cohort younger than that month, or no cohort is 12 months old. Fix: blank it and say which cohorts are still too young.
2. **Second window.** Re-run steps 2 to 6 on the three months before. Fails when: cost per new customer moves over 25% between the two windows. Fix: show both and say payback is unstable.
3. **Low and high.** Fails when: the high cost per new customer is over 30% above the low one. Fix: lead with the range, not the low figure, and name the spend with no known destination.
4. **First order.** Re-read step 10. Fails when: the first order loses money after its cost to win and no cohort pays back in 12 months. Fix: say every new website customer loses money today, and name order size as the lever. An order worth at least 2x the main product's single price is the default bar.
5. **Costs left out.** Fails when: `contribution_basis.not_counted` names a cost over 5% of sales. Fix: say payback reads that much fast, with the cost named.

Output:
- Answer first: does a new website customer pay back, and in how many months? Cost per new customer as low and high. If no cohort pays back within 12 months, say so plainly.
- Table: spend by source counted and left out, new customers, cost each.
- Table by acquisition month: profit per customer at month 1, 3, 6 and 12, payback month.
- One line: whether the first order alone covers its cost.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-cac-payback". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
