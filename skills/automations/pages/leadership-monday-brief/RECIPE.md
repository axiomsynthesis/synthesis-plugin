# Your Monday one-pager

Channel: Leadership · Level: On a schedule · Status: Ready after we build it
Schedule: every Monday 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Your Monday one-pager" (id: leadership-monday-brief, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every Monday it reads the whole business and writes one page: last week's sales, one fire, one win and one decision for you. It checks every source is current before it says anything.

What to read: All channels
What to give me: Last week's sales, one fire, one win and one decision for you, by email every Monday

Synthesis tools to use:
- `data_freshness`
- `get_weekly_brief`
- `channel_revenue_mix`
- `query_series`
- `monthly_projection`
- `export_pdf`

Steps:
1. Call `data_freshness` to see how current each source is. Note anything more than 2 days old.
2. Call `get_weekly_brief` for the stored movers and attention items for last week.
3. Call `query_series` with `metric=net_revenue`, `grain="week"` and the last 8 closed weeks, to show last week against the weeks before.
4. Call `channel_revenue_mix` for the split across channels, and `monthly_projection` for where the month will land.
5. Pick one fire, one win and one decision. Save with `export_pdf`, `filename="monday-brief.pdf"`.

Checks before answering:
- Use the last closed week only. Sunday's numbers may still be filling in.
- If a source is stale, say so on the page before its numbers.
- If a read fails, say that number is missing. Never print a zero in its place.
- One week up or down is not a trend. Compare with the 8-week average.

Output:
- One page. First line: last week's sales and the change.
- Then: one fire, one win, one decision, each in one or two sentences with dollars.
- File: monday-brief.pdf from `export_pdf`, which works in any Claude. If you can save files here, save a copy too and tell me its name.

Never:
- Never send the brief to anyone. Email sending waits on our server.
- Never guess a number a tool did not return.
- Nothing changes in any account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: leadership-monday-brief". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every Monday 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

Not fully ready yet (ready after we build it): Repeats by itself only in Claude Code on a computer that is on at that time. In the Claude app or website, run it by hand each time, or use a scheduled task if your Claude offers one. Sending it by email with the laptop off needs our server to run and send it, which is not built yet. Do the parts you can and say plainly what is missing.
