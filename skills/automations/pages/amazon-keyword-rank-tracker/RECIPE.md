# Track where you rank on your top searches

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Track where you rank on your top searches" (id: amazon-keyword-rank-tracker, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how you are moving on the searches that matter, week by week. For each top search it gives your share of clicks and purchases, the change from last week, and where your product sits on the shelf today.

What to read: Search query performance
What to give me: Your share of clicks and sales on every key search, week by week, with the biggest gain and loss

Synthesis tools to use:
- `amazon_metric metric=search_query_performance`
- `amazon_metric metric=search_query_trend`
- `keyword_rank_tracker`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=search_query_performance`, `grain=week`, `periods=4` and `top=20` for your share on the top searches.
2. For the five searches with the biggest moves, call `amazon_metric` with `metric=search_query_trend` and that `keyword` for twelve weeks of history.
3. Use `find_product` to pick the main product for each search.
4. Call `keyword_rank_tracker` with that `asin` and `keyword` for the live shelf position, both organic and sponsored.
5. Mark each search up, down or flat against last week.

Checks before answering:
- Search data lands a few days late. Use the last closed week only.
- One week of movement is not a trend. Say when a move rests on a single week.
- If the search tools return nothing, say Brand Analytics could not be read. Never report a share of zero.
- A live shelf position is one moment. Say when it was checked.

Output:
- One line first: the biggest gain and the biggest loss this week.
- A table: search, search volume, click share, purchase share, change, arrow, live shelf position.
- One move: the search to defend or push next, and what to watch next week.

Never:
- Never change bids, ads or the listing. A person does that.
- Never guess a share or a rank the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-keyword-rank-tracker". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
