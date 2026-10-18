# Build the lender pack

Channel: Money · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build the lender pack" (id: ops-lender-pack, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Assembles what a lender looks at before offering a credit line or inventory loan: revenue history, margins, stock that can secure the loan, how fast sales turn into cash, and how concentrated the business is. It states plainly what has to come from the accountant instead.

What to read: Revenue trend, closed-month margins, stock value, channel and customer concentration and payout timing
What to give me: The pack a bank or inventory lender asks for, every figure sourced and every gap stated

Synthesis tools to use:
- `cost_rules for=ops-lender-pack`
- `netsuite_metric metric=pnl_trend months=13`
- `netsuite_metric metric=inventory_position limit=50`
- `amazon_metric metric=daily_settled_revenue days=180`
- `customer_concentration`
- `netsuite_metric metric=customer_trend months=12 top=10`
- `render_report format=pdf`

Steps:
1. Call `netsuite_metric metric=pnl_trend months=13` for revenue and, on closed months, margin and EBITDA.
2. Call `netsuite_metric metric=inventory_position limit=50` for stock value by location.
3. Call `amazon_metric metric=daily_settled_revenue days=180` for payout rhythm and size.
4. Call `customer_concentration` and `netsuite_metric metric=customer_trend months=12 top=10` for dependence on top accounts.
5. Render with `render_report format=pdf` with sections: Summary, Revenue, Margins (closed months), Stock, Cash timing, Concentration, What is not included.

Checks before answering:
- Profit and margin only from closed months, each labelled.
- No balance sheet, cash balance, receivables or payables position from the ledger movement tables. Say these come from the accountant.
- The rendering checks numbers against the source; if it refuses a figure, fix the figure, do not force it.
- If the ledger is not connected, the pack is Amazon and website only. Say so on the cover.

Output:
- A PDF of four to six pages with the sections above.
- One line in chat listing what the lender will still need from the accountant.

Never:
- Never send the pack to a lender.
- Never quote a cash or receivables balance from the ledger movement tables.
- Never round a declining year into growth.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-lender-pack". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
