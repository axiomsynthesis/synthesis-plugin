---
description: "Add an add-on or after-payment upsell: A tick-box add-on under the buy button, or an after-payment upsell only once a real order proves the item ships, built after your yes, with both cart lines checked and the take rate read later"
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
Sets up or changes an order-size booster: a tick-box add-on under the buy button, or a one-click offer after payment.
Hard stop, said up front: an after-payment upsell is never called done until one real paid order is proven to ship with the extra item. On one live brand the app added the item after the order had already gone to the warehouse. 20 of 20 buyers were charged and none got the item. Default to the tick box. It is in the order before payment.

What to read: What your buyers add and buy next, your order sizes, the offer product and its cost
What to give me: A tick-box add-on under the buy button, or an after-payment upsell only once a real order proves the item ships, built after your yes, with both cart lines checked and the take rate read later

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
5. Profit per yes: call `first_order_contribution_margin` with `price`, `cogs`, extra postage, pick and packing as `misc` and `referral_fee_pct=2.9`. Ask the extra postage when the box gets heavier.
6. Tick box: change the theme section's settings on a hidden preview theme, then live on a go. Follow the live page shortcut's steps and price checks. Hide express pay buttons while an add-on is ticked. They buy one product only.
7. After payment, before building: ask how orders reach the warehouse. If they go the moment an order is placed, an item added after payment never ships. Stop and say so, unless the person shows the sync waits for the app's hold or picks up order edits.
8. Build in the upsell app in a tab kept in front. Clicks can stop part way, so read each screen back. Save as a draft. Turn off countdown timers and badges. Keep its price equal to the tick-box price. A plain Shopify plan cannot show offers inside checkout. A subscribe price must not be above the one-time price.
9. On a go, publish that one offer, then Settings, Checkout, Post-purchase page: pick the app. A second offer needs its own yes.
10. Read back. Call `web_fetch` on the preview and live page for box, price and copy. In the browser open /cart/clear.js, add the main product and the add-on, open /cart.js. Both lines at the right prices. Empty the cart.
11. Call `log_decision` with `kind=promotion`, the offer, price, pages, `made_on` and `measure=page`.
12. Ship proof: call `shopify_metric` with `metric=order_tags`, `months=1` and `limit=50` for the app's tag. It counts buyers, never shipping. Open the first tagged orders in admin: each must show the extra line Fulfilled in the same shipment. One shipped without it: ask to set Post-purchase page to None the same day, and list tagged orders not yet shipped so the item is added first.

Checks before answering:
- Safe test run: tick box on the preview theme only, upsell saved as a draft, unpublished.
- Spend: this spends nothing. Show profit per yes before the yes.
- Never change an add-on while its own readout or a split test on the same buy box runs.
- The offer product sits on the online store only, outside any discount-code collection.
- Ask; default keep the add-on when at least 3% of orders take it.

Rounds (relook before you answer):
1. **Ship proof.** Re-run step 12 and open every tagged order. Fails when: any tagged order is Fulfilled without the extra line, or none has shipped yet. Fix: say "not proven", ask to set Post-purchase page to None, list orders to fix.
2. **Price match.** Re-read /cart.js for every pack with and without the add-on, and the after-payment screen. Fails when: any line is 1 cent off the page, or the after-payment price differs from the tick box. Fix: correct the price, re-run.
3. **Money per yes.** Re-run `first_order_contribution_margin` with the real extra postage. Fails when: money kept per yes is under $0, or the box crosses a heavier postage band the draft did not count. Fix: raise the price or pick a lighter item.
4. **Take-rate bar.** After 2 weeks divide tagged orders by website orders from `daily_revenue` for the same days. Fails when: under 3%, or under the tick box's own take. On one live brand after payment took 2.86% against 4.0% for the tick box. Fix: propose turning it off.
5. **Free gift eats the add-on.** Re-run `product_attach` before and after any free gift of the same item. Fails when: the paid add-on's take fell by a third or more. One live brand fell from 17.5% to 5.7%. Fix: drop the gift or swap the add-on.

Output:
- First line: tick box or after payment, product, price, pages, live or draft, and ship proof yes or not yet.
- Cart check, one line per pack with and without the add-on.
- The take-rate read date.

Never:
- Never call an after-payment upsell done before one real order shipped with the item.
- Never change the price of the main product.
- Never publish a second upsell offer without its own yes.
- Never accept an app's paid plan or charge. The person clicks that.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-shopify-order-add-on". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
