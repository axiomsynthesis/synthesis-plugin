---
description: "Which Amazon products actually make money?: Each Amazon product's profit after fees, ads, returns and cost, ranked, with losers and break-even ad spenders named"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Which Amazon products actually make money?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which Amazon products actually make money?" (id: money-profit-by-product-after-everything, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what each Amazon product keeps after fees, ads, returns and product cost. It ranks them, names the losers and the ones that spend on ads but keep almost nothing, and says whether repeat buyers pay those back. Amazon only.

What to read: Settlements, ads, product costs
What to give me: Each Amazon product's profit after fees, ads, returns and cost, ranked, with losers and break-even ad spenders named

Synthesis tools to use:
- `cost_rules for=money-profit-by-product-after-everything`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=ppc_profit_by_asin`
- `amazon_metric metric=return_reasons`
- `operator_inputs`
- `product_ltv_windowed asin=<asin>`
- `find_product`
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `business_profit month=YYYY-MM`

Steps:
1. Call `amazon_metric` with `metric=ppc_profit_by_asin` and no month (it picks the last settled month). Each advertised product's `profit_after_ads` is the Profit page's own profit: refunds, discounts, fees, its share of Amazon's storage and other account charges, product cost and all its ads are already taken off. Use that figure as the product's profit. Do not subtract anything from it again.
2. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3` for products with no ads that month. Their figure is before Amazon's storage and other account charges: say so beside each one.
3. Call `amazon_metric` with `metric=return_reasons` and `months=3` to explain WHY a product's refunds are high. Refunds are already in both figures above. Never subtract return cost a second time.
4. Call `operator_inputs` with `section=cogs` to check every product has a cost. Name each product with `find_product`.
5. Profit per unit = `profit_after_ads` divided by units. Rank the advertised products by profit per unit and by profit a month. Rank the products with no ads in a separate table, because their figure is on a different basis.
6. For each product under 5% of its sales after ads, call `product_ltv_windowed` with its `asin` (or its `family:<family_id>` from `find_product`). Repeat sales per first buyer = the 180-day value less the first order. Estimate the repeat profit as that times the product's margin before ads, and say it is an estimate. Add it to the profit per unit. If the sum is above zero, label the product "pays back on repeat". If not, "does not pay back".

Checks before answering:
- A product with no cost entered is flagged "no cost", never shown as pure profit.
- Use the last settled month. Fees and refunds settle late.
- Profit comes from one figure per product. Never add it up from sales, fees, ads and returns in different tools.
- If ad spend for a product is missing, say so. Do not treat it as zero ad cost.
- One bad month is not a pattern. Check the month before when a product turns negative.
- Also name every product whose profit after ads is under 5% of its sales while its ad cost is over 10% of its sales. Show its ad dollars and what it kept.
- Never mix the two bases in one ranking.
- If `product_ltv_windowed` is gated or its cohort is young, say repeat value is unknown for that product. Never label it "pays back" without the number.
- This is Amazon only. Marketing paid outside Amazon that drives Amazon sales, such as an influencer agency or Meta ads sent to Amazon, is not in these figures. Say so.

Rounds (relook before you answer):
1. **Ties to the page.** Call `amazon_metric` with `metric=pnl_waterfall` for the same month. Fails when: the advertised products' profit plus the rest misses the page's Amazon profit by more than 1%. Fix: name the gap and which products it sits in.
2. **One bad month.** Call `amazon_metric` with `metric=ppc_profit_by_asin` for the month before. Fails when: a product you call a loser made money that month. Fix: call it "lost money this month", not a loser.
3. **Payback proven.** Fails when: a product is called "pays back on repeat" without a 180-day value, or its first buyers are under 180 days old. Fix: say repeat value is unknown.
4. **Marketing outside Amazon.** Call `business_profit` and read `ads_by_destination`. Fails when: ad spend from other platforms pointing at Amazon is over 5% of Amazon ad spend and the answer does not say product profit reads high by that much. Fix: name the dollars.
5. **Cost gap.** Fails when: a product with no cost is in a ranking, or the first line lacks "product cost missing for X% of sales" while any is missing. Fix: take it out and say so.
6. **Fix the biggest dollars first.** Fails when: the product to fix first loses less a month than another on the list. Fix: rank the move by monthly dollars, not per unit.

Output:
- One line first: how many products lose money, and how many make under 5% after ads, with the ad dollars behind them.
- A table of advertised products: product, units, sales, fees and account charges, ad cost, refunds, product cost, profit per unit, profit a month, and pays back on repeat or not.
- A separate table for products with no ads, marked "before account charges".
- One move: the product to fix first and what to change.

Never:
- Never change a price, budget or listing. A person does that.
- Never guess a product cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-profit-by-product-after-everything". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
