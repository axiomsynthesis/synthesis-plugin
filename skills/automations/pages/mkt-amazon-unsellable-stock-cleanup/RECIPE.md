# Clear out damaged and dead stock

Channel: Inventory · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Clear out damaged and dead stock" (id: mkt-amazon-unsellable-stock-cleanup, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Unsellable and dead stock keeps paying storage. This builds the list of what to pull out, throw away or keep, and how much it saves.

What to read: Unfulfillable units per product at Amazon, excess and dead stock by days of cover, and storage fees per month
What to give me: A remove, dispose or keep call for unsellable and dead stock, and the monthly storage it frees up

Synthesis tools to use:
- `amazon_metric metric=inventory_position limit=60`
- `amazon_metric metric=days_of_cover status=DEAD_STOCK limit=40`
- `amazon_metric metric=days_of_cover status=EXCESS limit=40`
- `amazon_metric metric=storage_fee_forecast limit=60`
- `export_xlsx`

Steps:
1. Call `amazon_metric metric=inventory_position limit=60` for unfulfillable units per product.
2. Call `amazon_metric metric=days_of_cover status=DEAD_STOCK limit=40` and `status=EXCESS limit=40`.
3. Call `amazon_metric metric=storage_fee_forecast limit=60` for each product's storage next month, its cubic feet per unit and the fee it could avoid.
4. Decide per product: remove (units worth more than removal cost), dispose (worth less), keep (seasonal or about to sell). Flag warehouse-damaged units as reimbursement candidates first.
5. Build `removal_list_<month>.xlsx` with `export_xlsx`: product, unsellable units, dead or excess units, suggestion, monthly storage saved.

Checks before answering:
- Stock is Amazon's live count, refreshed when asked. Quote Amazon's update time, and name any product the answer left out because its numbers did not add up.
- A product at zero sales because it was out of stock is not dead. The cover tool separates these. Respect it.
- Storage per product is a forecast from Amazon's posted sizes and rates. Say so, and say when the rate is published rather than measured.

Output:
- One line: units to act on and monthly storage saved.
- The spreadsheet above.

Never:
- Never create removal or disposal orders.
- Never dispose of units that may be owed a reimbursement before the person checks.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-unsellable-stock-cleanup". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
