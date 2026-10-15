---
description: "Find your next product in search demand: Searches where shoppers want something you don't sell and the shelf is weak, ranked by demand"
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
Finds searches where shoppers want something you do not sell, and where the products that show up are weak. It ranks the ideas by demand and by how easy the shelf looks to win.

What to read: Search data, rival listings
What to give me: Searches where shoppers want something you don't sell and the shelf is weak, ranked by demand

Synthesis tools to use:
- `amazon_metric metric=search_term_gaps`
- `amazon_metric metric=keyword_opportunities`
- `scrape_amazon_search`
- `competitor_review_voice`
- `google_trends`

Steps:
1. Call `amazon_metric` with `metric=search_term_gaps` and `limit=100` for searches near your products where you do not show.
2. Call `amazon_metric` with `metric=keyword_opportunities` and `top=5` for search volume and how crowded each search is.
3. For the top 3 searches, call `scrape_amazon_search` with that `keyword` and `k=20` to read the shelf: price, rating, reviews.
4. Call `competitor_review_voice` with `limit=50` for what rival customers complain about, which points to the gap.
5. Call `google_trends` with the top 3 searches and `timeframe="today 12-m"` to check the demand is growing, not fading.

Checks before answering:
- Search volume is an estimate. Say so and round it.
- Google Trends is a relative index with no volume in it. Never call it searches a month.
- If a shelf read fails, say the search could not be checked. Never call it an easy shelf.
- Leave out searches for products you already sell.
- Every shelf read and trend check spends a paid search allowance. Make at most three shelf reads and one trend check per run, and ask before doing more.

Output:
- One line first: the single best idea and the demand behind it.
- A table of up to 10 ideas: search, searches a month, top rival rating, average price, trend, why it is open.

Never:
- Never launch, list or order anything. A person decides.
- Never make up a search volume or a rival's rating.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: growth-new-product-ideas-from-search". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
