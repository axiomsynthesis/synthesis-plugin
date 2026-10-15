# Clear slow stock before it costs you

Channel: Inventory · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Clear slow stock before it costs you" (id: inventory-slow-stock-clearance-plan, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds products sitting too long in Amazon warehouses and picks the cheapest way to move each one: a deal, a bundle, or a removal.

What to read: Stock age, storage fees, sales speed
What to give me: Products sitting too long at Amazon, and the cheapest way to move each: a deal, a bundle or a removal

Synthesis tools to use:
- `amazon_metric metric=days_of_cover`
- `amazon_metric metric=inventory_position`
- `amazon_metric metric=storage_fee_forecast`
- `amazon_metric metric=promotion_performance`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=days_of_cover` and `limit=50` and keep products over 120 days.
2. Call `amazon_metric` with `metric=inventory_position` for units and age by product.
3. Call `amazon_metric` with `metric=storage_fee_forecast` and `limit=50` to price each product's storage next month and the fee it could avoid.
4. Call `amazon_metric` with `metric=promotion_performance` and `months=6` to see how past deals moved each product.
5. Name each with `find_product` and pick deal, bundle or removal by which costs least.

Checks before answering:
- If the stock read fails, say so. Never call an empty list "no slow stock".
- A product with a new launch or a big sale coming is not slow. Check before flagging.
- Base deal effects on past deals. If there are none, say the effect is a guess.

Output:
- One line first: dollars tied up in slow stock and storage cost a month.
- A table: product, days of cover, units, storage a month, action, expected clear date.

Never:
- Never create a deal, coupon or removal order. A person does that.
- Never guess a unit count or a fee.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: inventory-slow-stock-clearance-plan". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
