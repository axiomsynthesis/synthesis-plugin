---
description: "Walmart profit after every fee: Walmart profit line by line, what Walmart takes per $100, and what is unpaid"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Walmart profit after every fee

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Walmart profit after every fee" (id: money-walmart-profit-every-fee, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows what Walmart Marketplace really left you for one month: sales, then Walmart's commission, fulfilment and label charges, warehouse and service fees, refunds and product cost, the same way the Profit page counts them. It checks the sales against what Walmart itself recorded and says what is still unpaid.

What to read: Walmart Marketplace sales, Walmart commission, fulfilment and label charges, warehouse and service fees, refunds, product cost, and what Walmart paid out
What to give me: Walmart profit line by line, what Walmart takes per $100, and what is unpaid

Synthesis tools to use:
- `cost_rules for=money-walmart-profit-every-fee`
- `walmart_metric metric=profit month=YYYY-MM`
- `walmart_metric metric=payouts periods=6`
- `walmart_metric metric=orders_trend months=12`
- `operator_inputs section=cogs`

Steps:
1. Call `walmart_metric` with `metric=profit` and `month=` set to last month. If it has `stopped_selling_since`, say Walmart had no sales since that date, so the month made $0 from Walmart sales. Never call it not connected. Then stop.
2. If the result has `no_headline_reason`, there is no profit to state. Say why and list `uncosted_products`. Still show the lines that are real.
3. If the month has no orders, call `walmart_metric` with `metric=orders_trend` and `months=12`. Find the last month with orders and say the channel has sold nothing since then. Stop there.
4. Read every entry in `column.lines` and `column.tie_out`. Sort the lines into counted, estimated (orders not paid out yet) and not connected.
5. Call `walmart_metric` with `metric=payouts` and `periods=6` for what Walmart paid out and its fee rates per payout.
6. Call `operator_inputs` with `section=cogs` to check costs are entered for the products Walmart sells.

Checks before answering:
- Read `data_quality_flags` first. If `gated` is true, there is no number: give the reason.
- If `tie_out` shows our sales do not match Walmart's own record, say so before any profit.
- A payout period is not the same orders as a sales month. Use the profit column for profit and the payouts only for rates and what is unpaid.
- A small month swings on a handful of orders. Say how many orders the month holds.
- A connected account with no orders is a stopped channel, not an unconnected one. Never call it unconnected. Say the date it last sold.
- Check the date of the newest payout. If it is more than a month old while orders still come in, say the payouts may be stale and the fee rates may be out of date.
- Walmart Connect ad spend is not read yet. If the brand runs Walmart ads, profit here reads too high. Say so in plain words.

Rounds (relook before you answer):
1. **Stopped or selling.** Re-read `orders_trend`. Fails when: orders appear after the stopped date. Fix: drop "stopped" and read the month.
2. **Payouts fresh.** Fails when: the newest payout is more than 35 days old while orders came in. Fix: say fee rates may be stale and unpaid is larger than shown.
3. **Small month.** Fails when: the month has under 30 orders and a margin is given without the order count and the 3-month average beside it. Fix: add both.
4. **Walmart ads counted.** Read the cost rules found. Fails when: a retail media or Walmart ad line appears there and profit does not name it. Fix: give profit after it as a second line, or ask.
5. **Marketplace, not stores.** Fails when: Walmart store sales from the stores and wholesale column are mixed into this profit. Fix: keep them apart and say store sales are elsewhere.

Output:
- One line first: Walmart profit for the month, its share of sales, settled or partly estimated. If the channel has stopped selling, that line is the date it last sold and nothing else.
- A table: line, dollars, share of sales, counted / estimated / not connected.
- Two lines: what Walmart takes per $100 of sales, and the amount not yet paid.
- One move: the one fee or cost to work on first.

Never:
- Never call order sales the payout.
- Never guess a product cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-walmart-profit-every-fee". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
