# Is Amazon taking a bigger cut?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is Amazon taking a bigger cut?" (id: mkt-amazon-fee-share-trend, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A single month's fee jump is easy to spot. A slow creep over a year is not. This tracks Amazon's share of each dollar month by month and names what moved it.

What to read: Referral and fulfilment fees as a share of settled sales, month by month, for the last 12 closed months
What to give me: Whether Amazon's total take is creeping up, by how much a year, and which fee is driving it

Synthesis tools to use:
- `amazon_metric metric=fee_rate_trend months=12`
- `amazon_metric metric=fee_breakdown`
- `amazon_metric metric=fee_anomaly months=6`

Steps:
1. Call `amazon_metric metric=fee_rate_trend months=12`.
2. Call `amazon_metric metric=fee_breakdown month=<last closed month>` for the dollar split by fee type.
3. If the fulfilment share rose, call `amazon_metric metric=fee_anomaly months=6` to find products whose per-unit fee stepped up.
4. Turn the rise in points into dollars a year at today's sales.

Checks before answering:
- Read several closed posted months, never one. The newest posted month is partial.
- Fees are by posted date and sales by order date in other tools. Never divide one by the other. This tool keeps both on settlement.
- Reserve holds in settlements are your own cash held and released. They are never a fee.

Output:
- One line: Amazon's share now, a year ago, and the dollar difference a year.
- A table: month, referral share, fulfilment share, total share.
- The products behind any step change.

Never:
- Never call a fee step a proven overcharge. It is a candidate to check in Seller Central.
- Never use an open month as the latest point.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-fee-share-trend". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
