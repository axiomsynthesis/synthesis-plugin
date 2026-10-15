# Where each product loses the shopper

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where each product loses the shopper" (id: mkt-amazon-search-funnel-leak, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Search data shows where a product drops out: not seen, seen but not clicked, clicked but not added, added but not bought. Each step has a different fix.
This names the step for each product's top searches and the lever that moves it.

What to read: For each product's most important searches, your share of views, clicks, cart adds and purchases against the market
What to give me: For each product, the step where shoppers drop off on its key searches, and the one fix that step needs

Synthesis tools to use:
- `amazon_metric metric=keyword_opportunities grain=month top=5 min_volume=1000`
- `amazon_metric metric=listing_score`
- `amazon_metric metric=shelf_position days=30 limit=30`

Steps:
1. Call `amazon_metric metric=keyword_opportunities grain=month top=5 min_volume=1000`. Each row names the product carrying the search and its main gap.
2. Group by product. Pick the gap that repeats across its searches.
3. Map gap to lever: not seen means ads or relevance; seen not clicked means main image, price, rating; clicked not carted means page content and reviews; carted not bought means price at checkout or delivery date.
4. For products with a click gap, call `amazon_metric metric=shelf_position days=30 limit=30` to check price and rating against rivals. For page gaps, call `amazon_metric metric=listing_score asin=<product id>`.

Checks before answering:
- Shares are already percentages. Never multiply by 100.
- Searches under 1,000 a month swing on one shopper. Keep the minimum at 1,000 unless the person asks.
- Use closed months only. The current month is incomplete.
- Read gaps between steps, not levels on their own.

Output:
- One line per product: the gap and the fix.
- A table: product, search, view share, click share, cart share, purchase share, gap, lever.

Never:
- Never call a missing search 0% share. It is not measured.
- Never change listings or ads.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-search-funnel-leak". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
