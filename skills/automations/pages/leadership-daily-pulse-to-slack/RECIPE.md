# Yesterday's sales in three lines on Slack

Channel: Leadership · Level: On a schedule · Status: Ready after we build it
Schedule: every weekday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Yesterday's sales in three lines on Slack" (id: leadership-daily-pulse-to-slack, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each weekday morning it writes three lines: yesterday's sales, whether that was normal, and the one thing that looked odd. It is meant to be read in ten seconds.

What to read: All channels
What to give me: Yesterday's sales, whether that was normal, and the one odd thing, readable in ten seconds

Synthesis tools to use:
- `data_freshness`
- `query_series`
- `amazon_metric metric=daily_revenue`
- `shopify_metric metric=daily_revenue`
- `meta_metric metric=pacing_anomaly`

Steps:
1. Call `data_freshness` to confirm yesterday has landed for each source.
2. Call `query_series` with `metric=net_revenue`, `grain="day"` and the last 29 days, to compare yesterday with the same weekday over 4 weeks.
3. Call `amazon_metric` with `metric=daily_revenue` and `days=8`, and `shopify_metric` with `metric=daily_revenue` and `days=8`, to see which channel moved.
4. Call `meta_metric` with `metric=pacing_anomaly` and `days=2` to catch ads that stopped or overspent.
5. Write three lines: sales, normal or not, the one odd thing.

Checks before answering:
- Yesterday may still be filling in. Say so if a source has not finished the day.
- Normal means within the range of the last 4 same weekdays, not one day before.
- If a read fails, say that channel is missing. Never call it a zero day.

Output:
- Three lines, no more. Line 1: yesterday's sales. Line 2: normal or not. Line 3: the one odd thing, or "nothing odd".
- Posted to Slack once the connection is back; until then, in the chat.

Never:
- Never change budgets or pause ads. A person does that.
- Never post more than three lines.
- Never guess a number a tool did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: leadership-daily-pulse-to-slack". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every weekday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

Not fully ready yet (ready after we build it): Repeats by itself only in Claude Code on a computer that is on at that time. In the Claude app or website, run it by hand each time, or use a scheduled task if your Claude offers one. Posting to Slack needs the Slack connection turned back on; until then the three lines appear in the chat. Do the parts you can and say plainly what is missing.
