---
description: "Can we afford this order?: Whether a purchase order fits your cash, what sell-out it prevents, and the chance it ties up cash too long"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Can we afford this order?

Channel: Inventory · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Can we afford this order?" (id: ops-can-we-afford-this-po, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Tests a purchase order before it is placed. It checks the cash left after the order, the stockout date the order is buying against, and how likely the stock is to sit longer than planned. It answers the question a founder asks the night before signing a factory order.

What to read: Entered cash, open purchase orders, current stock cover and sales pace for the products on the order
What to give me: Whether a purchase order fits your cash, what sell-out it prevents, and the chance it ties up cash too long

Synthesis tools to use:
- `operator_inputs section=cash`
- `operator_inputs section=purchase_orders`
- `amazon_metric metric=restock_plan target_days=90 limit=50`
- `amazon_metric metric=days_of_cover limit=50`
- `run_scenario scenario_type=inventory_bet`

Steps:
1. Ask for the order: products, units, unit cost, deposit and balance terms, and supplier lead time. Never invent a lead time.
2. Call `operator_inputs section=cash` for current cash and the cash floor, and `operator_inputs section=purchase_orders` for orders already committed.
3. Call `amazon_metric metric=days_of_cover limit=50` and `amazon_metric metric=restock_plan target_days=90 limit=50` for the products on the order. Note sellable stock, inbound stock and the date each runs out.
4. Run `run_scenario scenario_type=inventory_bet units=<units> unit_cost=<cost> sku=<ASIN> expected_monthly_units=<pace> units_on_hand=<stock already at Amazon and in warehouses> lead_time_days=<lead_time>`, plus `dio`, `dso` and `dpo` if known. An ASIN as sku measures the Amazon fees; otherwise pass `fee_pct` and `unit_fees`. Leave lead_time_days out if nobody gave one; the tool then names the lead-time check as not run.
5. Compare: cash after the deposit and after the balance, the stockout date versus the arrival date, and the scenario's chance of cash running short.
6. If the order fails the cash floor, test one alternative: two smaller orders, or a smaller first order.

Checks before answering:
- The restock plan has no lead time in it. Its order-by date is when stock runs out, not when to place the order. Subtract the lead time the person gave.
- A product at zero sellable stock with a shipment arriving may be fine. Read inbound beside cover.
- A failed stock read is not zero stock. If the stock feed failed, say so and stop.
- The cash floor and payment terms must come from the person. If they are missing, say the answer depends on them.

Output:
- Five lines: cash after the order, the stockout it prevents and when, the scenario's chance of trouble, the binding limit, and the recommendation.
- A small table if an alternative was tested: Option | Cash low point | Stockout risk | Chance of short cash.

Never:
- Never place, change or cancel a purchase order.
- Never invent lead times, minimum order quantities or payment terms.
- Never call a scenario result a forecast. It is a range of outcomes on stated inputs.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-can-we-afford-this-po". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
