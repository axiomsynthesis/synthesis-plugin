# The TikTok videos that actually sell

Channel: TikTok Shop · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "The TikTok videos that actually sell" (id: mkt-tiktok-video-winners, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ranks every video that sold your products by sales per 1,000 views, so a viral video with no sales does not crowd out a quiet one that sells.

What to read: Sales, views and sales per 1,000 views for every video that sold your products in the last 120 days, by creator and by your own account
What to give me: The videos and creators that really sell, and a short brief built from what the winners share

Synthesis tools to use:
- `tiktok_metric metric=shop_video_performance days=60 limit=50`
- `tiktok_metric metric=shop_performance months=2`

Steps:
1. Call `tiktok_metric metric=shop_video_performance days=60 limit=50`.
2. Rank by sales per 1,000 views, with total sales beside it. Split creator videos from your own.
3. Call `tiktok_metric metric=shop_performance months=2` for video share of total shop sales.
4. Ask the person to watch the top five and note the opening, length and offer. Write a five-line brief from what they share.

Checks before answering:
- Video sales are a slice of shop sales, never extra. Never add them to shop totals.
- Video sales include orders later cancelled, so they read about 5% high.
- Videos under 5,000 views are too small to rank. List them apart.
- What a creator was paid is not here. Never call a creator profitable from this alone.

Output:
- One line: the share of sales from the top videos.
- A table: video, creator, author type, views, sales, sales per 1,000 views.
- A five-line creator brief.

Never:
- Never boost videos or contact creators.
- Never describe a video the person has not watched.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-tiktok-video-winners". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
