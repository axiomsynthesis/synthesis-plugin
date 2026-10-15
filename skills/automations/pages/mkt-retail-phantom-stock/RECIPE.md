# Stores that show stock but sell nothing

Channel: Retail · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Stores that show stock but sell nothing" (id: mkt-retail-phantom-stock, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A store can show stock on hand while the shelf is empty: the stock is lost, damaged or in the back. The retailer's system will not reorder. This finds those stores.

What to read: Store-level on-hand units and weekly sales by item
What to give me: Stores the system says are stocked where nothing sells, so the retailer won't reorder, with weekly sales lost

Synthesis tools to use:
- `gsheets_metric metric=tables`
- `gsheets_metric metric=breakdown`

Steps:
1. Call `gsheets_metric metric=tables` to find on-hand and sales tabs.
2. Call `gsheets_metric metric=breakdown` for on hand and units sold per store and item.
3. Flag stores with on hand of at least 3 units and zero sales for 3 weeks while the item sells elsewhere.
4. Value at the item's normal rate per store.

Checks before answering:
- Exclude new items in their first 4 weeks.
- A whole region at zero is likely a data gap. Check before listing it.
- Sheet figures are typed by people. Say so.

Output:
- One line: stores flagged and weekly sales at stake.
- A table: store, item, on hand, weeks at zero, normal weekly units.

Never:
- Never contact stores.
- Never call shelf dollars your revenue.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-retail-phantom-stock". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): No governed tool reads store on-hand stock for customers yet. Needs store-level inventory and sales connected per retailer. Until then it works only from a store export kept in a connected Google Sheet. Do the parts you can and say plainly what is missing.
