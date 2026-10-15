# Are we on pace to hit this month?

Channel: Money · Level: On a schedule · Status: Ready now
Schedule: weekly Monday and on the 15th, 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are we on pace to hit this month?" (id: ops-month-pace-vs-target, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Answers "are we going to hit the month" while there is still time to act. It compares month-to-date with the same days last month, projects the finish, and turns the gap to target into a daily number.

What to read: Month-to-date sales, the same days last month, the full-month projection and your entered targets
What to give me: Mid-month, whether you're on pace for the target, and the daily sales needed to hit it

Synthesis tools to use:
- `mtd_comparison`
- `monthly_projection`
- `amazon_metric metric=plan_vs_actual periods=3`

Steps:
1. Call `mtd_comparison` for month-to-date against the same number of days last month.
2. Call `monthly_projection` for the projected finish and its confidence band.
3. Call `amazon_metric metric=plan_vs_actual periods=3` for the entered targets and pace.
4. Required daily sales = (target minus month-to-date) divided by days left.
5. Compare the required daily rate with the month's daily rate so far.

Checks before answering:
- No target entered means no attainment. Say "no target set" and show only the projection. Never show 0% attained.
- An open month is not a miss. Report pace, not attainment, until the month closes.
- Today's sales are still arriving. Make sure month-to-date stops at yesterday.
- A deal or event later in the month changes the math. Ask if one is planned.

Output:
- Four lines: month-to-date and change, projected finish and range, target and gap, daily sales needed against daily sales so far.

Never:
- Never call an open month a miss.
- Never invent a target.
- Never change spend or prices to chase the target.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-month-pace-vs-target". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday and on the 15th, 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
