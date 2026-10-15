# Is it the market or is it you?

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is it the market or is it you?" (id: grw-category-demand-trend, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Sets Google search interest for your category, your brand and two rivals beside your own monthly sales. It tells you whether a good or bad stretch came from the market moving or from your share of it.

What to read: Google search interest for your category, your brand and two rivals
What to give me: Whether your growth or slump comes from the whole category or from you

Synthesis tools to use:
- `google_trends keyword=<category> comparison_keywords=<brand,rivals>`
- `query_series metric=net_revenue grain=month`
- `shopify_metric metric=monthly_revenue months=24`

Steps:
1. Ask for the category term and two rival names if not known.
2. Run `google_trends` with the category term and comparison keywords over five years.
3. Pull `query_series metric=net_revenue grain=month` and `shopify_metric metric=monthly_revenue months=24`.
4. Index each to 100 at the same month a year ago and compare the year-on-year change.

Checks before answering:
- Google Trends is relative interest from 0 to 100, not search volume. Never call it volume.
- Use closed months only.

Output:
- Answer first. A short table by quarter: category interest change, brand interest change, your sales change. A line chart via `emit_chart` when asked.

Never:
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-category-demand-trend". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
