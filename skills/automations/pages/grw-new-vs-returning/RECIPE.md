# Is growth from new or old customers?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is growth from new or old customers?" (id: grw-new-vs-returning, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits each month's website revenue into first-time buyers and returning ones. A business living on returning customers while new ones fall is shrinking slowly.

What to read: New and returning website customers and revenue by month
What to give me: Where growth came from, and whether the new-customer engine is slowing

Synthesis tools to use:
- `shopify_metric metric=new_vs_returning months=12`
- `new_customers_dtc month=<YYYY-MM>`
- `returning_customers_dtc month=<YYYY-MM>`

Steps:
1. Pull `shopify_metric metric=new_vs_returning months=12`.
2. For the last 3 closed months, pull `new_customers_dtc` and `returning_customers_dtc`. Both count website customers only. Never use the Amazon new-to-brand count here: it is a different channel with a different meaning of new.
3. Show the year-on-year change in new and returning revenue.

Checks before answering:
- If a customer tool returns gated, do not state the number. Give its refusal reason.
- Shopify new means first website order, not first purchase from the brand anywhere. Say so.
- Leave the current month out.

Output:
- Answer first. Table by month: new customers, new revenue, returning customers, returning revenue.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-new-vs-returning". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
