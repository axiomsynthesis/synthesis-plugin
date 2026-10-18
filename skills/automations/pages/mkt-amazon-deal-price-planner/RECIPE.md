# Set deal prices that still make money

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Set deal prices that still make money" (id: mkt-amazon-deal-price-planner, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Amazon judges a deal against your recent low price. A past deep discount sets a floor that the next deal must beat.
This sets a deal price per product, checks what is left after fees and cost, and flags products where any qualifying deal loses money.

What to read: Your own price history per product, profit per unit, and how deep your past deals went and what they returned
What to give me: A deal price that should qualify for each product, the profit per unit at that price, and the one to skip

Synthesis tools to use:
- `cost_rules for=mkt-amazon-deal-price-planner`
- `shelf_history marketplace=amazon days=90`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=promotion_performance months=12 limit=30`
- `breakeven_roas`

Steps:
1. Ask for the products and the event or deal type.
2. For each, call `shelf_history marketplace=amazon days=90 asin=<product id>` to find the lowest price in the window.
3. Call `amazon_metric metric=contribution_by_asin months=3` for fees and cost per unit.
4. Call `amazon_metric metric=promotion_performance months=12 limit=30` for how past discounts paid back.
5. Plan a deal price just under the recent low. Compute profit per unit there with `breakeven_roas asin=<product id>` for the line-by-line math. Mark products that lose money at a qualifying price.

Checks before answering:
- Price history starts the day tracking began. If it is shorter than 30 days, the low may be missing. Say so.
- Amazon's reference price rules change. Tell the person to confirm the required price in Seller Central.
- A missing product cost means unknown profit. Never fill it.

Output:
- One line: products worth a deal and the one to skip.
- A table: product, 90-day low, planned deal price, profit per unit at deal price, past deal payback.

Never:
- Never create or submit deals.
- Never state Amazon's eligibility rule as certain.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-deal-price-planner". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
