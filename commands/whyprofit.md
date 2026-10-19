---
description: "Why did profit move this month?: A line-by-line walk from last month's profit to this month's, with the dollars each line added or took away"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Why did profit move this month?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Why did profit move this month?" (id: ops-profit-bridge-month, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Explains a change in company profit between two months as a bridge, every line in dollars. It tests each line against its own recent norm, so an odd month is not read as a business change. A brand with no accounting system connected gets the same bridge for its Amazon profit.

What to read: Accounting ledger P&L for two closed months and operating cost by category, or Amazon's own profit lines when no ledger is connected
What to give me: A line-by-line walk from last month's profit to this month's, with the dollars each line added or took away

Synthesis tools to use:
- `cost_rules for=ops-profit-bridge-month`
- `netsuite_metric metric=pnl_trend months=13`
- `monthly_pnl month=YYYY-MM`
- `netsuite_metric metric=opex_category months=<K> limit=20`
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `amazon_metric metric=fee_rate_trend months=7`
- `emit_chart type=waterfall`

Steps:
1. Call `netsuite_metric metric=pnl_trend months=13`. If it says no ledger is connected, skip to step 8. Default to `last_closed_month` against the closed month before it. If `last_closed_month` is more than 45 days old, also build the bridge for the latest two months on file, labelled provisional with product cost at standard cost, and lead with it next to the closed one.
2. Call `monthly_pnl month=YYYY-MM` for each month. Read revenue, product cost, gross profit, operating cost, EBITDA, `cogs_source`, `other_income`, `other_expense` and `net_income`.
3. Split the gross profit change: revenue change times last month's margin rate (volume), and this month's revenue times the change in margin rate (rate).
4. `netsuite_metric metric=opex_category` sums the last N months and takes no month. For one month, call `months=<K>` and `months=<K-1>` with `limit=20` and subtract (K = months back from the latest on file, that month = 1). Leave out Other Expense here.
5. Name one-off items over $10,000.
6. Run-rate test: from `pnl_trend`, compare each line's share of sales in both months with its average over the six months before. If either month is more than 2 points off its norm, label it a one-off and show the bridge again with that month restated to its norm.
7. Draw it with `emit_chart type=waterfall`. Pass the earlier month's EBITDA first, then only the changes, with a cost that rose as a negative. Never pass the later EBITDA as a last bar. The last step must equal the later EBITDA.
8. No ledger: call `amazon_metric metric=pnl_waterfall month=YYYY-MM` for the latest month not flagged as still settling, and the month before. Bridge sales, discounts, refunds, referral fee, FBA fee, account charges, product cost and ad spend to net profit, drawn as in step 7. For the run-rate test, call `amazon_metric metric=fee_rate_trend months=7` for the fees and the waterfall for earlier months for the rest. If product cost is missing, end at profit after fees and ads and name the products.

Checks before answering:
- A month that is not closed is provisional. Say so beside it. Never silently swap in another month.
- The bars must add to the change in EBITDA within $1. Otherwise show the gap as "unexplained".
- If the opex categories do not tie to the P&L operating cost within 1%, show both.
- When the earlier month is the one off its norm, the change is a reversion, not a new problem. Say so.
- No ledger: say so in one line. The Amazon bridge is Amazon profit only. If Amazon has no profit lines either, stop.

Output:
- Three lines on top: the change in one sentence, the biggest driver in dollars, and whether it is a real change or a one-off.
- One chart and a table: Line | Earlier month | Later month | Effect on profit.
- EBITDA to net income: other income, other expense and net income for both months.
- Say which profit it is: the whole company, or Amazon only.

Never:
- Never soften a loss. If the month lost money, say it lost money.
- Never treat an estimate-to-closed swing as a business change.
- Never write "vs budget".

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-profit-bridge-month". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
