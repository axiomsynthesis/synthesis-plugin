# Profit per pack size

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Profit per pack size" (id: ops-pack-size-price-ladder, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lines up every pack size of one product so the price per unit steps down sensibly as packs grow, and each step still earns you money. A broken ladder sends shoppers to the pack that earns you least.

What to read: Price, cost, fees and units for every pack size of a product on Amazon
What to give me: Price and profit per unit for each pack size, and any rung where a bigger pack is worse for you or the shopper

Synthesis tools to use:
- `find_product query=<product_name>`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=shelf_position`

Steps:
1. Call `find_product query=<product_name>` to get every pack size of the product, with its count of units.
2. Call `amazon_metric metric=contribution_by_asin months=3` and keep price, fees, product cost and units for each pack.
3. For each pack compute price per unit of content and profit per unit of content.
4. Flag any rung where a larger pack costs the shopper more per unit than a smaller one, and any rung where profit per unit falls by more than the price step.
5. Read the shelf with `amazon_metric metric=shelf_position` to see rivals' price per unit at the same counts.
6. Show each pack's share of units.

Checks before answering:
- Compare per unit of content, never per listing.
- A pack with no entered cost cannot be judged on profit. Say so.
- Fees differ by size tier. Use each pack's real fees, not a shared rate.
- Prices from a deal month distort the ladder. Use the regular price when a deal ran.

Output:
- Table: Pack | Price | Price per unit | Profit per unit | Share of units | Flag.
- Two lines: the broken rung, and the price change that fixes it with its monthly effect.

Never:
- Never change a price or listing.
- Never compare across different products as if they were pack sizes of one.
- Never guess a cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-pack-size-price-ladder". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
