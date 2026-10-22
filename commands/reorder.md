---
description: "What to reorder, and the purchase order to send: How much of each product to order and by when, with a purchase order drafted for you to check"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# What to reorder, and the purchase order to send

Channel: Inventory · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What to reorder, and the purchase order to send" (id: inventory-reorder-plan-and-po-draft, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Works out how much to order of each product and by when, then drafts a purchase order. It sizes each order on normal sales with sale spikes removed, adds the sales ahead, and takes off stock you already have or have already ordered. A person checks it and sends it to the supplier.

What to read: Amazon stock and its run-out forecast with sales events, stock and orders already placed in NetSuite, supplier lead times, transfer times
What to give me: How much of each product to order and by when, with a purchase order drafted for you to check

Synthesis tools to use:
- `amazon_metric metric=stockout_forecast limit=200`
- `netsuite_metric metric=inventory_position limit=200`
- `amazon_metric metric=closed_shipments limit=10`
- `amazon_metric metric=velocity_momentum weeks=8 limit=200`
- `operator_inputs`
- `export_xlsx`

Steps:
1. Call `amazon_metric metric=stockout_forecast limit=200` for each product's `normal_pace_per_day`, `late_runs_out`, stock landing, and each upcoming sale in `events` with its `extra_units`. Read every page: call again with the next `result_page` the result names.
2. Call `netsuite_metric metric=inventory_position limit=200` for each product's `lead_time_days`, `on_order` and stock by location. Use only its non-Amazon locations. Its Amazon location runs stale, so Amazon stock comes from step 1. If NetSuite is not connected, ask for open orders.
3. Call `amazon_metric metric=closed_shipments limit=10`. The time to move stock into Amazon is `arrival_times` US `received_90pct_p90`.
4. Call `amazon_metric metric=velocity_momentum weeks=8 limit=200`. A product whose last two weeks sell under a fifth of its first two, while in stock, is winding down.
5. Call `operator_inputs` with `section=all` for unit costs and any purchase orders entered there. Never take lead times from it. It has none.
6. A product still missing its lead time, or your own warehouse stock: ask in one plain question. Say the dollars: each week of lead time adds a week of sales to the order.
7. For each product: units to order = `normal_pace_per_day` times (lead time + transfer time + 90 days of cover) + `extra_units` of every sale in that window, minus Amazon stock, stock landing, your own warehouse stock and units on order. Order-by date = `late_runs_out` minus lead time minus transfer time minus 7 days.
8. Use `export_xlsx` with `filename=reorder-plan.xlsx`: a reorder tab and a PO draft tab.

Checks before answering:
- A product with no lead time, after asking, is flagged, never given a made-up one.
- If the stock read fails, stop and say so.
- Count stock at Amazon, at your own warehouse and already on order before ordering more.
- Never size from trailing sales speed or days of cover. They count sale spikes as normal sales.
- Skip any product winding down. List it as wind-down, never as a reorder line. There is no discontinued flag to read yet.
- No safety stock from forecast error yet. The 7-day buffer stands in for it. Say so.
- Pace times days ignores the month pattern. Say a busy season may need more.
- Minimum order and case pack are not known. Ask before rounding.

Rounds (relook before you answer):
1. **Counted twice.** Fails when: a product's units on order also appear as stock landing in the forecast. Fix: count them once and redo the line.
2. **Lead time stress.** Add 14 days to every lead time. Fails when: an order-by date moves into the past. Fix: flag it as order now.
3. **Sales in the window.** Fails when: a known sale falls inside a product's cover window but its `extra_units` is zero. Fix: add the last same sale's lift and say so.
4. **Money on order.** Total units to order times unit cost. Fails when: a line has no unit cost, or the total is over the cash the person gives. Fix: blank the line, or rank by run-out date and stop at the cash.
5. **Too much stock.** Fails when: any line covers over 180 days of normal sales. Fix: cut it to 90 days of cover and say the cash saved.

Output:
- One line first: the most urgent order and its order-by date.
- An Excel file, reorder-plan.xlsx: product, run-out date, units to order, order-by date, unit cost, total cost. A second tab is the PO draft. A third lists wind-down products.

Never:
- Never send a PO to a supplier. A person does that.
- Never guess a lead time or a unit cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Inputs only I know: supplier lead time in days; units at your own warehouse or 3PL. If the tools lack one, ask me ONE plain question for it, all in one message: why it matters and about how many dollars it moves. Use my answer for this run. Never invent one. If I do not know, say what the answer leaves out. Nothing saves the lead time or own warehouse stock yet: say it was used for this run only. On a scheduled run, name what is missing instead.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: inventory-reorder-plan-and-po-draft". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
