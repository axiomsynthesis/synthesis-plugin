---
description: "Is website growth from new or old customers?: Whether website growth came from new or returning customers, and why. Website only"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Is website growth from new or old customers?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is website growth from new or old customers?" (id: grw-new-vs-returning, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits each month's website revenue into first-time buyers and returning ones, against the same months a year earlier. It then shows whether returning revenue moved because fewer old customers came back or because each one spent less. It reads the website only.

What to read: New and returning website customers and revenue by month, two years back, plus subscriptions and repurchase by start month
What to give me: Whether website growth came from new or returning customers, and why. Website only

Synthesis tools to use:
- `shopify_metric metric=new_vs_returning months=24`
- `shopify_metric metric=cohort_retention limit=24`
- `recharge_metric metric=mrr months=24`
- `channel_revenue_mix`

Steps:
1. Call `channel_revenue_mix` for the website's share of company sales. Put it in the first line, so a website change is read at its true size.
2. Pull `shopify_metric metric=new_vs_returning months=24`, so the last three closed months each have a year-ago month to compare with.
3. Add up the last three closed months, and the same three months a year earlier, for new and returning revenue. Split the returning change into returning customers and revenue per returning customer.
4. Show the month-by-month count of new customers over the last six closed months, so a slide inside the year is not hidden.
5. Report `subscription_customers` by month from step 2. Pull `recharge_metric metric=mrr months=24` for recurring revenue a year apart. If it fell, say how much of the returning change it may explain.
6. Pull `shopify_metric metric=cohort_retention limit=24`. Compare the 3 and 6 month repurchase rate of start months a year apart, to see whether fewer customers come back.

Checks before answering:
- This reads the website only. Never call it the source of the business's growth. Amazon has new and repeat customer counts but no revenue split by them yet. Say that plainly if asked about the whole business.
- Shopify new means first website order, not first purchase from the brand anywhere. Say so. Never use the Amazon new-to-brand count here.
- Revenue here is order totals and can include tax and shipping. Call it order revenue, never net sales.
- A first subscription order counts as new. The subscription read counts customers and recurring revenue. It cannot split returning revenue into subscription and one-time orders. Say so.
- Young start months have not had time to come back. Compare only months old enough.
- Leave the current month out.

Output:
- Answer first: the year-on-year change in new and returning revenue for the last three closed months, and the website's share of company sales.
- Table by month: new customers, new revenue, returning customers, returning revenue, subscription customers, and the same month a year earlier.
- One line on why returning revenue moved: fewer customers back, or less spent by each.
- One line on whether new customers are rising or falling over the last six months.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-new-vs-returning". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
