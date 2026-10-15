# What Amazon hasn't paid you yet

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What Amazon hasn't paid you yet" (id: mkt-amazon-not-yet-paid, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Order value and money paid are not the same. Amazon pays on a cycle and takes coupons and refunds off.
This shows how much is still to come and how much of order value never turns into cash.

What to read: Daily order value against what Amazon has settled for those same orders, refunds, and the coupon gap
What to give me: How much of this month's sales Amazon still owes you, when it should land, and any gap between orders and payout

Synthesis tools to use:
- `amazon_metric metric=daily_settled_revenue days=60`
- `amazon_metric metric=pnl`

Steps:
1. Call `amazon_metric metric=daily_settled_revenue days=60`. Sum unsettled order value, settled principal, refunds and the coupon gap.
2. Read settled share by order date. Recent days will be low. That is the settlement lag.
3. Call `amazon_metric metric=pnl month=<last closed month>` to compare a fully settled month's payout with its order value.

Checks before answering:
- Keep unsettled order value apart. Never add it to settled money.
- The settlement lag differs by account. Read it from this account's data, never assume two weeks.
- If settled share is near zero for weeks, settlement data may have stopped syncing. Check before calling it lag.

Output:
- Three lines: order value, settled so far, still to come.
- One line: the share of order value lost to coupons and refunds on settled orders.

Never:
- Never present order value as cash received.
- Never forecast a deposit date as certain.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-not-yet-paid". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
