---
description: "Set up a discount code or offer: One Shopify discount code or automatic discount, built in your admin after your yes, with profit per order shown first and every price checked in the cart"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Set up a discount code or offer

Channel: Website · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Set up a discount code or offer" (id: do-shopify-discount-code, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Creates or changes one Shopify discount code or automatic discount for an offer.
That covers a page-only code, a minimum spend, a free gift or a pack saving.
It shows the profit per order first, builds it after your yes, then checks the price in the cart.

What to read: Your order sizes, your product costs, the page that uses the offer
What to give me: One Shopify discount code or automatic discount, built in your admin after your yes, with profit per order shown first and every price checked in the cart

Synthesis tools to use:
- `cost_rules for=do-shopify-discount-code`
- `shopify_metric metric=aov_distribution`
- `shopify_metric metric=daily_revenue days=30`
- `first_order_contribution_margin`
- `web_fetch`
- `log_decision kind=promotion`

Steps:
1. Ask in one message: code or automatic, the value, the minimum spend, which products or collection, which page uses it, start and end dates, and what it may combine with.
2. Ask the cost of each product it touches. Never assume a cost. If cost rulings could not be read, say so and use only costs the person gives in chat.
3. Call `shopify_metric` with `metric=aov_distribution` to see where a minimum spend would land. It takes no window and returns all-time order sizes. Say so. For today's order size, call `shopify_metric` with `metric=daily_revenue` and `days=30`.
4. Call `first_order_contribution_margin` with `price`, `cogs` and `discounts` passed by hand for each pack the offer touches. It has no shipping field. Pass shipping, warehouse and card fees as `misc`, and add the shipping the shopper pays to `price`. Show profit per order. Only propose offers that keep it positive.
5. Ask. Default to a free extra or free shipping over a percent off. A percent off on a pack that is already discounted usually loses money. Ask before allowing it.
6. In Shopify admin, Discounts, fill the form exactly as approved.
7. Combining: a free-gift buy X get Y discount combines with nothing. A shopper using an email code then pays for the "free" gift. Price the gift product at $0 instead. Two product discounts on one line do not stack. Shopify applies the better one.
8. Never let codes for one product line stack with codes for another unless the person asks.
9. Turning off combining on one code can break a bundle page price. Check every page that uses the products.
10. Press Save. The safety check often blocks Save even after a yes. Then leave the form filled and ask the person to click Save.
11. A page-only code keeps store prices unchanged. The page applies it with the store's discount link. That page change goes through the live page shortcut.
12. Read back. Reload the discount and read every field. Add each pack to the cart, with and without each add-on and with and without an email code. Read the cart and checkout price. Place no order. Remove every code and empty the cart after. Call `web_fetch` on the page to confirm its price still equals checkout.
13. Call `log_decision` with `kind=promotion`, the code, value, dates, the profit per order, `measure` and `made_on`.

Checks before answering:
- Safe test run: when the person asks to test the shortcut, create a code like CLAUDETEST1 at 1% off, $9,999 minimum, on one hidden test product, ending tomorrow. Make that product first with the offer product shortcut's safe test. Read it back after reload. Nobody can trigger it.
- Spend: a discount is money given up. Show the dollars given up per order and at expected volume before the yes.
- New products may fall into a smart collection that a code covers. Check what is in it.
- Rebuilding a code resets its one-use-per-customer history. Rename old codes instead.

Output:
- One line: the code or offer, value, minimum, dates, live or scheduled.
- Profit per order for each pack it touches.
- Cart check, one line per pack and code.

Never:
- Never delete a code. Rename or end it.
- Never place an order to test a price.
- Never change store prices for a page-only offer.
- Never save an offer that makes profit per order negative without the person calling it a loss leader.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-shopify-discount-code". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
