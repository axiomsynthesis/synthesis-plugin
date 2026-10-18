# Find ads that lose money after product cost

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find ads that lose money after product cost" (id: mkt-amazon-ad-profit-after-cost, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ad dashboards stop at sales. This goes to profit: sales minus fees, product cost and the product's own ad spend.
It names the products where advertising is losing money.

What to read: Each advertised product's settled sales, Amazon fees, product cost and its own ad spend for a closed month
What to give me: Products whose ads turn a profit into a loss once product cost is counted, with the dollars at stake

Synthesis tools to use:
- `cost_rules for=mkt-amazon-ad-profit-after-cost`
- `amazon_metric metric=ppc_profit_by_asin limit=40`
- `amazon_metric metric=contribution_by_asin months=3`
- `operator_inputs section=cogs`

Steps:
1. Call `amazon_metric metric=ppc_profit_by_asin month=<last fully settled month> limit=40`.
2. Call `amazon_metric metric=contribution_by_asin months=3` to see whether the loss is new or steady.
3. Call `operator_inputs section=cogs` and list any advertised product that has no cost entered.
4. Sort losers by dollars lost. For each, give one move: cut ad spend, raise price, or stop advertising it.

Checks before answering:
- Use a fully settled month: one whose settlement coverage is at least 95%. A month that has ended but is still settling has all its ad spend and only part of its sales, so it shows false losses.
- A product with incomplete cost is flagged by the tool. Never call it a loser or a winner.
- Total ad spend across products should be close to the month's ad spend. A big gap means unmatched campaigns. Say how much is unmatched.
- One bad month is not a pattern. Use the 3-month view before recommending a stop.

Output:
- One line: total dollars lost on ads last month and the number of products.
- A table: product, units, profit before ads, ad spend, profit after ads, 3-month direction, move.
- A list of advertised products with no cost entered.

Never:
- Never estimate a missing product cost.
- Never change ads or prices in any account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-ad-profit-after-cost". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
