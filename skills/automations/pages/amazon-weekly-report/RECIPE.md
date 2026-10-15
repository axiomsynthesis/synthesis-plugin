# Your Amazon week, in your inbox Monday

Channel: Amazon · Level: On a schedule · Status: Ready now
Schedule: weekly, Monday, on our server

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Your Amazon week, in your inbox Monday" (id: amazon-weekly-report, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every Monday, your Amazon week in one branded report, emailed to the people you choose.
It runs on our servers, so your computer can be off.
It covers sales, profit, ads, stock and search in eight sections.
This is the paid weekly report. In any Claude you can read the latest one or make a fresh copy.

What to read: All Amazon data
What to give me: A branded weekly report by email: sales, profit, ads, stock and the one thing to act on

Synthesis tools to use:
- `get_weekly_report`
- `generate_weekly_report`

Steps:
1. Call `get_weekly_report` to read the latest stored report for the brand.
2. If the person wants a fresh copy now, call `generate_weekly_report` with `period=last_week` and `format=pdf`.
3. Answer first with the week's headline: sales, change, ad cost as a share of sales, products low on stock.
4. Point to the full report and the one section that needs action this week.

Checks before answering:
- Check the week the report covers. If the stored report is older than the last closed week, say so.
- If the report read fails or comes back empty, say it could not be read. Never fill the headline from memory.
- One week's move is not a trend. Say when a change is inside the brand's normal swing.

Output:
- Three lines: the week's headline, the one thing to act on, and the link to the full PDF.
- The full report is about 6 pages in 8 sections, sent by email on Monday.

Never:
- Never change the email recipients or the schedule from Claude Code. That is set in Settings.
- Never guess a number the report does not show.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-weekly-report". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This one runs on the Synthesis server (weekly, Monday, on our server). Do not set up a repeat yourself; read the latest copy instead.
