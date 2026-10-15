# How hard can you bid on each product?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How hard can you bid on each product?" (id: mkt-amazon-breakeven-acos-by-product, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Sets a ceiling on ad cost for each product. A product people rebuy can afford more than its first sale suggests. A one-time product cannot.
It compares today's ad cost with that ceiling, so you know which products are overbid.

What to read: Each product's settled price, Amazon fees, product cost and repeat buying over 1, 3, 6 and 12 months
What to give me: The highest ad cost each product can carry and still make money, on the first order and over a customer's life

Synthesis tools to use:
- `amazon_metric metric=breakeven_acos_ltv months=12 limit=30`
- `breakeven_roas`
- `amazon_metric metric=ppc_spend_by_parent days=30 limit=30`

Steps:
1. Call `amazon_metric metric=breakeven_acos_ltv months=12 limit=30` for the whole catalogue.
2. For any product the person names, call `breakeven_roas asin=<product id>` to show the single-order math line by line.
3. Call `amazon_metric metric=ppc_spend_by_parent days=30 limit=30` for today's ad cost share per parent product. Compare at parent level, because a click on one size is often credited to another.
4. Rank products by the gap between today's ad cost and the ceiling. Use the first-order ceiling for one-time products and the 3-month ceiling for products with proven repeat buying. Say which.

Checks before answering:
- A product without an entered cost has no ceiling. Flag it. Never assume a cost.
- Lifetime ceilings need old enough customers. If a product launched under 6 months ago, show only first-order and 3-month figures.
- Fees come from closed settlement months only. If the newest month is still open, say the ceiling uses the month before.
- If every product shows the same ceiling, the cost data is probably a placeholder. Stop and say so.

Output:
- A table: product, first-order ceiling, 3-month ceiling, today's ad cost share, verdict (room to push, on target, overbid).
- Two lines on the biggest overbid and its monthly cost in dollars.

Never:
- Never treat a lifetime ceiling as safe for a product with no proven repeat buying.
- Never change bids. This is advice.
- Never fill a missing cost with an average.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-breakeven-acos-by-product". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
