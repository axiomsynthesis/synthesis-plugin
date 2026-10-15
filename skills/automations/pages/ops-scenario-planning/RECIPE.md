# Four ways next year could go

Channel: Strategy · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Four ways next year could go" (id: ops-scenario-planning, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds four futures from the two uncertainties with the biggest impact on the business, then puts a revenue range on each. The point is not to predict, but to know which future you are drifting into early, and to have a plan ready for each.

What to read: The uncertainties that matter most to the business and your revenue and margin base
What to give me: Four plausible futures from your two biggest unknowns, each with a revenue range and the early signs it is coming

Synthesis tools to use:
- `strategy_framework framework=scenario_2x2`
- `run_monte_carlo`
- `metric_timeseries metric_keys=[revenue] start_month=YYYY-MM end_month=YYYY-MM`
- `google_trends keyword=<category_term>`
- `export_docx`

Steps:
1. List candidate uncertainties with the founder (ad costs, tariffs, category demand, a big account, platform fees). Rate each on impact and uncertainty, 1 to 10.
2. Run `strategy_framework framework=scenario_2x2 variables=[{name, impact, uncertainty}]` with every rated uncertainty, to pick the top two and build four futures.
3. Call `metric_timeseries metric_keys=["revenue"]` for the base and `google_trends keyword=<category_term>` for demand direction.
4. For each future, run `run_monte_carlo` with growth and shock settings that match it, passing the spread explicitly.
5. For each future, name one or two measured early signs and a level that would confirm it.
6. Write it with `export_docx`.

Checks before answering:
- Impact and uncertainty ratings are judgement. Label them.
- Each future's range must come from the simulation with stated inputs, not a guess.
- Early signs must be metrics we can actually measure.

Output:
- Word document: the 2x2, one section per future with range, early signs and the first move.
- Two lines in chat: the most likely future today and its early sign.

Never:
- Never present a future as a forecast.
- Never use default volatility.
- Never act on a plan.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-scenario-planning". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
