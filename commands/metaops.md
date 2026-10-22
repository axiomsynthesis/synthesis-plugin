---
description: "Run my Meta ads each morning: One numbered morning list (pause, raise, hold, too new), the moves you approve applied and read back, and every move logged so tomorrow judges it"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Run my Meta ads each morning

Channel: Meta · Level: Does it for you · Status: Ready now
Schedule: Every morning

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Run my Meta ads each morning" (id: do-meta-morning-operator, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each morning it judges yesterday's moves, builds today's list by the brand's ad rules, and applies what you approve.
It remembers each move in the decision log, so the next morning says which worked.

What to read: Yesterday's logged moves and how each did since, every live website ad set and ad over the last 7 closed days against the brand's own keep line and ad rules, live budgets and switches
What to give me: One numbered morning list (pause, raise, hold, too new), the moves you approve applied and read back, and every move logged so tomorrow judges it

Synthesis tools to use:
- `cost_rules for=do-meta-morning-operator`
- `recall_decisions`
- `meta_metric metric=ad_returns limit=50`
- `meta_metric metric=pacing_anomaly`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. Call `recall_decisions`. Find this brand's moves from the last 7 days and any line starting "STANDING YES". Call `meta_metric` with `metric=daily_actions limit=60`: use its yesterday and recent_moves blocks too.
2. Judge each move: spend and sales in the days before against the days since. Say worked, did not, or too soon.
3. Build today's list from daily_actions when it ran. Else call `meta_metric` with `metric=ad_returns` and `limit=50`, read every `result_page`, and apply the rules to each row's keep line, last 7 closed days.
4. The rules, the same for every brand, overridable per brand: pause at 2x the keep line spent with no sale. Pause at 3x spent when an 80% chance says the true cost per sale is over 1.25x the line. Raise 20% after 5 sales at 0.75x the line or less, once per 3 days, never above the ceiling. Nothing judged in its first 3 days unless it hits the no-sale line. Leave out anything changed in the last 3 days.
5. Call `meta_metric` with `metric=pacing_anomaly`. Call `ad_health_check` with `ads={"adset_id": "<id>"}` and `only=["switched_on","schedule_budget"]` for each ad set on the list, for live budgets and switches.
6. Show ONE numbered list: pauses with daily spend saved, raises with old and new daily budget and the 30-day dollars, holds with why, too new, new videos waiting from yesterday's log. End with "Reply yes, or yes except 2".
7. On yes: if your tools include `ad_change`, call `ad_change` with `action=status`. Pauses go through `ad_change` with `action=propose` and the `items`. A raise goes there only if its description offers a budget change. Show the plan, then call `ad_change_apply` with its plan id and hash.
8. Otherwise follow "Switch Meta ads on or off for me" and "Change a Meta budget for me" in Ads Manager.
9. Read every changed row back with `ad_health_check`.
10. Call `log_decision` per move: `kind=campaign` for a pause, `kind=budget` for a raise, the dollars, `made_on` today, and the measure. Tomorrow's run judges it.
11. Standing yes: if the person says "always apply pauses inside my rules", log it with `log_decision` as "STANDING YES: pauses inside the ad rules". Then pauses that lower spend apply without asking. "Stop the standing yes" withdraws it the same way.

Checks before answering:
- Anything that raises spend is shown with dollars and waits for a yes, every time.
- The standing yes covers pauses only. Undo, raises and switch-ons always ask.
- On a scheduled run with no standing yes, apply nothing. Send the list.
- A Meta read error is a failure, not zero sales. Never pause from missing data.
- Use closed days. Today is still filling in.
- A row with no keep line is not judged. Say the lines are not set.

Rounds (relook before you answer):
1. **Did the saving happen.** For each pause judged in step 2, set the ad set's total spend before and since. Fails when: the pause "saved" money but the ad set spent the same, because its budget stayed. Fix: count the saving as $0 and add a budget cut to today's list.
2. **Second window.** For each raise, read `last3_spend` and `last3_sales`. Fails when: the last 3 days pay over the keep line a sale. Fix: move it to hold.
3. **Starved, not new.** Fails when: a row on the "too new" list spent $0 for 2 closed days while its ad set spent. Fix: list it as starved and propose an ad set of its own.
4. **Profit guard.** Fails when: a raise sits where cost per sale is over half the order value (house default; the brand's profit kept per order overrides). Fix: hold the raise and say it loses money per order.

Output:
- One line first: yesterday's moves and what they did, then today's dollars at stake.
- The numbered list.
- After applying: one row per change, before, after, read back.
- What this run did not see: repeat buyers, hand edits in Ads Manager.

Never:
- Never raise a budget above the brand's ceiling or by more than 20%.
- Never delete anything. Leave it off.
- Never accept a Meta suggestion to raise spend.
- Never apply a move the person excluded with "except".

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-morning-operator". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (Every morning). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due. On a repeat run nobody is there to say yes: change only what I gave a standing yes to, which can only lower spend, and send everything else as the list.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
