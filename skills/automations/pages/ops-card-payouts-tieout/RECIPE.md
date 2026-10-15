# Do website sales match bank deposits?

Channel: Money · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Do website sales match bank deposits?" (id: ops-card-payouts-tieout, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ties website sales to bank deposits the way the Amazon settlement ties to Amazon payouts. Without this, website revenue has never been checked against cash, and a fee change, a refund surge or a run of chargebacks can go unseen.

What to read: Website orders, card processor charges, fees, refunds, disputes and payouts
What to give me: Whether website sales tie to what landed in the bank, with fees, refunds, disputes and timing named

Synthesis tools to use:
- `net_revenue_dtc month=YYYY-MM`
- `shopify_metric metric=monthly_revenue months=3`

Steps:
1. Call `net_revenue_dtc month=YYYY-MM` and `shopify_metric metric=monthly_revenue months=3` for website sales.
2. Once the build lands, read processor charges, fees, refunds, disputes and payouts for the same month.
3. Bridge: website sales, less refunds, less processor fees, less disputes lost, plus or minus timing (charges in the month paid out next month), equals payouts.
4. Report the unexplained amount against a 0.5% tolerance.
5. List disputes opened in the month with amount and status.

Checks before answering:
- Until the reader exists, say the tie-out cannot be done and show only website sales.
- Amounts arrive in minor units, and not every currency has two decimals. Convert per currency.
- A payout's status can change from pending to available; the amounts do not. Use amounts.
- A processor with no rows for the month is not zero. Check the connection.

Output:
- Bridge table: Website sales | Refunds | Fees | Disputes lost | Timing | Payouts | Unexplained.
- One line: tied or not tied, and the biggest item.

Never:
- Never use our own billing key in place of the brand's processor key.
- Never move money, refund a customer or respond to a dispute.
- Never treat processor fees as product cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-card-payouts-tieout". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Stripe and PayPal connectors land charges, fees, refunds, disputes and payouts in the warehouse, but there is no reader tool for them and raw SQL is not open to every brand. Needs a card-payout tool that returns payouts, fees, refunds and disputes by month, with amounts in minor units converted per currency. Do the parts you can and say plainly what is missing.
