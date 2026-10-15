# What else your buyers put in the cart

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What else your buyers put in the cart" (id: mkt-amazon-basket-with-rivals, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Your own orders only show what people buy from you. Amazon's basket data also shows what they buy from others in the same order.
This finds products you sell that buyers are getting from a rival, and products you could target.

What to read: Amazon's market basket data, the products bought in the same order as yours, including other brands
What to give me: What your buyers pair with your product, which of those are rivals' versions of what you sell, and the bundle or ad to try

Synthesis tools to use:
- `amazon_metric metric=market_basket months=3 limit=30`
- `cross_sell`

Steps:
1. Call `amazon_metric metric=market_basket months=3 limit=30`.
2. For each pair where both products are yours, call `cross_sell asin_a=<your product id> asin_b=<your paired product id>` to see how often your own buyers take both. Judge by lift, not raw count.
3. Mark each pair: rival version of a product you sell (steal it), complementary product you do not sell (target its page), your own product (bundle).

Checks before answering:
- The pair figure is a percent of the anchor product's orders. Pairs do not add to 100.
- Amazon only reports the top few pairs per product. Missing does not mean never.

Output:
- One line: the best pairing to act on.
- A table: your product, paired product, brand (yours or other), share of orders, move.

Never:
- Never set up ads or bundles in any account.
- Never sum pair percentages.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-basket-with-rivals". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
