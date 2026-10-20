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
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-morning-operator". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (Every morning). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due. On a repeat run nobody is there to say yes: change only what I gave a standing yes to, which can only lower spend, and send everything else as the list.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
