# Plan your year around the peaks

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Plan your year around the peaks" (id: growth-seasonal-plan, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads your sales history to find the peaks and dips in your year, then lays out a month-by-month plan for stock, ads and promos. It tells you when to start each ramp.

What to read: Sales history
What to give me: Your peak and slow months, and a month-by-month plan for stock, ads and promos

Synthesis tools to use:
- `amazon_metric metric=seasonality`
- `shopify_metric metric=seasonality`
- `metric_timeseries`
- `amazon_metric metric=days_of_cover`
- `export_xlsx`

Steps:
1. Call `amazon_metric` with `metric=seasonality` and `shopify_metric` with `metric=seasonality` for each month's index against the average. Each uses all the history the brand has loaded, so say how many years that is.
2. Call `metric_timeseries` with `metric_keys="revenue"` for the last 24 closed months, to check the pattern repeats each year.
3. Call `amazon_metric` with `metric=days_of_cover` to see how much stock you hold going into the next peak.
4. Set ramp dates: stock lead time plus a buffer before each peak, ads about six weeks before. No lead time known: ask for it, with the sales a late order would miss at the peak.
5. Save the plan with `export_xlsx`, `filename="seasonal-plan.xlsx"`.

Checks before answering:
- A peak counts only if it shows in at least two years.
- Deal events like Prime Day move by date. Mark them apart from true season.
- If history is under 2 years, say the pattern is not proven yet.

Output:
- One line first: your peak months and when to start the first ramp.
- A table by month: index, stock action, ad action, promo action.
- File: seasonal-plan.xlsx.

Never:
- Never place a stock order or change an ad budget. A person does that.
- Never guess a month that has no history.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Inputs only I know: supplier lead time in days. If the tools lack one, ask me ONE plain question for it, all in one message: why it matters and about how many dollars it moves. Use my answer for this run. Never invent one. If I do not know, say what the answer leaves out. Nothing saves the lead time yet: say it was used for this run only. On a scheduled run, name what is missing instead.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: growth-seasonal-plan". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
