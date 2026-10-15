# Is GMV Max earning its spend?

Channel: TikTok Shop · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is GMV Max earning its spend?" (id: mkt-tiktok-gmv-max-return, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
GMV Max credits itself with sales that may have happened anyway. This checks its return against total shop sales and against what TikTok actually pays you.

What to read: TikTok Shop ad cost, ad-credited sales and orders by month, set against total shop sales and payouts
What to give me: What GMV Max really returns across total shop sales and payouts, not just the sales it credits itself

Synthesis tools to use:
- `tiktok_metric metric=shop_ad_efficiency months=6`
- `tiktok_metric metric=shop_sales_trend months=6`
- `tiktok_metric metric=shop_payouts months=6`
- `tiktok_metric metric=spend_trend months=6`

Steps:
1. Call `tiktok_metric metric=shop_ad_efficiency months=6` for cost and credited sales by month.
2. Call `tiktok_metric metric=shop_sales_trend months=6` for total shop sales, samples excluded.
3. Call `tiktok_metric metric=spend_trend months=6` for any other TikTok ad spend.
4. Call `tiktok_metric metric=shop_payouts months=6` for the payout rate after fees and shipping.
5. Compare month-to-month changes in ad spend with changes in total sales. That ratio is the extra return. Multiply by payout rate for cash return.

Checks before answering:
- Ad-credited sales are a slice of total sales. Never add them together. The credited figure can even exceed total.
- Months with big promotions or viral videos break the comparison. Name them.
- Payout months are not the same orders as sales months. Use payout rates, never payout dollars, against sales.
- Exclude the current month.

Output:
- Three lines: credited return, extra return from total sales, cash return after payout rate.
- A table: month, ad cost, credited sales, total sales, payout rate.

Never:
- Never change GMV Max budgets.
- Never add credited sales to shop sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-tiktok-gmv-max-return". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
