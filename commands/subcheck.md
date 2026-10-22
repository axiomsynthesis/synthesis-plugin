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
9. Verdict per product: keep, change the perk, or one-time only. One perk only, never discount plus free shipping plus a gift. Keep the price above any floor held on another channel. Offer the subscription at the first checkout: on one live brand 8.6% subscribed there against 0.3% of one-time buyers later. Default plans: small pack every 1, 2 or 3 months, bigger pack every 3, 4 or 6.
10. Draft a note to the subscription app's support if needed. Send it only when the person says "send it".

Checks before answering:
- Safe test: this only reads. Nothing in the store or the app changes.
- Spend: say the dollars a month the discount and free shipping cost across billing subscribers.
- Counts must tie to the app's own totals. If not, say by how much.
- If product cost is missing, give revenue per subscriber only.
- Under 50 billing subscribers on a product is too thin to judge.
- Changing the store-wide shipping profile changes every renewal. Never call it small.
- A new default cadence applies to new subscribers only.

Rounds (relook before you answer):
1. **Enough subscribers.** Fails when: a product has under 50 billing subscribers. Fix: mark its verdict "too thin" and leave it out of the headline.
2. **Skips counted.** Re-check that subscriber value was multiplied by (1 minus skip rate). Fails when: it was not, or the skip rate used is from a month with charges still queued. Fix: redo with the last fully read months.
3. **Hidden free shipping.** Divide subscription order revenue from `subscription_mix` by its order count. Fails when: that is below the price after discount plus the shipping the person said subscribers pay. Fix: say renewals likely ship free, and count step 1's cost per box against every renewal.
4. **Price floor.** Fails when: any subscription price is below the lowest price held on another channel. Fix: make that pack one-time only or cut the discount.
5. **Self-choice.** Subscribers chose to come back, so their value runs high. Fails when: the verdict "keep" rests on under $5 a customer more than one-time buyers. Fix: call it even, not a win.

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
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: check-subscriptions-worth-it". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
