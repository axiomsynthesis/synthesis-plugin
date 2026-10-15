# Fix broken pack-size pricing

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Fix broken pack-size pricing" (id: mkt-amazon-pack-size-ladder, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shoppers compare price per unit across sizes. A ladder that does not reward buying more pushes them to the smallest pack.
This checks every step in each family and flags broken ones.

What to read: Price per unit and profit per unit for each pack size in a product family, and how sales split across sizes
What to give me: Spots where a bigger pack costs more per unit than a smaller one, or saves too little to move shoppers up

Synthesis tools to use:
- `find_product`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=pnl_by_asin limit=60`
- `shelf_history marketplace=amazon days=30`

Steps:
1. Call `find_product query=<family name>` to list every pack size. Never group sizes by name alone.
2. Call `amazon_metric metric=pnl_by_asin limit=60` for each size's realized price and units.
3. Divide price by count for price per unit. Each larger size should save at least 5% per unit over the size below it.
4. Call `amazon_metric metric=contribution_by_asin months=3` to make sure any suggested cut still makes money.
5. For the current listed price, call `shelf_history marketplace=amazon days=30 asin=<product id>`.

Checks before answering:
- Realized price includes discounts. Listed price does not. Say which one the ladder uses.
- If the brand has not set up product families, say so and stop. Never group sizes by name.
- Missing product cost means the cut cannot be checked. Say so.

Output:
- One line per family: ladder healthy or the broken step.
- A table: size, count, price, price per unit, saving against the size below, share of family units, profit per unit.

Never:
- Never change prices.
- Never match products by name.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-pack-size-ladder". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
