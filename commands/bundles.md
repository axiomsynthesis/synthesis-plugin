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
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-bundle-finder". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
