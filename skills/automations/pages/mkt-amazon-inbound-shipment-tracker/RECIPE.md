# Where's my shipment?

Channel: Inventory · Level: On a schedule · Status: Ready now
Schedule: weekly Monday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where's my shipment?" (id: mkt-amazon-inbound-shipment-tracker, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Stock sent to Amazon can sit in receiving for weeks or arrive short. This lists each open shipment, how much has been checked in, and which products run out while it waits.

What to read: Each open shipment you sent to Amazon, units sent against units received, its status and destination, stock cover for the products in it, and closed shipments that came in short
What to give me: Shipments still landing or short at Amazon, the units still owed, what sells out before they arrive, and likely refunds

Synthesis tools to use:
- `amazon_metric metric=inbound_shipments limit=100`
- `amazon_metric metric=days_of_cover limit=40`
- `amazon_metric metric=inventory_position limit=60`
- `amazon_metric metric=closed_shipments limit=20`

Steps:
1. Call `amazon_metric metric=inbound_shipments limit=100` for every open shipment: status, destination, units sent, received and still owed, and the products on each.
2. Call `amazon_metric metric=days_of_cover limit=40`. For each product still owed on a shipment, compare its days of cover with how long the shipment has been open.
3. Call `amazon_metric metric=inventory_position limit=60` for the inbound buckets per product, to confirm the shipment list against Amazon's own count.
4. Call `amazon_metric metric=closed_shipments limit=20` for closed shipments that came in short, netted per shipping plan, with the same product's lost-inbound refunds beside each.

Checks before answering:
- Read `tie_out` first. If `ties` is false, say the shipment list does not match Amazon's inbound count and trust the count.
- Units Amazon no longer counts as arriving are worth checking in Seller Central. Never call them money owed.
- The shipment list is pulled once a day. Quote its pull time. Stock is Amazon's live count; quote Amazon's update time.
- A shipment's date comes from its default name. A renamed shipment has no date: say so, never guess one.
- Closed shipments are history. Their received units are already in the stock count: never add them to inbound or to stock. Quote the shortfall after netting, not shipment by shipment, and call a refund beside it a likely match, never proof.

Output:
- One line: shipments still being received or short, and the product most at risk.
- A table: shipment, status, destination, products, units sent, units received, units still owed, product cover, action.
- A table of closed shipping plans that came in short: plan date, product, sent, received, short, likely refund.

Never:
- Never open cases or claims with Amazon.
- Never name a shipment as late or short from totals alone.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-inbound-shipment-tracker". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
