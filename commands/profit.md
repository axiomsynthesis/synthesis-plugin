---
description: "Which Amazon products actually make money?: Each Amazon product's profit after fees, ads, returns and cost, ranked, with losers and break-even ad spenders named"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Which Amazon products actually make money?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which Amazon products actually make money?" (id: money-profit-by-product-after-everything, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what each Amazon product keeps after fees, ads, returns and product cost. It ranks them, names the losers and the ones that spend on ads but keep almost nothing, and says whether repeat buyers pay those back. Amazon only.

What to read: Settlements, ads, product costs
What to give me: Each Amazon product's profit after fees, ads, returns and cost, ranked, with losers and break-even ad spenders named

Synthesis tools to use:
- `cost_rules for=money-profit-by-product-after-everything`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=ppc_profit_by_asin`
- `amazon_metric metric=return_reasons`
- `operator_inputs`
- `product_ltv_windowed asin=<asin>`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=ppc_profit_by_asin` and no month (it picks the last settled month). Each advertised product's `profit_after_ads` is the Profit page's own profit: refunds, discounts, fees, its share of Amazon's storage and other account charges, product cost and all its ads are already taken off. Use that figure as the product's profit. Do not subtract anything from it again.
2. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3` for products with no ads that month. Their figure is before Amazon's storage and other account charges: say so beside each one.
3. Call `amazon_metric` with `metric=return_reasons` and `months=3` to explain WHY a product's refunds are high. Refunds are already in both figures above. Never subtract return cost a second time.
4. Call `operator_inputs` with `section=cogs` to check every product has a cost. Name each product with `find_product`.
5. Profit per unit = `profit_after_ads` divided by units. Rank the advertised products by profit per unit and by profit a month. Rank the products with no ads in a separate table, because their figure is on a different basis.
6. For each product under 5% of its sales after ads, call `product_ltv_windowed` with its `asin` (or its `family:<family_id>` from `find_product`). Repeat sales per first buyer = the 180-day value less the first order. Estimate the repeat profit as that times the product's margin before ads, and say it is an estimate. Add it to the profit per unit. If the sum is above zero, label the product "pays back on repeat". If not, "does not pay back".

Checks before answering:
- A product with no cost entered is flagged "no cost", never shown as pure profit.
- Use the last settled month. Fees and refunds settle late.
- Profit comes from one figure per product. Never add it up from sales, fees, ads and returns in different tools.
- If ad spend for a product is missing, say so. Do not treat it as zero ad cost.
- One bad month is not a pattern. Check the month before when a product turns negative.
- Also name every product whose profit after ads is under 5% of its sales while its ad cost is over 10% of its sales. Show its ad dollars and what it kept.
- Never mix the two bases in one ranking.
- If `product_ltv_windowed` is gated or its cohort is young, say repeat value is unknown for that product. Never label it "pays back" without the number.
- This is Amazon only. Marketing paid outside Amazon that drives Amazon sales, such as an influencer agency or Meta ads sent to Amazon, is not in these figures. Say so.

Output:
- One line first: how many products lose money, and how many make under 5% after ads, with the ad dollars behind them.
- A table of advertised products: product, units, sales, fees and account charges, ad cost, refunds, product cost, profit per unit, profit a month, and pays back on repeat or not.
- A separate table for products with no ads, marked "before account charges".
- One move: the product to fix first and what to change.

Never:
- Never change a price, budget or listing. A person does that.
- Never guess a product cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-profit-by-product-after-everything". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
