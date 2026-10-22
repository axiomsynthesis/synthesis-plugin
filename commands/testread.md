---
description: "Read a running test and make the call: Keep running, call the winner, or stop, judged on profit per visitor with gift costs in, and the one number that would flip the call"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Read a running test and make the call

Channel: Website · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Read a running test and make the call" (id: website-test-readout, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads any running test and makes the call: keep running, call the winner, or stop.
It judges on profit per visitor, not buy rate, with gift and add-on costs in. It says whether the result is settled, and which number would change the call.

What to read: A running page split, Meta page test or offer test, its orders and visitors per side, pack and gift costs, untagged orders
What to give me: Keep running, call the winner, or stop, judged on profit per visitor with gift costs in, and the one number that would flip the call

Synthesis tools to use:
- `cost_rules for=website-test-readout`
- `recall_decisions`
- `meta_metric metric=campaign_performance`
- `shopify_metric metric=order_tags months=1`
- `operator_inputs section=cogs`
- `first_order_contribution_margin`
- `run_bayesian alpha=1 beta=1`
- `measurable_test`
- `log_decision kind=other`

Steps:
1. Call `recall_decisions` and find the test: the change, the control, start and read dates, the agreed metric. If none, ask: the test type (on-page split, Meta page test or offer), dates and counts per side.
2. Counts per side. On-page split: visitors, orders, sales and add-on take per side from the split-test app. Meta page test: call `meta_metric` with `metric=campaign_performance` for spend, sales and cost per sale of the test and control campaigns. Offer test: orders taking the offer and order size.
3. Untagged orders. Call `shopify_metric` with `metric=order_tags` and `months=1`. Express-pay buys from the buy box often carry no test tag. Assign them by landing page and time, or say the share left out.
4. Costs. Call `operator_inputs` with `section=cogs`. Every pack and gift needs a cost. A gift with no cost makes its side look richer. Call `first_order_contribution_margin` per pack with `price`, `cogs` and `misc` for shipping, packing and the gift.
5. Profit per visitor per side = orders x profit per order / visitors. For a Meta page test, profit per order minus cost per sale.
6. Odds. Call `run_bayesian` with `alpha=1`, `beta=1`, `successes` = orders and `trials` = visitors for each side. Give the chance B beats A and the likely range.
7. Settled? Full weeks, read date reached, visitors a side at least 16 x p x (1 - p) / d squared. Meta page test: about $700 to $1,000 spent per side and about 10 days. Exclude today.
8. The call. Name the number that would flip it. Call `measurable_test` with the claim, metric, `check_date` and `direction`. Save with `log_decision` with `kind=other`, `measure` and `made_on`.

Checks before answering:
- A side under 40% of visitors means the split broke. Say so before any call.
- A free gift can eat a paid add-on. Compare the paid add-on's take rate per side and count lost add-on profit.
- A small test campaign catches disasters, not close calls. Under a 30% gap in cost per sale is not proven.
- "What removes a decision wins, what adds one loses" is a rule to check, never the verdict. Say which side removes a decision and whether the data agrees.
- Name any overlap: another test on the same buy box, a price change, a sale day, a budget change mid-test.

Rounds (relook before you answer):
1. **Profit, not buy rate.** Re-compute with gift costs and add-on take. Fails when: the side ahead on buy rate is behind on profit per visitor. Fix: call on profit.
2. **Halves.** Split the test window into two halves by date. Fails when: the leader in the first half trails in the second. Fix: keep running.
3. **Untagged orders.** Fails when: untagged orders are over 10% of orders, or would flip the leader if all went to the trailing side. Fix: assign them or extend.
4. **Cannibalised add-on.** Fails when: the paid add-on take falls by a third or more on the gift side. Fix: subtract the lost add-on profit and re-rank.
5. **Argue the loser.** Fails when: the top of the losing side's likely range beats the winner's middle. Fix: call it not settled and give the visitors still needed.

Output:
- First line: keep running, call the winner, or stop, and the number that would flip it.
- Table: side, visitors, orders, buy rate, order size, profit per order, profit per visitor.
- Chance B beats A, settled or not, and what was left out.

Never:
- Never call a winner on buy rate alone.
- Never call before the read date unless a disaster stop fires.
- Never end a test or roll out a winner here. That is the split-test or page-test shortcut, after a yes.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-test-readout". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
