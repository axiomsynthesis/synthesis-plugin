# Where you show up on walmart.com search

Channel: Walmart · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where you show up on walmart.com search" (id: mkt-walmart-search-shelf, Walmart).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Tracks where your products appear on walmart.com search and who moves around you.

What to read: Your position, price and reviews on walmart.com search results for tracked searches, over time, against the products around you
What to give me: Whether you're rising or falling on key walmart.com searches, and who passed you

Synthesis tools to use:
- `shelf_history marketplace=walmart days=30`
- `scrape_walmart k=20`

Steps:
1. Call `shelf_history marketplace=walmart days=30` for each tracked search.
2. For a search the person names that is not tracked, call `scrape_walmart query=<search> k=20` once for today's shelf.
3. Report position change, price and review gap against the top 10.

Checks before answering:
- Shelf history only covers searches set up for tracking. Say so if the one asked for is not.
- Positions move daily. Judge the trend over the window.
- Scraped data is third-party. Label it with the date. Scrapes draw on a shared monthly allowance.

Output:
- One line per search: position now, 30 days ago, and the reason.
- A table: search, your position, price, reviews, top-10 median price, top-10 median reviews.

Never:
- Never change listings or prices.
- Never run scrapes in a loop.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-walmart-search-shelf". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
