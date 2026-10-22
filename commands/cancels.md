---
description: "Why subscribers cancel, and what to change: How fast paying subscriptions shrink, how often charges are skipped, and the changes that fix it"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Why subscribers cancel, and what to change

Channel: Subscriptions · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Why subscribers cancel, and what to change" (id: grw-sub-cancel-reasons-fix, Subscriptions).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how fast paying subscriptions shrink and how often charges are skipped, then groups the reasons subscribers give when they cancel and turns each into a change. Many skips and too much product are usually a plan-length problem, not a product problem.

What to read: Six months of subscription cancels, skips, cancel reasons, plan lengths and products
What to give me: How fast paying subscriptions shrink, how often charges are skipped, and the changes that fix it

Synthesis tools to use:
- `recharge_metric metric=cancellation_reasons months=6`
- `recharge_metric metric=churn months=6`
- `recharge_metric metric=interval_mix`
- `recharge_metric metric=product_subscriptions limit=60`
- `recharge_metric metric=rebill_health months=6`

Steps:
1. Pull `recharge_metric metric=churn months=6`. Report new and cancelled subscriptions per month and the net change. Split cancels into chosen and failed payment.
2. Pull `recharge_metric metric=interval_mix` and `recharge_metric metric=product_subscriptions limit=60`. Divide each month's cancels by `billing_active_subs` from the plan-length read, labelled share of paying subscriptions lost each month.
3. Pull `recharge_metric metric=rebill_health months=6`. Report `skip_rate` per closed month and failed charges on their own line. If skips are above 30%, put a longer default plan first among the changes, ahead of the cancel reasons.
4. Pull `recharge_metric metric=cancellation_reasons months=6`. Rank named reasons by count. Show other as a residual, not a driver.
5. Map each top reason to a change: too much product to a longer plan or a skip offer, too expensive to a smaller pack, stopped using to a pause offer and a how-to-use reminder, signed up by accident to a clearer sign-up step, dissatisfied to a product question.

Checks before answering:
- If no subscription app is connected, say so. Never say zero subscribers or zero churn.
- Report how many cancellations had a named reason.
- Failed payments are a different problem from cancels. Give them on their own line as failed charges. Never count them as cancellations.
- Cancel reasons are six-month totals. They are not split by month or product, so never tie a reason to a plan length or a product. Show plan lengths beside them as their own read.
- A skip keeps the subscription. It is not a cancel, but many skips mean the plan ships too often.
- The share lost each month uses today's paying count as the base, so older months are rough. Say so.
- Plan-length lifespans cover cancelled subscriptions only, so they run short. Say so.
- Count only subscriptions that are billing now as active. The plan-length read also counts old ones that never formally ended. Say which number you use.
- One perk per change. Never pair a discount with free shipping and a gift to save a subscriber.

Rounds (relook before you answer):
1. **Named reasons carry the ranking.** Re-read how many cancels had a named reason. Fails when: under half did, or "other" is the largest group. Fix: call the ranking a hint, and make "ask a clearer cancel question" the first change.
2. **Skips point to plan length.** Re-read `skip_rate`. Fails when: skips are above 30% and the first change is not a longer default plan. On one live brand 61 to 64% of charges were skipped. Fix: reorder the changes.
3. **Plan lengths agree.** Compare lifespans by plan length from `interval_mix`. Fails when: monthly plans last as long as longer ones, so plan length is not the problem. On one live brand monthly plans lasted about 154 days against about 260 on 2- and 3-month plans. Fix: drop the longer-plan change.
4. **Failed payments kept apart.** Fails when: any failed charge sits inside the cancel count or the share lost. Fix: move it to its own line.
5. **Closed months only.** Fails when: the latest month still has charges queued or is the current month. Fix: drop it and say why.

Output:
- Answer first: the net change in paying subscriptions per month, the skip rate, and the first change to make.
- Table by month: new, cancelled, net change, share lost, skip rate.
- Table: reason, cancellations, share, change to make.
- One test: the first change for new subscribers or at cancel time, read by save rate and how many are still paying after 90 days.

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
- On every Synthesis tool call, start `context` with "automation: grw-sub-cancel-reasons-fix". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
