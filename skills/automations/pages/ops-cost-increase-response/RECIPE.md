# A cost went up. Now what?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "A cost went up. Now what?" (id: ops-cost-increase-response, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
When a supplier raises prices or a tariff lands, this sizes the hit and prices the options side by side. It keeps the decision on dollars and odds, not on a gut feeling about how shoppers will react.

What to read: Product cost, Amazon fees and price per product, sales pace, and the size of the cost increase
What to give me: What a supplier or tariff increase costs a month, and three priced responses: absorb it, raise price, or change the pack

Synthesis tools to use:
- `cost_rules for=ops-cost-increase-response`
- `amazon_metric metric=contribution_by_asin months=3`
- `unit_economics_waterfall asp=<price> amazon_fees=<fees> cogs=<cost>`
- `run_scenario scenario_type=price_change`
- `breakeven_roas asin=<asin>`
- `amazon_metric metric=shelf_position`

Steps:
1. Ask for the increase: which products, how much per unit, and from when.
2. Call `amazon_metric metric=contribution_by_asin months=3` for price, fees, product cost and units per affected product.
3. For each product run `unit_economics_waterfall` with the current cost and again with the new cost. Note the margin before and after.
4. Monthly hit = increase per unit times units per month.
5. Price option: run `run_scenario scenario_type=price_change price_change_pct=<pct> unit_price=<price> unit_cogs=<new_cost> fee_pct=<referral share> unit_fees=<fixed fees per unit> units_per_month=<units>`, with the fees from step 2. The tool has no elasticity of its own: pass one only if the person gives it or a past price move on this product shows it, and say which. Without one, give the break-even it returns, not odds.
6. Check the shelf with `amazon_metric metric=shelf_position` so the new price is seen against rivals.
7. Recompute the ad ceiling with `breakeven_roas asin=<asin>` at the new cost, since a thinner margin lowers how hard you can bid.

Checks before answering:
- A product with no entered cost cannot be assessed. Say so rather than guess.
- The elasticity is an assumption unless measured. State where it came from beside every price result.
- Always pass the fees to the price option. Without them the margin is price minus product cost only and is overstated.
- If the new price crosses a round price point a rival sits under, call that out.
- Check that units per month come from closed full months, not a deal month.

Output:
- Table: Product | Cost increase per unit | Monthly hit | Margin before | Margin after | Break-even price rise | Chance price rise loses money.
- Three options in plain words with their monthly dollar effect, then one recommendation and how we will know in 30 days.

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
