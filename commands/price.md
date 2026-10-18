---
description: "What happens if you change the price?: How much volume a price change can lose and still pay, and the odds once buyer reaction is known"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# What happens if you change the price?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What happens if you change the price?" (id: money-price-change-simulator, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs thousands of what-ifs on a price change before you make it. It gives the likely range of profit change and the odds that profit goes up.

What to read: Sales history, price changes, conversion
What to give me: How much volume a price change can lose and still pay, and the odds once buyer reaction is known

Synthesis tools to use:
- `cost_rules for=money-price-change-simulator`
- `amazon_metric metric=contribution_by_asin months=3`
- `brand_brain action=moves kind=price_change page=<page-id>`
- `query_series metric=units grain=week asin=<asin>`
- `operator_inputs`
- `run_scenario scenario_type=price_change`
- `find_product`

Steps:
1. Use `find_product` to pin the exact product the person means.
2. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3`. From the last fully settled month take that product's price per unit, units, Amazon fees per unit and product cost per unit. Split the fees into the share of price Amazon keeps (the referral fee, as a fraction of price) and the fixed fees per unit (fulfilment).
3. If the product cost is missing there, call `operator_inputs` with `section=cogs`.
4. Look for a past price change on this product: `brand_brain` with `action=moves`, `kind=price_change` and the product's page. If one exists, call `query_series` with `metric=units`, `grain=week` and the `asin` over the weeks around it, and estimate how units moved for that price move (the elasticity). Say how you estimated it.
5. Call `run_scenario` with `scenario_type=price_change`, the `price_change_pct`, `unit_price`, `unit_cogs`, `fee_pct` (the referral share), `unit_fees` (fixed fees per unit), `units_per_month` and `months=6`. Pass `elasticity` and an `elasticity_sigma` at least half its size only when step 4 found a past move.

Checks before answering:
- If product cost is missing, stop and say so. A price test without cost is not a profit test.
- Always pass the fees. Without them the tool's margin is price minus product cost only, which on Amazon overstates it by a third or more.
- With no past price change there is no elasticity, and the tool returns the break-even (how much volume the change can lose and still pay) and a table of what-ifs, not odds. Give those, say plainly that the odds need a short price test, and never invent an elasticity.
- Never state a single profit number. Give the break-even, and the range and odds when an elasticity exists.

Output:
- One line first: how much volume the change can lose and still pay, then the odds and likely range a month if an elasticity exists.
- A table: price, units a month, profit a month, for low, likely and high cases.
- One move, and how we will know it worked: units and profit after four weeks.

Never:
- Never change a price in any account. A person does that.
- Never invent a past price change or a cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-price-change-simulator". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
