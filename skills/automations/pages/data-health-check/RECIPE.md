# Is all my data fresh?

Channel: Data · Level: On a schedule · Status: Ready now
Schedule: every weekday 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is all my data fresh?" (id: data-health-check, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each morning it checks every connected source for two things. Is the data current, and does yesterday look complete? It lists anything late, short or broken, which answers lean on it, and the fix. If all is well it says so in one line.

What to read: All connectors
What to give me: Every source checked for late data and a short yesterday, with the fix

Synthesis tools to use:
- `data_freshness`
- `data_freshness_sweep stale_days=3`
- `query_series metric=orders grain=day`
- `query_series metric=net_revenue grain=day`
- `shopify_metric metric=daily_revenue days=28`
- `warehouse_freshness`

Steps:
1. Call `data_freshness` for the newest data date of each connected source. Note any result that says complete=false or lists skipped checks.
2. Call `data_freshness_sweep` with `stale_days=3` for each built table and whether it is stale. Note any dataset that came back with no tables.
3. Volume check for yesterday, the last closed day. For Amazon call `query_series` with `metric=orders`, `grain="day"` and a start 29 days back, then again with `metric=net_revenue`. For the website call `shopify_metric` with `metric=daily_revenue` and `days=28`. Compare yesterday's orders and revenue with the median of the same weekday over the 4 weeks before. Flag a drop of more than 30%.
4. Only if the brand has a direct database connection, call `warehouse_freshness` for the last sync of each mirrored table and any error on the last run. If it says not configured, leave it out of the answer.
5. Merge all lists by source, one line per source. For each problem, say which kinds of answers read it, such as win-back lists, profit or ad returns, and since when. Rank by that channel's revenue over the last 28 days from step 3, biggest first.
6. Give each problem its fix: reconnect, wait for a delayed sync, or tell us.

Checks before answering:
- If any result says complete=false, lists skipped checks, or a call failed or timed out, the headline is "Check incomplete: N checks did not run". List each one. Never say all current on an incomplete run.
- Judge by the newest data date, not the time a table was written. The sweep's age is the last write time, so a rebuilt table can look fresh with old data.
- The sweep uses one flat age for every table. A table built weekly or monthly can show stale at 3 days and still be on time. Say so before calling it broken.
- A dataset the brand has connected that comes back with no tables is a failed read, not a healthy one. Say the sweep could not read it.
- The sweep only covers some datasets, and it skips empty tables. Say that ads, TikTok, Walmart, subscription, support and creator tables are not swept today.
- Backup copies and tables nothing reads may show as stale. Name them as likely leftovers, not as a broken feed.
- The website daily read ends on its newest day held. If that day is not yesterday, the website is behind. Report it as late, not as a quiet day.
- A drop over 30% on yesterday is "possibly a partial day", not "broken". Same-day data keeps arriving for a day or more.
- A source with no sales for days may just be quiet. Check its newest record before calling it broken.
- This check cannot yet tie yesterday's orders and revenue back to the source, or say which scheduled jobs ran or were skipped last night. Say so when a problem might come from either.

Output:
- One line first: all current, how many sources need attention, or "Check incomplete: N checks did not run".
- A short list, biggest channel first: source, last good date, days behind, fix.
- Yesterday's volume: any channel more than 30% under its normal weekday, with both numbers.
- Affected answers: which kinds of answers are reading old or short data, and since when.
- Not checked: every check that did not run, and every area the sweep does not cover.

Never:
- Never reconnect or change a connection. A person does that.
- Never hide a stale source because the rest look fine.
- Never say all current when any check did not run.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: data-health-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every weekday 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
