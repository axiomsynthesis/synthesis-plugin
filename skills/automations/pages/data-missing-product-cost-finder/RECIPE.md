# Fill in missing product costs

Channel: Data · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Fill in missing product costs" (id: data-missing-product-cost-finder, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds every product that sells but has no product cost entered, and ranks them by sales so you fill in the ones that matter first. It hands you a file to fill in.

What to read: Catalog, costs
What to give me: Every selling product with no cost entered, ranked by sales, in a file to fill in

Synthesis tools to use:
- `operator_inputs section=cogs`
- `amazon_metric metric=pnl_by_asin`
- `top_products`
- `shopify_metric metric=top_products limit=50`
- `find_product`
- `export_xlsx`

Steps:
1. Call `operator_inputs` with `section="cogs"` for every product cost entered today.
2. Call `amazon_metric` with `metric=pnl_by_asin` for the last closed month to see which products sell and which have no cost.
3. Call `top_products` with `metric="revenue"`, the last 3 closed months and `top_n=50` to rank Amazon products by sales. It reads Amazon only. Call `shopify_metric metric=top_products limit=50` for website products. That read covers all time, so rank the two channels separately and never add them. Store and Walmart products are not covered. Say so.
4. Use `find_product` to name each product the way the brand does.
5. Save the list with `export_xlsx`, `filename="missing-product-costs.xlsx"`, with an empty cost column. A person fills it in and enters it on the Operator inputs page.

Checks before answering:
- A cost of zero and a missing cost are different. Treat a zero as missing unless the owner set it.
- If the cost read fails, say so. Never report "all costs entered" from an empty read.
- Show the share of sales without a cost, so the size of the gap is clear.

Output:
- One line first: how many products lack a cost and what share of sales they are.
- A table: product, sales last 3 months, share of sales, cost (empty), notes.
- File: missing-product-costs.xlsx.

Never:
- Never guess or fill in a cost. The owner enters it.
- Never show profit for a product with no cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: data-missing-product-cost-finder". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
