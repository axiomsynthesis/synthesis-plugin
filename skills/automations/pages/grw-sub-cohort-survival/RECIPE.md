# Are new subscribers staying longer?

Channel: Subscriptions · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are new subscribers staying longer?" (id: grw-sub-cohort-survival, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Compares how many subscribers from each start month are still active after 1, 3 and 6 months. It shows whether retention is getting better or worse before revenue tells you.

What to read: Month-by-month subscription survival for each start month
What to give me: Whether recent subscriber groups stay longer or shorter than older ones

Synthesis tools to use:
- `recharge_metric metric=survival`
- `skio_metric metric=survival`
- `recharge_metric metric=cohort_ltv`

Steps:
1. Pull `recharge_metric metric=survival` (or `skio_metric metric=survival` on Skio).
2. Pull `recharge_metric metric=cohort_ltv`.
3. Compare month 3 survival for the last three complete cohorts against the three before.

Checks before answering:
- If no subscription app is connected, say so. Never say zero subscribers or zero churn.
- Use Recharge tools for Recharge brands and Skio tools for Skio brands. Never mix the two in one total.
- Young cohorts have not reached month 3 or 6. Leave those cells blank, never zero.
- Groups under 50 subscribers are flagged as small.

Output:
- Answer first. Table: start month, starters, month 1, month 3, month 6 survival.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sub-cohort-survival". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
