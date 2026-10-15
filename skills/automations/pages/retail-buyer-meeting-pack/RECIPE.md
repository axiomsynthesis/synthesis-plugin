# Build the retail buyer meeting deck

Channel: Retail · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build the retail buyer meeting deck" (id: retail-buyer-meeting-pack, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds the short deck a retail buyer expects: how your items sell per store, how that compares with the set, and one clear ask. Every number comes from your own retailer files or sheets, so you walk in with facts the buyer can check.

What to read: Retail POS, category data
What to give me: A 6 to 8 slide deck: sales per store, rank in the set, promo results, and one clear ask

Synthesis tools to use:
- `list_files`
- `search_file_content`
- `read_file`
- `gsheets_metric metric=trend`
- `netsuite_metric metric=customer_trend`
- `export_pptx`

Steps:
1. Call `list_files` with `limit=50`, then `search_file_content` with `query="store sales by week"` and `k=8`, to find the latest retailer sales and category files.
2. Open the newest ones with `read_file` and pull the last 13 weeks of units, dollars and store counts per item.
3. If the brand keeps retail sales in a sheet, call `gsheets_metric` with `metric=trend` on that table for the same 13 weeks.
4. Call `netsuite_metric` with `metric=customer_trend` and `months=12` to show what the retailer bought from you, next to what shoppers bought off the shelf.
5. Work out sales per store per week for each item and its rank in the set, then write one ask with its dollar value.
6. Build the deck with `export_pptx`, `filename="buyer-meeting-pack.pptx"`.

Checks before answering:
- Say which week each file ends on. Two files with different week ends are never added together.
- Shelf sales and what the retailer bought from you are different numbers. Never call one the other.
- If no retailer file or sheet is found, say so. Never build a deck from an empty read.
- One strong week is not a trend. Use at least 8 weeks for any rank.

Output:
- One line first: your best item's rank in the set and the ask.
- A deck of 6 to 8 slides: summary, sales per store by item, rank in the set, trend, promo results, the ask with its dollar value.
- File: buyer-meeting-pack.pptx from `export_pptx`, which works in any Claude. If you can save files here, save a copy too and tell me its name.

Never:
- Never send the deck to a buyer. A person does that.
- Never guess store counts or category totals that no file holds.
- Never quote a share figure without saying where it came from.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: retail-buyer-meeting-pack". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Store sales by retailer and SPINS share sit in our warehouse, but no customer tool reads them yet, so a store-sales tool has to be built. Until then the pack works from the retailer files you upload or a connected sheet. Do the parts you can and say plainly what is missing.
