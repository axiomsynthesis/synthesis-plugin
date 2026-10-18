---
description: "Which first product makes the best customers?: Customer lifetime value by the product they bought first and the channel, and which product to lead with"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Which first product makes the best customers?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which first product makes the best customers?" (id: customers-lifetime-value-by-first-product, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows which first purchase turns into your best customers over time. It gives the lifetime value of customers by the product they bought first, on your website and on Amazon, so you know which product to lead with in ads.

What to read: Orders by customer
What to give me: Customer lifetime value by the product they bought first and the channel, and which product to lead with

Synthesis tools to use:
- `cost_rules for=customers-lifetime-value-by-first-product`
- `shopify_metric metric=product_ltv`
- `top_products metric=revenue top_n=10 start_month=<YYYY-MM> end_month=<YYYY-MM>`
- `find_product query=<name>`
- `product_ltv`
- `repeat_rate`

Steps:
1. Call `shopify_metric` with `metric=product_ltv` for website customers by first product: count, value, orders and repeat rate. This read has no date setting, so say the dates the result covers.
2. Call `top_products metric=revenue top_n=10` with `start_month` and `end_month` spanning the last 12 closed months to pick your top Amazon first products and their IDs. To look up one product by name, call `find_product` with a `query`. It needs one.
3. For each, call `product_ltv` with the `asin` and `window=365d` for the value of customers who started there.
4. Call `repeat_rate` with the same `asin` for the share of those first-time buyers who ever ordered again. It is the same measure as the website repeat rate in step 1.
5. Rank first products by 12-month value, side by side for each channel.

Checks before answering:
- If a tool says the value is gated, explain why and do not state it.
- Recent customers have not had a full year. Compare only groups old enough for the window.
- A first product with only a few dozen customers is too small to rank. Say so.
- Amazon order history reaches back about two years and the website's further. Say each repeat rate covers its own span.
- If a channel's read is empty, say it is missing. Never show it as zero value.

Output:
- One line first: the best first product and how much more its customers are worth.
- A table: first product, channel, customers, 12-month value, repeat rate.
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

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
