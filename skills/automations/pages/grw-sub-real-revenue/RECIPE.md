# Subscription revenue: booked vs actually paid

Channel: Subscriptions · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Subscription revenue: booked vs actually paid" (id: grw-sub-real-revenue, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows the honest subscription number. Book revenue counts every active subscription. Realized revenue is what customers paid. The gap is skips, failures and pauses, and each has a different fix.

What to read: Booked recurring revenue, realized charges and net revenue retention
What to give me: The gap between what the book says and what was paid, and what drives it

Synthesis tools to use:
- `recharge_metric metric=mrr months=12`
- `recharge_metric metric=nrr`
- `recharge_metric metric=subscriber_state`
- `skio_metric metric=recurring_revenue`

Steps:
1. Pull `recharge_metric metric=mrr months=12` (or `skio_metric metric=recurring_revenue`).
2. Pull `recharge_metric metric=nrr`.
3. Pull `recharge_metric metric=subscriber_state` for active, paused and dormant counts.
4. Split the book-to-paid gap into skips, failures and pauses where the data allows.

Checks before answering:
- Book recurring revenue (every active subscription at list price) is a ceiling, not cash. Never call it revenue.
- A skipped charge is not churn. The subscription stays active.
- If no subscription app is connected, say so. Never say zero subscribers or zero churn.
- Use Recharge tools for Recharge brands and Skio tools for Skio brands. Never mix the two in one total.
- The current month is in flight. Leave it out.

Output:
- Answer first: paid revenue last month and the gap. Table by month: booked, paid, gap, net revenue retention.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sub-real-revenue". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
