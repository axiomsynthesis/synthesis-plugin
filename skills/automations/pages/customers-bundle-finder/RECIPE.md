# Find bundles buyers already want

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find bundles buyers already want" (id: customers-bundle-finder, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds the products people buy together, more often than chance. It picks the best pair to bundle, sets a bundle price that keeps your margin, and says which product should lead.

What to read: Orders
What to give me: The products people buy together, the best pair to bundle, and a bundle price that keeps your margin

Synthesis tools to use:
- `shopify_metric metric=market_basket`
- `amazon_metric metric=market_basket`
- `sequenced_cross_sell`
- `amazon_metric metric=pnl_by_asin`
- `find_product`

Steps:
1. Call `shopify_metric` with `metric=market_basket` for website pairs ranked by lift. This read has no date setting, so say the dates the result covers.
2. Call `amazon_metric` with `metric=market_basket` and `limit=20` for Amazon pairs.
3. For the top three pairs, call `sequenced_cross_sell` with both product IDs for which product is bought first.
4. Call `amazon_metric` with `metric=pnl_by_asin` for each product's margin per unit.
5. Use `find_product` to name each product, then set a bundle price that keeps the margin above the single-product level.

Checks before answering:
- Judge pairs by lift, not raw count. Your two best sellers will pair by chance.
- If product costs are missing, say so and do not set a price.
- If a pair rests on only a few dozen buyers, say it is a small sample.

Output:
- One line first: the best bundle and its expected monthly sales in dollars.
- A table: pair, share buying both, lift, which comes first, bundle price, margin per bundle.
- One move: the bundle to test first, and how we will know it worked.

Never:
- Never create a bundle or listing in any store. A person does that.
- Never set a price without a known product cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-bundle-finder". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
