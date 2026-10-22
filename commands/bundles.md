---
description: "Find bundles buyers already want: The best pair to bundle on your top sellers, what it keeps after fees and lost full-price sales, and a test"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Find bundles buyers already want

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find bundles buyers already want" (id: customers-bundle-finder, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds the products people buy together more often than chance, starting from your top sellers. It works out what a bundle keeps after Amazon fees and product costs, against the full-price sales it replaces, and names a test to prove it.

What to read: Orders, Amazon fees and product costs
What to give me: The best pair to bundle on your top sellers, what it keeps after fees and lost full-price sales, and a test

Synthesis tools to use:
- `cost_rules for=customers-bundle-finder`
- `top_products metric=revenue top_n=5 start_month=<YYYY-MM> end_month=<YYYY-MM>`
- `amazon_metric metric=market_basket months=1`
- `shopify_metric metric=market_basket`
- `sequenced_cross_sell`
- `amazon_metric metric=contribution_by_asin months=3`
- `first_order_contribution_margin`
- `find_product`
- `cross_sell window=90d`

Steps:
1. Call `top_products metric=revenue top_n=5` with `start_month` and `end_month` spanning the last 3 closed months for your top products and their codes.
2. For each, call `amazon_metric` with `metric=market_basket`, that `asin` and `months=1` for the newest month. Say which month it covers.
3. Call `shopify_metric` with `metric=market_basket` for website pairs, ranked by lift: how many times more often the two sell together than chance. It covers all time, so use `find_product` to check each product is still active and skip pairs with one that is not.
4. For the top three pairs where both products are yours, call `sequenced_cross_sell` with both product codes to see which is bought first. It only sees your own orders.
5. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3` for each product's keep per unit and its fees. Referral fee divided by sales is the referral rate. Ask the person for the bundle's fulfilment fee from Amazon's fee preview.
6. For a bundle price, call `first_order_contribution_margin` with `price`, `cogs` as both product costs, `referral_fee_pct` and `fba_fee` as the bundle's fee. That is what one bundle keeps.
7. Compare with selling apart. Let s be the share of bundle buyers who would have bought both anyway. The rest would have bought only the lead product. The bundle wins when its keep is above s times both items' keep plus the rest times the lead's keep. Give the deepest discount that still wins at s of 0%, 25% and 50%.

Checks before answering:
- Judge pairs by lift, not raw count. Your two best sellers will pair by chance. Where a report gives no lift, say so.
- Amazon reports only the top three pairs per product and gives a share of buyers, with no order count. If a website pair rests on under 50 orders, say it is a small sample.
- We cannot look up the fee for a bundle that is not listed yet. Without the person's fee, leave the bundle keep blank and give the formula.
- The share who would have bought both anyway is not measured. Show all three cases, never one.
- There is no margin read for website-only pairs. Leave their price blank and say so.
- If product costs are missing, say so and do not set a price.

Rounds (relook before you answer):
1. **Chance or real pair.** Re-read each pair's lift and buyer count. Fails when: a chosen pair has lift under 1.5, or a website pair rests on under 50 orders. Fix: drop it and take the next pair.
2. **What they buy next.** Call `cross_sell` with both codes and `window=90d`. Fails when: under 5% of the lead's buyers buy the second item within 90 days, or more of them rebuy the lead itself. Fix: offer a bigger pack of the lead instead of a pair.
3. **Argue the losing case.** Re-run step 7 at a 50% share who would have bought both anyway. Fails when: the bundle keeps less than selling apart at the proposed discount. Fix: a shallower discount, or a free extra in place of a percent off.
4. **Price ladder.** Check the bundle price against each item's own price and any multi-pack already listed. Fails when: the bundle costs more per unit than buying apart, or undercuts an existing pack by over 10%. Fix: reprice between them.
5. **Second product.** Run steps 2 to 7 for the second-best seller too. Fails when: the winning rule holds for one product only. Fix: say the bundle is a one-product play, not a range rule.

Output:
- One line first: the bundle to test, which product leads, what it keeps per sale, and the deepest discount that still wins.
- A table: pair, share buying both, lift where known, which comes first, bundle price, bundle keep, keep sold apart, deepest discount at 0%, 25% and 50%.
- One test: four weeks, the bundle as a listing variation or a website offer to half of visitors. Read units per order and profit per visitor against the other half.

Never:
- Never create a bundle or listing in any store. A person does that.
- Never set a price without a known product cost.
- Never forecast monthly bundle sales. No read measures it.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-bundle-finder". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
