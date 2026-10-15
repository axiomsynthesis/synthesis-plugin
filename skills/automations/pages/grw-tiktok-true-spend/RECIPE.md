# Your real TikTok ad spend

Channel: TikTok Ads · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Your real TikTok ad spend" (id: grw-tiktok-true-spend, TikTok Ads).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
TikTok reports ad spend in two separate places. Reading one alone has made a big account look tiny. This adds both, checks nothing is missing, and shows what each part returned.

What to read: TikTok auction ad spend and shop ad (GMV Max) spend by month
What to give me: Total TikTok ad spend from both places it's reported, and what each part returned

Synthesis tools to use:
- `tiktok_metric metric=coverage`
- `tiktok_metric metric=spend_trend months=6`
- `tiktok_metric metric=shop_ad_efficiency months=6`

Steps:
1. Run `tiktok_metric metric=coverage`.
2. Pull `tiktok_metric metric=spend_trend months=6` for auction ads.
3. Pull `tiktok_metric metric=shop_ad_efficiency months=6` for shop ads.
4. Add the two per month for total spend. Show each part's platform-reported return separately.

Checks before answering:
- Run `tiktok_metric metric=coverage` first. If any authorized ad account is not selected or the authorization is near its 30-day end, say so before reading spend.
- TikTok spend lives in two places that never overlap: auction ads and shop ads (GMV Max). Always name which you quote, and add them only for total spend.
- Platform-reported return is not settled cash and can exceed whole-shop sales. Never add it to shop sales.
- Exclude the current month unless asked.

Output:
- Answer first: total spend last month and the split. Table by month: auction spend, shop ad spend, total, each return.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-tiktok-true-spend". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
