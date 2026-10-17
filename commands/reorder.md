---
description: "What to reorder, and the purchase order to send: How much of each product to order and by when, with a purchase order drafted for you to check"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# What to reorder, and the purchase order to send

Channel: Inventory · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What to reorder, and the purchase order to send" (id: inventory-reorder-plan-and-po-draft, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Works out how much to order of each product and by when, then drafts a purchase order. A person checks it and sends it to the supplier.

What to read: Sales speed, lead times, stock
What to give me: How much of each product to order and by when, with a purchase order drafted for you to check

Synthesis tools to use:
- `amazon_metric metric=restock_plan`
- `amazon_metric metric=days_of_cover`
- `amazon_metric metric=seasonality`
- `operator_inputs`
- `export_xlsx`

Steps:
1. Call `amazon_metric` with `metric=restock_plan` for suggested units by product.
2. Call `amazon_metric` with `metric=days_of_cover` and `limit=50` for current cover.
3. Call `amazon_metric` with `metric=seasonality` to lift the order for busy months ahead.
4. Call `operator_inputs` with `section=all` for unit costs, open purchase orders and shipments. Take lead times from there or from the reorder sheet the person names.
5. Use `export_xlsx` with `filename=reorder-plan.xlsx`: a reorder tab and a PO draft tab.

Checks before answering:
- A product with no lead time is flagged, never given a made-up one.
- If the stock read fails, stop and say so.
- Count stock already on the way before ordering more.

Output:
- One line first: the most urgent order and its order-by date.
- An Excel file, reorder-plan.xlsx: product, cover now, units to order, order-by date, unit cost, total cost. A second tab is the PO draft.

Never:
- Never send a PO to a supplier. A person does that.
- Never guess a lead time or a unit cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: inventory-reorder-plan-and-po-draft". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
