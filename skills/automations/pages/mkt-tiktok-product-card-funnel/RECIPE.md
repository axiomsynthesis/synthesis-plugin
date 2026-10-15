# Where TikTok shoppers drop off

Channel: TikTok Shop · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Where TikTok shoppers drop off" (id: mkt-tiktok-product-card-funnel, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
TikTok shows a product card in feeds, search and the shop tab. This finds which step loses each product and suggests the fix.

What to read: For each TikTok Shop product, impressions, clicks, add to carts and orders from its product card, plus stock and listing status
What to give me: Products seen but not clicked, or clicked but not bought, with the likely fix for each

Synthesis tools to use:
- `tiktok_metric metric=shop_product_performance days=30 limit=30 grain=product`
- `tiktok_metric metric=shop_product_mix months=3 limit=30`

Steps:
1. Call `tiktok_metric metric=shop_product_performance days=30 limit=30 grain=product`.
2. Compare each product's click rate and click-to-order rate with the shop average.
3. Call `tiktok_metric metric=shop_product_mix months=3 limit=30` for declared stock and listing status.
4. Low click rate: image, price, title. Low click-to-order: price, reviews, delivery time, stock.

Checks before answering:
- Rates are computed from the window's totals, not averaged daily. Keep it that way.
- Products under 1,000 impressions are too small to judge.
- TikTok serves 120 days at most.

Output:
- One line: the biggest leak.
- A table: product, impressions, click rate, click-to-order rate, orders, leak, fix.

Never:
- Never edit TikTok Shop listings.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-tiktok-product-card-funnel". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
