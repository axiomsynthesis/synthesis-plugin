---
description: "Change a Meta budget for me: The new daily budget or end date set on each ad set you named, with Meta's own budget bumps undone and the live figure read back"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Change a Meta budget for me

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Change a Meta budget for me" (id: do-meta-budget-change, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Raises or cuts the daily budget on the Meta ad sets you name, or moves their end date.
It uses the Synthesis ad change tools where the brand has them switched on, and your own signed-in Ads Manager otherwise.
It also puts back budgets Meta raised on its own when an ad set was published.

What to read: Each named ad set's daily budget, end date, last 7 closed days of spend, sales and cost per sale, then the same ad set read back live after the change
What to give me: The new daily budget or end date set on each ad set you named, with Meta's own budget bumps undone and the live figure read back

Synthesis tools to use:
- `cost_rules for=do-meta-budget-change`
- `meta_metric metric=ad_returns`
- `meta_metric metric=pacing_anomaly`
- `ad_health_check`
- `log_decision kind=budget`

Steps:
1. Ask which ad sets and the exact new dollar figure for each, or the new end date. A phrase like "150 a day each" gets one question back to confirm it.
2. Call `meta_metric` with `metric=ad_returns` and `limit=50` for 7-day spend, sales and cost per sale of each named ad set. Call `meta_metric` with `metric=pacing_anomaly`. If a named ad set's campaign spiked or stalled in the last 3 days, say so first.
3. Call `ad_health_check` with `ads={"adset_id": "<id>"}` and `only=["switched_on","schedule_budget"]` for each one to read its live budget, end date and switches. If it ends within 7 days, say so. A raise on an ad set that stops tomorrow needs an end-date yes too, with the added spend shown.
4. Show one line per ad set: name, budget now, budget asked, 7-day spend, sales, cost per sale.
5. Ask the brand's raise rule. Default: raise 20% after 5 sales at 0.75x the keep line or less, once per 3 days, never above the brand's ceiling, and only while 7-day profit per order after ads is above $0. Default cut: spent 3x the keep line with an 80% chance the true cost per sale is over 1.25x it.
6. Prefer raising a winner's own ad set over copying the winner into a bigger one.
7. If `ad_change` is in your tools and offers a budget change, call it with `action=propose` and each new daily budget. Show the plan. After the yes, call `ad_change_apply`. Go to step 14.
8. Otherwise, in Ads Manager, open the Ad sets tab and filter to the named ad sets only. Check the row name before typing, because a mis-click on the biggest ad set costs the most. Click the budget cell, type the agreed figure and use that cell's own Publish.
9. For an end date, open the ad set, change only Schedule, End, and publish that ad set alone.
10. Never use the global Review and publish. It bundles every draft in the account.
11. If the inline editor shows someone else's pending draft on that ad set, stop and ask. Leave it alone.
12. Meta may offer to raise the budget further. Decline it every time.
13. Reload the page and read the budget cell again. Meta can round a budget up on publish, for example $10 to $15 or $100 to $134. If it moved, set it back to the agreed figure.
14. Call `ad_health_check` again the same way. It reads the budget and end date from Meta, so it is the final read-back, not the page.
15. Call `log_decision` with `kind=budget`, the old and new figure as `decision`, and `measure` set to cost per sale over the next 7 days.

Checks before answering:
- Every new figure was named in chat by the person, per ad set. A raise with no number is not done.
- Spend check: the new daily total across the changed ad sets is stated next to the old total. Never above what was approved.
- The read-back budget equals the agreed figure on every ad set. If not, say so plainly.
- The person sometimes changes budgets too. Re-read right before reporting.
- Safe test, when asked for one: change a paused test ad set by $1 and back, then read both values.
- Use closed days. A Meta read error is a failure, not zero sales.

Rounds (relook before you answer):
1. **Re-read before typing.** Read the live budget again right before the change. Fails when: it differs from the step 3 read, because someone else changed it. Fix: show the new before and after and ask again.
2. **Argue against the raise.** Set the 7-day cost per sale beside the last 3 days and the order value. Fails when: the last 3 days pay over the keep line a sale, or the cost per sale is over half the order value (house default; the brand's profit kept per order overrides). Fix: say the raise loses money and hold it unless the person still says yes.
3. **Rounding read-back.** Fails when: any read-back budget differs from the agreed figure by any amount. Fix: set it back and read again.
4. **Next-day pacing.** The next day, call `meta_metric` with `metric=pacing_anomaly` and read `ad_returns`. Fails when: yesterday's spend was under 70% or over 120% of the new budget. Fix: say so; under-spend means the raise bought nothing.

Output:
- One line first: how many ad sets changed and the new daily total against the old.
- One row per ad set: name, before, after, read back, 7-day cost per sale.
- Anything that differs from the plan, and any draft left untouched.
- Next look: tomorrow, check spend tracks the new level.

Never:
- Never change a budget the person did not name with a number.
- Never accept a Meta suggestion to raise a budget.
- Never touch another person's pending draft.
- Never share one campaign budget across pages with very different order sizes without saying the risk.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-budget-change". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
