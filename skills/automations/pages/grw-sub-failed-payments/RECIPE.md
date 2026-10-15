# Recover failed subscription payments

Channel: Subscriptions · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Recover failed subscription payments" (id: grw-sub-failed-payments, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Some subscribers leave only because a card failed. This sizes the money in failed charges each month and checks how much of churn comes from payments rather than choice.

What to read: Failed and retried subscription charges and the money behind them
What to give me: Dollars stuck in failed card payments, and the recovery steps to add

Synthesis tools to use:
- `recharge_metric metric=rebill_health months=3`
- `skio_metric metric=dunning_exposure`
- `recharge_metric metric=churn months=6`

Steps:
1. Pull `recharge_metric metric=rebill_health months=3` (or `skio_metric metric=dunning_exposure` on Skio).
2. Pull `recharge_metric metric=churn months=6` and read the share of cancellations from payment errors.
3. Report failed charges, their dollar value and how many were retried.

Checks before answering:
- If no subscription app is connected, say so. Never say zero subscribers or zero churn.
- Use Recharge tools for Recharge brands and Skio tools for Skio brands. Never mix the two in one total.
- Exposure is money at risk, not expected loss. Recovery rates need charge history that is not synced. Say so.
- Never say no churn comes from failed payments without reading the error count.

Output:
- Answer first: dollars in failed charges per month. Table: month, failed charges, value, retried, share of churn from payment errors.
- Three recovery steps: retry timing, card update email, SMS reminder.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sub-failed-payments". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
