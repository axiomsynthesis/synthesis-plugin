---
description: "Find your next product in search demand: Searches for things you could make but don't sell, on a weak shelf, sized in yearly revenue"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Find your next product in search demand

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find your next product in search demand" (id: growth-new-product-ideas-from-search, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds searches where shoppers want something you do not sell and the products that win are weak. It keeps only ideas the brand could make, sizes each in yearly revenue, and ranks them.

What to read: Amazon search data, the winners on each search, rival reviews, what the brand makes
What to give me: Searches for things you could make but don't sell, on a weak shelf, sized in yearly revenue

Synthesis tools to use:
- `amazon_metric metric=search_term_gaps limit=15 kind=NOT_SURFACING weeks=12`
- `amazon_metric metric=search_query_performance scope=nonbranded top=25`
- `brand_facts`
- `competitor_review_voice`
- `scrape_amazon_search`

Steps:
1. Call `amazon_metric` with `metric=search_term_gaps`, `limit=15`, `kind=NOT_SURFACING` and `weeks=12`. These are searches near your products where Amazon never shows you. Searches for a rival's brand name and off-category searches are already set aside.
2. Call `amazon_metric` with `metric=search_query_performance`, `scope=nonbranded` and `top=25`. For each gap, find the nearest search you do show on. Take its purchases per search (market purchases divided by searches).
3. Shelf strength, free, from the gap rows: add the top 3 winners' click shares. Under 30% is open, 30% to 60% is contested, over 60% is locked. Winnable share: 5% if open, 2% if contested, 0 if locked. Say these shares are rules of thumb.
4. Trend, free: call `amazon_metric` with `metric=search_term_gaps`, `kind=NOT_SURFACING` and `weeks=4`. A term whose best rank in the last 4 weeks matches its 12-week best is holding or rising. Much worse means fading.
5. Fit: call `brand_facts`. Mark FIT yes only if the idea is a format or formula the brand already makes, or its supplier lists. Otherwise FIT no, and say why.
6. Size each FIT yes idea: weekly searches x 52 x purchases per search x winnable share x price. For price, use the brand's own price for its nearest product.
7. Call `competitor_review_voice` with `asin` set to each winner of the top 2 ideas. It only works for products on your watchlist. Say so when one is not.
8. Only if the person asks, call `scrape_amazon_search` with that `keyword` and `k=20` for the top idea's shelf prices and ratings. It is paid.

Checks before answering:
- Search counts are the biggest single week, not a month. Call them searches a week, rounded, as estimates.
- A gap with no search count stays unsized. Never fill it. This cannot yet estimate volume from search rank alone.
- Leave out searches for products you already sell.
- A search for a part or refill that fits another brand's device is an add-on play. List it on its own.
- Revenue is sized before costs. Margin, launch and stock costs are not in it. Say so.
- Duplicate rival reviews across two listings count once.

Output:
- One line first: the single best FIT yes idea, its yearly revenue size, and why the shelf is open.
- A table of up to 10 ideas: search, searches a week (estimate), top-3 click share, trend, fit, yearly size.
- Then FIT no ideas in one line each.

Never:
- Never launch, list or order anything. A person decides.
- Never make up a search count, a share or a rival's rating.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: growth-new-product-ideas-from-search". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
