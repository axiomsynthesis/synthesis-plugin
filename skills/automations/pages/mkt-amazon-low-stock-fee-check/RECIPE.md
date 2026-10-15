# Dodge Amazon's low-stock and storage fees

Channel: Inventory · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Dodge Amazon's low-stock and storage fees" (id: mkt-amazon-low-stock-fee-check, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Amazon charges a fee when you keep too little stock and limits how much you can store. Both push in opposite directions.
This finds the products caught by each and the stock level that avoids both.

What to read: Amazon's low-inventory level fees and storage capacity limits per product, against days of cover
What to give me: Products paying a fee for too little stock, products pushing you over your storage limit, and the level that avoids both

Synthesis tools to use:
- `amazon_metric metric=fee_breakdown`
- `amazon_metric metric=days_of_cover limit=40`
- `amazon_metric metric=restock_plan target_days=45 limit=40`

Steps:
1. Call `amazon_metric metric=fee_breakdown month=<last closed month>`. Once low-stock fees are a separate line, read them per product.
2. Call `amazon_metric metric=days_of_cover limit=40`. Products under 28 days of cover are the usual low-stock fee targets.
3. Call `amazon_metric metric=restock_plan target_days=45 limit=40` for units needed to reach 45 days.
4. Compare the fee saved with the extra storage cost, per product.

Checks before answering:
- Until the fee line is synced, never state a low-stock fee amount. Say which products are likely exposed.
- Amazon's thresholds change. Point to Seller Central for the current rule.
- Stock is Amazon's live count, refreshed when asked. Quote Amazon's update time, and name any product the answer left out because its numbers did not add up.

Output:
- One line: products exposed and the stock level to hold.
- A table: product, days of cover, likely exposed, units to reach 45 days.

Never:
- Never create shipments or change settings.
- Never invent a fee amount.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-low-stock-fee-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Fees are synced as referral, fulfilment, storage and other. The low-inventory fee and the storage capacity limit are not separated or synced, so the fee per product cannot be read. Needs those fee lines and the capacity limit added to the Amazon sync. Do the parts you can and say plainly what is missing.
