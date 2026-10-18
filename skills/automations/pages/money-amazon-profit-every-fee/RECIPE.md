# Amazon profit after every fee and cost

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Amazon profit after every fee and cost" (id: money-amazon-profit-every-fee, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what Amazon really left you for one month after every cost: discounts, refunds, the referral fee, fulfilment, storage, inbound freight and placement, removal and disposal, deal and coupon fees, other Amazon charges, unlabelled deductions, product cost, lost stock and Amazon ads. It matches the Profit page to the cent, then breaks it down per unit and per product.

What to read: Amazon sales, discounts, refunds, every Amazon fee and account charge, product cost and Amazon ads, as the Profit page shows them
What to give me: One month of Amazon profit line by line, every fee by name, profit per unit sold, the line that moved most, and the products that lose money

Synthesis tools to use:
- `cost_rules for=money-amazon-profit-every-fee`
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `amazon_metric metric=ppc_profit_by_asin month=YYYY-MM`
- `operator_inputs section=cogs`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=pnl_waterfall` and `month=` set to last month. Read `settlement_status`. If `fully_settled` is false, the profit is in `net_profit_estimate`: give it as an estimate with its range, then call the month before, which is the latest fully settled month, and lead with that one.
2. Call `amazon_metric` with `metric=pnl_waterfall` for the month before the one you lead with. Compare each line as a share of sales. Name the line whose share moved the most.
3. Divide each line by `units` to get the cost per unit sold, so the founder sees what one unit pays for.
4. Call `amazon_metric` with `metric=ppc_profit_by_asin` and `month=` set to the fully settled month you lead with. Read every `result_page`. It carries each product's fees, account charges, product cost and ads, and adds up to the Profit page. List the products whose profit after ads is below zero, with the loss per unit and for the month. Name each from `asin_names`, and use `find_product` only for a code it does not name.
5. Call `operator_inputs` with `section=cogs`. If the waterfall's `units_missing_cost` is above zero, name the products with sales and no cost.

Checks before answering:
- The net must equal the Profit page. If `profit_page_tie` shows any drift, say so first and do not state a profit.
- Sales are before discounts. Discounts and refunds are their own lines below. Never take them off twice.
- A month still settling has an estimate, not a result. Say "estimate" and give its range.
- Amazon labels some deductions only "Others". Where the brand has ruled them display-ad bills, the page moves them into advertising. Say how much was moved, and if what is left unlabelled is over 2% of sales, say it is worth checking in Seller Central.
- Shipping buyers paid is a memo line. It is not profit.
- Read which outside costs the page counts from its own lines: creator and affiliate pay is counted where the brand has ruled it in. Meta ads sent to Amazon and anything a line does not show are not counted. Say which.
- If ad spend coverage says a day or an ad type is missing, profit is overstated. Say so.

Output:
- One line first: profit for the month, as dollars and as a share of sales, settled or estimated.
- A table: line, dollars, share of sales, per unit, change in share from the month before.
- One line on the biggest fee and one on the line that moved most.
- The products that lose money after ads, with the loss per unit and per month.
- One move: the one cost to work on first, and the number that will show it worked next month.

Never:
- Never use fees grouped by the date Amazon posted them for this view. They cover different orders.
- Never take per-product profit from a view that leaves out Amazon account charges. Those charges can turn a product from profit to loss.
- Never guess a product cost.
- Never change a price, budget or listing. A person does that.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-amazon-profit-every-fee". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
