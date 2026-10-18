# Send me the inventory report every Monday

Channel: Inventory · Level: On a schedule · Status: Ready now
Schedule: every Monday, early morning Pacific time, from our server

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Send me the inventory report every Monday" (id: inventory-weekly-stock-email, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Once a week, reads Amazon's live stock, the date each product runs out (counting upcoming sales, booked deals and stock on its way), every open shipment into Amazon and the finished shipments that came in short, and puts the answer first: what to act on now, then what is coming.

What to read: Amazon's live stock in every bucket, when each product runs out with upcoming sales and stock on its way, every open shipment into Amazon, and finished shipments that came in short
What to give me: Every Monday, one email: what is sold out or runs out within 30 days, what runs out in the next 90, where your stock sits, and what is on its way, with the full detail as a spreadsheet

Synthesis tools to use:
- `amazon_metric metric=inventory_position limit=200`
- `amazon_metric metric=stockout_forecast limit=200`
- `amazon_metric metric=inbound_shipments limit=200`
- `amazon_metric metric=closed_shipments limit=10`

Steps:
1. Call `amazon_metric metric=inventory_position limit=200` for the stock in every bucket and Amazon's update time.
2. Call `amazon_metric metric=stockout_forecast limit=200` for each product's run-out dates: `late_runs_out` (the date to plan against), `runs_out_for_good`, the gap before stock on its way lands (`gap_days`, `gap_lost_units`) and `normal_sales_usd_per_day`. Read every page: call again with the next `result_page` the result names. The product list is cut to a few rows per page whatever the limit.
3. Call `amazon_metric metric=inbound_shipments limit=200` for every open shipment and the units still owed on it. Read shipment totals from `by_status` and `tie_out`, not from the rows on page 1.
4. Call `amazon_metric metric=closed_shipments limit=10` for finished shipments that came in short.

Checks before answering:
- Quote Amazon's update time. If a fresh pull could not be taken, say so at the top.
- Plan against `late_runs_out`, one run-out date per product, from the forecast only; never also quote days of cover.
- Name every product by its short name AND its ASIN.
- Name every product left out because Amazon's own numbers did not add up. Never show it as zero.
- Say which sales are in the dates and which are expected rather than announced. If no booked deals are entered, say a booked Lightning Deal or Deal of the Day is not in the dates.
- Units Amazon no longer expects on a shipment are worth checking, never money owed.
- If only the forecast fails, still give the stock and say the run-out dates are missing this week.

Output:
- One line: how many products are sold out, and how many more run out within 30 days, with the soonest date.
- Act now: each sold-out or within-30-days product with its ASIN, ready, sells a day (with dollars), on the way, and days left with the date.
- Coming up: the same for products running out in 31 to 90 days.
- Where it is: units in each bucket with its share of the total.
- Shipments to Amazon: by stage, with units still owed, and any units Amazon no longer expects.
- Came in short: the three biggest shortfalls on finished shipments, and whether Amazon paid any back.

Never:
- Never create shipments, place orders or open cases. A person does that.
- Never count stock moving between warehouses as ready to sell. It lands later, and the gap before it lands is lost sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: inventory-weekly-stock-email". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This one runs on the Synthesis server (every Monday, early morning Pacific time, from our server). Do not set up a repeat yourself; read the latest copy instead.
