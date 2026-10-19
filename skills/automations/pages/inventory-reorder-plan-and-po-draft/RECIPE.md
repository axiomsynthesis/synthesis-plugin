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
2. Call `netsuite_metric metric=inventory_position limit=200` for each product's `lead_time_days`, `on_order` and stock by location. Use only its non-Amazon locations. Its Amazon location runs stale, so Amazon stock comes from step 1. If NetSuite is not connected, ask the person for lead times and open orders.
3. Call `amazon_metric metric=closed_shipments limit=10`. The time to move stock into Amazon is `arrival_times` US `received_90pct_p90`.
4. Call `amazon_metric metric=velocity_momentum weeks=8 limit=200`. A product whose last two weeks sell under a fifth of its first two, while in stock, is winding down.
5. Call `operator_inputs` with `section=all` for unit costs and any purchase orders entered there. Never take lead times from it. It has none.
6. For each product: units to order = `normal_pace_per_day` times (lead time + transfer time + 90 days of cover) + `extra_units` of every sale in that window, minus Amazon stock, stock landing, your own warehouse stock and units on order. Order-by date = `late_runs_out` minus lead time minus transfer time minus 7 days.
7. Use `export_xlsx` with `filename=reorder-plan.xlsx`: a reorder tab and a PO draft tab.

Checks before answering:
- A product with no lead time is flagged, never given a made-up one.
- If the stock read fails, stop and say so.
- Count stock at Amazon, at your own warehouse and already on order before ordering more.
- Never size from trailing sales speed or days of cover. They count sale spikes as normal sales.
- Skip any product winding down. List it as wind-down, never as a reorder line. There is no discontinued flag to read yet.
- No safety stock from forecast error yet. The 7-day buffer stands in for it. Say so.
- Pace times days ignores the month pattern. Say a busy season may need more.
- Minimum order and case pack are not known. Ask before rounding.

Output:
- One line first: the most urgent order and its order-by date.
- An Excel file, reorder-plan.xlsx: product, run-out date, units to order, order-by date, unit cost, total cost. A second tab is the PO draft. A third lists wind-down products.

Never:
- Never send a PO to a supplier. A person does that.
- Never guess a lead time or a unit cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: inventory-reorder-plan-and-po-draft". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
