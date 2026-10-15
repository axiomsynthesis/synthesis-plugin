# Bring back past subscribers

Channel: Subscriptions · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Bring back past subscribers" (id: grw-sub-reactivation-pool, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds past subscribers most likely to come back: long tenure, recent exit, a fixable reason. It drafts the come-back offer by reason, for a person to send.

What to read: Cancelled and paused subscribers, when they left and what they bought
What to give me: Past subscribers worth a come-back offer, ranked, with the offer for each

Synthesis tools to use:
- `recharge_metric metric=reactivation months=12`
- `recharge_metric metric=subscriber_rfm`
- `recharge_metric metric=cancellation_reasons months=12`

Steps:
1. Pull `recharge_metric metric=reactivation months=12`.
2. Pull `recharge_metric metric=subscriber_rfm` and keep cancelled or paused customers.
3. Pull `recharge_metric metric=cancellation_reasons months=12` and attach the reason where known.
4. Rank by past charges and recency of exit. Draft one offer per reason group.

Checks before answering:
- If no subscription app is connected, say so. Never say zero subscribers or zero churn.
- Count customers, not subscriptions. One customer can hold two.
- Exclude anyone who cancelled for a product reaction or complaint.

Output:
- A spreadsheet via `export_xlsx` named reactivation-list-<date>.xlsx: customer id, tenure, exit month, reason, offer. Plus offer copy per group.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never send messages. A person exports the segment.
- Never put customer emails into chat. Keep them in the file.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sub-reactivation-pool". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
