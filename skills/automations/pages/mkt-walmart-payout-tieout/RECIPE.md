# Does each Walmart payout add up?

Channel: Walmart · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Does each Walmart payout add up?" (id: mkt-walmart-payout-tieout, Walmart).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ties each Walmart payout to the orders, fees and refunds behind it. The gap is either timing or money owed.

What to read: Walmart Marketplace settlement reports, fees, refunds and deposits, against order value for the same period
What to give me: Whether each payout ties to orders minus fees and refunds, and any gap in dollars

Synthesis tools to use:
- `walmart_metric metric=revenue months=3`
- `walmart_metric metric=orders_trend months=3`

Steps:
1. Once settlement data lands: read each payout's total, fees, refunds and adjustments.
2. Call `walmart_metric metric=revenue months=3` for order value in the same periods.
3. Compute order value minus fees minus refunds, by payout period, and compare with the deposit.
4. List any gap over 1% with the lines behind it.

Checks before answering:
- Until settlement data exists, never present a payout or fee figure. Say the data is not available.
- Payout periods do not match calendar months. Compare by payout period.

Output:
- One line per payout: ties, or the gap in dollars.
- A table: payout date, orders, fees, refunds, adjustments, expected, paid, gap.

Never:
- Never call order value the payout.
- Never open disputes with Walmart.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-walmart-payout-tieout". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Walmart sends its settlement as a zipped file. The sync reads it as a plain file today, so no Walmart settlement data has ever landed. Needs the settlement reader fixed before payouts can be tied out. Do the parts you can and say plainly what is missing.
