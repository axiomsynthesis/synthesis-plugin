# Will TikTok demand outrun your stock?

Channel: TikTok Shop · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Will TikTok demand outrun your stock?" (id: mkt-tiktok-stock-vs-demand, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A TikTok video can multiply demand in a day. This compares each product's TikTok stock with its current pace, so a viral moment does not sell out.

What to read: Stock in TikTok's own warehouses when the brand uses them, otherwise each product's declared stock, plus recent daily units and the videos currently driving it
What to give me: Products whose TikTok stock runs out at today's pace, especially those riding a video that's taking off

Synthesis tools to use:
- `tiktok_metric metric=shop_warehouse_stock limit=30`
- `tiktok_metric metric=shop_product_mix months=1 limit=30`
- `tiktok_metric metric=shop_product_performance days=14 limit=30 grain=sku`
- `tiktok_metric metric=shop_video_performance days=14 limit=20`

Steps:
1. Call `tiktok_metric metric=shop_warehouse_stock limit=30` first. If it returns items, that is the real count in TikTok's warehouses, with days of cover already worked out and stock on the way in listed separately.
2. If it returns no stored stock, the brand is not yet on our warehouse-enabled TikTok app or does not use TikTok's warehouses. Fall back to `tiktok_metric metric=shop_product_mix months=1 limit=30` for declared stock and listing status.
3. Call `tiktok_metric metric=shop_product_performance days=14 limit=30 grain=sku` for daily units, last 7 days against the 7 before.
4. Call `tiktok_metric metric=shop_video_performance days=14 limit=20` to see whether one video drives the jump.
5. When working from declared stock, days of stock = declared stock divided by last 7 days' daily units. Flag under 14 days.

Checks before answering:
- Say which count you used: TikTok's warehouse count, or what the shop declared on the listing.
- No stored warehouse stock is not zero stock. Never call a product out of stock from that alone.
- Stock on the way in is not available to sell. Do not add it to days of cover; say when it is expected instead.
- Days are shop-local for analytics, UTC for orders.
- A jump driven by one video can fade fast. Say whether demand is one video or broad.

Output:
- One line: products at risk and days left.
- A table: product, available stock, on the way in, daily units last 7 days, prior 7 days, days of cover, top video share.

Never:
- Never change stock or listings in TikTok Shop.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-tiktok-stock-vs-demand". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
