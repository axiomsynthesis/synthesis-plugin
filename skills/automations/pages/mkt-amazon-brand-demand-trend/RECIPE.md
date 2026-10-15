# Are more people searching your brand?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are more people searching your brand?" (id: mkt-amazon-brand-demand-trend, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Branded searches are the cleanest sign that marketing outside Amazon is building the brand. This tracks them over time and checks you still win them.

What to read: Searches for your brand name on Amazon over time, and your share of the purchases on them
What to give me: Whether searches for your brand are growing, flat or fading, month by month, with the season taken out

Synthesis tools to use:
- `amazon_metric metric=search_query_trend grain=month periods=17`
- `amazon_metric metric=seasonality month=0`
- `amazon_metric metric=ppc_branded_split days=90`

Steps:
1. Call `amazon_metric metric=search_query_trend grain=month periods=17`. Use the branded series.
2. Call `amazon_metric metric=seasonality month=0` and divide each month's searches by its season index before calling a trend.
3. Compare your purchase share on branded searches over time. A falling share means rivals are taking your own buyers.
4. Call `amazon_metric metric=ppc_branded_split days=90` for what you spend to hold your name.

Checks before answering:
- Never sum weekly figures into a month. Use the monthly grain.
- Shares are percentages. Never rescale.
- Event months (big sale months) spike. Name them and do not call them growth.
- If branded searches are empty, check which terms count as branded before reporting none.

Output:
- One line: brand demand growing, flat or fading, and your share of it.
- A table: month, branded searches, season-adjusted change, your purchase share.

Never:
- Never mix branded and non-branded into one trend.
- Never call an event month a trend.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-brand-demand-trend". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
