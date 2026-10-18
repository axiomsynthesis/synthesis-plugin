# Catch costs creeping up

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Catch costs creeping up" (id: ops-opex-creep-and-spikes, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds operating costs that grow faster than revenue, and single months where a category jumped. It turns "costs feel high" into a short list of named categories with the dollars at stake.

What to read: Accounting ledger operating cost by category and monthly revenue
What to give me: Cost lines growing faster than sales, and one-off spikes to question, in dollars

Synthesis tools to use:
- `cost_rules for=ops-opex-creep-and-spikes`
- `netsuite_metric metric=opex_category months=12 limit=15`
- `netsuite_metric metric=pnl_trend months=12`

Steps:
1. Call `netsuite_metric metric=pnl_trend months=12` for monthly net revenue and total operating cost.
2. Call `netsuite_metric metric=opex_category months=12 limit=15` for operating cost by category. It sums the window, so also request shorter windows (`months=6`, `months=3`) to get the recent run rate per category.
3. For each category compute the monthly average for the last 3 months and the prior 3 months, and the growth of each against revenue growth over the same months.
4. Flag CREEP where a category grows more than 10 points faster than revenue and adds more than $2,000 a month.
5. Flag SPIKE where one month is more than 1.5 times that category's average and more than $5,000 above it.
6. Split out marketplace fulfilment and online fees. They sit in operating cost by design and move with sales, so show them on their own line.

Checks before answering:
- The category tool sums its whole window. Divide by the months in the window before calling anything a monthly figure.
- Compare full months only. Leave out the running month.
- A category that appears only in recent months may be a new account code, not new spend. Say "new line, confirm with finance".
- If the brand has no ledger connected, say so and stop.

Output:
- Table: Category | Monthly now | Monthly before | Growth vs revenue growth | Flag (creep or spike) | Dollars a month at stake.
- Up to five rows. Then one line naming the single category to review first.

Never:
- Never move marketplace fees into product cost or out of operating cost.
- Never call a cost wasteful. The tool sees amounts, not value. A person judges.
- Never cancel a vendor or subscription.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-opex-creep-and-spikes". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
