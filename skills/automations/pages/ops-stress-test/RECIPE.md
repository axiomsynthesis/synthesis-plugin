# Could we survive a bad year?

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Could we survive a bad year?" (id: ops-stress-test, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Applies hard but plausible shocks to the business using your real margin and cost structure, one at a time and together. It shows how much room you have and which shock hurts most, so protection can be arranged before it is needed.

What to read: Revenue, closed-book margin, fixed costs and cash
What to give me: What happens to profit and cash if sales drop, ad costs rise or product cost jumps, alone and together

Synthesis tools to use:
- `netsuite_metric metric=pnl_trend months=12`
- `operator_inputs section=cash`
- `strategy_framework framework=stress_test`
- `strategy_framework framework=antifragility`
- `run_monte_carlo`

Steps:
1. Call `netsuite_metric metric=pnl_trend months=12` for revenue, margin and operating cost on closed months.
2. Call `operator_inputs section=cash` for current cash.
3. Run `strategy_framework framework=stress_test base_revenue=<monthly revenue> base_cogs_pct=<measured product cost share> monthly_operating_costs=<every other monthly cost> base_cac=<cost per new customer> new_customers_per_month=<count> cash_on_hand=<cash>`. It returns monthly profit under each shock and under all three together, months of cash and survival; without operating costs it will not call survival. Leave out a field you do not have and say it was not tested. Shocks are sales down 30%, acquisition cost up 50%, product cost up 20%.
4. Months of cash under each shock = cash divided by monthly loss.
5. Run `strategy_framework framework=antifragility plus_shock=<gain under the upside> minus_shock=<loss under the downside>` to show whether the business gains or loses more from swings.
6. Optionally run `run_monte_carlo` with shock probabilities to show the range.

Checks before answering:
- Use the measured margin, never the tool's default cost share.
- Cash must be recent (within 7 days). Otherwise ask.
- If the ledger is not connected, run on Amazon profit only and say the company view needs the books.

Output:
- Table: Shock | Monthly profit | Months of cash.
- Two lines: the shock that hurts most and the cheapest protection.

Never:
- Never call a stress result a forecast.
- Never use default margins.
- Never arrange financing or cut costs.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-stress-test". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
