# Is the Subscribe and Save discount paying?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is the Subscribe and Save discount paying?" (id: mkt-amazon-sns-discount-payback, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Subscribe and Save trades a discount for repeat orders. Many shoppers take the discount once and cancel.
This weighs the discount against the repeat orders it really earns, per product.

What to read: Subscribe and Save discount given, how long subscribers stay, sign-ups that never got a second delivery, and profit per unit
What to give me: Whether your Subscribe and Save discount buys enough extra repeat orders to pay for itself, product by product

Synthesis tools to use:
- `cost_rules for=mkt-amazon-sns-discount-payback`
- `amazon_metric metric=promotion_performance months=6 limit=30`
- `amazon_metric metric=subscription_ladder limit=20`
- `amazon_metric metric=sns_fake_rate maturity_days=90 months=12`
- `amazon_metric metric=contribution_by_asin months=3`

Steps:
1. Call `amazon_metric metric=promotion_performance months=6 limit=30` and keep the Subscribe and Save rows for discount dollars by product.
2. Call `amazon_metric metric=sns_fake_rate maturity_days=90 months=12` for sign-ups that never got a second delivery.
3. Call `amazon_metric metric=subscription_ladder limit=20` for how many deliveries real subscribers take.
4. Call `amazon_metric metric=contribution_by_asin months=3` for profit per unit after fees and cost.
5. Per product: discount cost per sign-up against extra profit from the extra deliveries. Say pays, roughly even, or does not pay.

Checks before answering:
- Sign-ups younger than the maturity window cannot be judged. They are excluded. Say how many.
- Deals and coupons are not in the discount figure. Only Subscribe and Save, coupons and percent-off promotions are. Never call it total discounting.
- If a product has no entered cost, profit is unknown. Leave it out and list it.

Output:
- One line: total discount given and the share wasted on one-time sign-ups.
- A table: product, discount dollars, sign-ups, never-repeated share, deliveries per real subscriber, verdict.

Never:
- Never change Subscribe and Save tiers in the account.
- Never judge sign-ups that have not had time to repeat.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-sns-discount-payback". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
