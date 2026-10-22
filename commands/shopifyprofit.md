---
description: "Website profit after every cost: One month of website profit line by line, which costs are counted and which have no data yet, and profit before and after ads"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Website profit after every cost

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Website profit after every cost" (id: money-website-profit-every-cost, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lays out website profit for one month the way the Profit page counts it: sales after tax, discounts, refunds, product cost, card and payment fees, shipping and warehouse costs. Then it sets the ad spend beside it. It names every cost line that has no data yet, so a high margin is never read as real when costs are missing.

What to read: Website orders, discounts, refunds, product cost and fees as the Profit page shows them, orders other marketplaces sent into the store, and Meta, Google and TikTok ad spend by where it sends shoppers
What to give me: One month of website profit line by line, which costs are counted and which have no data yet, and profit before and after ads

Synthesis tools to use:
- `cost_rules for=money-website-profit-every-cost`
- `shopify_metric metric=profit month=YYYY-MM`
- `net_revenue_dtc month=YYYY-MM`
- `operator_inputs section=cogs`

Steps:
1. Call `shopify_metric` with `metric=profit` and `month=` set to last month.
2. If the result has `no_headline_reason`, there is no profit to state. Say why in plain words, list the products in `uncosted_products`, and say entering their costs on the costs page fixes it. Still show the lines that are real.
3. Read every entry in `column.lines` when present. Sort them into three groups: counted, estimated, and not connected.
4. `value` is profit on the website's own orders. If `marketplace_orders` is present, show it as its own line: orders another marketplace sent into the store, with their sales, orders and `profit_before_commission`. Say the app's commission on them is not connected. `own_store` plus `marketplace_orders` add back to `column_profit`.
5. Call `net_revenue_dtc` with the same month. If its revenue differs from `own_store.sales` by more than 5%, state both figures. Then say which orders make the difference, usually the `marketplace_orders` sales or TikTok Shop orders sent into the store. Never pick one figure and drop the other.
6. Read `ad_columns` and `profit_after_ads`. Show profit before ads, then `profit_after_ads.pointed_here`, the ad spend that sends shoppers to the website, and `profit_after_ads_pointed_here`. Give `profit_if_unknown_ads_also_pointed_here` as the low end of the range. Name the spend in `pointing_elsewhere`. It never comes off the website.
7. Call `operator_inputs` with `section=cogs` to check costs are entered for the products the website sells.

Checks before answering:
- Read `data_quality_flags` first. Each line not connected makes profit too high. Say so in the same sentence as the profit.
- If `gated` is true, there is no number. Give the reason, not a guess.
- A margin above 70% on physical products almost always means costs are missing. Say that, and do not call the channel very profitable.
- Shipping and fees are paid per order, so a small order can lose money while the month looks fine. Give profit per own-store order beside the average order value.
- Meta and Google ads can send buyers to Amazon too. Only `pointed_here` comes off the website. Never take all of their spend off it. Show the range.
- Use a closed month. The current month is still taking orders and refunds.
- Never call the marketplace orders website profit. They never visited the website. If they are more than a small share of the column, say so in the first line. Their app's commission is not counted yet, so their profit reads high.

Rounds (relook before you answer):
1. **Own store first.** Fails when: orders sent in by another marketplace are over 20% of the column and the first line leads with the combined profit. Fix: lead with own-store profit.
2. **Shipping and card fees per order.** Fails when: orders shipped but shipping cost per order is not counted or estimated, or card fees are not loaded. Fix: say profit reads high, and by about how much where an estimate exists.
3. **Refunds really in.** Fails when: refunds are under 0.5% of sales in a month with more than 200 orders. Fix: say refunds may not be loaded, and profit reads high.
4. **Profit per order after ads.** Fails when: profit after ads per own-store order is below zero and the answer does not say the loss per order. Fix: lead with it, and the order size it would take to break even.
5. **Ads range.** Fails when: spend with no known destination is larger than spend pointed here and only one profit figure is given. Fix: give the range.
6. **What moved since last time.** Fails when: profit moved more than 20% from the last run or month before and no line explains most of it. Fix: name the lines, or call it unexplained.

Output:
- One line first: profit on orders placed on the website, before ads, for the month, its share of the website's own sales, and how many cost lines are missing.
- A second line when present: orders other marketplaces sent in, their sales and profit before the app's commission.
- A table: line, dollars, share of sales, counted / estimated / not connected.
- Two lines: profit after website ads as a range, and the one missing feed that would change the answer most.
- One move: the cost to enter or the feed to connect first.

Never:
- Never fill a missing fee or cost with an industry average.
- Never compare this to Amazon profit while lines here are not connected.
- Never move ad budget. A person does that.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-website-profit-every-cost". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
