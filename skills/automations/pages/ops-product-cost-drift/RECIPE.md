# Is product cost creeping up?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is product cost creeping up?" (id: ops-product-cost-drift, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Watches the cost per unit of each product over time and flags the ones that moved. A supplier price rise, a new tariff or a costing change shows up here before it shows up as a lower margin in the monthly P&L.

What to read: Product cost per unit by month per Amazon product, and entered product costs
What to give me: Products whose cost per unit moved over six months, and the monthly profit effect

Synthesis tools to use:
- `cost_rules for=ops-product-cost-drift`
- `amazon_metric metric=contribution_by_asin months=6`
- `operator_inputs section=cogs`
- `find_product query=<name>`

Steps:
1. Call `amazon_metric metric=contribution_by_asin months=6` and keep product, month, units and product cost per unit.
2. Call `operator_inputs section=cogs` to see the entered cost per product and when it was last updated.
3. For each product, compare the latest month's cost per unit with the average of the first three months in the window.
4. Flag a product when cost per unit moved more than 5% and the monthly effect at current units is more than $1,000.
5. Use `find_product query=<name>` to group pack sizes of one product, so a 3-pack is not compared with a single.

Checks before answering:
- A product with no cost is not a zero-cost product. List uncosted products separately and never compute a margin for them.
- Compare like with like: cost per unit of the same pack size, and cost per unit of content when packs differ.
- A cost change that lines up exactly with an entry date is a data entry change, not a supplier change. Say which it looks like.
- This view covers Amazon products only. Say so.

Output:
- Table: Product | Cost per unit then | Cost per unit now | Change % | Units per month | Profit effect per month.
- Up to ten rows, biggest dollar effect first. One line on what to check with the supplier or finance.

Never:
- Never edit an entered cost.
- Never guess a missing cost.
- Never contact a supplier.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-product-cost-drift". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
