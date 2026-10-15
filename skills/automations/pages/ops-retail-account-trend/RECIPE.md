# Which retail accounts are growing or shrinking

Channel: Retail · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which retail accounts are growing or shrinking" (id: ops-retail-account-trend, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows which retail and wholesale accounts are buying more or less, using invoiced revenue from the books. Retail orders are lumpy, so it looks for two quarters in a row before calling a trend.

What to read: Invoiced revenue per retail and wholesale account by month from the ledger
What to give me: Accounts growing, flat or shrinking over two quarters, with dollars

Synthesis tools to use:
- `netsuite_metric metric=customer_trend months=12 top=12`
- `customer_concentration`

Steps:
1. Call `netsuite_metric metric=customer_trend months=12 top=12`.
2. Keep retail and wholesale accounts. Leave out the brand's own storefronts by account type.
3. For each account compare the last three closed months with the three before, and those with the three before that.
4. Label GROWING or SHRINKING only when the move is over 10% in both comparisons. One quarter alone is "watch".
5. Call `customer_concentration` for the share each account holds of the total.

Checks before answering:
- Drop the running month. It comes back as a separate partial figure.
- One large order can make a quarter. Name accounts whose change is one order.
- Invoiced revenue is before statement discounts and refunds. Say so.
- If the ledger is not connected, say so and stop.
- The read covers the 12 largest accounts. Ask for more and the result is cut to fit, which reads as fewer accounts, not more. Say accounts outside the 12 are not covered.

Output:
- Table: Account | Last 3 months | Prior 3 | Prior 3 before that | Label | Share of total.
- Two lines: the account most at risk in dollars, and the account growing fastest.

Never:
- Never contact a buyer.
- Never call one quarter a trend.
- Never treat the brand's own storefronts as retail accounts.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-retail-account-trend". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
