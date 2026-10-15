# Where shoppers see you and skip you

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where shoppers see you and skip you" (id: amazon-search-query-performance, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows which searches you show up on, get clicked on, and win the sale.
It ranks searches by the sales you could win.
It splits "never shown" from "shown and not clicked", and keeps your own brand searches apart.

What to read: Amazon Search Query Performance
What to give me: Searches where you're seen but not clicked, and searches you never show up on

Synthesis tools to use:
- `amazon_metric metric=search_query_performance`
- `amazon_metric metric=search_term_gaps`
- `amazon_metric metric=ppc_branded_split`

Steps:
1. Call `amazon_metric` with `metric=search_query_performance` with `grain=week` and `periods=4` to get impression, click and purchase share by search.
2. Call `amazon_metric` with `metric=search_term_gaps` and `limit=25` to find searches with real volume where you barely appear.
3. Call `amazon_metric` with `metric=ppc_branded_split` and `days=30` to mark which searches contain your brand name, and keep them in a separate list.
4. Rank the rest by sales you could win: purchases on that search times the gap between your click share and your purchase share.

Checks before answering:
- If the search data comes back empty, say Brand Analytics may not be on for this account. Never say "no gaps".
- Use whole closed weeks. A part week makes share look low.
- One week of share on a small search is not a trend. Use 4 weeks.

Output:
- Two short tables. Seen but skipped: search, your click share, your purchase share, sales at stake. Never shown: search, monthly searches, your impression share.
- Brand searches listed apart.
- One move for the top search, and the share number to watch.

Never:
- Never change a listing or an ad. A person does that.
- Never guess a share the tool did not return.
- Never mix your own brand searches into the gap list.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-search-query-performance". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
