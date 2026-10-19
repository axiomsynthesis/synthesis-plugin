# Is all my data fresh?

Channel: Data · Level: On a schedule · Status: Ready now
Schedule: every weekday 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is all my data fresh?" (id: data-health-check, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each morning it checks every connected source and last night's scheduled jobs. It lists anything late, skipped, short or broken, which answers lean on it, and the fix. If all is well it says so in one line.

What to read: All connectors
What to give me: Every source and last night's jobs checked for late data, skipped work and a short yesterday, with the fix

Synthesis tools to use:
- `data_freshness`
- `data_freshness_sweep stale_days=3`
- `query_series metric=orders grain=day`
- `query_series metric=net_revenue grain=day`
- `shopify_metric metric=daily_revenue days=28`
- `warehouse_freshness`

Steps:
1. Call `data_freshness` for the newest data date of each connected source, the website payments feed, and `last_night_jobs`, what each scheduled task did last night. Note any result that says complete=false or lists skipped checks.
2. Call `data_freshness_sweep` with `stale_days=3` for every built table, judged on its newest data date.
3. Volume check for yesterday, the last closed day. For Amazon call `query_series` with `metric=orders`, `grain="day"` and a start 29 days back, then again with `metric=net_revenue`. For the website call `shopify_metric` with `metric=daily_revenue` and `days=28`. Compare yesterday's orders and revenue with the median of the same weekday over the 4 weeks before. Flag a drop of more than 30%.
4. Only if the brand has a direct database connection, call `warehouse_freshness` for the last sync of each mirrored table and any error on the last run. If it says not configured, leave it out of the answer.
5. Merge all lists by source, one line per source. For each problem, say which kinds of answers read it, such as win-back lists, profit or ad returns, and since when. Rank by that channel's revenue over the last 28 days from step 3, biggest first.
6. Give each problem its fix: reconnect, wait for a delayed sync, or tell us.

Checks before answering:
- If any result says complete=false, lists skipped checks, or a call failed or timed out, the headline is "Check incomplete: N checks did not run". List each one. Never say all current on an incomplete run.
- A task in `last_night_jobs` that failed or was cut for time is a problem, even if its tables look fresh. Say when it last succeeded. A status of `not_recorded`, `out_of_date`, `did_not_finish` or `unreadable` means you do not know if it ran. It is not a pass.
- FROZEN_SOURCE means a table was rebuilt but the data inside stopped. FROZEN_SOURCE, EMPTY and ERROR are problems. NOT_CONNECTED is not. Weekly and monthly tables get longer limits.
- Sources in the sweep's `errors` or `sources_unchecked` were not read. Never count them as healthy.
- If the website payments feed says it never landed, say the Profit page has no card fees for that store yet.
- The website daily read ends on its newest day held. If that day is not yesterday, the website is behind. Report it as late, not as a quiet day.
- A drop over 30% on yesterday is "possibly a partial day", not "broken". Same-day data keeps arriving for a day or more.
- A source with no sales for days may just be quiet. Check its newest record before calling it broken. A status of `quiet` has already been checked against the source.
- This check cannot yet tie yesterday's orders and revenue back to the source. Say so when it matters.

Output:
- One line first: all current, how many problems, or "Check incomplete: N checks did not run". Count skipped or failed jobs as problems.
- Then the jobs line, if any task failed or was not run: each task in plain words and when it last succeeded.
- A short list, biggest channel first: source, last good date, days behind, fix.
- Yesterday's volume: any channel more than 30% under its normal weekday, with both numbers.
- Not checked: every check that did not run, and every source the sweep could not read.

Never:
- Never reconnect or change a connection. A person does that.
- Never rerun or reschedule a job. A person does that.
- Never hide a stale source because the rest look fine.
- Never say all current when any check did not run.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: data-health-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every weekday 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
