# How is the business doing, metric by metric?

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How is the business doing, metric by metric?" (id: ops-operating-state, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Names the condition the business is in before prescribing anything. Growing, steady, slipping or in trouble each call for different moves, and treating a slipping business like a growing one wastes money. It reads several metrics and ranks the weakest first.

What to read: Revenue, customers, margin and efficiency trends
What to give me: Which condition each key metric is in, worst first, and the steps that condition calls for

Synthesis tools to use:
- `diagnose_state_map metrics=[...]`
- `diagnose_operating_state metric=revenue`
- `run_state_formula state=<state>`
- `metric_timeseries metric_keys=[revenue,customers,new_customers] start_month=YYYY-MM end_month=YYYY-MM`

Steps:
1. Call `metric_timeseries metric_keys=["revenue","customers","new_customers"]` for the last 12 full months.
2. Call `diagnose_state_map metrics=[...]` with those series and any margin or efficiency series held.
3. For the lowest metric, call `diagnose_operating_state metric=<metric>` for detail.
4. Call `run_state_formula state=<state>` for the ordered steps for that condition.
5. Turn the first two steps into concrete actions using the brand's own numbers.

Checks before answering:
- Use full months only, and mark event months.
- A metric with under six months of data cannot be placed. Say so.
- Revenue steady while new customers fall is a split picture. Report the split, not the average.

Output:
- Table: Metric | Condition | Months in this condition.
- Three lines: the weakest metric, its condition, and the first step in plain words.

Never:
- Never label the business from one metric.
- Never prescribe before the condition is placed.
- Never take an action.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-operating-state". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
