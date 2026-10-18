# How could this big decision fail?

Channel: Leadership · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How could this big decision fail?" (id: leadership-pre-mortem-before-a-big-call, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Before a big decision, it imagines the decision has already failed and works out the most likely reasons why. For each one it names the number to watch and the level that means stop.

What to read: Your numbers on the decision
What to give me: The likeliest ways it fails, what each would cost, and the number to watch for each

Synthesis tools to use:
- `cost_rules for=leadership-pre-mortem-before-a-big-call`
- `strategy_framework`
- `run_scenario`
- `query_series`
- `shelf_history`

Steps:
1. Ask the owner for the decision, the goal and the date it should pay off, in one sentence each.
2. Call `query_series` with the metric the decision should move, `grain="week"` and the last 52 weeks, to set the baseline and its normal swings.
3. List the ways it fails, each with a chance from 0 to 1, an impact from 1 to 10 and how hard it is to see coming from 0 to 1. Call `strategy_framework framework=premortem_score failure_modes=[{name, prob, impact, detection_penalty}]` to score them. A failure mode with no chance given is refused, so ask rather than leave it out.
4. Call `run_scenario` with the closest `scenario_type` and `months=6` to size the downside in dollars.
5. If a rival is part of the risk, call `shelf_history` with `marketplace="amazon"` and `days=90` to see how they have moved before.

Checks before answering:
- Each failure mode needs a number to watch and a stop level. A worry with no measure is cut.
- Use the normal weekly swing from the baseline, so the stop level is not set inside noise.
- If a read fails, say so. Never size a risk from a missing number.

Output:
- One line first: the single most likely way this fails.
- A table of 3 to 5 failure modes: what goes wrong, how likely, cost in dollars, number to watch, stop level.
- One move to lower the biggest risk before committing.

Never:
- Never make the decision for the owner.
- Never present a scenario as a forecast.
- Nothing changes in any account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: leadership-pre-mortem-before-a-big-call". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
