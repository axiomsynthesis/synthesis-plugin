---
description: "Is growth from new or old customers?: Where growth came from, and whether the new-customer engine is slowing"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Is growth from new or old customers?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is growth from new or old customers?" (id: grw-new-vs-returning, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits each month's website revenue into first-time buyers and returning ones, against the same months a year earlier. A business living on returning customers while new ones fall is shrinking slowly.

What to read: New and returning website customers and revenue by month, two years back
What to give me: Where growth came from, and whether the new-customer engine is slowing

Synthesis tools to use:
- `shopify_metric metric=new_vs_returning months=24`

Steps:
1. Pull `shopify_metric metric=new_vs_returning months=24`, so the last three closed months each have a year-ago month to compare with.
2. Add up the last three closed months, and the same three months a year earlier, for new and returning revenue.
3. Show the year-on-year change in new and returning revenue, then the month-by-month count of new customers over the last six closed months, so a slide inside the year is not hidden.

Checks before answering:
- Shopify new means first website order, not first purchase from the brand anywhere. Say so. Never use the Amazon new-to-brand count here.
- A first subscription order counts as new, so a business moving to subscriptions shows fewer returning orders than it really has. If the result says so, say it in one line.
- Leave the current month out.

Output:
- Answer first: the year-on-year change in new and returning revenue for the last three closed months.
- Table by month: new customers, new revenue, returning customers, returning revenue, and the same month a year earlier.
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
