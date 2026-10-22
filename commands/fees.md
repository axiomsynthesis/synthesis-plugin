---
description: "Check for Amazon fee jumps: Every product whose fee per unit or referral rate changed, and what it costs"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Check for Amazon fee jumps

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Check for Amazon fee jumps" (id: amazon-fee-overcharge-check, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds Amazon fees that changed for no business reason, like a product re-measured into a bigger size tier or a referral rate that crept up. It sizes each change in dollars a month and says which ones are worth a case with Amazon. It finds changes only. A fee that was wrong from the start, or a storage, placement or returns fee, is not checked yet.

What to read: Amazon settlement fees by product
What to give me: Every product whose fee per unit or referral rate changed, and what it costs

Synthesis tools to use:
- `cost_rules for=amazon-fee-overcharge-check`
- `amazon_metric metric=fee_anomaly`
- `amazon_metric metric=fee_rate_trend`
- `amazon_metric metric=fee_breakdown month=YYYY-MM`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=fee_anomaly` and `months=6` to get per-unit fulfilment fee step changes and referral rate drift by product.
2. Call `amazon_metric` with `metric=fee_rate_trend` and `months=12` to see whether fees as a share of sales are creeping across the whole catalog.
3. Call `amazon_metric` with `metric=fee_breakdown` and `month=YYYY-MM` set to the latest closed month to put the changes next to total referral and fulfilment fees. If it marks that month still posting while the fee change tool counts it closed, say the two disagree and use the month before for totals only.
4. For each product with a step change, use `find_product` to name it the way the brand does, and multiply the change per unit by last month's units for the monthly cost.
5. Rank by monthly cost and mark the ones that look like a size tier or weight change.

Checks before answering:
- Use settled months only. A month still settling can look like a fee jump that is not there.
- A step change needs at least two weeks at the new fee before it counts. One odd order is not a change.
- If the fee tools return nothing or an error, say the fee data could not be read. Never report "no overcharges" from an empty result.
- Check the change against a price change. A referral fee rises with price, and that is not an overcharge.
- "Per unit" is really per order line. A month with many multi-unit orders can look like a jump. Say so beside any jump.
- If fees as a share of sales rose with no product jump, say it is mix or price, a pricing and pack-size question, not a case to open.

Rounds (relook before you answer):
1. **Real step or noise.** Fails when: the new fee has held under 14 days, or a price change landed within 2 weeks of a referral jump. Fix: drop it, or call it price.
2. **Settled weeks only.** Fails when: the change date falls in a month `fee_breakdown` marks still posting. Fix: wait for it to settle and say when to look again.
3. **Still charging?** Call `amazon_metric` with `metric=fee_anomaly` and `months=3` as well. Fails when: a change found over 6 months is gone over 3. Fix: it reverted, so size only the months it ran and ask for a refund of those.
4. **Catalog creep explained.** Fails when: fees as a share of sales rose more than 1 point in 12 months and the product jumps explain under half of it. Fix: name the rest as mix or price, not a case.
5. **Worth a case.** Fails when: a case is advised for a change under $100 a month, or without the old fee, new fee and date to quote. Fix: drop it or add the three facts.

Output:
- One line answer first: open a case or not, and how much a month the fee changes cost.
- One line on fees as a share of sales over 12 months, and what drove it.
- A table: product, old fee per unit, new fee per unit, date it changed, units a month, cost a month, likely cause.
- One move: which product to open a case for first, and what to ask Amazon to re-measure.

Never:
- Never open a case or change anything in Seller Central. A person does that.
- Never guess a fee or a unit count that the tools did not return.
- Never call a fee change an overcharge without saying how sure you are and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-fee-overcharge-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
