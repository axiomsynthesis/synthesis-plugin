# Subscription cash coming in the next 8 weeks

Channel: Subscriptions · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Subscription cash coming in the next 8 weeks" (id: grw-sub-upcoming-charges, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lists the charges already scheduled for the next eight weeks and cuts them by how many usually skip, fail or cancel. It gives finance a subscription cash line it can trust.

What to read: Scheduled subscription charges for the coming weeks
What to give me: Expected subscription revenue week by week, with a realistic haircut

Synthesis tools to use:
- `recharge_metric metric=upcoming_charges weeks=8`
- `recharge_metric metric=mrr months=6`
- `recharge_metric metric=rebill_health months=3`

Steps:
1. Pull `recharge_metric metric=upcoming_charges weeks=8`.
2. Pull `recharge_metric metric=mrr months=6` for booked against realized in past months.
3. Pull `recharge_metric metric=rebill_health months=3` for the failure share.
4. Apply the past realized-to-booked ratio to each future week.

Checks before answering:
- Book recurring revenue (every active subscription at list price) is a ceiling, not cash. Never call it revenue.
- Use the expected revenue the tool returns, not the raw scheduled total.
- If no subscription app is connected, say so. Never say zero subscribers or zero churn.
- A skipped charge is not churn. The subscription stays active.

Output:
- Answer first: expected next 8 weeks. Table by week: scheduled, expected after skips and failures.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sub-upcoming-charges". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
