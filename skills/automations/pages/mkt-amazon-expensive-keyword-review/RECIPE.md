# Which pricey keywords are worth it?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which pricey keywords are worth it?" (id: mkt-amazon-expensive-keyword-review, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A keyword can look bad on return and still be the biggest prize in the category. This joins ad results to the size of each search, so a cut is made with the market in view.

What to read: Ad spend and return per search term, joined to how many shoppers search it and your share of its purchases
What to give me: For your costliest keywords, whether they are a big market worth paying into or a small one you overpay for

Synthesis tools to use:
- `amazon_metric metric=ppc_keyword_roi days=60 min_spend=200 limit=40`
- `amazon_metric metric=search_query_performance grain=month periods=3 scope=nonbranded top=50`

Steps:
1. Call `amazon_metric metric=ppc_keyword_roi days=60 min_spend=200 limit=40`.
2. Call `amazon_metric metric=search_query_performance grain=month periods=3 scope=nonbranded top=50` for search volume and your purchase share trend.
3. Classify each keyword: big market low share (invest and fix conversion), small market high share (cut), big market high share (defend), small low (cut).

Checks before answering:
- Shares are already percentages. 0.42 means 0.42%, not 42%. Never multiply by 100.
- A keyword missing from search data means you did not surface for it, not that you have 0%. Say "not measured".
- Never print a tiny share as 0.0%. Write "under 0.1%".
- Search data is weekly or monthly only. Never divide a week into days.

Output:
- One line: the keyword to keep despite poor return and the keyword to cut.
- A table: keyword, spend, return per $1, monthly searches, your purchase share, class, move.

Never:
- Never change bids or keywords in the account.
- Never rescale shares.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-expensive-keyword-review". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
