---
description: "Are subscriptions worth it, product by product?: For each product: does a subscriber earn more than a one-time buyer after the discount and shipping, and the one change worth making"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Are subscriptions worth it, product by product?

Channel: Subscriptions · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are subscriptions worth it, product by product?" (id: check-subscriptions-worth-it, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks whether a subscription pays, product by product, before you change the offer. It weighs how long subscribers stay, skips, the discount and shipping on each box, against a one-time buyer.

What to read: Subscriptions by product, lifespan, skips and failed charges, the subscription discount, shipping per box and product cost
What to give me: For each product: does a subscriber earn more than a one-time buyer after the discount and shipping, and the one change worth making

Synthesis tools to use:
- `cost_rules for=check-subscriptions-worth-it`
- `recharge_metric metric=product_subscriptions limit=50`
- `recharge_metric metric=survival`
- `recharge_metric metric=rebill_health months=6`
- `recharge_metric metric=discount_penetration months=6`
- `shopify_metric metric=subscription_mix months=12`
- `shopify_metric metric=product_ltv`
- `skio_metric metric=product_subscriptions`
- `operator_inputs section=cogs`
- `subscription_economics`

Steps:
1. Ask: which products, today's offer (discount, free shipping, a gift), and shipping cost per box. No tool reads the shipping profile.
2. Call `recharge_metric` with `metric=product_subscriptions` and `limit=50`. Use billing_active_subs, not active_subs, which counts dormant ones. If it returns no products, call `skio_metric` with `metric=product_subscriptions`.
3. Months kept per product is avg_lifespan_days_churned from step 2. Call `recharge_metric` with `metric=survival` for the brand-wide curve only. Never use the churn metric's rate. It counts dormant subscriptions.
4. Call `recharge_metric` with `metric=rebill_health` and `months=6`. Skip rate is skips over due charges. On one live brand it ran 61 to 64%. Count only charges that went through. A closed month with past-due charges still queued cannot be read. Use the last fully read months.
5. Call `recharge_metric` with `metric=discount_penetration` and `months=6` for the discount subscribers really get.
6. Call `shopify_metric` with `metric=subscription_mix` and `months=12`. Read subscription order counts, not the share, which falls in marketplace spike months.
7. Call `operator_inputs` with `section=cogs` for product cost, and `shopify_metric` with `metric=product_ltv` for one-time buyer value. It mixes in subscribers, so it is the high end. Call `subscription_economics` with monthly churn (3000 over lifespan days), order size, discount and that value. Multiply its subscriber value by (1 minus skip rate). The tool assumes every month bills.
8. Shipping: a hidden profile can ship every box free. Count step 1's cost per box. The person can check the app settings without saving.
9. Verdict per product: keep, change the perk, or one-time only. One perk only, never discount plus free shipping plus a gift. Keep the price above any floor held on another channel.
10. Draft a note to the subscription app's support if needed. Send it only when the person says "send it".

Checks before answering:
- Safe test: this only reads. Nothing in the store or the app changes.
- Spend: say the dollars a month the discount and free shipping cost across billing subscribers.
- Counts must tie to the app's own totals. If not, say by how much.
- If product cost is missing, give revenue per subscriber only.
- Under 50 billing subscribers on a product is too thin to judge.
- Changing the store-wide shipping profile changes every renewal. Never call it small.
- A new default cadence applies to new subscribers only.

Output:
- One line first: which products' subscriptions pay and which lose money.
- A table: product, billing subscribers, months kept, skip rate, profit per box after discount and shipping, verdict.
- The one change worth making, and what to measure in 60 days.

Never:
- Never change existing subscribers' price, shipping, cadence or products.
- Never send anything to support without "send it".
- Never count a skipped charge as revenue.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: check-subscriptions-worth-it". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
