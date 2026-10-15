# What the subscribe discount really costs

Channel: Subscriptions · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What the subscribe discount really costs" (id: grw-sub-discount-cost, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Adds up what subscription discounts cost each month and checks whether discounted subscribers stay long enough to earn it back. It uses a simple model to compare subscriber value with one-time buyers.

What to read: Subscription discount use, depth and subscriber value
What to give me: The dollars given away in subscription discounts, and whether they buy longer stays

Synthesis tools to use:
- `recharge_metric metric=discount_penetration months=6`
- `recharge_metric metric=subscriber_ltv`
- `subscription_economics`

Steps:
1. Pull `recharge_metric metric=discount_penetration months=6`.
2. Pull `recharge_metric metric=subscriber_ltv`.
3. Run `subscription_economics monthly_churn_pct=<value> sub_aov=<value> discount_pct=<value> nonsub_ltv=<value>` with the brand's figures.
4. Show discount dollars per month and the value premium of a subscriber over a one-time buyer.

Checks before answering:
- If no subscription app is connected, say so. Never say zero subscribers or zero churn.
- Discount codes on subscriptions are often text, not numbers. Report how many charges carried a readable discount.
- If one-time buyer value is unknown, say the comparison cannot be made.

Output:
- Answer first. Discount dollars per month and the subscriber value premium. One line on whether to change the discount.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-sub-discount-cost". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
