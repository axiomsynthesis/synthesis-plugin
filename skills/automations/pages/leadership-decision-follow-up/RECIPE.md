# Did our decisions work?

Channel: Leadership · Level: On a schedule · Status: Ready now
Schedule: every Monday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Did our decisions work?" (id: leadership-decision-follow-up, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each week it reads your logged decisions and finds the ones due for a result. For each one it pulls the number the decision was meant to move and says whether it worked so far.

What to read: Your decision log
What to give me: Your logged decisions that are due for a result, and whether each one moved its number

Synthesis tools to use:
- `recall_decisions`
- `query_series`
- `explain_metric_move`

Steps:
1. Call `recall_decisions` to list every logged decision with its date, what it should move and when to check.
2. Keep the ones that reach their check date within the next 7 days or are already past it.
3. For each, call `query_series` with the metric the decision named, `grain="week"`, from 8 weeks before the decision to the last closed week.
4. Where the number moved, call `explain_metric_move` with that metric and month to rule out season and other causes.
5. Write a short read per decision: before, after, the change, and how sure we are.

Checks before answering:
- Compare with the same weeks a year ago where you can, so season is not read as a result.
- If the decision did not name a measure, say so. Never pick one for it.
- A few days of data is not a result. Say when the read will be fair.
- If the log is empty or fails to load, say so plainly.

Output:
- One line first: how many decisions are due and which one matters most.
- A table: decision, date, check date, measure, before, after, change, verdict.

Never:
- Never log an outcome for the owner. They confirm it.
- Never call a decision a success on less than its stated window.
- Nothing changes in any account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: leadership-decision-follow-up". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every Monday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
