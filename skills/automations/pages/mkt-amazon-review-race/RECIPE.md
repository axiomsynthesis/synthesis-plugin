# Who's gaining reviews faster than you?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Who's gaining reviews faster than you?" (id: mkt-amazon-review-race, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Review pace moves before sales rank does. A rival that suddenly gains reviews fast is usually spending to scale.
This compares review pace and rating drift for you and your watched rivals.

What to read: Reviews gained per week and rating drift for your products and the rivals on your watchlist
What to give me: Rivals collecting reviews faster than you, a sign they are scaling, and how long until they pass you

Synthesis tools to use:
- `amazon_metric metric=review_velocity days=60 limit=30`
- `amazon_metric metric=shelf_position days=60 limit=30`

Steps:
1. Call `amazon_metric metric=review_velocity days=60 limit=30`.
2. Call `amazon_metric metric=shelf_position days=60 limit=30` to set rank and price movement beside review pace.
3. For any rival gaining faster than you, compute weeks until it passes your review count at today's pace.

Checks before answering:
- Rival rows exist only for products on the brand's watchlist. If none show, say the watchlist is empty, not that rivals are quiet.
- A sudden one-day jump in reviews can be Amazon merging pages. Check whether it is steady over weeks.
- Judge rank over the window, never a single day.

Output:
- One line: the rival to watch.
- A table: product, yours or rival, reviews now, reviews per week, rating change, rank change.

Never:
- Never suggest buying or trading reviews.
- Never present scraped rival data without labeling it scraped.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-review-race". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
