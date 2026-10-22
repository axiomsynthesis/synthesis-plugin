---
description: "Was it price, volume or mix?: How much of a revenue change came from units, price, mix, and new or dropped products"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Was it price, volume or mix?

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Was it price, volume or mix?" (id: ops-price-volume-mix-bridge, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits a revenue change into plain causes: more or fewer units, higher or lower price per unit, a shift toward pricier or cheaper products, and products that were new or dropped. It compares like with like, so a sale event that moved between months is not read as a price or volume change.

What to read: Units and net revenue per product for two periods on Amazon
What to give me: How much of a revenue change came from units, price, mix, and new or dropped products

Synthesis tools to use:
- `cost_rules for=ops-price-volume-mix-bridge`
- `query_series metric=units grain=month asin=<asin>`
- `query_series metric=net_revenue grain=month asin=<asin>`
- `top_products metric=revenue top_n=25 start_month=<YYYY-MM> end_month=<YYYY-MM>`
- `brand_brain action=moves kind=promotion`
- `query_series metric=units grain=week`
- `emit_chart type=waterfall`

Steps:
1. Pick the two periods. By default, the last 12 closed months against the 12 before. If the person picks a quarter or a month, call `brand_brain action=moves kind=promotion` with `since` and `until` covering both periods, to find big sale events such as Prime Day. The move log holds the brand's own logged events. If it shows none, call `query_series metric=units grain=week` over both periods and treat a week far above its neighbours as a sale event. If only one period has one, move the window so both do or neither does, and say so.
2. Call `top_products metric=revenue top_n=25` with `start_month` and `end_month` set to each period to choose the products that make up most of revenue. Put everything else in an "all other" row.
3. That read gives revenue and units per product. Only for a product whose units are missing, call `query_series metric=units grain=month asin=<asin>` and `query_series metric=net_revenue grain=month asin=<asin>` over both periods.
4. Sort products into three groups: sold in both periods, new (later period only) and dropped (earlier period only). New and dropped products are their own bars, at their own revenue.
5. For products sold in both periods only: price per unit = revenue divided by units. Volume = change in their total units times the earlier period's average price. Price = sum of later units times the change in that product's price. Mix = sum of (later share minus earlier share) times later total units times the earlier price.
6. Draw it with `emit_chart type=waterfall`. Pass the earlier total first, then only the volume, price, mix, new and dropped changes. Never pass the later total as a last bar: it would be stacked on top. The top of the last step is the later total. Say that figure in the summary.

Checks before answering:
- The bars must add to the total change within $1. If they do not, show the gap as "unexplained" and never fold it into mix.
- Revenue here is after promotions, so deeper coupons and deals show up as price. Say so beside the price bar. A split of list price from discount depth is not available yet.
- If you moved a period to line up a sale event, say which event and the new dates.
- Compare whole periods only. Leave out the running month.

Rounds (relook before you answer):
1. **It adds up.** Fails when: the bars miss the total change by more than $1. Fix: show the gap as "unexplained".
2. **Sale events lined up.** Re-read the promotion moves and weekly units. Fails when: one period holds a week more than 2x its neighbours and the other does not. Fix: move the window and say so.
3. **Price or discount?** Fails when: the price bar is over 30% of the change and the move log shows deeper deals or coupons in the later period. Fix: say the price bar is mostly discounting, not list price.
4. **Second window.** Re-run the bridge on the period one quarter earlier. Fails when: the main driver changes sign or drops out of the top two. Fix: say the call is not stable and lead with what both windows agree on.
5. **Too much in "all other".** Fails when: the "all other" row is more than 25% of the change. Fix: call `top_products` again with `top_n=50`.

Output:
- One line first: the main driver in dollars and what to do about it.
- Chart plus table: Effect | Dollars | Share of the change.
- A second table for the top five products by contribution to the change, with new and dropped products named.
- One line on the one to watch.

Never:
- Never mix order-basis revenue with settlement revenue in one bridge.
- Never call a mix gain good news on its own. A shift to bigger packs can lift revenue and cut profit per unit.
- Never compare a part month.
- Never change prices.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-price-volume-mix-bridge". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
