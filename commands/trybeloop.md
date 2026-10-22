---
description: "Run my creator video tests each morning: One morning list: winners moved into the winners ad set, losers switched off, test sets closed, new videos built into new test sets by product, each change read back and logged"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Run my creator video tests each morning

Channel: Meta · Level: Does it for you · Status: Ready now
Schedule: Each morning

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Run my creator video tests each morning" (id: do-meta-creator-video-loop, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Keeps creator videos tested every day without a daily meeting.
Each morning it moves winners up, switches losers off, closes old test sets and builds newly approved videos into new ones.
Then it sends one short note of what changed.

What to read: Yesterday's logged moves, every live creator test ad's spend and sales over the last 7 closed days against the brand's keep line, newly approved creator videos and their scripts, live test ad sets with their budgets and end dates
What to give me: One morning list: winners moved into the winners ad set, losers switched off, test sets closed, new videos built into new test sets by product, each change read back and logged

Synthesis tools to use:
- `cost_rules for=do-meta-creator-video-loop`
- `recall_decisions`
- `brand_brain action=moves`
- `meta_metric metric=ad_returns limit=200`
- `trybe_creator_program view=performance days=30`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. Call `recall_decisions` and `brand_brain` with `action=moves`. Find this job's moves from the last 7 days, any "STANDING YES" line, and the newest saved keep line, per-set budget, set count and daily ceiling. Judge yesterday's moves: worked, did not, or too soon. If the owner says a standing yes exists but none is logged, ask once to log it; apply nothing until it is.
2. Call `meta_metric` with `metric=ad_returns` and `limit=200`, every `result_page`. Read the `adsets` list once from page 1. If `ads_total` is above the rows returned, say how many ads were not read. Creator ads carry the creator id in their name, such as trybe=<id>.
3. The rules, with the owner's saved limits. Missing: ask once; defaults $21 keep line, $50 a set, 3 sets, $150 a day, for this run only, and say so.
   - Move up: 4 or more sales at or under the keep line, not most of them in the last 3 days (else "next morning"). Follow "Move winning test ads into the main campaign" into the winners ad set, same post.
   - Switch off: an ad that spent 2x the keep line with no sale. Switch off ads, never an ad set that holds a winner.
   - Close: a test ad set 7 days after it started, only after its winners moved up.
   - Build: newly approved videos into new test ad sets at the per-set budget, within the set count and ceiling.
4. For each test ad set from step 2, call `ad_health_check` with `ads={"adset_id": "<id>"}` and `only=["switched_on","schedule_budget"]` for budgets and end dates. A campaign-wide check times out. Count live test sets.
5. Call `trybe_creator_program` with `view=performance` and `days=30` for program totals. The approved list comes from the program's own Submissions screen.
6. Read each new video's script on the creator program and watch it. No browser: list the videos as "held: watch first" and build none. Sort each by the product it shows. A video for one product goes only to that product's page. Unclear or two products: hold.
7. Show ONE numbered list, move-ups before closes: moves up, switch-offs with daily spend saved, closes, new sets with budget and new daily total. End with "Reply yes, or yes except 2".
8. On yes: if your tools include `ad_change`, call `ad_change` with `action=status`. Switch-offs go through `ad_change` with `action=propose`. Show the plan, then call `ad_change_apply` with its plan id and hash. Else follow "Switch Meta ads on or off for me". Builds follow "Turn approved Trybe videos into Meta ads for me". Keep the creator id in every ad name and link.
9. Read every changed ad back with `ad_health_check` and `ads={"ad_ids": ["<id>"]}`.
10. Call `log_decision` per move with `kind=campaign`, `made_on` today and the measure. Tomorrow's run judges it.

Checks before answering:
- Anything that adds spend is shown with dollars and waits for a yes, unless a STANDING YES names that exact limit.
- The standing yes covers switch-offs and closes only. New sets ask, unless the owner logged a standing yes for them with the per-set budget and set count.
- On a scheduled run with no standing yes, apply nothing. Send the list.
- A Meta read error is a failure, not zero sales.
- Never above the saved set count or daily ceiling.
- This daily loop judges on the 7-day keep line. Say once that 28-day and last-year reads do not apply.

Rounds (relook before you answer):
1. **Settled sales.** Re-read each move-up and switch-off on closed days only. Fails when: a switch-off ad has a sale yesterday or a move-up falls under 4 sales. Fix: hold it a day.
2. **Starvation.** Check spend reached yesterday's new ads. Fails when: a new set or moved winner shows $0 or under 10% of its budget after a full day. Fix: flag it, do not count it as tested.
3. **Product match.** Re-check each new ad set with `ad_health_check`, `ads={"adset_id": "<id>"}` and `only=["right_product","creator_tag"]`. Fails when: a video lands on another product's page or lost its creator id. "Unknown" with the product in the ad name counts as named. Fix: hold it.
4. **Spend ceiling.** Add up live test sets after today's plan. Fails when: over the set count or the daily ceiling, or a set's budget is over the per-set budget. Fix: build none. List the newest sets over the cap to pause, each with its budget, and ask.
5. **Argue the losing case.** For each switch-off, ask if it is too early. Fails when: it spent under 2x the keep line, or under 3 days live. Fix: keep it on.
6. **Winner inside a close.** Fails when: a set to close holds an ad at or under the keep line that is not moved up. Fix: move it up first, then close.

Output:
- One line first: moved up, switched off, closed, built, and the new daily spend.
- The numbered list, then one row per change read back.
- Videos held and why. Live test sets against the saved set count. "Not checked:" ads not read.

Never:
- Never put a video in another product's ad set or page.
- Never drop the creator id from a name or link.
- Never raise the per-set budget, the set count or the winners budget without a new yes.
- Never delete anything. Leave it off.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-creator-video-loop". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (Each morning). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due. On a repeat run nobody is there to say yes: change only what I gave a standing yes to, which can only lower spend, and send everything else as the list.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
