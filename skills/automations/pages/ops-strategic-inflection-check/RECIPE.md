# Is something big changing in your market?

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is something big changing in your market?" (id: ops-strategic-inflection-check, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Looks for the rare shift that changes the rules for the business, rather than a bad month. It checks the big forces (demand, cost to reach buyers, platform fees, new rivals, suppliers, technology) for a change of scale, and names the one that matters.

What to read: Long-run trends in demand, ad costs, platform fees, rival entry and your own growth
What to give me: Whether the forces on your business have shifted enough to change the rules, and which one to watch

Synthesis tools to use:
- `strategy_framework framework=ten_x_forces`
- `strategy_framework framework=detect_phase_transition`
- `google_trends keyword=<category_term>`
- `amazon_metric metric=fee_rate_trend`
- `meta_metric metric=cpm month=YYYY-MM`
- `metric_timeseries metric_keys=[revenue,new_customers] start_month=YYYY-MM end_month=YYYY-MM`

Steps:
1. Pull long series: `google_trends keyword=<category_term>` for demand, `meta_metric metric=cpm month=YYYY-MM` for each of the last 12 months for the cost of reach, `amazon_metric metric=fee_rate_trend` for platform take, and `metric_timeseries metric_keys=["revenue","new_customers"]` for 24 months of your own results.
2. Run `strategy_framework framework=detect_phase_transition values=[...] metric_name=<series>` on each series, oldest first and at least 5 points, for a change in state.
3. Rate each force as tailwind or headwind with a magnitude 1 to 10, citing its series.
4. Run `strategy_framework framework=ten_x_forces forces=[{name, direction, magnitude}]` for the net pressure.
5. Name the force with the biggest change in scale and what it would mean if it continues a year.

Checks before answering:
- A one-quarter move is not an inflection. Require a sustained change.
- Mixed bases (order and settled revenue) must not share a series.
- Magnitudes are judgement except where a series shows them. Label which.

Output:
- Table: Force | Direction | Magnitude | Evidence | Changed state (yes or no).
- Two lines: the force to watch and the decision it would change.

Never:
- Never call a normal swing an inflection.
- Never copy any book's text.
- Never act on the finding.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-strategic-inflection-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
