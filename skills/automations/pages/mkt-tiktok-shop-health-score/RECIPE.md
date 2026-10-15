# Protect your TikTok Shop score

Channel: TikTok Shop · Level: On a schedule · Status: Ready now
Schedule: weekly Monday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Protect your TikTok Shop score" (id: mkt-tiktok-shop-health-score, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
TikTok scores every shop on a rolling 90 days. Fall below 3.5 and TikTok limits what you can do. This checks the score weekly and names the metric dragging it.

What to read: TikTok's Shop Performance Score and every metric behind it with TikTok's own thresholds
What to give me: A weekly warning before your shop score nears the level where TikTok restricts the shop, and what's pulling it down

Synthesis tools to use:
- `tiktok_metric metric=shop_performance months=3`
- `tiktok_metric metric=shop_returns months=3 limit=10`

Steps:
1. Call `tiktok_metric metric=shop_performance months=3`. Read the latest score and the metrics listed below excellent.
2. If returns or refunds are among them, call `tiktok_metric metric=shop_returns months=3 limit=10` for the top reasons.
3. Report the score, its direction, and the one metric to fix with TikTok's threshold beside it.

Checks before answering:
- The score is rolling 90 days. A fix today shows slowly. Say so.
- The score series starts the day the shop was connected. Say if history is short.
- If the score is missing, check the connection before saying all is well.

Output:
- One line: score, change, and distance to 3.5.
- A table only of metrics below excellent: metric, your value, TikTok's threshold, status.

Never:
- Never change shop settings.
- Never stay silent when the score is missing. Say it could not be read.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-tiktok-shop-health-score". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
