---
description: "A cost went up. Now what?: What a supplier or tariff increase costs a month, and three priced responses: absorb it, raise price, or change the pack"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# A cost went up. Now what?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "A cost went up. Now what?" (id: ops-cost-increase-response, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
When a supplier raises prices or a tariff lands, this sizes the hit, says when it starts, and prices the options side by side: absorb it, raise the price, or move buyers to a different pack size. It keeps the decision on dollars, not on a guess about how shoppers will react.

What to read: Product cost, Amazon fees, ads and price per product, stock on hand, open purchase orders, sales pace, and the size of the cost increase
What to give me: What a supplier or tariff increase costs a month, and three priced responses: absorb it, raise price, or change the pack

Synthesis tools to use:
- `cost_rules for=ops-cost-increase-response`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=ppc_profit_by_asin`
- `amazon_metric metric=inventory_position`
- `operator_inputs section=purchase_orders`
- `unit_economics_waterfall asp=<price> amazon_fees=<fees> cogs=<cost> marketing=<ad_cost_per_unit>`
- `run_scenario scenario_type=price_change`
- `run_scenario scenario_type=price_change simulations=1000`
- `breakeven_roas asin=<asin>`
- `amazon_metric metric=shelf_position`

Steps:
1. Ask for the increase: which products, how much per unit, and from when. A tariff is a percent of the customs value, not of the price.
2. Call `amazon_metric metric=contribution_by_asin months=3` for price, fees, product cost and units per affected product, from the last settled month.
3. Call `amazon_metric metric=ppc_profit_by_asin` for each product's ad spend. Ad cost per unit = ad spend divided by units.
4. For each product run `unit_economics_waterfall` with the current cost and again with the new cost, passing `marketing` = ad cost per unit, so profit after ads is shown before and after.
5. Monthly hit = increase per unit times units per month.
6. Timing: call `amazon_metric metric=inventory_position` and `operator_inputs section=purchase_orders`. Stock on hand and on order was bought at the old cost. The new cost lands when it runs out. Give the month the hit starts and the total hit over the first 6 months.
7. Price option: run `run_scenario scenario_type=price_change price_change_pct=<pct> unit_price=<price> unit_cogs=<new_cost> fee_pct=<referral share> unit_fees=<fixed fees per unit> units_per_month=<units>`. Pass an elasticity only if the person gives a measured one. Without one, give the break-even it returns, not odds. If it times out, retry once with `simulations=1000` added.
8. Pack option: for each pack size in the same family from step 2, run `unit_economics_waterfall` with the new cost times the units in the pack. Show profit per order and per unit, so moving buyers to a bigger pack is priced.
9. Check the shelf with `amazon_metric metric=shelf_position`.
10. Recompute the ad ceiling with `breakeven_roas asin=<asin>` at the new cost.

Checks before answering:
- A product with no entered cost cannot be assessed. Say so rather than guess.
- Use one price per product, the last settled month's, in every option. If a tool used a different price, say so.
- The elasticity is an assumption unless measured. There is no tool yet that measures it, so the price option gives a break-even, not odds. Say so.
- Always pass the fees to the price option.
- If `shelf_position` returns no rivals, say the rival list is not set up. Never call the new price safe against rivals.
- If stock or purchase orders are not entered, say the hit is shown from today and may start later.
- Units per month come from closed full months, not a deal month.

Output:
- One line first: the monthly hit, the month it starts, and the option to take.
- Table: Product | Cost increase per unit | Monthly hit | Starts | Profit after ads per unit before | After | Break-even price rise.
- The three options with their monthly dollar effect, then how we will know in 30 days.

Never:
- Never change a price or a listing.
- Never present an assumed elasticity as measured.
- Never contact the supplier.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-cost-increase-response". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
