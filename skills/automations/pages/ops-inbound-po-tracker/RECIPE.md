# Factory orders vs sell-out dates

Channel: Inventory · Level: On a schedule · Status: Ready now
Schedule: weekly Monday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Factory orders vs sell-out dates" (id: ops-inbound-po-tracker, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lines up every purchase order on its way against the date each product runs out. It catches the order that will arrive too late while there is still time to expedite, split or slow sales.

What to read: Entered purchase orders and shipments, Amazon inbound stock and stock cover per product
What to give me: Every open purchase order, and whether it lands before that product runs out

Synthesis tools to use:
- `operator_inputs section=purchase_orders`
- `operator_inputs section=shipments`
- `amazon_metric metric=days_of_cover limit=100`

Steps:
1. Call `operator_inputs section=purchase_orders` and `operator_inputs section=shipments` for open orders, units, expected dates and status.
2. Call `amazon_metric metric=days_of_cover limit=100` for sellable, inbound and reserved units, daily pace and the projected stockout date per product.
3. For each open order, compare its expected arrival (plus receiving time at Amazon, which the person should give) with the stockout date.
4. Flag LATE when arrival is after stockout, and TIGHT when it is within 7 days.
5. Days out of stock times daily sales gives the sales at risk.

Checks before answering:
- An empty section means nothing entered, not zero orders. Say "no orders entered".
- Units already inbound at Amazon are not on this order. Do not count them twice.
- A failed stock read is not zero stock. Stop and say so.
- Receiving at Amazon can take days to weeks. Use the person's figure or flag the date as optimistic.

Output:
- Table: Order | Product | Units | Expected arrival | Stockout date | Gap in days | Sales at risk | Flag.
- One line for each LATE order with the suggested move.

Never:
- Never change, expedite or cancel an order.
- Never invent arrival dates or receiving times.
- Never contact a supplier or forwarder.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-inbound-po-tracker". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
