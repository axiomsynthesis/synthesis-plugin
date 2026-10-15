# Which products to cut, fix or back?

Channel: Inventory · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which products to cut, fix or back?" (id: ops-sku-rationalization, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Rates every product on revenue, margin, growth and strategic role, then sorts them into hero, keep, fix or cut. A long tail of slow products ties up cash and attention; this names them with numbers so the founder can decide.

What to read: Revenue, profit, growth and stock per product across Amazon and the website
What to give me: A hero, keep, fix or cut call for every product, each backed by a number

Synthesis tools to use:
- `amazon_metric metric=contribution_by_asin months=6`
- `amazon_metric metric=velocity_momentum`
- `amazon_metric metric=days_of_cover limit=100`
- `shopify_metric metric=top_products limit=50`
- `operator_inputs section=cogs`
- `score_sku_rationalization skus=[...]`

Steps:
1. Call `amazon_metric metric=contribution_by_asin months=6` for revenue, units and profit per product.
2. Call `amazon_metric metric=velocity_momentum` for growth over recent weeks.
3. Call `shopify_metric metric=top_products limit=50` for website revenue per product.
4. Call `amazon_metric metric=days_of_cover limit=100` for units on hand and inbound, and `operator_inputs section=cogs` for each product's entered unit cost. Stock value = units times entered cost. A product with no entered cost has no stock value. Say so, never show it as zero.
5. Turn each measure into a 1 to 5 rating by quintile across the catalogue. Strategic role is the founder's call; ask, or mark it unknown.
6. Run `score_sku_rationalization skus=[{name, rev, margin, growth, strategic}]` with all four ratings filled for every product.

Checks before answering:
- A rating left out becomes zero silently and pushes a product toward cut. Fill all four or mark the product unscored.
- A product with no cost has no margin rating. Mark it unscored, never low margin.
- Group pack sizes of one product before rating, or the small pack looks like a loser.
- A product that brings in first-time buyers may earn little itself. Check its role in new customer acquisition before calling it a cut.

Output:
- Table: Product | Revenue | Profit | Growth | Stock value | Ratings | Call.
- Three lines: heroes' share of profit, the cut list's revenue and stock value, and the first decision to make.

Never:
- Never delist, discontinue or remove stock. A cut call is a shortlist entry.
- Never rate a product on a guessed cost.
- Never present a call as final when any rating is missing.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-sku-rationalization". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
