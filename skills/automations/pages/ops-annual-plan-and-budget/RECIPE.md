# Build next year's budget

Channel: Money · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build next year's budget" (id: ops-annual-plan-and-budget, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds next year's budget starting from what actually happened, not a blank sheet. It shapes each month by your own seasonality, carries each cost category forward from its run rate, and puts every growth assumption on a line the founder can change.

What to read: Twelve months of closed P&L, operating cost by category, monthly seasonality and channel revenue
What to give me: A month-by-month budget built from your real numbers, every assumption on its own line

Synthesis tools to use:
- `cost_rules for=ops-annual-plan-and-budget`
- `netsuite_metric metric=pnl_trend months=13`
- `netsuite_metric metric=opex_category months=12 limit=20`
- `amazon_metric metric=seasonality`
- `metric_timeseries metric_keys=[revenue] start_month=YYYY-MM end_month=YYYY-MM`
- `run_monte_carlo`
- `export_xlsx filename=annual-plan.xlsx`

Steps:
1. Call `netsuite_metric metric=pnl_trend months=13` for revenue, gross margin, operating cost and EBITDA. Use closed months for margin and profit; revenue can use every full month.
2. Call `netsuite_metric metric=opex_category months=12 limit=20` and divide by 12 for each category's monthly base.
3. Call `amazon_metric metric=seasonality` for each calendar month's index, and `metric_timeseries metric_keys=["revenue"]` for the last 24 months to check the shape on more than one year.
4. Ask for the growth assumptions per channel, planned price changes, launches and hires. Do not invent them.
5. Build each month: base revenue times seasonal index times growth, margin from closed months, costs from run rate plus planned changes.
6. Run `run_monte_carlo monthly_revenue=<base> growth_rate=<rate> growth_sigma=<spread> cogs_pct=<cost_share> months=12` for a range around the base case. Pass the spread explicitly; never take the default.
7. Write it with `export_xlsx filename=annual-plan.xlsx`: tabs for Summary, Monthly P&L, Cost categories, Assumptions, Range.

Checks before answering:
- Margin must come from closed months. An estimate month's margin can be several points off.
- Seasonality from one year is one data point per month. Say how many years shaped it.
- Every growth number is the founder's, not ours. Label each with its owner.
- If the ledger is not connected, build revenue only and say costs need the books.

Output:
- Spreadsheet with five tabs as above.
- In chat: base-case revenue, margin and EBITDA, the range, and the two assumptions that move it most.

Never:
- Never present the plan as a forecast. It is a target built on stated assumptions.
- Never use a default volatility in the range.
- Never write the plan into a connected sheet or accounting system.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-annual-plan-and-budget". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
