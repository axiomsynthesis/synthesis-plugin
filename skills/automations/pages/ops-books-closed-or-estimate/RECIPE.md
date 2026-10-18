# Which months are final, which are guesses?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which months are final, which are guesses?" (id: ops-books-closed-or-estimate, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Before anyone quotes a profit, margin or year-over-year figure, this says which months are on closed books and which are still estimates. Revenue is reliable on every month. Profit is reliable only on closed months, because product cost is booked at month end. It stops a pre-close estimate being read as a real swing.

What to read: Accounting ledger monthly P&L and the closed month-end packages
What to give me: Closed months versus estimates, and how far each estimate could still move

Synthesis tools to use:
- `cost_rules for=ops-books-closed-or-estimate`
- `netsuite_metric metric=pnl_trend months=13`
- `monthly_pnl month=YYYY-MM`

Steps:
1. Call `netsuite_metric metric=pnl_trend months=13`. For each row keep the month, net revenue, gross margin, EBITDA, `cogs_recognized` and `yoy_basis`.
2. Mark a month CLOSED only when `cogs_recognized` is true. Every other month is an ESTIMATE.
3. For the latest two months, call `monthly_pnl month=YYYY-MM` and read `cogs_from_month_end` and `cogs_source`, so the basis comes from the tool, not from the row order.
4. For each estimate month, note the size of its profit and whether a sign flip is plausible. A month within a few percent of breakeven is "could flip".
5. List which months have a valid year-over-year: only those where `yoy_basis` says both months are closed.

Checks before answering:
- If the brand has no accounting ledger connected, say so in one line and stop. Never borrow another source's profit as a stand-in.
- A gross margin far above the brand's closed-month range on an estimate month means product cost is missing. Lead with that caveat, not the margin.
- A profit jump between a closed month and an estimate month is an accounting artifact until the estimate closes. Say so in the same sentence as the number.
- Closed months can still move when cost or refunds post late. If a closed month is more than a week old, re-pull before quoting.

Output:
- One table: Month | Basis (closed or estimate) | Net revenue | EBITDA | Year-over-year valid (yes or no).
- Two lines under it: the latest closed month's result, and the latest estimate labelled as an estimate.

Never:
- Never quote an estimate month's profit without the word "estimate" in the same sentence.
- Never build a year-over-year from two numbers when either month is not closed.
- Never write "vs budget". The ledger holds no budget.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-books-closed-or-estimate". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
