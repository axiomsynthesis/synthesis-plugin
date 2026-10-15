# What if ads get 50% more expensive?

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What if ads get 50% more expensive?" (id: grw-cac-stress, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs your numbers through hard shocks: sales down 30%, customer cost up 50%, product cost up 20%. It shows which hurts most and how long cash lasts in each.

What to read: Your revenue, cost per new customer, product cost share and cash
What to give me: How the business holds up if customer costs jump, and the first lever to pull

Synthesis tools to use:
- `strategy_framework framework=stress_test`
- `mer month=<YYYY-MM>`
- `new_customers_dtc month=<YYYY-MM>`

Steps:
1. Ask for cash on hand and product cost share if not known.
2. Compute the base cost per new customer from spend and `new_customers_dtc`.
3. Run `strategy_framework framework=stress_test base_revenue=<one month> base_cac=<value> new_customers_per_month=<value> base_cogs_pct=<value> monthly_operating_costs=<value> cash_on_hand=<value>`. Without new_customers_per_month the cost-per-customer shock is per customer only; without operating costs there is no monthly profit or months of cash.
4. Name the shock that hurts most and the first lever.

Checks before answering:
- Every input must be stated with where it came from. Never invent one.
- This is a what-if, not a forecast. Say so.

Output:
- Answer first. Table: shock, monthly profit change, months of cash.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-cac-stress". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
