# What would a buyer pay for the business?

Channel: Strategy · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What would a buyer pay for the business?" (id: ops-exit-readiness, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Looks at the business the way a buyer would, a year or two before a sale. It produces a valuation range from several methods and a gap list where every item is either measured, measured and short, or not measurable here. It never grades the business on numbers it did not measure.

What to read: Revenue growth, closed-book margins, EBITDA, concentration, recurring revenue, cohort retention and cash cycle
What to give me: A valuation range and what a buyer would mark you down for, each item measured

Synthesis tools to use:
- `cost_rules for=ops-exit-readiness`
- `netsuite_metric metric=pnl_trend months=13`
- `netsuite_metric metric=adjusted_ebitda months=12`
- `customer_concentration`
- `cohort_retention_table`
- `recharge_metric metric=mrr months=12`
- `valuation_and_exit_readiness`
- `export_pdf`

Steps:
1. Call `netsuite_metric metric=pnl_trend months=13` and `netsuite_metric metric=adjusted_ebitda months=12` for revenue, growth and EBITDA on closed months.
2. Call `customer_concentration` for top account share, and the channel split from invoiced revenue.
3. Call `cohort_retention_table` for retention, reading only matured cohorts for level.
4. Call `recharge_metric metric=mrr months=12` if subscriptions are connected, for recurring revenue share.
5. Ask for what cannot be measured: founder dependence, team depth, audit quality.
6. Run `valuation_and_exit_readiness` passing every input explicitly. `growth_3yr`, `gross_margin`, `channel_concentration_pct` and `strategic_stage` are required: they pick the multiples, and the tool refuses without them. Any other input not measured, leave out; the result lists every factor and haircut that rested on an engine default.
7. Write it with `export_pdf`: range, inputs table (measured or supplied), gap list, three priorities.

Checks before answering:
- The tool fills missing inputs with defaults that look like measurements, including channel concentration. Pass every input or say it was not measured.
- Adjusted EBITDA equals reported EBITDA when no add-backs are booked. Say so.
- Report the range, never just the midpoint.
- Newest cohorts are not finished. Use them for direction only.

Output:
- A PDF of three to five pages.
- Gap list rows: Area | Status (meets, below, not measurable here) | Figure and source | Gap in dollars or points.

Never:
- Never present a valuation as a quote or an offer.
- Never contact advisers or buyers.
- Never fill a missing input with the tool's default.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-exit-readiness". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
