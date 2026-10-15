# Stores that should carry you and don't

Channel: Retail · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Stores that should carry you and don't" (id: mkt-retail-distribution-voids, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A store authorized for an item that sells none is usually a store that never put it on the shelf. This lists those stores so a rep can walk them.

What to read: Store-level weekly sales and store counts by item for each retailer, against the store list each item was authorized for
What to give me: Stores approved for an item that show no sales, with weekly dollars at stake, ready for your broker or rep

Synthesis tools to use:
- `gsheets_metric metric=tables`
- `gsheets_metric metric=breakdown`
- `search_files query=store authorization`
- `export_xlsx`

Steps:
1. Call `gsheets_metric metric=tables` to find the store-sales tab and the authorized store list.
2. Call `gsheets_metric metric=breakdown` by store and item for the last 4 complete weeks.
3. Void = authorized for the item, zero units for 4 weeks, while the item sells in other stores.
4. Value each void at the item's average units per selling store per week times shelf price.
5. Build `voids_<week>.xlsx` with `export_xlsx`: store number, city, region, item, weeks at zero, weekly dollars at stake.

Checks before answering:
- A store with zero sales on every item is likely a data gap or a closed store. Leave it out and list it apart.
- New items need 4 weeks after the set date before a zero means a void.
- Sheet figures are typed by people, not measured. Say so.
- Shelf dollars are the retailer's sales, not your revenue.

Output:
- One line: voids found and weekly dollars at stake.
- The spreadsheet above.

Never:
- Never send the list to anyone. A person sends it.
- Never call shelf dollars your revenue.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-retail-distribution-voids". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): No governed tool reads store-level retail sales for customers yet. Store sales and authorized store lists must be connected first. Until then this works only if the brand keeps a store-by-item export in a connected Google Sheet. Do the parts you can and say plainly what is missing.
