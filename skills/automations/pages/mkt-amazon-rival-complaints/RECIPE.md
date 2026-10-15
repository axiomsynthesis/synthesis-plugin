# Win on what rival buyers complain about

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Win on what rival buyers complain about" (id: mkt-amazon-rival-complaints, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads what your rivals' buyers dislike and matches it to what your buyers like. The overlap is your best ad angle.

What to read: Review text from the rival products on your watchlist, and what your own buyers praise
What to give me: Complaints rival buyers repeat that your product already solves, written as listing lines and ad angles to test

Synthesis tools to use:
- `competitor_review_voice limit=60`
- `review_themes`
- `amazon_metric metric=review_voice sentiment=positive limit=20`

Steps:
1. Call `competitor_review_voice limit=60` for rival review text.
2. Pass the critical ones to `review_themes reviews=<list>` to group them into themes with counts.
3. Call `amazon_metric metric=review_voice sentiment=positive limit=20` for what your own buyers praise.
4. Match rival complaints to your praise. Draft one listing line and one ad headline for each of the top three matches.

Checks before answering:
- Rival reviews exist only for watchlisted products. If none, say the watchlist is empty.
- Counts are small samples. Show the count behind every theme.
- Only claim what your own reviews support. Never invent a product benefit.

Output:
- Three matches: rival complaint with count, your matching praise with count, a listing line, an ad headline.

Never:
- Never name a rival brand in your ad copy.
- Never quote a review at length. Short phrases only.
- Never publish the copy. A person approves and posts it.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-rival-complaints". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
