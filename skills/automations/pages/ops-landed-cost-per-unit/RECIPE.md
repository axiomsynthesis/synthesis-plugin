# What each unit really costs landed

Channel: Money · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What each unit really costs landed" (id: ops-landed-cost-per-unit, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds the true cost of a unit on the shelf: factory price plus inbound freight, duty, brokerage and receiving, spread over the units that arrived on each order. Margin reports built on factory price alone overstate profit whenever freight or tariffs rise.

What to read: Purchase orders, freight and duty bills, and units received per product
What to give me: Cost per unit once freight, duty and fees to reach the warehouse are added, and how it changed

Synthesis tools to use:
- `cost_rules for=ops-landed-cost-per-unit`
- `operator_inputs section=cogs`
- `operator_inputs section=purchase_orders`
- `netsuite_metric metric=vendor_spend limit=25`
- `export_xlsx filename=landed-cost.xlsx`

Steps:
1. Call `operator_inputs section=cogs` for the entered cost per product, and note whether each entry says it includes freight and duty.
2. Call `operator_inputs section=purchase_orders` for orders, units and dates.
3. Call `netsuite_metric metric=vendor_spend limit=25` to find freight forwarders, customs brokers and duty lines among supplier bills.
4. Once the build lands, allocate each order's freight and duty to its lines by units (or by volume when the order records it) and divide by units received.
5. Compare landed cost to the entered cost per product and to the prior order.
6. Write the result with `export_xlsx filename=landed-cost.xlsx`, one tab per product family and one summary tab.

Checks before answering:
- Until freight and duty are tied to orders, say the landed cost is not measurable and show only what is held. Never estimate freight as a flat percent.
- Units received, not units ordered, are the denominator. A short shipment raises cost per unit.
- If an entered cost already includes freight, do not add freight again.

Output:
- Spreadsheet: Product | Factory cost | Freight per unit | Duty per unit | Other per unit | Landed cost | Entered cost | Gap.
- Three lines in chat: the biggest gap, its monthly dollar effect at current volume, and whether to update the entered cost.

Never:
- Never overwrite the entered product cost. A person updates it.
- Never present a guessed freight rate as measured.
- Never contact a supplier or forwarder.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-landed-cost-per-unit". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Synthesis holds entered product cost and supplier bills, but not freight, duty and brokerage tied to each purchase order or units received per order. Needs a purchase-order line feed with freight and duty (Inventory Planner purchase orders plus a freight bill source) and a landed-cost reader tool. Do the parts you can and say plainly what is missing.
