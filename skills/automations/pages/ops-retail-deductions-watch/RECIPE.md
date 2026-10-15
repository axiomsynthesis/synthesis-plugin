# What retailers take back each month

Channel: Retail · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What retailers take back each month" (id: ops-retail-deductions-watch, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Retailers take money back through promo allowances, damages, short shipments and penalties. This puts those deductions next to what each account actually buys, so a creeping deduction rate is caught while it can still be disputed.

What to read: Discounts, refunds and credit memos booked against retail and wholesale accounts in the ledger
What to give me: What each retail account takes back in deductions and credits each month, against what it buys

Synthesis tools to use:
- `netsuite_metric metric=contra_revenue months=12`
- `netsuite_metric metric=returns_credits months=12`
- `netsuite_metric metric=customer_trend months=12 top=20`

Steps:
1. Call `netsuite_metric metric=customer_trend months=12 top=20` for invoiced revenue per account. Keep accounts whose type is a retail or wholesale customer, not the brand's own storefronts.
2. Call `netsuite_metric metric=contra_revenue months=12` for discount and refund dollars by channel.
3. Call `netsuite_metric metric=returns_credits months=12` for credit memos by month.
4. For each retail account compute deductions and credits as a share of invoiced revenue over the last quarter and the same quarter last year.
5. Flag accounts whose share rose more than 3 points or whose quarterly credits exceed $10,000 above last year.

Checks before answering:
- The customer list includes the brand's own channels as "customers". Read the account type before calling anything a retailer.
- Credit memos are dated by issue. A big memo may cover several months of trade.
- Invoiced revenue runs above statement revenue. Use invoiced revenue as the base for this share, and say so.
- If the ledger is not connected, say so and stop.

Output:
- Table: Account | Invoiced last quarter | Deductions and credits | Share | Share a year ago | Flag.
- Two lines: the account to dispute or query, and the dollars at stake.

Never:
- Never dispute a deduction or contact a buyer.
- Never treat an own storefront as a retailer.
- Never net deductions against unrelated invoices.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-retail-deductions-watch". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
