# Your Amazon dashboard

Channel: Dashboards · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Your Amazon dashboard" (id: dashboards-amazon-dashboard, Dashboards).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds one Amazon page with sales, profit after fees, ad cost, stock and search share. It flags anything that needs you, like a product about to run out.

What to read: All Amazon data
What to give me: One page with sales, profit after fees, ad cost, stock and search share, flagging anything that needs you

Synthesis tools to use:
- `amazon_metric metric=pnl`
- `amazon_metric metric=acos_tacos`
- `amazon_metric metric=days_of_cover`
- `amazon_metric metric=search_query_performance`
- `emit_chart`

Steps:
1. Call `amazon_metric` with `metric=pnl` for the last closed month and the month so far, for sales and profit after fees.
2. Call `amazon_metric` with `metric=acos_tacos` for ad cost as a share of sales this month, then again with `month=` set to last month. This read is monthly only.
3. Call `amazon_metric` with `metric=days_of_cover` and `limit=20` for stock cover by product.
4. Call `amazon_metric` with `metric=search_query_performance` with `grain=week` and `periods=8` for search share.
5. Call `emit_chart` once per trend tile, then write the page as amazon-dashboard.html. If you can save files here, save it and tell me its name. If not, show it in full.

Checks before answering:
- A tile with a failed read shows "could not read", never a zero.
- Mark the current week as in progress. Trend lines stop at the last closed day.
- Stock flags are per product. Never average cover across products.

Output:
- One HTML page, amazon-dashboard.html: five tiles across the top, trend charts below, a short list of flags.

Never:
- Never change anything in Seller Central from the page.
- Never fill a missing tile with a guess.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: dashboards-amazon-dashboard". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
