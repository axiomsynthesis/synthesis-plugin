# Which first product makes the best customers?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which first product makes the best customers?" (id: customers-lifetime-value-by-first-product, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows which first purchase turns into your most profitable customers. It compares products at the same customer age, turns sales into what you keep after costs, and sets that against the cost to win a new customer.

What to read: Orders by customer, product margins, ad cost per new customer
What to give me: Profit per customer by first product at the same age, against the cost to win them, and which to lead with

Synthesis tools to use:
- `cost_rules for=customers-lifetime-value-by-first-product`
- `top_products metric=revenue top_n=10 start_month=<YYYY-MM> end_month=<YYYY-MM>`
- `find_product query=<name>`
- `product_ltv_windowed asin=<family> windows=[90,180,365]`
- `amazon_metric metric=breakeven_acos_ltv`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=ppc_ntb days=90`
- `first_order_contribution_margin`
- `shopify_metric metric=product_ltv`

Steps:
1. Call `top_products metric=revenue top_n=10` with `start_month` and `end_month` spanning the last 12 closed months to pick your top Amazon products. Call `find_product` with a `query` for each to get its family.
2. For each family, call `product_ltv_windowed` with `asin=family:<id>` and `windows=[90,180,365]`. It averages each window over only the customers old enough to fill it. Rank on the longest window every compared product can fill, and say how many customers each window covers.
3. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3` for each product's margin after fees, refunds and product cost. Multiply each window's sales value by that margin to get margin value.
4. Call `amazon_metric` with `metric=breakeven_acos_ltv` and each `asin` for the margin value and payback at 1, 3, 6 and 12 months. Use it to check step 3.
5. Call `amazon_metric` with `metric=ppc_ntb` and `days=90` for the cost per new-to-brand order. Then call `first_order_contribution_margin` with the `asin` and that cost as `cac` for the first-order profit after the cost to win. Margin value divided by that cost is the value-to-cost ratio. Months until margin value covers the cost is payback.
6. Call `shopify_metric` with `metric=product_ltv` for website customers by first product. It has no date window, so show it on its own line and never rank it beside Amazon.

Checks before answering:
- If a tool says a value is gated, explain why and do not state it.
- Compare products only at the same window. A window with no value means no customer is old enough. It is not a low value.
- If a window is filled by under 60% of a product's customers, say it will move as they age.
- Rank on margin value, never on sales value. A high-selling product with a thin margin can be the worst way in.
- The cost to win a customer covers Sponsored Brands and Display only. Amazon reports no new-to-brand count for Sponsored Products. So it is one account-wide figure, not a cost per product. Say so, and say the ratio cannot tell products apart on cost yet.
- Amazon order history starts about two years back. A customer who first bought before that counts as new here. Say so for long-selling products.
- A product with a few dozen customers is too small to rank. Say so.
- If product cost is missing, say margin value cannot be shown.
- If a channel's read is empty, say it is missing. Never show it as zero.

Output:
- One line first: the product to lead ads with, and how much more margin its customers bring at the same age.
- A table: first product, window, customers, sales value, margin value, cost to win, value-to-cost ratio, payback months.
- One line for the website read, with the dates it covers.
- One move: which product to lead with in ads, and how we will know it worked.

Never:
- Never change ads or offers. A person does that.
- Never mix website and Amazon values into one number.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-lifetime-value-by-first-product". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
