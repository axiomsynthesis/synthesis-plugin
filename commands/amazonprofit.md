---
description: "Amazon profit after every fee and cost: One month of Amazon profit line by line, every fee by name, cost per unit, the line off its norm, and the products that lose money"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Amazon profit after every fee and cost

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Amazon profit after every fee and cost" (id: money-amazon-profit-every-fee, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what Amazon really left you for one month after every fee by name, product cost, lost stock and Amazon ads. It matches the Profit page to the cent, then breaks it down per unit and per product, and tests the biggest move against its own norm.

What to read: Amazon sales, discounts, refunds, every Amazon fee and account charge, product cost and Amazon ads, as the Profit page shows them
What to give me: One month of Amazon profit line by line, every fee by name, cost per unit, the line off its norm, and the products that lose money

Synthesis tools to use:
- `cost_rules for=money-amazon-profit-every-fee`
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `amazon_metric metric=ppc_profit_by_asin month=YYYY-MM`
- `amazon_metric metric=fee_rate_trend months=7`
- `operator_inputs section=cogs`
- `find_product`
- `business_profit month=YYYY-MM`

Steps:
1. Call `amazon_metric` with `metric=pnl_waterfall` and `month=` set to last month. Read `settlement_status`. If `fully_settled` is false, the profit is in `net_profit_estimate`: give it as an estimate with its range, then call the month before, the latest fully settled month, and lead with that one.
2. Call `amazon_metric` with `metric=pnl_waterfall` for each of the five months before the one you lead with. Compare each line as a share of sales with the month before and with its 6-month average. Name the line that moved most. If last month was the one off its norm, call it a reversion, not a new problem. `amazon_metric metric=fee_rate_trend months=7` gives the fee norm as a cross-check.
3. Call `amazon_metric` with `metric=ppc_profit_by_asin` and `month=` set to the month you lead with. If the result names a next `result_page`, call again with it until all are read. It adds up to the Profit page. From `by_family`, give each line per unit by product family. Keep the blended per-unit figure as one summary line. List the products whose profit after ads is below zero, with the loss per unit and for the month, named from `asin_names`, and `find_product` only for a code it does not name.
4. Call `operator_inputs` with `section=cogs`. If the waterfall's `units_missing_cost` is above zero, name the products with sales and no cost.

Checks before answering:
- The net must equal the Profit page. If `profit_page_tie` shows any drift, say so first and do not state a profit.
- Sales are before discounts. Discounts and refunds are their own lines below. Never take them off twice.
- A month still settling has an estimate, not a result. Say "estimate" and give its range.
- Some deductions Amazon labels only "Others". Where the brand has ruled them display-ad bills, the page moves them into advertising, sometimes into the month the ads ran. Name the month and the dollars moved, and say that month's profit was restated. If what is left unlabelled is over 2% of sales, say to check it.
- Shipping buyers paid is a memo line, not profit.
- Read which outside costs the page counts from its own lines. Meta ads sent to Amazon, an outside agency, and anything a line does not show are not counted, so profit reads high. Say which.
- If ad spend coverage says a day or an ad type is missing, profit is overstated. Say so.

Rounds (relook before you answer):
1. **Ties to the Profit page.** Re-read `profit_page_tie`. Fails when: drift is above $1. Fix: state no profit, name the gap.
2. **Settled or estimate.** Fails when: the month you lead with has `fully_settled` false and the first line does not say "estimate" with its range. Fix: lead with the latest settled month.
3. **Is the big move real?** Re-check the line that moved most against the 3 months before as well as the 6. Fails when: it is within 1 point of its norm on either window, or the earlier month was the odd one. Fix: call it a reversion or noise, not a new problem.
4. **Marketing outside Amazon.** Call `business_profit` for the same month and read `ads_by_destination`. Fails when: ad spend from other platforms pointing at Amazon, or an agency or influencer bill in the cost rules found, is over 0.5% of sales and no second, lower profit line includes it. Fix: give profit after it as a second line.
5. **Cost gap.** Fails when: `units_missing_cost` is above zero and the first line does not say "product cost missing for X% of sales". Fix: add it and name the products.
6. **What changed since last run.** Fails when: profit share moved more than 3 points from the last run or month before, or unlabelled deductions moved more than 50%, and the answer does not name the lines behind 80% of it. Fix: name them, and any month restated by a cost ruling.

Output:
- One line first: profit for the month, as dollars and as a share of sales, settled or estimated.
- A table: line, dollars, share of sales, per unit, change in share from the month before, 6-month norm.
- One line on the biggest fee and one on the line that moved most, real change or reversion.
- Per unit by product family, and the products that lose money after ads.
- One move: the one cost to work on first, and the number that will show it worked next month.

Never:
- Never use fees grouped by the date Amazon posted them for this view. They cover different orders.
- Never take per-product profit from a view without Amazon account charges.
- Never guess a product cost.
- Never change a price, budget or listing. A person does that.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-amazon-profit-every-fee". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
