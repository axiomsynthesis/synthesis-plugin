---
description: "Add an add-on or after-payment upsell: A tick-box add-on under the buy button or a one-click after-payment upsell, built after your yes, with both cart lines checked and the take rate read later"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Add an add-on or after-payment upsell

Channel: Website · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Add an add-on or after-payment upsell" (id: do-shopify-order-add-on, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Sets up or changes an order-size booster.
That is a tick-box add-on under the buy button, or a one-click offer after payment.
It checks both lines land in the cart at the right price, then reads the take rate.

What to read: What your buyers add and buy next, your order sizes, the offer product and its cost
What to give me: A tick-box add-on under the buy button or a one-click after-payment upsell, built after your yes, with both cart lines checked and the take rate read later

Synthesis tools to use:
- `cost_rules for=do-shopify-order-add-on`
- `shopify_metric metric=product_attach limit=20`
- `shopify_metric metric=aov_distribution`
- `shopify_metric metric=daily_revenue days=28`
- `operator_inputs section=cogs`
- `first_order_contribution_margin`
- `shopify_metric metric=order_tags months=1 limit=50`
- `web_fetch`
- `log_decision kind=promotion`

Steps:
1. Ask in one message: product and price, pages, tick box or after payment, and the copy. Use the person's copy. Never write results-promising copy.
2. Call `shopify_metric` with `metric=product_attach`, `anchor=<a word from the page's main product title>` and `limit=20`. Without one it reads the all-time best seller. Ask; default to leading with more of what they just bought.
3. Call `shopify_metric` with `metric=aov_distribution`. It is all-time, so say so. For recent order sizes call `metric=daily_revenue` with `days=28` and divide sales by orders.
4. Call `operator_inputs` with `section=cogs`. A cost of 0 or no row means no cost: stop and ask. No product yet: use the offer product shortcut first.
5. Profit per order, with and without the add-on: call `first_order_contribution_margin` with `price`, `cogs`, shipping and packing per order as `misc` and `referral_fee_pct=2.9` for card fees. Ask the shipping cost. Count a lower shipping charge past a shipping tier.
6. Tick box: change the theme section's settings on a hidden preview theme, then live on a go. Follow the live page shortcut's steps and price checks.
7. Express pay buttons buy one product only. Hide them while an add-on is ticked.
8. After-payment upsell: open the upsell app, for example Zipify One Click Upsell, in a tab kept in front. Clicks can stop part way, so read each screen back. Build it as a draft. Turn off any countdown timer and badge. Show the offer screens.
9. Keep the after-payment price equal to the tick-box price in every funnel, changed the same day. No deep discounts.
10. A plain Shopify plan cannot show offers inside checkout. If the offer shows a subscribe price, check it is not above the one-time price.
11. On a go, publish that one offer. Then Settings, Checkout, Post-purchase page: pick the upsell app. A second offer needs its own yes.
12. Read back. Call `web_fetch` on the preview and live page for the box, price and copy. Then in the browser open /cart/clear.js, add the main product and the add-on, and open /cart.js. Both lines must show the right prices. Empty the cart after.
13. Call `log_decision` with `kind=promotion`, the offer, price, pages, `made_on` and `measure=page`. After two weeks call `shopify_metric` with `metric=order_tags`, `months=1` and `limit=50`. Use the tag "OCU Zipify Post-Purchase Upsell Bought". Divide by website orders for the same days from `daily_revenue`. Check the first tagged orders shipped as one box.

Checks before answering:
- Safe test run: when the person asks to test the shortcut, put the tick box on the preview theme only and save the upsell offer as a draft, unpublished.
- Spend: this spends nothing. Show the profit per order with and without the add-on before the yes.
- Never change an add-on while its own readout or a split test on the same buy box is running.
- The offer product sits on the online store channel only, outside any discount-code collection.
- Never copy page claims into anything sent by email.
- Ask; default keep the add-on when at least 3% of orders take it.
- Upsell undo: set the post-purchase page to None.

Output:
- One line: tick box or after payment, product, price, pages, live or draft.
- Cart check, one line per pack with and without the add-on.
- The take-rate read date.

Never:
- Never change the price of the main product.
- Never publish a second upsell offer without its own yes.
- Never accept an app's paid plan or charge. The person clicks that.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-shopify-order-add-on". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
