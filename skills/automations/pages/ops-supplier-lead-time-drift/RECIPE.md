# Are suppliers getting slower?

Channel: Inventory · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are suppliers getting slower?" (id: ops-supplier-lead-time-drift, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Measures real supplier lead times from order to arrival and compares them with what was promised. Every reorder plan rests on a lead time; when it quietly stretches, stockouts follow.

What to read: Purchase order dates, promised dates and actual received dates per supplier
What to give me: How long each supplier really takes against what they promise, and whether it is getting longer

Synthesis tools to use:
- `operator_inputs section=purchase_orders`
- `operator_inputs section=shipments`

Steps:
1. Call `operator_inputs section=purchase_orders` and `operator_inputs section=shipments` for order and arrival dates.
2. Once the build lands, compute days from order to received for each order, per supplier, and the promised days beside it.
3. Compare the last six orders' average with the six before.
4. Flag suppliers whose actual lead time exceeds the promise by more than 7 days, or grew by more than 7 days.

Checks before answering:
- Until received dates exist, say lead time is not measured and use only what the person states.
- Split production time from transit time when both dates exist. A port delay is not a factory problem.
- Fewer than three orders is too few for a trend.

Output:
- Table: Supplier | Orders | Promised days | Actual days | Change vs prior orders | Flag.
- One line: the lead time every reorder plan should use now.

Never:
- Never invent a lead time.
- Never change a reorder setting or an order.
- Never contact a supplier.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-supplier-lead-time-drift". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Entered purchase orders carry product, units and dates but not promised and received dates per order. Inventory Planner purchase orders land with expected dates but have no reader tool. Needs received dates per order and a lead-time tool. Do the parts you can and say plainly what is missing.
