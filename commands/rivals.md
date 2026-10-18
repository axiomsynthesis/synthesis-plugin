---
description: "Who's stealing your search shoppers?: The named rival products winning shoppers on your searches, and which of your searches each one threatens"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Who's stealing your search shoppers?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Who's stealing your search shoppers?" (id: mkt-amazon-search-rivals-named, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Search data shows your share and leaves the rest anonymous. This names the products taking the rest.
It ranks rivals by how many of your searches they win and whether they are rising.

What to read: Amazon's top clicked products on your own search terms, with their click share next to yours
What to give me: The named rival products winning shoppers on your searches, and which of your searches each one threatens

Synthesis tools to use:
- `amazon_metric metric=search_competitors grain=week periods=4 top=20`
- `scrape_amazon_product`
- `amazon_metric metric=shelf_position days=30 limit=40`

Steps:
1. Call `amazon_metric metric=search_competitors grain=week periods=4 top=20`. Rivals and terms come back over several pages. Call again with the next `result_page` until all 20 rivals are in hand. Skip terms whose `search_relevance` is off_category.
2. Rank rivals by the number of your searches where they are in the top three clicked, then by click share.
3. Call `amazon_metric metric=shelf_position days=30 limit=40` first. It already holds price, rating and review count for tracked rivals, and shows whether they cut price recently.
4. Scrape only top-three rivals missing from it: call `scrape_amazon_product asin=<rival product id>` for live price, rating and reviews. Ask before more than three scrapes: they draw on a shared monthly allowance.

Checks before answering:
- Rival data comes from Amazon's top-three clicked list. A rival outside the top three is invisible here. Say so.
- Shares are percentages already. Never rescale.
- Scraped data is a snapshot from a third-party source. Label it scraped, with the date.
- If the tool returns no rivals, check whether search data is loaded before saying you have none.

Output:
- One line: the one rival to watch and why.
- A table: rival product, title, number of your searches it leads, its click share, yours, change over 4 weeks, price, rating, reviews.

Never:
- Never run scrapes in a loop over every rival.
- Never call a rival's sales figure. This data has clicks, not their sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-search-rivals-named". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
