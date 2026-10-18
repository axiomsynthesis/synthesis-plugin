# Stop discounts stacking on one order

Channel: Amazon · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Stop discounts stacking on one order" (id: mkt-amazon-stacked-discount-leak, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Amazon lets several discounts land on one order. A coupon on top of Subscribe and Save can push a product below cost.
This finds orders with stacked promotions and the products where the stack loses money.

What to read: Orders that carried more than one promotion at once, and the discount given on each
What to give me: What you lose when coupons, Subscribe and Save and percent-off promos pile onto one order, and which products it hits

Synthesis tools to use:
- `cost_rules for=mkt-amazon-stacked-discount-leak`
- `amazon_metric metric=promotion_performance months=3 limit=40`
- `amazon_metric metric=contribution_by_asin months=3`

Steps:
1. Call `amazon_metric metric=promotion_performance months=3 limit=40`. Note which products carry more than one promotion type in the same months.
2. Once the per-order read exists: for each product with stacked orders, compute total discount share on those orders. Until then, say which products could stack and stop there.
3. Call `amazon_metric metric=contribution_by_asin months=3` for profit per unit. Flag products where stacked discount exceeds profit per unit.

Checks before answering:
- One order can carry several promotion ids. Never add promotion totals across rows without removing the overlap. The tool flags it.
- Deals and Prime-only discounts are not in this data. Say the leak may be larger during events.
- A product with no entered cost cannot be judged. List it.

Output:
- One line: dollars lost on stacked orders and the worst product.
- A table: product, stacked orders, average total discount, profit per unit, loss.

Never:
- Never change promotions in Seller Central.
- Never sum overlapping promotions.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-stacked-discount-leak". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): The promotion tool reports payback per promotion and warns that one order can carry several, but it does not count stacked orders per product. A per-order read of promotions landing together is not built. Do the parts you can and say plainly what is missing.
