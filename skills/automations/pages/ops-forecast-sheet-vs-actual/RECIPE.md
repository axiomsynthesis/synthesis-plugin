# How good is your forecast sheet?

Channel: Google Sheets · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How good is your forecast sheet?" (id: ops-forecast-sheet-vs-actual, Google Sheets).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Scores the team's own forecast against what happened. A forecast that is always high leads to overstock and cash tied up; one that is always low leads to stockouts. Knowing the lean is worth more than any single month's accuracy.

What to read: The monthly forecast in your Google Sheet and measured revenue and units for the same months
What to give me: How accurate your own forecast has been, month by month and product by product, and which way it leans

Synthesis tools to use:
- `gsheets_metric metric=profile table=<table>`
- `gsheets_metric metric=breakdown table=<table> dimension_column=<col> value_column=<col>`
- `gsheets_metric metric=trend table=<table> date_column=<col> value_column=<col> grain=month`
- `query_series metric=units grain=month asin=<asin>`
- `metric_timeseries metric_keys=[revenue] start_month=YYYY-MM end_month=YYYY-MM`

Steps:
1. Call `gsheets_metric metric=profile table=<table>` on the forecast tab to find the month, product and value columns.
2. Call `gsheets_metric metric=trend` for the forecast total by month, and `gsheets_metric metric=breakdown` by product if the tab has a product column.
3. Pull actuals: `metric_timeseries metric_keys=["revenue"]` for totals and `query_series metric=units grain=month asin=<asin>` per product.
4. For each closed month compute error = (forecast minus actual) divided by actual.
5. Report the average error, the average absolute error, and how often it ran high.
6. Name the products with the biggest misses and what was special about those months.

Checks before answering:
- Compare closed months only.
- Make sure the forecast and the actual share a definition (revenue before or after promos, which channels).
- Forecast rows typed after the month began are not forecasts. Ask when the sheet was locked, if versions are kept.
- Fewer than six months is too few to call a lean.

Output:
- Table: Month | Forecast | Actual | Error.
- Product table for the top five misses.
- Two lines: the lean and the one change to the forecasting method.

Never:
- Never edit the forecast sheet.
- Never judge a month that has not closed.
- Never blame a person.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-forecast-sheet-vs-actual". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
