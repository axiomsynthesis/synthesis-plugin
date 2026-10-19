---
description: "TikTok Shop profit after every fee: One month of TikTok Shop profit line by line, what is unpaid, and the shop-ad return it needs to break even"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# TikTok Shop profit after every fee

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "TikTok Shop profit after every fee" (id: money-tiktok-shop-profit-every-fee, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what TikTok Shop really left you for one month: sales, then TikTok's commission and fees, shipping and TikTok fulfilment, refunds, free creator samples, warehouse charges and product cost, the same way the Profit page counts them. It checks the sales against what TikTok recorded, shows what is still unpaid, and sets TikTok ad spend beside it.

What to read: TikTok Shop sales, TikTok commission and fees, shipping, refunds, free samples, product cost, what TikTok paid out, and TikTok ad spend
What to give me: One month of TikTok Shop profit line by line, what is unpaid, and the shop-ad return it needs to break even

Synthesis tools to use:
- `cost_rules for=money-tiktok-shop-profit-every-fee`
- `tiktok_metric metric=shop_profit month=YYYY-MM`
- `tiktok_metric metric=shop_payouts months=3`
- `tiktok_metric metric=shop_returns months=3`
- `tiktok_metric metric=spend_trend months=3`
- `operator_inputs section=cogs`

Steps:
1. Call `tiktok_metric` with `metric=shop_profit` and `month=` set to last month.
2. If the result has `no_headline_reason`, there is no profit to state. Say why, list `uncosted_products`, and say entering their costs on the costs page fixes it. Still show the lines that are real.
3. Read every entry in `column.lines` when present, and `column.tie_out`. Sort the lines into counted, estimated (orders not paid out yet) and not connected.
4. Call `tiktok_metric` with `metric=shop_payouts` and `months=3`. Report the fee, shipping and payout rates for the last three statement months, the amount not yet paid, and any fee type that moved more than 2 points.
5. Call `tiktok_metric` with `metric=shop_returns` and `months=3` for the refund rate. Split delivery failures from complaints.
6. Call `tiktok_metric` with `metric=spend_trend` and `months=3`. For the same month read `shop_ad_spend`, `shop_ad_revenue`, `shop_ad_roas` and `auction_spend`. Profit after shop ads = profit before ads minus `shop_ad_spend`. Show `auction_spend` on its own line as "may drive other channels", never taken off shop profit.
7. Break-even shop-ad return = shop sales divided by (profit before ads plus free samples plus creator pay). Set `shop_ad_roas` beside it and say how far below or above it.
8. Call `operator_inputs` with `section=cogs` to check costs are entered for the products TikTok sells.

Checks before answering:
- Read `data_quality_flags` first. If `gated` is true, there is no number: give the reason.
- If `tie_out` shows our sales do not match TikTok's own record, say so before any profit.
- Free samples are a real cost of selling on TikTok. They are not sales.
- A statement month is not the same orders as a sales month. Use the profit column for profit and the payouts only for rates and what is unpaid.
- Reserve holds are your money held back, not a fee.
- A margin above 60% after TikTok fees usually means product cost is missing. Say so.
- Creator pay is taken off profit but may not be listed in `column.lines`. If the lines do not add up to the profit, say the gap is unlisted, most likely creator pay.
- Shop-ad return is TikTok's own credit. When shop-ad sales near all shop sales, treat it as a ceiling, not proof the ads caused them.

Output:
- One line first: do shop ads pay? Shop-ad return against its break-even, and profit after shop ads. If the return is below break-even, say the shop loses money on shop ads, and by how much.
- One line: TikTok Shop profit before ads for the month, its share of sales, settled or partly estimated.
- A table: line, dollars, share of sales, counted / estimated / not connected.
- Three lines: what TikTok takes per $100 of sales, the amount not yet paid, and auction ad spend on its own.
- One move: the one fee, cost or ad budget to work on first, and the number that shows it worked.

Never:
- Never call order sales the payout.
- Never count ad-credited shop sales on top of shop sales.
- Never guess a product cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-tiktok-shop-profit-every-fee". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
