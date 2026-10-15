# How much stock to send for the big sale

Channel: Inventory · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How much stock to send for the big sale" (id: inventory-big-sale-stock-plan, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Works out how much to send in for Prime Day or Black Friday, per product, and the date it has to ship by.

What to read: Last year's event, current speed
What to give me: Units to send per product for Prime Day or Black Friday, and the date each must ship by

Synthesis tools to use:
- `amazon_metric metric=seasonality`
- `amazon_metric metric=stockout_forecast horizon_days=180 limit=50`
- `amazon_metric metric=days_of_cover`
- `amazon_metric metric=restock_plan`

Steps:
1. Call `amazon_metric` with `metric=seasonality` to see how much last year's event lifted sales.
2. Call `amazon_metric metric=stockout_forecast horizon_days=180 limit=50` for each product's expected lift at the coming sale. Its events list gives the extra units and the times-normal figure from that product's own last three Amazon sales. Promotion code reads have no product or dates, so never use them for lift.
3. Call `amazon_metric` with `metric=days_of_cover` and `limit=50` for today's cover.
4. Call `amazon_metric` with `metric=restock_plan` for stock already on the way.
5. Units to send = event lift times today's speed, minus stock on hand and on the way. Ship-by date allows for Amazon check-in time.

Checks before answering:
- A product new since last year has no event history. Say its number is a guess.
- If last year's event data is missing, say so. Never assume a lift.
- Judge each product on its own.

Output:
- One line first: total units to send and the earliest ship-by date.
- A table: product, normal weekly units, expected lift, units to send, ship-by date.

Never:
- Never create a shipment. A person does that.
- Never guess a lift the data does not show.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: inventory-big-sale-stock-plan". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
