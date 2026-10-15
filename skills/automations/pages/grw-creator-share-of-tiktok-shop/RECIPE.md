# How much of TikTok Shop rides on creators?

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How much of TikTok Shop rides on creators?" (id: grw-creator-share-of-tiktok-shop, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits TikTok Shop sales into creator videos, your own account and the rest. It shows whether creators are the engine of the shop and whether that share is rising or fading.

What to read: TikTok Shop sales by source: creators, your own videos and ads
What to give me: The share of your TikTok Shop sales that comes from creators, and the trend

Synthesis tools to use:
- `tiktok_metric metric=shop_video_performance days=120 limit=30`
- `tiktok_metric metric=shop_product_performance days=120 limit=30`
- `tiktok_metric metric=shop_sales_trend months=6`
- `growi_creator_channel_trend months=6 granularity=month`

Steps:
1. Pull `tiktok_metric metric=shop_video_performance days=30 limit=30`, then again with `days=60`, `days=90` and `days=120`. Each gives video sales split by who posted: creators, your own account and marketing accounts.
2. Pull `tiktok_metric metric=shop_product_performance days=30 limit=30` and the same three longer windows. Its total is whole-shop sales on the same basis as the video read.
3. Take each 30-day block by subtracting the shorter window from the longer one. Creator share = creator video sales over shop sales in the same block. Own-account share the same way.
4. Pull `tiktok_metric metric=shop_sales_trend months=6` only for the monthly shape of the shop. Never divide a creator figure by it. It leaves out cancelled orders and the video read keeps them.
5. Pull `growi_creator_channel_trend months=6 granularity=month` if connected, as a second view. Show it beside, never add it.

Checks before answering:
- Creator sales are the platform's own attribution. They will not tie to your order records, and they are a slice of the shop, not all of it.
- TikTok keeps 120 days of video history. Older months cannot be split this way. Say so.
- If the video read says days are missing, the creator figure for that window is a floor. Say which block it is.
- Overlapping sources are shown side by side, never added together.
- Exclude zero-price free sample orders from shop sales before computing shares.
- Growi drops its last 3 days as in-flight. Compare closed months only.

Output:
- Answer first. Table by 30-day block, newest first: shop sales, creator sales, own-account sales, creator share.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-creator-share-of-tiktok-shop". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
