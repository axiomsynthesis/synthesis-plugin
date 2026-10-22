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

Rounds (relook before you answer):
1. **It adds up.** Fails when: the bars miss the change by more than $1. Fix: show the gap as "unexplained".
2. **Reversion.** Fails when: the earlier month is more than 2 points off its 6-month norm on the line that drives the change, and the answer calls it new. Fix: call it a reversion.
3. **Closed, not in flight.** Fails when: either month is not closed in the books, or Amazon's month is still settling, and it is not labelled provisional. Fix: label it, and lead with the closed pair.
4. **Season.** Read the same two months a year earlier from `pnl_trend`. Fails when: the driver moved the same way then by at least half as much. Fix: call it seasonal.
5. **Restated, not real.** Fails when: an unlabelled deduction or a cost ruling moved more than $10,000 between the months and is not its own bar. Fix: give it its own bar and say which month it restated.
6. **Headline is money.** Fails when: the first line names a driver under 10% of the change. Fix: lead with the biggest dollar driver.

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
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-profit-bridge-month". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
