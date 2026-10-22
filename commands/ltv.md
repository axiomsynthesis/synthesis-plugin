---
description: "Which first product makes the best customers?: Profit per customer by first product at the same age, against the cost to win them, and which to lead with"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Which first product makes the best customers?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which first product makes the best customers?" (id: customers-lifetime-value-by-first-product, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows which first purchase turns into your most profitable customers. It compares products at the same customer age, turns sales into what you keep after costs, and sets that against the cost to win a new customer.

What to read: Orders by customer, product margins, ad cost per new customer
What to give me: Profit per customer by first product at the same age, against the cost to win them, and which to lead with

Synthesis tools to use:
- `cost_rules for=customers-lifetime-value-by-first-product`
- `top_products metric=revenue top_n=10 start_month=<YYYY-MM> end_month=<YYYY-MM>`
- `find_product query=<name>`
- `product_ltv_windowed asin=<family> windows=[90,180,365]`
- `amazon_metric metric=breakeven_acos_ltv`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=ppc_ntb days=90`
- `first_order_contribution_margin`
- `shopify_metric metric=product_ltv`
- `cross_sell window=90d`

Steps:
1. Call `top_products metric=revenue top_n=10` with `start_month` and `end_month` spanning the last 12 closed months to pick your top Amazon products. Call `find_product` with a `query` for each to get its family.
2. For each family, call `product_ltv_windowed` with `asin=family:<id>` and `windows=[90,180,365]`. It averages each window over only the customers old enough to fill it. Rank on the longest window every compared product can fill, and say how many customers each window covers.
3. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3` for each product's margin after fees, refunds and product cost. Multiply each window's sales value by that margin to get margin value.
4. Call `amazon_metric` with `metric=breakeven_acos_ltv` and each `asin` for the margin value and payback at 1, 3, 6 and 12 months. Use it to check step 3.
5. Call `amazon_metric` with `metric=ppc_ntb` and `days=90` for the cost per new-to-brand order. Then call `first_order_contribution_margin` with the `asin` and that cost as `cac` for the first-order profit after the cost to win. Margin value divided by that cost is the value-to-cost ratio. Months until margin value covers the cost is payback.
6. Call `shopify_metric` with `metric=product_ltv` for website customers by first product. It has no date window, so show it on its own line and never rank it beside Amazon.

Checks before answering:
- If a tool says a value is gated, explain why and do not state it.
- Compare products only at the same window. A window with no value means no customer is old enough. It is not a low value.
- If a window is filled by under 60% of a product's customers, say it will move as they age.
- Rank on margin value, never on sales value. A high-selling product with a thin margin can be the worst way in.
- The cost to win a customer covers Sponsored Brands and Display only. Amazon reports no new-to-brand count for Sponsored Products. So it is one account-wide figure, not a cost per product. Say so, and say the ratio cannot tell products apart on cost yet.
- Amazon order history starts about two years back. A customer who first bought before that counts as new here. Say so for long-selling products.
- A product with a few dozen customers is too small to rank. Say so.
- If product cost is missing, say margin value cannot be shown.
- If a channel's read is empty, say it is missing. Never show it as zero.

Rounds (relook before you answer):
1. **Same age.** Re-read every window you ranked on. Fails when: two products are compared at different windows, or a window is filled by under 60% of a product's customers. Cohorts younger than 12 months are censored. Fix: drop to the longest window both can fill.
2. **Profit, not sales.** Re-rank on margin value. Fails when: the lead pick changes from the sales ranking, or any row has no product cost. Sales value overstates; on one live brand it read about 75% above profit. Fix: rank on margin, blank rows with no cost.
3. **Pack inside the family.** Call `product_ltv_windowed` per pack size of the winning family. Fails when: one pack's buyers bring over 1.3x the family's margin value at the same window. Bigger first packs often make more valuable buyers. Fix: lead with that pack.
4. **Argue the losing case.** Is it the product, or who buys it? Fails when: the gap at 90 days is already as big as at 365. Then it is who buys, not the product. Fix: call it a correlation and propose a default-pack test.
5. **What they buy next.** Call `cross_sell` with the lead and the next product and `window=90d`. Fails when: the second order is mostly a product with a thinner margin than the lead. Fix: value the follow-on at its own margin.
6. **Against the cost to win.** Fails when: margin value over cost to win is under 1.3x at 365 days, the default bar unless the brand set its own. Fix: say leading with it does not yet pay.

Output:
- One line first: the product to lead ads with, and how much more margin its customers bring at the same age.
- A table: first product, window, customers, sales value, margin value, cost to win, value-to-cost ratio, payback months.
- One line for the website read, with the dates it covers.
- One move: which product to lead with in ads, and how we will know it worked.

Never:
- Never change ads or offers. A person does that.
- Never mix website and Amazon values into one number.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-lifetime-value-by-first-product". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
