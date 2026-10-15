# Plan a creative test that knows when to stop

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Plan a creative test that knows when to stop" (id: grw-creative-test-plan, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Plans a fair test of 3 to 5 new angles: how much each needs to spend, for how long, and what result counts as a win. It files the prediction so the result gets checked.

What to read: Your account's cost per purchase, daily spend and conversion counts
What to give me: A test of new angles with budget, length and the result that ends it

Synthesis tools to use:
- `meta_metric metric=account_daily`
- `meta_metric metric=weekly_trend weeks=8`
- `measurable_test`
- `register_prediction`

Steps:
1. Pull `meta_metric metric=account_daily` and `meta_metric metric=weekly_trend weeks=8` for cost per purchase and daily volume.
2. Ask for the angles to test.
3. Set spend per angle at 3 times your target cost per purchase as the minimum before judging.
4. Run `measurable_test` for each angle with a success line, a warning line and `direction` (`lower_is_better` for cost per purchase).
5. With approval, run `register_prediction` for the main bet.

Checks before answering:
- If the account gets under 10 purchases a day, say the test needs more time or fewer angles.
- Run angles at the same time, never one after another.

Output:
- Table: angle, budget, days, win line, stop line, check date.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Register a prediction only after the person agrees.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-creative-test-plan". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
