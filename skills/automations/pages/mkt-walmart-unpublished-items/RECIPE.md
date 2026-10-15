# Get your Walmart items back live

Channel: Walmart · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Get your Walmart items back live" (id: mkt-walmart-unpublished-items, Walmart).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
An unpublished Walmart item is invisible to shoppers. This lists them by Walmart's reason and sorts by how much the product sells on your other channels.

What to read: Every Walmart Marketplace item by publish and lifecycle status, with Walmart's reason for each unpublished one, and what the same products sell elsewhere
What to give me: Unpublished Walmart items grouped by reason, most valuable first

Synthesis tools to use:
- `walmart_metric metric=catalog_health`
- `walmart_metric metric=top_skus months=6 limit=50`
- `amazon_metric metric=pnl_by_asin limit=40`

Steps:
1. Call `walmart_metric metric=catalog_health`. Group unpublished items by reason.
2. Call `walmart_metric metric=top_skus months=6 limit=50` to see what each item sold before it went down, if anything.
3. Call `amazon_metric metric=pnl_by_asin limit=40` and match by your own product code to size each item's demand elsewhere. If you cannot match codes for certain, say so instead of guessing.
4. For each reason, write the usual fix: price parity, content, compliance, or inventory.

Checks before answering:
- Match products across channels by code, never by title.
- An item retired on purpose is not a problem. Ask before listing retired items.
- If the catalog read is empty, check the Walmart connection is live before saying all items are fine.

Output:
- One line: items not live and the most valuable one.
- A table: item, reason, sales elsewhere per month, fix.

Never:
- Never edit or republish items in Walmart Seller Center.
- Never match products by name.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-walmart-unpublished-items". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
