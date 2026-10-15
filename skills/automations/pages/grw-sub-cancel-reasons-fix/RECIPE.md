# Why subscribers cancel, and what to change

Channel: Subscriptions · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Why subscribers cancel, and what to change" (id: grw-sub-cancel-reasons-fix, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Groups the reasons subscribers give when they cancel and turns each into a change you can make. Too much product is usually a timing problem, not a product problem.

What to read: Subscription cancellation reasons by month and product
What to give me: The top cancel reasons turned into product, cadence and offer changes

Synthesis tools to use:
- `recharge_metric metric=cancellation_reasons months=6`
- `recharge_metric metric=interval_mix`
- `recharge_metric metric=product_subscriptions limit=20`

Steps:
1. Pull `recharge_metric metric=cancellation_reasons months=6`.
2. Pull `recharge_metric metric=interval_mix` and `recharge_metric metric=product_subscriptions limit=20`.
3. Rank named reasons by count. Show other as a residual, not a driver.
4. Map each top reason to a change: too much product to a longer interval or skip offer, too expensive to a smaller pack, did not work to a product question.

Checks before answering:
- If no subscription app is connected, say so. Never say zero subscribers or zero churn.
- Report how many cancellations had a named reason.
- Payment-error cancellations are a different problem. Keep them apart.

Output:
- Answer first. Table: reason, cancellations, share, change to make.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sub-cancel-reasons-fix". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
