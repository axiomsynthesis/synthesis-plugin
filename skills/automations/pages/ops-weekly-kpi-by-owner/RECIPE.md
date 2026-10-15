# Weekly KPIs, with who owns each

Channel: Leadership · Level: On a schedule · Status: Ready now
Schedule: weekly Monday 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Weekly KPIs, with who owns each" (id: ops-weekly-kpi-by-owner, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs the weekly KPI review the way a leadership team does it: each number has one owner, a target and a status. The owners and targets come from your sheet; the values come from measured data, so nobody grades their own homework.

What to read: Your KPI list with owners and targets from a Google Sheet, and the measured value of each KPI
What to give me: Every KPI with its owner, this week's value, target, trend and status

Synthesis tools to use:
- `gsheets_metric metric=profile table=<kpi_tab>`
- `gsheets_metric metric=breakdown table=<kpi_tab> dimension_column=<kpi> value_column=<target>`
- `query_series metric=<metric> grain=week`
- `meta_metric metric=weekly_trend weeks=8`
- `amazon_metric metric=ppc_week_over_week`
- `metric_health_band`
- `export_xlsx filename=weekly-kpis.xlsx`

Steps:
1. Call `gsheets_metric metric=profile table=<kpi_tab>` to confirm the KPI, owner and target columns.
2. Call `gsheets_metric metric=breakdown` to read each KPI's target.
3. Map each KPI to a measured source. Sales, units, conversion: `query_series metric=<metric> grain=week`. Meta: `meta_metric metric=weekly_trend weeks=8`. Amazon ads: `amazon_metric metric=ppc_week_over_week`. Stock: `amazon_metric metric=days_of_cover`.
4. For each KPI read this week, last week and the 4-week average.
5. Run `metric_health_band` with the target as the healthy line and the person's warning line.
6. Write it with `export_xlsx filename=weekly-kpis.xlsx` and post the summary in chat.

Checks before answering:
- A KPI with no measured source is shown as "typed by owner", never mixed in as measured.
- The latest week may still be settling for ad-credited sales. Mark it.
- A KPI whose definition in the sheet differs from the measured one gets a note, not a silent swap.
- Never show people's contact details from the sheet. Owner names or roles only.

Output:
- Table: KPI | Owner | This week | Last week | 4-week average | Target | Status.
- Three lines: what is off target and who owns it.

Never:
- Never write values back to the sheet.
- Never set or change a target.
- Never send the table to anyone.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-weekly-kpi-by-owner". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
