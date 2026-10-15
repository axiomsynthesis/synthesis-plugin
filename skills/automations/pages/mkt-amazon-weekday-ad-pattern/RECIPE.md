# Find your worst ad days of the week

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find your worst ad days of the week" (id: mkt-amazon-weekday-ad-pattern, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks whether some days of the week are reliably worse for ads. If so, it sizes what a day-based bid schedule would save and cost.

What to read: Sponsored Products results by day of the week over the last 90 days
What to give me: Whether some weekdays reliably earn less, and whether the gap is big enough to schedule budgets around

Synthesis tools to use:
- `amazon_metric metric=ppc_day_of_week days=90`

Steps:
1. Call `amazon_metric metric=ppc_day_of_week days=90`.
2. Read the flags for thin weekday samples and spreads too small to act on.
3. If the gap is real, estimate the effect of a 20% bid cut on the weak days: spend saved and sales likely lost, using that day's own return.

Checks before answering:
- This is day level. Never suggest hour-of-day scheduling from it. For hours, use `amazon_metric metric=ppc_hour_of_day` where hourly is switched on.
- A gap driven by one event week is not a pattern. Check it held across most weeks.
- If the tool says the spread is too small to act on, say "no change" and stop.

Output:
- One line: act or do not act.
- A table: weekday, spend, sales, return per $1, orders.
- If act: the suggested bid change by day and its monthly effect.

Never:
- Never set up bid schedules in the account.
- Never present hour-level advice from day-level data.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-weekday-ad-pattern". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
