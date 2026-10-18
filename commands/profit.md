---
description: "Which products actually make money?: Every product's profit after fees, ads, returns and product cost, ranked, with the money-losers named"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Which products actually make money?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which products actually make money?" (id: money-profit-by-product-after-everything, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what each product really keeps after Amazon fees, ads, returns and the cost to make it. It ranks them and names the ones losing money.

What to read: Settlements, ads, product costs
What to give me: Every product's profit after fees, ads, returns and product cost, ranked, with the money-losers named

Synthesis tools to use:
- `cost_rules for=money-profit-by-product-after-everything`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=ppc_profit_by_asin`
- `amazon_metric metric=return_reasons`
- `operator_inputs`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=ppc_profit_by_asin` and no month (it picks the last settled month). Each advertised product's `profit_after_ads` is the Profit page's own profit: refunds, discounts, fees, its share of Amazon's storage and other account charges, product cost and all its ads are already taken off. Use that figure as the product's profit. Do not subtract anything from it again.
2. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3` for products with no ads that month. Their figure is before Amazon's storage and other account charges: say so beside each one.
3. Call `amazon_metric` with `metric=return_reasons` and `months=3` to explain WHY a product's refunds are high. Refunds are already in both figures above; never subtract return cost a second time.
4. Call `operator_inputs` with `section=cogs` to check every product has a cost. Name each product with `find_product`.
5. Rank by profit per unit and by profit a month.

Checks before answering:
- A product with no cost entered is flagged "no cost", never shown as pure profit.
- Use the last settled month. Fees and refunds settle late.
- Profit comes from one figure per product. Never add up sales, fees, ads and returns from different tools: the per-product table already nets refunds, and it leaves out account charges.
- If ad spend for a product is missing, say so. Do not treat it as zero ad cost.
- One bad month is not a pattern. Check the month before when a product turns negative.

Output:
- One line first: how many products lose money and how much a month in total.
- A table: product, units, sales, fees and account charges, ad cost, refunds, product cost, profit per unit, profit a month, and which figure it is (Profit page, or before account charges).
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
