# How much do you need to sell to break even?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How much do you need to sell to break even?" (id: ops-breakeven-sales-level, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds the monthly sales level where the company stops losing money, from your own closed books. It tells the founder how much room there is before a slow month turns into a loss, and which cost lines would move that line most.

What to read: Closed-month revenue, product cost, variable costs and fixed operating cost
What to give me: The monthly sales that cover all costs, and how far above or below it you are

Synthesis tools to use:
- `cost_rules for=ops-breakeven-sales-level`
- `netsuite_metric metric=pnl_trend months=12`
- `netsuite_metric metric=opex_category months=3 limit=20`
- `strategy_framework framework=stress_test`

Steps:
1. Call `netsuite_metric metric=pnl_trend months=12` and keep closed months only.
2. Call `netsuite_metric metric=opex_category months=3 limit=20` and split categories into variable (marketplace fees, fulfilment, shipping, payment fees, most ad spend) and fixed (payroll, rent, software, professional fees). Show the split and let the person change it.
3. Contribution rate = (revenue minus product cost minus variable costs) divided by revenue.
4. Break-even sales = fixed costs per month divided by the contribution rate.
5. Cushion = (average closed-month revenue minus break-even) divided by average revenue.
6. Run `strategy_framework framework=stress_test base_revenue=<average closed-month revenue> base_cogs_pct=<measured product cost share> monthly_operating_costs=<operating cost per month>` to show the effect of a sales drop and a cost rise on monthly profit.

Checks before answering:
- Use closed months only for margin. An estimate month can carry no product cost and inflate the contribution rate.
- The variable and fixed split is a judgement. List it so the person can correct it.
- Ad spend that the founder treats as fixed should be moved. Ask.
- If the ledger is not connected, say break-even needs the books.

Output:
- Four lines: break-even sales per month, current average sales, cushion in percent and dollars, and the cost line that moves break-even most.
- A small table of the variable and fixed split.

Never:
- Never use the stress test's default cost share. Pass the measured one.
- Never call a month profitable from an estimate.
- Never cut a cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-breakeven-sales-level". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
