# What TikTok Shop really sells, and the next move

Channel: TikTok Shop · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What TikTok Shop really sells, and the next move" (id: tiktok-shop-strategy, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads your TikTok Shop and splits free samples from paid orders, so you see what the shop really sells. It ranks creators by sales, not views, and names one move for the month.

What to read: TikTok Shop orders, GMV Max, creators
What to give me: Real sales with free samples split out, creators ranked by sales, and one move for the month

Synthesis tools to use:
- `tiktok_metric metric=shop_sales_trend`
- `tiktok_metric metric=shop_performance`
- `tiktok_metric metric=shop_product_performance`
- `tiktok_metric metric=shop_video_performance`
- `tiktok_metric metric=shop_ad_efficiency`

Steps:
1. Call `tiktok_metric` with `metric=shop_sales_trend` and `months=6` for sales, orders and order size by month.
2. Call `tiktok_metric` with `metric=shop_performance` and `months=3` to separate free sample orders from paid ones.
3. Call `tiktok_metric` with `metric=shop_product_performance` and `limit=10` to see which products earn the paid sales.
4. Call `tiktok_metric` with `metric=shop_video_performance` and `limit=20` to rank creators and videos by sales.
5. Call `tiktok_metric` with `metric=shop_ad_efficiency` and `months=3` to see what GMV Max spend returns.

Checks before answering:
- Never count free samples as sales. If samples cannot be separated, say the sales figure includes them.
- Use closed months. The current month is still filling in.
- If a read comes back empty or fails, say which one. Never call it zero sales.
- One viral video is not a trend. Say when one creator drives most of the sales.

Output:
- One line first: real monthly sales and the share that is samples.
- A table: product, paid sales, sample orders, top creator, ad return.
- One move for the month, its cost in dollars, and how we will know it worked.

Never:
- Never change a campaign, product or creator deal. A person does that.
- Never guess a number the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: tiktok-shop-strategy". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
