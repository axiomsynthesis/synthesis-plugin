---
description: "Are orders still coming in right after a site change?: Whether orders still flow after a new page, offer, app or theme push, whether each order holds what the offer promised at the page price, and the exact fix plus the orders that need a hand"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Are orders still coming in right after a site change?

Channel: Website · Level: On a schedule · Status: Ready now
Schedule: Every hour for the first day after a site change, then once a day for the next 6 days

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are orders still coming in right after a site change?" (id: website-order-watch-after-change, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Watches the website after anything changes: a new page, a new offer or gift, an add-on or upsell, a subscribe box, a discount code, a new app or a theme push. It answers two questions. Are orders still coming in at the usual rate for this hour and weekday? And does each order come out right: the products, gifts and add-ons the offer promised, subscriptions taken, codes behaving and the price charged equal to the page price? It ends with what broke, the fix, and the orders a person must handle before they ship.

What to read: Your website orders by hour and by day, what is on each order, subscriptions, discount codes and the change you just made
What to give me: Whether orders still flow after a new page, offer, app or theme push, whether each order holds what the offer promised at the page price, and the exact fix plus the orders that need a hand

Synthesis tools to use:
- `recall_decisions`
- `brand_brain action=moves`
- `data_freshness`
- `shopify_metric metric=daily_revenue days=49`
- `shopify_metric metric=order_tags months=1`
- `shopify_metric metric=subscription_mix months=3`
- `shopify_metric metric=aov_levers months=3`
- `run_bayesian`

Steps:
1. Read `recall_decisions` and `brand_brain` with `action=moves` and `since` 7 days ago for a logged change. Page, price and offer changes on the store are often in neither, so ask in one message: what changed, on which page, and the time it went live, and wait for it. Write down what a right order looks like: each pack, its price, its gift, its add-ons, the subscribe choice and any code.
2. Call `data_freshness` and read the store orders line's age in hours. Treat that many hours, and at least 3, as not yet in: read them from the store's own order list, never as zero. If last night's check that every store table exists and is filled failed, say so beside every count.
3. Synthesis holds no hourly orders and cannot open a single order. Orders by hour since the change come from the store's order list in the person's own browser or a pasted export, set against the same hour on the last 7 same weekdays. With neither, say in the first line: "Orders could not be opened; hours and rounds 3 and 4 not checked".
4. Call `shopify_metric` with `metric=daily_revenue` and `days=49` for closed days, so 7 prior same weekdays exist. Today is not in it. Say if ad spend jumped or a big sale (Prime days, Black Friday) falls in the window.
5. Open every order since the change, or the last 50 when there are more. For each: products and packs, gift lines, add-on and upsell lines, subscribe or one-time, discount code, price charged per line, and whether it has shipped.
6. Call `shopify_metric` with `metric=order_tags` and `months=1` for gift, upsell and subscription tags. Call it with `metric=subscription_mix` and `months=3`. Work out the first-order subscribe share per month: (subscription orders minus recurring orders) / (one-time orders plus that). The total subscription share is mostly renewals and hides a broken box. Cross-check with the first-order subscription tag count and give both when they differ.
7. Call `shopify_metric` with `metric=aov_levers` and `months=3`. A change that moves price per unit or units per order shows here.
8. For a rate with few orders, such as subscribe opt-ins, call `run_bayesian` with the usual rate as the prior and today's count.
9. For each break, name the fix and the shortcut: an add-on with /addon, a code with /codes, a gift or offer item with /offeritem, a page or a missing subscribe choice with /pagelive. Size it in dollars a month.

Checks before answering:
- Same hours, same weekday. Mornings and weekends sell less. Never compare an hour with the day's average.
- An hour with no orders can be chance: on one live brand a 1.5-hour gap on a 90-orders-a-day page closed by itself.
- Read checkouts started beside orders: checkouts with no purchases point at payment, not traffic.
- Gift and add-on rules break when a shopper swaps packs in the cart. On one live brand a free gift stayed on after a swap to a smaller pack.
- Never place, edit, refund or cancel an order. List what a person should do.

Rounds (relook before you answer):
1. **Same hours, closed days.** Re-read hourly counts, or closed days when hours are not open, against the last 7 same weekdays. Fails when: an hour or day falls below the lowest of those 7, or the hours still coming in were read as zero. Fix: call a gap only past the lowest, and mark the recent hours as still coming in.
2. **Noise or broken.** Re-run the chance of the gap or low rate at the usual rate, always including the first-order subscribe share against its earlier months. Fails when: the chance is under 5%. On one live brand it fell from 16% to under 3% of new orders. Fix: call it broken and find the cause.
3. **Order matches offer.** Re-open every order against the right-order list. Fails when: one order has a gift, add-on or pack the offer does not give, or lacks one it does. Fix: list each order, and say which have shipped. Orders not opened: "not checked", never a pass.
4. **Price charged.** Set each line's charged price against the page. Fails when: one line is a cent off, or a code took more off than it should. Fix: name the page, code or rule that caused it. Lines not opened: "not checked".
5. **Full fix, not a diagnosis.** Fails when: the answer names a break without the setting or shortcut that fixes it and the orders a person must handle. Fix: add both.
6. **After the fix.** On the next run, re-read the orders placed since the fix. Fails when: one still comes out wrong. Fix: say so and try the next cause.

Output:
- One line first: orders flowing or not, against the same hours on the last 7 same weekdays, and each break found.
- A small grid: hour or day, orders, usual for it, checkouts started (or "not available").
- Each break: what is wrong, how many orders, the dollars, the exact fix and the shortcut.
- Orders to act on before they ship: order number, what is wrong, what to do.
- One line: what this run did not check.

Never:
- Never change a page, app, code, price or order. The fixes are proposals for the person's yes.
- Never call the hours still coming in zero, or an unopened order right.
- Never show a customer's name, email or address. Use the order number.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-order-watch-after-change". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (Every hour for the first day after a site change, then once a day for the next 6 days). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
