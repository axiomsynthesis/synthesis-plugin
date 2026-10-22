---
description: "Get ready for the next big Amazon sale: A go or fix checklist three weeks before a big sale event, a low, middle and high sales forecast, and a day-one read of the live sale"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Get ready for the next big Amazon sale

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Get ready for the next big Amazon sale" (id: mkt-amazon-prime-event-readiness, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Most big sale event losses are set three weeks before: no stock, no buy box, a capped budget, or a deal price that is not low enough. This checks each product against each and gives a fix list with dates. It also forecasts the sale from your last two big sales, and on the first sale day reads whether it is on pace.

What to read: Stock cover, buy box, ratings, ad budget caps, deal prices against recent prices, sales on the last two big sales, and on sale day the live sales and ads
What to give me: A go or fix checklist three weeks before a big sale event, a low, middle and high sales forecast, and a day-one read of the live sale

Synthesis tools to use:
- `amazon_metric metric=stockout_forecast limit=200`
- `amazon_metric metric=buybox_health days=30 limit=40`
- `amazon_metric metric=rating_watch days=60 limit=30`
- `amazon_metric metric=ppc_budget_utilisation days=30 limit=50`
- `amazon_metric metric=velocity_momentum weeks=52 asin=<asin>`
- `shelf_history marketplace=amazon days=30`
- `amazon_metric metric=daily_revenue start_date=YYYY-MM-DD end_date=YYYY-MM-DD tz=America/Los_Angeles`
- `meta_metric metric=amazon_ads period=week`

Steps:
1. Ask the person for the event date and the products in the event.
2. Call `amazon_metric metric=stockout_forecast limit=200` and read each product's `events` for this sale (`x_normal`, `extra_units`, `extra_units_high`) and `late_runs_out`. Use `amazon_metric metric=velocity_momentum weeks=52 asin=<asin>` only for a product with no event history.
3. Use the `late_runs_out` date from step 2, not days of cover, because days of cover does not include the event lift. Will each product cover the event at last year's lift plus two weeks after?
4. Call `amazon_metric metric=buybox_health days=30 limit=40` and `amazon_metric metric=rating_watch days=60 limit=30`. Use `days_below_sla` and `avg_buy_box_pct` (the day average), not `wtd_buy_box_pct`. A product fails at 3 or more days under 90% in 30. Also flag a rating step down.
5. Call `amazon_metric metric=ppc_budget_utilisation days=30 limit=50` for campaigns that cap out today. Ask whether the account has event budget rules. On one live brand, day-one spend ran over 4x the listed daily budgets, so a listed budget is not always the cap.
6. Call `shelf_history marketplace=amazon days=30` for your own recent prices. A deal must beat the recent low Amazon checks against. Remind the person to confirm the exact rule in Seller Central. This history is weekly and misses deal days, so take the recent low from Seller Central.
7. Forecast. Call `amazon_metric metric=daily_revenue start_date=YYYY-MM-DD end_date=YYYY-MM-DD tz=America/Los_Angeles` for each of the last two big sales and the 4 weeks before each. Lift is sales a sale day over a normal day. Today's normal day is the last 28 days. Low: the lower of the two lifts x today's normal day. High: the higher one. Middle: in between, nudged up for a shorter sale, which packs more into each day. Subtract the normal sales lost in the days around the sale.
8. Day one, by midday Pacific: call step 7's tool for today and label it still coming in. Compare with the low case's pace. For ads that send shoppers from Meta to Amazon, call `meta_metric metric=amazon_ads period=week`. Defaults, change them to your own: over $20 a day per Amazon order, cut that ad's daily budget hard; under $12, keep it. Amazon credit lags, so also check the cost per click against your best ads.

Checks before answering:
- Stock is Amazon's live count. Quote Amazon's update time. Count inbound units only if they will be checked in before the event; stock moving between Amazon warehouses usually returns within days.
- A product with no event last year has no lift to borrow. Use the family's lift and say so.
- Never state Amazon's deal eligibility rules as fact. They change. Point to Seller Central.
- The budget column is per campaign, not per product. No tool maps campaigns to products yet. Say so, never fill it by guess.
- If the last 30 days held a big sale, budget caps from that window run high. Say so.
- The check-in cut-off is not computed. Take it from Seller Central.
- Use Pacific days for sale days. A sale's last day spills into the next day in other time zones.
- The forecast is a range from two past sales, never a promise. Which deals were booked can swing it most.

Rounds (relook before you answer):
1. **Cross-check the forecast.** Take last year's same sale x this year's change against last year in normal weeks. Fails when: that lands outside the low to high range. Fix: say which input differs and widen the range.
2. **Stock against the high case.** Fails when: any product's high case uses over 75% of its sellable stock, or `late_runs_out` falls before 14 days after the sale. Fix: move it to the top of the fix list with the check-in date.
3. **Budget advice.** Fails when: a fix says raise a budget only because it capped in a window with no sale. Fix: drop it, or tie it to the account's event budget rules.
4. **Deal price.** Fails when: a deal price is not under the recent low the person read in Seller Central. Fix: show the price it needs to beat.
5. **Day-one pace.** Re-read step 8. Fails when: sales by midday Pacific run more than 15% under the low case's pace. Fix: check each top product for a live deal, the buy box, stock and price, in that order.
6. **Grade it.** Two days after the sale ends, call step 7's tool for the sale days. Fails when: the actual lands outside low to high. Fix: name the input that missed and keep it for the next forecast.

Output:
- One line first: go or fix, how many products are ready, the first fix with its date, and the low, middle and high forecast.
- A table: product, stock ready, buy box, rating, budget, deal price check, fix and by when.
- On sale day: sales so far against the low case, and each Meta to Amazon ad to cut or keep.

Never:
- Never create deals, shipments or budget changes.
- Never promise an event result.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-prime-event-readiness". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
