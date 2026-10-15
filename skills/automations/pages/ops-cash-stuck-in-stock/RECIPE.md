# Free up cash stuck in stock

Channel: Inventory · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Free up cash stuck in stock" (id: ops-cash-stuck-in-stock, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Values the stock you hold beyond a sensible cover target, so overstock reads as a cash number. It covers stock at Amazon and in your own or a third-party warehouse, so a pile in one place is not missed because the other looks lean.

What to read: Amazon stock cover by product, warehouse stock value by location, and product cost
What to give me: Dollars tied up in stock beyond what you need, by product and location

Synthesis tools to use:
- `amazon_metric metric=days_of_cover limit=100`
- `netsuite_metric metric=inventory_position limit=100`
- `operator_inputs section=cogs`

Steps:
1. Ask for the cover target in days. Default to 90 and say so.
2. Call `amazon_metric metric=days_of_cover limit=100` for sellable units, daily sales pace and status per product.
3. Call `netsuite_metric metric=inventory_position limit=100` for units and value by product and location outside Amazon, if the ledger is connected.
4. Call `operator_inputs section=cogs` for cost per unit where the ledger value is missing.
5. Excess units = units on hand minus (daily pace times target days), across all locations, never below zero. Excess value = excess units times cost per unit.
6. Rank products by excess value. Show months to sell through at today's pace.

Checks before answering:
- A days-of-supply of 999 is a no-sales marker, not three years. Treat those products as dead stock and value them in full.
- Stock moving between Amazon warehouses is not extra stock. Do not add it twice.
- A product with no cost cannot be valued. List it separately.
- Do not double count units that appear in both the ledger's Amazon location and Amazon's own count. Use one source per location and say which.

Output:
- Table: Product | Units on hand (all locations) | Days of cover | Excess units | Excess value | Months to sell through.
- Top line: total excess value and the two products holding most of it.

Never:
- Never create a removal, liquidation or price cut. A person decides, and removed stock cannot come back.
- Never value stock at selling price.
- Never treat a failed stock read as zero stock.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-cash-stuck-in-stock". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
