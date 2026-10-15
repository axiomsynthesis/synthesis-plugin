# Is your Amazon affiliate program paying?

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is your Amazon affiliate program paying?" (id: mkt-amazon-affiliate-program-return, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Measures the Amazon affiliate program as a cost of sale. It shows the program's cost per dollar, who earns it, and who is dead weight.

What to read: Commissions paid, Amazon sales and conversion per creator in your Amazon affiliate program, by month
What to give me: What the program costs per dollar of sales, which creators earn their commission, and the rate to pay

Synthesis tools to use:
- `levanta_metric metric=commission_economics months=6`
- `levanta_metric metric=top_creators months=6 limit=30`
- `levanta_metric metric=funnel months=6`
- `levanta_metric metric=data_freshness`

Steps:
1. Call `levanta_metric metric=data_freshness`. If the data is stale, say so first.
2. Call `levanta_metric metric=commission_economics months=6` for commission paid against sales.
3. Call `levanta_metric metric=top_creators months=6 limit=30` to rank creators.
4. Call `levanta_metric metric=funnel months=6` for clicks to orders.
5. Group creators: earning (sales per dollar of commission above the program average), weak, inactive (no sales in 90 days).

Checks before answering:
- This works only for brands with an Amazon affiliate platform connected. Say so if empty.
- Small gaps between platform and Amazon numbers are normal. Do not treat them as errors unless large.
- Recent weeks are still settling. Prefer closed months.

Output:
- One line: cost per dollar of sales and the share driven by the top creators.
- A table: creator, clicks, orders, sales, commission, sales per $1 commission, group.

Never:
- Never change rates or remove creators in the platform.
- Never treat program sales as fully extra to what Amazon would have sold.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-affiliate-program-return". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
