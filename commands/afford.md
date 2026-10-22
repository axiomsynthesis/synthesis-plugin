---
description: "Test a purchase order (needs your cash balance): The sell-out date an order prevents and the units it covers. No cash verdict yet"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Test a purchase order (needs your cash balance)

Channel: Inventory · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Test a purchase order (needs your cash balance)" (id: ops-can-we-afford-this-po, Inventory).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Tests a purchase order before it is placed. It shows the run-out date the order prevents and how many units it covers. It does not say whether you can afford it. That needs a week-by-week cash forecast with payouts and bills, which this cannot build yet.

What to read: Entered cash, open purchase orders, Amazon stock and its run-out forecast, stock and orders already placed in NetSuite
What to give me: The sell-out date an order prevents and the units it covers. No cash verdict yet

Synthesis tools to use:
- `cost_rules for=ops-can-we-afford-this-po`
- `operator_inputs section=cash`
- `operator_inputs section=purchase_orders`
- `amazon_metric metric=stockout_forecast limit=200`
- `netsuite_metric metric=inventory_position limit=200`

Steps:
1. Ask for the order: products, units, unit cost, deposit and balance terms.
2. Call `operator_inputs section=cash` for cash on hand, and `operator_inputs section=purchase_orders` for orders already entered. It holds no cash floor.
3. Call `netsuite_metric metric=inventory_position limit=200` for units already on order, stock at your own warehouse and `lead_time_days`. Use only its non-Amazon locations. Its Amazon count runs stale. If NetSuite is not connected, ask for open orders.
4. Still missing the lead time, cash on hand, the cash floor or stock at your own warehouse: ask for each in one plain question. Say the dollars it moves: a lead time a month longer means a month of sales short; cash decides the cash-left line.
5. Call `amazon_metric metric=stockout_forecast limit=200` for the products on the order: `late_runs_out`, `runs_out_for_good`, `normal_pace_per_day` and each sale in `events`. Read every page: call again with the next `result_page` the result names.
6. Arrival = today plus the lead time. Compare it with the run-out date without the order. Units short without it = `normal_pace_per_day` times the days from run-out to arrival, plus sale `extra_units` in that gap. Days covered = order units over that pace.
7. Only with cash on hand, entered or given: cash left = cash on hand minus the deposit, minus the balance, minus other open orders due before the balance. Compare it with the cash floor if given.

Checks before answering:
- With no cash on hand entered or given, give only the date and units. Never a cash line.
- Even with cash entered, cash left is plain subtraction. Payouts, bills and ad spend in between are not counted. Never call it affordable.
- Credit the order only with sales stock you already have could not make. Stock on hand is not a return on the new order.
- Never use the inventory scenario tool here. It grows demand with month-to-month swings and credits stock on hand to the order.
- The cash floor and payment terms come only from the person.
- A failed stock read is not zero stock. If the stock feed failed, say so and stop.

Rounds (relook before you answer):
1. **Counted twice.** Fails when: units on order in NetSuite also show as stock landing at Amazon in the forecast. Fix: count them once.
2. **Lead time stress.** Re-run step 6 with the lead time 30 days longer. Fails when: the order no longer lands before the run-out. Fix: say the order is late on a normal slip, and by how many units.
3. **Sale in the gap.** Fails when: a known sale in `events` falls between run-out and arrival. Fix: add its `extra_units` and lead with it.
4. **Money already on order.** Fails when: an entered open order is over 30 days old or has no due date. Fix: ask whether it is still open before the cash line.
5. **Too much stock.** Fails when: the order covers over 180 days of normal sales. Fix: say the cash and storage tied up, and offer a smaller first order.

Output:
- Four lines: the run-out it prevents and when, units short without it, days the order covers, and cash left only if cash is known.
- One line on what this cannot answer: whether the cash holds week by week.

Never:
- Never place, change or cancel a purchase order.
- Never invent lead times, minimum order quantities or payment terms.
- Never give a yes or no on affordability.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Inputs only I know: supplier lead time in days; cash in the bank; the lowest cash you will let the business hold; units at your own warehouse or 3PL. If the tools lack one, ask me ONE plain question for it, all in one message: why it matters and about how many dollars it moves. Use my answer for this run. Never invent one. If I do not know, say what the answer leaves out. Then tell me to save cash on the Costs (COGS) page, Cash box. Nothing saves the lead time, the cash floor or own warehouse stock yet: say it was used for this run only. On a scheduled run, name what is missing instead.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-can-we-afford-this-po". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
