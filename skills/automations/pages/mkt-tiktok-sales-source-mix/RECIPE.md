# Video, LIVE or shop tab: where TikTok sales come from

Channel: TikTok Shop · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Video, LIVE or shop tab: where TikTok sales come from" (id: mkt-tiktok-sales-source-mix, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
TikTok sales come through three doors. This shows the split, how it is moving, and what each door needs.

What to read: TikTok Shop sales split by video, product card and LIVE, by month, with visitors and conversion
What to give me: Where your TikTok sales come from, how that mix is shifting, and which source to invest in next

Synthesis tools to use:
- `tiktok_metric metric=shop_performance months=6`
- `tiktok_metric metric=shop_video_performance days=60 limit=20`

Steps:
1. Call `tiktok_metric metric=shop_performance months=6`. Read each source's sales and share by month.
2. Call `tiktok_metric metric=shop_video_performance days=60 limit=20` to see whether video sales lean on a few creators.
3. Name the fastest growing source and the one move for it.

Checks before answering:
- Months are shop-local. They will not match order months to the day.
- These sales include orders later cancelled, so they run about 5% above the sales report.
- A source with under 2% share is too small to call a trend.

Output:
- One line: the split and the move.
- A table: month, video share, card share, LIVE share, total.

Never:
- Never add this to other TikTok sales figures.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-tiktok-sales-source-mix". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
