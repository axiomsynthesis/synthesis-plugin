# Stores selling far below their peers

Channel: Retail · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Stores selling far below their peers" (id: mkt-retail-store-outliers, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds stores that carry your item but sell far less than similar stores. That gap is usually fixable on the shelf.

What to read: Weekly units per store for each item, grouped with stores of similar size and region
What to give me: Stores selling well under similar stores, a sign of a shelf or stock problem, ranked by weekly dollars lost

Synthesis tools to use:
- `gsheets_metric metric=tables`
- `gsheets_metric metric=breakdown`

Steps:
1. Call `gsheets_metric metric=tables` to find store sales and any store size or cluster column.
2. Call `gsheets_metric metric=breakdown` for units per store per week over 6 complete weeks.
3. Group stores by region and size. Flag stores under a third of their group median for 6 straight weeks.
4. Value each at the gap to half the median, times shelf price.

Checks before answering:
- Six weeks in a row, not one bad week. One week is noise.
- Compare stores of like size. A small store is not an outlier against a supercenter.
- Sheet figures are typed by people. Say so.

Output:
- One line: stores flagged and weekly dollars at stake.
- A table: store, region, units per week, group median, weeks below, stock on hand if known.

Never:
- Never contact stores or retailers.
- Never call shelf dollars your revenue.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-retail-store-outliers". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): No governed tool reads store-level retail sales for customers yet. Needs store sales with store size or cluster connected. Until then this works only from a store-by-item export kept in a connected Google Sheet. Do the parts you can and say plainly what is missing.
