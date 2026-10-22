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

What to read: TikTok Shop sales, TikTok commission and fees, shipping, refunds, free samples, product cost, what TikTok paid out, and TikTok ad spend by where it sends shoppers
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
5. Call `tiktok_metric` with `metric=shop_returns` and `months=3` for the refund rate. Split failed deliveries from complaints.
6. Read `ad_columns` and `profit_after_ads`. Profit after shop ads is `profit_after_ads_pointed_here`. `profit_if_unknown_ads_also_pointed_here` is the low end.
7. Call `tiktok_metric` with `metric=spend_trend` and `months=3`. Read `shop_ad_roas` and `auction_spend` for the month. Show `auction_spend` on its own line as "may drive other channels".
8. Break-even shop-ad return = shop sales divided by (profit before ads plus free samples plus creator pay). Set `shop_ad_roas` beside it and say how far below or above it.
9. Call `operator_inputs` with `section=cogs` to check costs are entered for the products TikTok sells.

Checks before answering:
- Read `data_quality_flags` first. If `gated` is true, there is no number: give the reason.
- If `tie_out` shows our sales do not match TikTok's own record, say so before any profit.
- Free samples are a real cost of selling on TikTok. They are not sales.
- A statement month is not the same orders as a sales month. Use the profit column for profit and the payouts only for rates and what is unpaid.
- Reserve holds are your money held back, not a fee.
- A margin above 60% after TikTok fees usually means product cost is missing. Say so.
- Creator pay is taken off profit but may not be listed in `column.lines`. If the lines do not add up to the profit, say the gap is unlisted, most likely creator pay.
- Shop-ad return is TikTok's own credit. When shop-ad sales near all shop sales, treat it as a ceiling, not proof the ads caused them.

Rounds (relook before you answer):
1. **Ties to TikTok.** Fails when: `tie_out` misses TikTok's own record by more than 1%. Fix: say so first, and do not call the profit final.
2. **Creator pay and samples in.** Fails when: the lines miss the profit by more than $1 and the gap is not named, or samples are $0 in a month creators posted. Fix: name the gap as creator pay or samples.
3. **Shop-ad credit is a ceiling.** Fails when: shop-ad credited sales are over 80% of shop sales and the answer treats the return as caused. Fix: call it a ceiling.
4. **Cost present.** Fails when: units have no cost or the margin after TikTok fees is above 60%. Fix: say "product cost missing for X% of sales" in the first line.
5. **Unpaid share.** Fails when: more than 25% of sales are not paid out and the answer calls profit settled. Fix: say partly estimated.
6. **What moved since last time.** Fails when: profit after ads moved more than 20% from the last run or month before and no line explains most of it. Fix: name the lines.

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
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-tiktok-shop-profit-every-fee". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
