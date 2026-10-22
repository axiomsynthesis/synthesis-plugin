---
description: "Is website growth from new or old customers?: Whether website growth came from new or returning customers, and why. Website only"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Is website growth from new or old customers?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is website growth from new or old customers?" (id: grw-new-vs-returning, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits each month's website revenue into first-time buyers and returning ones, against the same months a year earlier. It then shows whether returning revenue moved because fewer old customers came back or because each one spent less. It reads the website only.

What to read: New and returning website customers and revenue by month, two years back, plus subscriptions and repurchase by start month
What to give me: Whether website growth came from new or returning customers, and why. Website only

Synthesis tools to use:
- `shopify_metric metric=new_vs_returning months=24`
- `shopify_metric metric=cohort_retention limit=24`
- `recharge_metric metric=mrr months=24`
- `channel_revenue_mix`

Steps:
1. Call `channel_revenue_mix` for the website's share of company sales. Put it in the first line, so a website change is read at its true size.
2. Pull `shopify_metric metric=new_vs_returning months=24`, so the last three closed months each have a year-ago month to compare with.
3. Add up the last three closed months, and the same three months a year earlier, for new and returning revenue. Split the returning change into returning customers and revenue per returning customer.
4. Show the month-by-month count of new customers over the last six closed months, so a slide inside the year is not hidden.
5. Report `subscription_customers` by month from step 2. Pull `recharge_metric metric=mrr months=24` for recurring revenue a year apart. If it fell, say how much of the returning change it may explain.
6. Pull `shopify_metric metric=cohort_retention limit=24`. Compare the 3 and 6 month repurchase rate of start months a year apart, to see whether fewer customers come back.

Checks before answering:
- This reads the website only. Never call it the source of the business's growth. Amazon has new and repeat customer counts but no revenue split by them yet. Say that plainly if asked about the whole business.
- Shopify new means first website order, not first purchase from the brand anywhere. Say so. Never use the Amazon new-to-brand count here.
- Revenue here is order totals and can include tax and shipping. Call it order revenue, never net sales.
- A first subscription order counts as new. The subscription read counts customers and recurring revenue. It cannot split returning revenue into subscription and one-time orders. Say so.
- Young start months have not had time to come back. Compare only months old enough.
- Leave the current month out.

Rounds (relook before you answer):
1. **Same age.** Re-read step 6. Fails when: a start month is compared at a month it has not reached, or a cohort under 12 months old backs a 12-month claim. Fix: compare at the 3 or 6 month mark only.
2. **Second window.** Re-run steps 3 and 4 on the last six closed months against a year earlier. Fails when: the direction of new or returning revenue flips. Fix: say the read depends on the window, and show both.
3. **Subscription share.** Fails when: the year-on-year change in recurring revenue is over half the change in returning revenue. Fix: lead with subscriptions as the reason.
4. **True size.** Multiply the change by the website's share of company sales. Fails when: the headline calls it growth or decline but the change is under 1% of company sales. Fix: say it is small for the business.
5. **Settled data.** Fails when: the newest month counted closed under 3 days ago, so late orders and refunds are still landing. Fix: drop it and use the month before.

Output:
- Answer first: the year-on-year change in new and returning revenue for the last three closed months, and the website's share of company sales.
- Table by month: new customers, new revenue, returning customers, returning revenue, subscription customers, and the same month a year earlier.
- One line on why returning revenue moved: fewer customers back, or less spent by each.
- One line on whether new customers are rising or falling over the last six months.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-new-vs-returning". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
