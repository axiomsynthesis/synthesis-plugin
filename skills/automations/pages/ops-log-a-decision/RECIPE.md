# Log a decision so you can check it later

Channel: Leadership · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Log a decision so you can check it later" (id: ops-log-a-decision, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Writes a decision down so it can be judged later: what was decided, why, what it should move, by how much, and when to check. Most decisions are never revisited because nobody wrote down what success looked like. This fixes that at the moment of deciding.

What to read: The decision you are making, the metric it should move, and that metric's current level
What to give me: A logged decision with its expected result, how and when it gets checked, and the starting number

Synthesis tools to use:
- `log_decision`
- `register_prediction`
- `measurable_test`
- `query_series metric=<metric> grain=week`

Steps:
1. Ask for the decision, the reason, and the metric it should move.
2. Pull the baseline: `query_series metric=<metric> grain=week` for the last 8 weeks.
3. Agree the expected direction and size, and the check date (long enough for the metric to settle).
4. Call `log_decision decision=<what> rationale=<why> kind=<type> measure=<metric> expected=<up|down> made_on=<date> window_weeks=<weeks> reversibility=<one-way_or_two-way>`.
5. Call `register_prediction claim=<claim> metric=<metric> direction=<increase|decrease|stable> target=<value> horizon_days=<days> falsifier=<what_would_prove_it_wrong>`.
6. Call `measurable_test` to set success and warning lines, with `direction` (`lower_is_better` for a cost such as cost per purchase or return rate).

Checks before answering:
- The baseline must exclude deal and stockout weeks, or the check will be unfair.
- The falsifier must be something a measured number can show. "Customers like it" is not one.
- The check date must fall after the metric settles (two weeks for ad-credited sales, the book close for profit).

Output:
- A short record: Decision | Why | Metric | Baseline | Expected | Success line | Warning line | Check date | Reversible.

Never:
- Never make or carry out the decision. A person does.
- Never log a decision with no measurable result; ask for one.
- Never backdate a decision.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-log-a-decision". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
