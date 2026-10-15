# Does TikTok sell on Amazon too?

Channel: TikTok Shop · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Does TikTok sell on Amazon too?" (id: mkt-tiktok-lift-on-amazon, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
TikTok viewers often buy on Amazon. This looks for that spillover in Amazon branded searches and tracked links.

What to read: TikTok ad spend and shop sales by week, Amazon branded searches by week, and Amazon sales from tracked TikTok links
What to give me: Whether TikTok activity lifts brand searches and sales on Amazon, and how big that spillover is

Synthesis tools to use:
- `tiktok_metric metric=spend_trend months=6`
- `tiktok_metric metric=shop_sales_trend months=6`
- `amazon_metric metric=search_query_trend grain=week periods=26`
- `amazon_metric metric=attribution_publishers days=180`

Steps:
1. Call `tiktok_metric metric=spend_trend months=6` and `tiktok_metric metric=shop_sales_trend months=6`.
2. Call `amazon_metric metric=search_query_trend grain=week periods=26`. Compare branded and non-branded series. Branded rising alone points to outside demand.
3. Call `amazon_metric metric=attribution_publishers days=180` for sales from tracked TikTok links.
4. If the pattern is strong, propose an on-off test.

Checks before answering:
- Other marketing moves branded searches too. Name anything else that changed.
- Search data is weekly only. Never break it into days.
- Tracked link sales are a floor. Most viewers search instead of clicking.
- A pattern is not proof. Say so.

Output:
- One line: spillover likely, unclear, or not seen.
- A table: week, TikTok spend, TikTok shop sales, Amazon branded searches, Amazon non-branded searches.

Never:
- Never call the spillover proven without a test.
- Never add TikTok and Amazon credited sales together.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-tiktok-lift-on-amazon". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
