# The cadence and pack size that keep subscribers

Channel: Subscriptions · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "The cadence and pack size that keep subscribers" (id: grw-sub-cadence-and-pack, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Compares retention across delivery intervals and pack sizes. The default you show at signup decides most of churn, so pick the one that keeps people.

What to read: Subscription interval mix and retention by quantity tier
What to give me: The delivery interval and pack size that keep subscribers longest, to make the default

Synthesis tools to use:
- `recharge_metric metric=interval_mix`
- `recharge_metric metric=quantity_tier_retention`
- `recharge_metric metric=survival`

Steps:
1. Pull `recharge_metric metric=interval_mix`.
2. Pull `recharge_metric metric=quantity_tier_retention`.
3. Pull `recharge_metric metric=survival`.
4. Rank intervals and pack sizes by month-3 retention and revenue per subscriber.

Checks before answering:
- If no subscription app is connected, say so. Never say zero subscribers or zero churn.
- A weekly subscription counts about 4.3 charges a month, not 4.
- Groups under 50 subscribers are flagged as small.

Output:
- Answer first: the default to offer. Table: interval or pack, subscribers, month-3 retention, revenue per subscriber.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sub-cadence-and-pack". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
