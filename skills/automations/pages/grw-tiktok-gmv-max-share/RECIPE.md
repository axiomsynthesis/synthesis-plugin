# How much of TikTok Shop is bought with ads?

Channel: TikTok Ads · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How much of TikTok Shop is bought with ads?" (id: grw-tiktok-gmv-max-share, TikTok Ads).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Compares the whole TikTok Shop's sales with the sales GMV Max ads claim. When ads claim most of the shop, it asks whether organic and creator sales are being re-labelled as ad sales.

What to read: TikTok Shop sales against sales credited to shop ads
What to give me: The share of shop sales that ads take credit for, and what that means for budget

Synthesis tools to use:
- `tiktok_metric metric=coverage`
- `tiktok_metric metric=shop_sales_trend months=6`
- `tiktok_metric metric=shop_ad_efficiency months=6`
- `tiktok_metric metric=shop_video_performance days=90 limit=20`

Steps:
1. Run `tiktok_metric metric=coverage`.
2. Pull `tiktok_metric metric=shop_sales_trend months=6` for all shop sales.
3. Pull `tiktok_metric metric=shop_ad_efficiency months=6` for ad-credited sales and spend.
4. Pull `tiktok_metric metric=shop_video_performance days=90 limit=20` for sales credited to creators' videos over the last 90 days. TikTok's bestseller lists rank the whole US market, not your shop, so never use them for this.
5. Compute ad-credited sales over shop sales per month, and spend over shop sales.

Checks before answering:
- Run `tiktok_metric metric=coverage` first. If any authorized ad account is not selected or the authorization is near its 30-day end, say so before reading spend.
- TikTok Shop orders include free samples sent to creators. Exclude zero-price sample orders before computing shares.
- Ad-credited sales can overlap creator sales. Show them side by side, never summed.
- The creator read covers the last 90 days, not calendar months. Put it beside the matching months and say so.

Output:
- Answer first. Table by month: shop sales, ad-credited sales, share, ad spend, spend as share of shop sales.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-tiktok-gmv-max-share". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
