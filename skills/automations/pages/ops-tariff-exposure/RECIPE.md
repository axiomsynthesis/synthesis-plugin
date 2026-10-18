# What a tariff change costs each product

Channel: Money · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What a tariff change costs each product" (id: ops-tariff-exposure, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how exposed each product is to a tariff change, in dollars a year and in share of margin. When a tariff announcement lands, the founder can answer "what does this cost us" the same day instead of after the next invoice.

What to read: Each product's country of origin and tariff code, its landed cost and its units per month
What to give me: The yearly cost of a tariff change on each product, and where it wipes out most of the margin

Synthesis tools to use:
- `cost_rules for=ops-tariff-exposure`
- `operator_inputs section=cogs`
- `amazon_metric metric=contribution_by_asin months=6`
- `netsuite_metric metric=vendor_spend limit=25`

Steps:
1. Call `operator_inputs section=cogs` for cost per product.
2. Call `amazon_metric metric=contribution_by_asin months=6` for units and margin per product.
3. Call `netsuite_metric metric=vendor_spend limit=25` to see duty and broker bills.
4. Once origin and duty data exist, compute for each product: customs value per unit, current duty, and duty under the announced rate.
5. Yearly cost of the change = extra duty per unit times units a year. Share of margin = extra duty per unit divided by profit per unit.

Checks before answering:
- Until origin and codes are held, say exposure cannot be computed and ask the person for origin by product.
- Duty is charged on customs value, not on selling price or landed cost. Use the right base.
- Refunds of past duty post back into closed months. Do not count them as current cost.

Output:
- Table: Product | Origin | Current duty per unit | New duty per unit | Yearly cost | Share of margin lost.
- Two lines: the total yearly cost and the products to act on first.

Never:
- Never give customs or legal advice; point to a customs broker for codes.
- Never guess a product's origin.
- Never change prices or orders.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-tariff-exposure". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Synthesis does not hold country of origin, tariff codes or duty paid per product. Needs a product-origin field (entered on the inputs page or read from purchase orders) and duty lines tied to purchase orders. Do the parts you can and say plainly what is missing.
