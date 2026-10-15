# Daily Inventory Report

Channel: Inventory · Level: On a schedule · Status: Ready now
Schedule: every morning, early Pacific time, from our server

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Daily Inventory Report" (id: inventory-daily-stock-report, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every morning, reads Amazon's live stock in the same nine buckets every time, gives the date each product runs out (counting upcoming sales, booked deals and stock on its way), and lists what is still owed on open shipments into Amazon.

What to read: Amazon's live stock in nine buckets per product, when each product runs out with upcoming sales and stock on its way, and every open inbound shipment
What to give me: All your Amazon stock in one read: ready to sell, moving between warehouses, on its way in, damaged, and when each product runs out

Synthesis tools to use:
- `amazon_metric metric=inventory_position limit=200`
- `amazon_metric metric=stockout_forecast limit=200`
- `amazon_metric metric=inbound_shipments limit=200`

Steps:
1. Call `amazon_metric metric=inventory_position limit=200` for the nine buckets per product and in total, and Amazon's update time.
2. Call `amazon_metric metric=stockout_forecast limit=200` for each product's run-out dates: `late_runs_out` (the date to plan against), `expected_runs_out`, `runs_out_for_good`, and the gap before stock on its way lands (`gap_days`, `gap_lost_units`).
3. Call `amazon_metric metric=inbound_shipments limit=200` for every open shipment and the units still owed on it.

Checks before answering:
- Quote Amazon's update time. If the answer says a fresh pull could not be taken, or the pull is stale, say so at the top.
- Show all nine buckets in their fixed order, even when a bucket is zero.
- Name every product the answer left out because Amazon's own numbers did not add up. Never show it as zero.
- Plan against `late_runs_out`. Give one run-out date per product, from the forecast only; never also quote days of cover, which uses a flat pace and gives a different date.
- Say which sales are in the dates and which are expected rather than announced. If the forecast says no booked deals are entered, say a booked Lightning Deal or Deal of the Day is not in the dates.
- Read the shipments' `tie_out`. Units Amazon no longer expects on a shipment are worth checking, never money owed.
- If the stock read fails, say "stock could not be read today", not silence. If only the forecast fails, still give the stock and say the run-out dates are missing today.

Output:
- One line: how many products are sold out, and how many more run out within 30 days, with the soonest date.
- Act now: each sold-out or within-30-days product with its ASIN, ready, sells a day (with dollars), on the way, and days left with the date.
- Coming up: the same for products running out in 31 to 90 days.
- Where it is: units in each of the nine buckets with its share of the total.
- Shipments to Amazon: by stage, with units still owed, and any units Amazon no longer expects.

Never:
- Never create shipments, place orders or open cases. A person does that.
- Never count stock moving between warehouses as ready to sell. It lands later, and the gap before it lands is lost sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: inventory-daily-stock-report". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This one runs on the Synthesis server (every morning, early Pacific time, from our server). Do not set up a repeat yourself; read the latest copy instead.
