# How many months of cash do we have?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How many months of cash do we have?" (id: money-cash-runway-plan, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Says how many months of cash you have and what changes it most. It draws a 12-month cash line with a base case, a slower case and a stock-heavy case.

What to read: NetSuite, settlements, inventory buys
What to give me: Months of runway, a 12-month cash line in three scenarios, and what moves it most

Synthesis tools to use:
- `working_capital`
- `monthly_pnl`
- `netsuite_metric metric=ar_aging`
- `netsuite_metric metric=inventory_position`
- `operator_inputs section=purchase_orders`
- `operator_inputs section=cogs`
- `run_scenario scenario_type=inventory_bet`

Steps:
1. Call `working_capital` for today's cash, what you owe and what you are owed, and the runway figure.
2. Call `monthly_pnl` for the last three closed months to get the monthly burn or profit.
3. Call `netsuite_metric` with `metric=ar_aging` and `metric=inventory_position` to see cash tied up in unpaid bills and stock.
4. For the next stock order, take its units from `operator_inputs section=purchase_orders` and the landed cost per unit from `operator_inputs section=cogs`. If either is not entered, ask the person. Then call `run_scenario scenario_type=inventory_bet months=12 units=<units> unit_cost=<cost>`. If neither is known, leave out the stock-heavy case and say why.
5. Build three lines: base, sales 15% slower, and the next order placed 60 days early.

Checks before answering:
- If `working_capital` says runway is empty because the business makes cash, say that. Never print it as zero months.
- If NetSuite is not connected, say the plan uses payouts only and is rougher.
- Use closed months. The current month is not finished.

Output:
- One line first: months of runway and the one thing that moves it most.
- A table: month, cash in, cash out, closing cash, for each of the three cases.
- One move and how we will know it worked.

Never:
- Never move money or place an order. A person does that.
- Never guess a bill or a payment date the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-cash-runway-plan". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
