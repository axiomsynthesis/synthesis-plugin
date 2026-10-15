# Know when you lose ground on a key search

Channel: Amazon · Level: On a schedule · Status: Ready now
Schedule: weekly Tuesday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Know when you lose ground on a key search" (id: mkt-amazon-search-share-drop-alert, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks your top searches each week and raises a flag only when your share of purchases drops sharply on one that matters.

What to read: Your weekly share of purchases on your top non-branded searches, against the prior 4 weeks
What to give me: A weekly alert naming any important search where your share of sales fell sharply, and who gained

Synthesis tools to use:
- `amazon_metric metric=search_query_trend grain=week periods=8`
- `amazon_metric metric=search_query_performance grain=week periods=1 scope=nonbranded top=15 min_volume=1000`
- `amazon_metric metric=search_competitors grain=week periods=2 top=10`

Steps:
1. Call `amazon_metric metric=search_query_performance grain=week periods=1 scope=nonbranded top=15 min_volume=1000` for the latest closed week.
2. Call `amazon_metric metric=search_query_trend grain=week periods=8` with `keyword=<search>` for each of those searches. Compare last week with the 4 weeks before.
3. Flag a drop of more than a third of your share, on a search of at least 1,000 weekly searches.
4. For flagged searches, call `amazon_metric metric=search_competitors grain=week periods=2 top=10` with `term=<search>` to see who gained.

Checks before answering:
- Shares are percentages already. Never multiply by 100.
- An event week is a different week. If last week or the base had an event, say so and do not alert.
- A search missing this week is not 0%. It is unmeasured.
- Only closed weeks. Never the current one.

Output:
- Nothing if nothing dropped.
- Otherwise, per flagged search: share last week, 4-week average, who gained, and "watch" or "act".

Never:
- Never change ads or prices in response.
- Never alert on a share change in a search under 1,000 weekly searches.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-search-share-drop-alert". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Tuesday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
