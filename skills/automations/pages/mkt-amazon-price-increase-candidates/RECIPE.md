# Which products can take a price rise?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which products can take a price rise?" (id: mkt-amazon-price-increase-candidates, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Most brands underprice their strongest products. This screens for products whose rating, conversion and share say shoppers would pay more, and sizes a test.

What to read: Each product's price against the shelf, rating, review lead, search purchase share, conversion and profit per unit
What to give me: The products with the strongest case for a price increase, the size to test, and the profit it adds if units hold

Synthesis tools to use:
- `cost_rules for=mkt-amazon-price-increase-candidates`
- `amazon_metric metric=shelf_position days=30 limit=40`
- `amazon_metric metric=conversion_funnel days=30 limit=40`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=search_query_performance grain=month periods=2 scope=nonbranded top=30`
- `measurable_test`

Steps:
1. Call `amazon_metric metric=shelf_position days=30 limit=40` for price and rating against tracked rivals.
2. Call `amazon_metric metric=conversion_funnel days=30 limit=40` for conversion against your average.
3. Call `amazon_metric metric=search_query_performance grain=month periods=2 scope=nonbranded top=30` for purchase share on each product's top searches.
4. Call `amazon_metric metric=contribution_by_asin months=3` for profit per unit.
5. A candidate is below shelf median price, at or above median rating, above-average conversion, and steady or rising share. For each, compute the unit drop that cancels the gain. Set up the test with `measurable_test`.

Checks before answering:
- A product that has a deal or coupon running will read cheaper than its list price. Use list price.
- Rival rows need the watchlist. Say if it is empty.
- Shares are percentages already. Never rescale.
- Missing product cost means unknown profit. Leave the product out.

Output:
- One line: products with room and the total monthly upside.
- A table: product, price, shelf median, rating, conversion index, search share, suggested rise, break-even unit drop.

Never:
- Never change prices.
- Never test more than one price change on the same product at once.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-price-increase-candidates". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
