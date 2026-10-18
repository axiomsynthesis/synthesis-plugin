# Why did profit move this month?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Why did profit move this month?" (id: ops-profit-bridge-month, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Explains a change in company profit between two months as a bridge: sales volume, gross margin rate, each operating cost category, and one-off items. It is the page a founder reads before a finance call, with every line in dollars. A brand with no accounting system connected gets the same bridge for its Amazon profit.

What to read: Accounting ledger P&L for two closed months and operating cost by category, or Amazon's own profit lines when no ledger is connected
What to give me: A line-by-line walk from last month's profit to this month's, with the dollars each line added or took away

Synthesis tools to use:
- `cost_rules for=ops-profit-bridge-month`
- `netsuite_metric metric=pnl_trend months=13`
- `monthly_pnl month=YYYY-MM`
- `netsuite_metric metric=opex_category months=1 limit=20`
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `emit_chart type=waterfall`

Steps:
1. Call `netsuite_metric metric=pnl_trend months=13` and pick the two months to compare. If it says no ledger is connected, skip to step 7. Default to the latest closed month against the closed month before it, and the same month last year when both are closed.
2. Call `monthly_pnl month=YYYY-MM` for each month. Read revenue, product cost, gross profit, operating cost, EBITDA and `cogs_from_month_end`.
3. Split the gross profit change into two parts: revenue change times last month's margin rate (volume), and this month's revenue times the change in margin rate (rate).
4. Call `netsuite_metric metric=opex_category months=1 limit=20` for each month's category amounts and take the difference for each category.
5. Name one-off items separately when they move a month by more than $10,000, such as tariff refunds or write-offs.
6. Draw the bridge with `emit_chart type=waterfall`. The chart adds up every bar as a step, so pass the earlier month's EBITDA first, then only the changes, with a cost that went up as a negative number. Never pass the later month's EBITDA as a last bar: it would be stacked on top. The top of the last step must equal the later month's EBITDA; check it before answering.
7. No ledger: call `amazon_metric metric=pnl_waterfall month=YYYY-MM` for the latest month that is not flagged as still settling, and for the month before it. Bridge each line from one month to the next: sales, discounts, refunds, referral fee, FBA fee, Amazon account charges, product cost, ad spend, ending at net profit. Draw it the same way as step 6, starting from the earlier month's net profit. If product cost is missing, end the bridge at profit after Amazon fees and ads, and name the products that need a cost entered.

Checks before answering:
- Both months must be closed. If either is an estimate, say so and offer the bridge as provisional, or wait for the close. Do not silently swap in another month.
- The bars must add up to the actual change in EBITDA within $1. If they do not, show the residual as "unexplained" rather than spreading it.
- If the opex category totals do not tie to the P&L operating cost within 1%, show both figures.
- If the brand has no ledger connected, say so in one line and use the Amazon bridge. It is Amazon profit only, not the whole company, so say that. If Amazon has no profit lines either, say so and stop.
- On the Amazon bridge, never use a month the result flags as still settling.

Output:
- One chart and a table: Line | Earlier month | Later month | Effect on profit.
- Say which profit it is: the whole company from the ledger, or Amazon only.
- Three lines on top: the change in one sentence, the biggest driver in dollars, and what to check next.

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
