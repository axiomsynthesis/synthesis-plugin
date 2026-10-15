# Why TikTok Shop orders come back

Channel: TikTok Shop · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Why TikTok Shop orders come back" (id: mkt-tiktok-returns-read, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Returns hurt both money and the shop score. This shows rates, reasons and the change behind a rise.

What to read: TikTok Shop return requests, refunds, replacements and reasons by month
What to give me: Return and refund rates, the reasons, who started each return, and the product or shipping fix

Synthesis tools to use:
- `tiktok_metric metric=shop_returns months=6 limit=15`
- `tiktok_metric metric=shop_sales_trend months=6`

Steps:
1. Call `tiktok_metric metric=shop_returns months=6 limit=15`.
2. Call `tiktok_metric metric=shop_sales_trend months=6` to put refunds against sales.
3. Find the reason that grew most and the month it started. Ask the person what changed that month.

Checks before answering:
- Return rate counts completed returns over orders. Refund rate is refunds over sales. Never mix them.
- Open requests are not final. Recent months will rise.
- Samples are excluded from sales. Keep them out of the rate.

Output:
- One line: return rate, refund dollars, and the reason that grew.
- A table: month, return rate, refund rate, refunds, top reason.

Never:
- Never approve or reject return requests.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-tiktok-returns-read". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
