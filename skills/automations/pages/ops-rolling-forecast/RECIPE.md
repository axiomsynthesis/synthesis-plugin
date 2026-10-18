# Six-month sales forecast, refreshed

Channel: Money · Level: On a schedule · Status: Ready now
Schedule: monthly, 3rd business day 9am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Six-month sales forecast, refreshed" (id: ops-rolling-forecast, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each month, rolls the revenue forecast forward six months from the latest closed month. It shows a range, not a single number, and records the forecast so next month can say how close it came.

What to read: Monthly revenue history, this month's pace, seasonality and the growth trend
What to give me: A six-month revenue forecast with a range, and how it changed from last month's

Synthesis tools to use:
- `cost_rules for=ops-rolling-forecast`
- `metric_timeseries metric_keys=[revenue] start_month=YYYY-MM end_month=YYYY-MM`
- `monthly_projection`
- `amazon_metric metric=seasonality`
- `analyze_trend metric=revenue start_month=YYYY-MM end_month=YYYY-MM`
- `run_monte_carlo`
- `register_prediction`

Steps:
1. Call `metric_timeseries metric_keys=["revenue"]` for the last 24 full months.
2. Call `analyze_trend metric=revenue` over the same window for the underlying trend with event months marked.
3. Call `amazon_metric metric=seasonality` for each calendar month's index.
4. Call `monthly_projection` for the running month's likely finish.
5. Run `run_monte_carlo monthly_revenue=<deseasonalised_base> growth_rate=<trend> growth_sigma=<measured_spread> months=6`. Measure the spread from the history; never take the default.
6. Re-apply seasonality to each month of the range.
7. Compare with last month's version if one was recorded. Explain the change in one line.
8. Record the six-month total with `register_prediction` so it can be scored.

Checks before answering:
- The fan from the simulation is a horizon total. Do not call it an annual figure.
- Event months (Prime Day, Black Friday) inflate a trend. Make sure the trend read marks them.
- The revenue here is Amazon plus website. Say so, and say retail is not in it unless added.
- If the history is shorter than 13 months, seasonality is not measured. Say so and widen the range.

Output:
- Table: Month | Low | Likely | High | Last version's likely.
- Three lines: the six-month total and range, the change since last version and why, and the month with the widest range.

Never:
- Never present the likely figure without its range.
- Never use default volatility.
- Never overwrite last month's recorded forecast.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-rolling-forecast". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (monthly, 3rd business day 9am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
