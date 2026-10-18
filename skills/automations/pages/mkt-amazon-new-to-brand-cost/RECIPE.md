# What a new Amazon customer really costs

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What a new Amazon customer really costs" (id: mkt-amazon-new-to-brand-cost, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Amazon only reports new-to-brand orders for Sponsored Brands and Display. This turns that into a cost per new customer and sets it against what those customers are worth.

What to read: Ad cost per new-to-brand order from Sponsored Brands and Display, and profit on new versus repeat buyers
What to give me: What a new Amazon customer costs you in ads, what they are worth over time, and whether that trade pays

Synthesis tools to use:
- `cost_rules for=mkt-amazon-new-to-brand-cost`
- `amazon_metric metric=ppc_ntb days=90`
- `amazon_metric metric=pnl_by_customer_type days=90`
- `product_ltv_windowed windows=[90,180,365]`

Steps:
1. Call `amazon_metric metric=ppc_ntb days=90`. Note cost per new-to-brand order for each ad type.
2. Call `amazon_metric metric=pnl_by_customer_type days=90` for profit on a new buyer's first order versus repeat orders.
3. For the main entry products, call `product_ltv_windowed asin=<product id> windows=[90,180,365]` to see value over time. It returns sales per customer, not profit. Turn it into profit with the repeat-order margin from step 2 and label the result as sales times margin.
4. Payback months = cost per new order divided by monthly profit per new customer. Give it per ad type.

Checks before answering:
- Sponsored Products reports no new-to-brand figure. Never present this as the account's total customer cost.
- Amazon's "new to brand" means no purchase in 12 months. Say it is not the same as a first-ever buyer.
- Long windows need old enough customers. Drop any window the cohort has not reached.
- Product costs must be entered. If they are not, profit is not known. Say so.

Output:
- One line: cost per new customer, value at 6 months, payback in months.
- A table: ad type, spend, new-to-brand orders, cost per new order, payback months.

Never:
- Never call this the account's overall customer cost.
- Never extend lifetime value past what the data has measured.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-new-to-brand-cost". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
