---
description: "Match our profit to your profit app: Our profit and the outside app's set side by side line by line, every gap in dollars with which side is right and why, and the fix for each"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Match our profit to your profit app

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Match our profit to your profit app" (id: money-profit-tool-match, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lines up our profit against the number an outside profit app shows for the same month, line by line.
It finds each gap, says which side is right and why, and gives the fix.
The settlement report, what Amazon actually paid, is the judge when the two disagree.

What to read: The outside profit app's numbers for one month from a file or paste, our Amazon profit line by line for the same month, what Amazon paid out, fees, refunds, reimbursements, promotions, ad spend, product cost per product and the whole-business profit
What to give me: Our profit and the outside app's set side by side line by line, every gap in dollars with which side is right and why, and the fix for each

Synthesis tools to use:
- `cost_rules for=money-profit-tool-match`
- `list_files`
- `search_files`
- `read_file`
- `ingest_file`
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`
- `amazon_metric metric=pnl month=YYYY-MM`
- `amazon_metric metric=fee_breakdown month=YYYY-MM`
- `amazon_metric metric=reimbursements`
- `amazon_metric metric=promotion_performance months=3`
- `amazon_metric metric=contribution_by_asin month=YYYY-MM`
- `amazon_metric metric=ad_spend_monthly months=3`
- `business_profit month=YYYY-MM`

Steps:
1. Ask which month and which app. Pick a closed month whose payouts are in. Call `list_files` or `search_files` for the app's export, then `read_file`. If the owner pastes or attaches it in chat, store it with `ingest_file` first so later rounds read the same copy. No export means: show our side for the month (the Output table, app column blank), then ask for the file in one message listing what it must hold: every line it shows, its date basis (order or payout date), the stores it covers, and its cost per product. Never guess their numbers. Say if the month holds a big sale (Prime, Black Friday).
2. Write down the app's lines: sales, discounts, refunds, Amazon fees, account charges, reimbursements, ads, product cost, shipping, freight and profit. Note its date basis (order date or payout date) and which stores it covers.
3. Call `amazon_metric` with `metric=pnl_waterfall` and `month=YYYY-MM` for our lines. If the app covers more than Amazon, also call `business_profit` with the same month.
4. Call `amazon_metric` with `metric=pnl` and `month=YYYY-MM` for what Amazon paid out. Call it with `metric=fee_breakdown` and the same month, and `metric=promotion_performance` with `months=3` for fee and discount detail. Three clocks: `fee_breakdown` counts the month Amazon posted a fee, `pnl_waterfall` order date, `pnl` the order month as paid. Judge each fee against `pnl`, never against `fee_breakdown`. `metric=reimbursements` gives reasons and their size only: it is a rolling 90-day total with no month rows. The month's reimbursements are the `adjustments` line of `pnl_waterfall`.
5. Call `amazon_metric` with `metric=ad_spend_monthly` and `months=3` for Amazon ad spend by month. Check which other ad spend each side charges to Amazon.
6. Call `amazon_metric` with `metric=contribution_by_asin` and `month=YYYY-MM` for our cost per product (product cost over units). Set it beside the app's where its export has one.
7. Build one table: line, the app, ours, gap. Work the biggest gap first. For each, name the cause and who is right. Usual causes: date basis; another country's store counted; cancelled orders that were paid; refunds counted before or after the discount given back; returned stock put back for sale; shipping charged without the shipping income; inbound freight left in or out; a product with no cost on one side; ads booked to the wrong store.

Checks before answering:
- What Amazon paid out decides any line both sides take from Amazon. Product cost and freight are the owner's call: ask, never assume.
- Match month, date basis and stores before calling any line wrong.
- A gap is explained only when its dollars are named. Show what is left unexplained.
- If our month is still settling, say so first. The gap will move.

Rounds (relook before you answer):
1. **Same month, same clock.** Fails when: the two sides' sales differ by more than 2% and one side uses order date and the other payout date. Fix: restate ours on their basis before judging any other line.
2. **Settlement judge.** For every Amazon line, check our figure against what Amazon paid. Fails when: our figure misses the payout by more than 1% on that line. Fix: our side is wrong; name the fix. Refunds and Amazon charges are dated the day Amazon posted them on our side: judge them only against a payout on the same clock, else mark "different clock" and move on.
3. **Product cost.** Fails when: products with no cost on one side carry over $500 or 0.5% of sales, or unit costs differ by more than 5%. Fix: show the dollars and ask the owner which cost is right.
4. **Gap adds up.** Fails when: the named causes add to more than the total gap, or leave over 1% of the app's profit unexplained. Fix: look again, and say the rest plainly.
5. **Second month.** Re-run the biggest three causes on the month before. Fails when: a cause found here does not show up there. Fix: call it a one-off, not a rule.
6. **Full solution.** Fails when: any gap of $500 or more ends at its cause with no fix: the cost rule to change, the cost to enter on the Costs page, or the data to load, with its dollars. Fix: add the fix.

Output:
- One line first: the app's profit, ours, the gap, and how much of it is explained.
- A table: line, the app, ours, gap, cause, which side is right.
- The full fix for every gap, biggest first, each with its dollars: on our side (the cost rule to change through `cost_rules`, the product cost to enter on the Costs page, the data to load or re-sync), then what to change in the app, then the owner's calls with the choices.
- Our profit once every fix is in, beside the app's.
- One line on what is left unexplained.
- With no app file, rounds that need its numbers say "not checked: no app file", never passed.

Never:
- Never call a line wrong without naming the cause.
- Never change a cost or setting. The owner does.
- Never invent the app's numbers.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-profit-tool-match". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
