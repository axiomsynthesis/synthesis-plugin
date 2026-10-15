# Are we really growing?

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are we really growing?" (id: ops-seasonally-adjusted-growth, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Takes the season out of the numbers so a normal holiday lift is not read as growth and a normal summer dip is not read as decline. It gives one honest answer to "are we growing" and names the months that broke pattern.

What to read: Monthly revenue history, monthly seasonality and known event months
What to give me: Growth with the season and big sale events taken out, and whether the trend is up, flat or down

Synthesis tools to use:
- `metric_timeseries metric_keys=[revenue] start_month=YYYY-MM end_month=YYYY-MM`
- `amazon_metric metric=seasonality`
- `analyze_trend metric=revenue start_month=YYYY-MM end_month=YYYY-MM`
- `explain_metric_move metric=revenue month=YYYY-MM`

Steps:
1. Call `metric_timeseries metric_keys=["revenue"]` for the last 24 full months.
2. Call `amazon_metric metric=seasonality` for each calendar month's index.
3. Divide each month by its index to get the adjusted series.
4. Call `analyze_trend metric=revenue` over the window for the trend verdict and the event months it marks.
5. For the latest month, call `explain_metric_move metric=revenue month=YYYY-MM` to rule causes in or out.
6. Report adjusted growth over 3, 6 and 12 months.

Checks before answering:
- An index built from one year is thin. Say how many years built it.
- Prime Day and similar months must be marked as events, not trend.
- Leave out the running month.
- Revenue here is Amazon plus website. Say so.

Output:
- Table: Month | Revenue | Seasonal index | Adjusted revenue | Adjusted change.
- Two lines: the trend verdict, and the one month that broke pattern with its likely cause.

Never:
- Never call a seasonal lift growth.
- Never quote an adjusted figure without saying it is adjusted.
- Never mix company-wide ledger revenue into this series.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-seasonally-adjusted-growth". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
