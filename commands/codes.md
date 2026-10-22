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
- One perk per offer. No code on a page that is already discounted.

Rounds (relook before you answer):
1. **Every pack still makes money.** Re-run `first_order_contribution_margin` for every pack the code can reach, the smallest pack first. Fails when: any pack's profit per order after the code, shipping, warehouse and card fees is under $0. Fix: raise the minimum, exclude that pack, or switch to a free extra.
2. **Minimum spend lands above today's order.** Re-read `daily_revenue` for today's order size. Fails when: the minimum is at or below today's average order, so the code pays people who would buy anyway. One live brand set its welcome code at a $45 minimum. Fix: raise it.
3. **Stacking in the cart.** Add each pack with the code plus every other live code, gift and automatic discount. Fails when: any checkout total is below the approved lowest price, or a "free" gift line shows a price above $0 with an email code. Fix: turn off combining, or use a $0 gift version of the pack.
4. **Everything that names the code says the same thing.** Read every page with `web_fetch`, and ask for the emails and pop-ups that state the code. Fails when: any of them states a different value, minimum or end date. Fix: reword them the same day.
5. **Pages that use these products still match.** Fails when: any page's shown price differs from checkout after the change. Fix: put the old setting back and ask.

Output:
- One line: the code or offer, value, minimum, dates, live or scheduled.
- Profit per order for each pack it touches.
- Cart check, one line per pack and code.

Never:
- Never delete a code. Rename or end it.
- Never place an order to test a price.
- Never change store prices for a page-only offer.
- Never save an offer that makes profit per order negative without the person calling it a loss leader.
- Never stack a percent off, free shipping and a gift on one offer.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-shopify-discount-code". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
