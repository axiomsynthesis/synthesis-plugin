---
description: "Switch Meta ads on or off for me: The ads, ad sets or finished tests you named switched on or off, every row read back live, with leftover copies checked"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Switch Meta ads on or off for me

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Switch Meta ads on or off for me" (id: do-meta-switch-ads-on-off, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Switches named Meta ads, ad sets or finished test campaigns on or off.
It works from the person's word, or from the stop rules agreed for a named test.
When most of an ad set goes off, it also proposes a lower budget, so the money does not just move to the rest.

What to read: Each named ad, ad set or campaign with its live status and spend and sales over the last 7 closed days, against the brand's stop rules
What to give me: The ads, ad sets or finished tests you named switched on or off, every row read back live, with leftover copies checked

Synthesis tools to use:
- `cost_rules for=do-meta-switch-ads-on-off`
- `meta_metric metric=ad_returns`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. If the person asks "is it live?", answer that first from a live read.
2. Ask which rows and on or off, or "apply the stop rules" to a named test. Ask the stop rules. Default: off at 2x the keep line spent with no sale, or at 3x spent with an 80% chance the true cost per sale is over 1.25x the line. Nothing judged in its first 3 days unless it hits the no-sale line.
3. Call `meta_metric` with `metric=ad_returns` and `limit=50` for 7-day spend, sales and cost per sale per row.
4. Call `ad_health_check` with `ads={"adset_id": "<id>"}` and `only=["switched_on","duplicates"]` for each ad set touched. It shows every copy that is on or off. A paused copy flagged "switch the ad on" is expected. Leave it off.
5. Show the plan: each row, on or off, spend, sales, why. Add the ad set budget cut when most of it goes off. Proposals still waiting for a yes are listed, not done.
6. For a test the person already agreed, stop-rule offs and the agreed switch-on count as approved. Anything else needs a yes.
7. If your tools include `ad_change`, prefer it. Call it with `action=status` first. To switch off, call it with `action=propose` and the `items` to pause. Propose changes nothing in the account, so it can run before the yes. Show its list, then call `ad_change_apply` with the plan id and hash after the yes. It can switch back on only what Synthesis switched off, through `action=undo` with the `undo_id`. Anything else goes on in the browser.
8. Otherwise use Ads Manager in the browser. Filter to the named campaign. Find each row by its ad id, not its name, because one video can run in many campaigns. Click its toggle. Check the ad set rows as well as the campaign, because a row can sit "Ads off" inside a live ad set.
9. A budget cut goes through the budget cell's own Publish, never the global Review and publish.
10. Leave copies off. Never delete anything.
11. Call `ad_health_check` with `ads={"adset_id": "<id>"}` for each changed ad set to read every row's live switches.
12. Call `log_decision` with `kind=campaign`, what changed, and the day to look again.

Checks before answering:
- Every switched row reads back in the state planned, including leftover copies.
- Spend check: switching on raises spend. State the daily budgets now live against before. Never switch on spend the person has not seen.
- If a platform safety check stops a switch-on the person agreed, quote that yes once, then stop.
- Safe test, when asked for one: switch off, then back on, an ad that is already off inside an off test ad set. Show both steps and the unchanged end state.
- Judge stop rules on closed days. Today is still filling in.
- A Meta read error is not zero sales. Never switch anything off from missing data.
- If the ad returns verdict disagrees with the stop rule, show both and ask.

Rounds (relook before you answer):
1. **Money moves.** Fails when: most of an ad set goes off but its budget stays the same. Fix: add the budget cut to the plan, or say the money moves to the ads left on.
2. **Second window.** For each row going off, read `last3_spend` and `last3_sales`. Fails when: it sold at or under the keep line in the last 3 days. Fix: show both windows and ask before switching it off.
3. **Copies and parents.** After the change, read every copy of each ad. Fails when: a copy of a switched-off ad is still on elsewhere, or a planned-on ad sits under an ad set or campaign that is off. Fix: name it and ask.
4. **Right judge.** Fails when: a row that sends people to Amazon is switched off on Meta's own sales. Fix: drop it from the plan; the Meta-to-Amazon keep and cut shortcut judges those.

Output:
- One line first: what is now on, what is now off, and the daily spend now live.
- One row per change: name, before, after, read back, 7-day spend and sales.
- Rows left alone and why, one line.
- Next look: the date to check the remaining ads.

Never:
- Never delete an ad, ad set or campaign. Leave it off.
- Never put a product's videos into another product's campaign.
- Never switch on anything outside what was approved or agreed.
- Never touch an agency's campaign without a yes.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-switch-ads-on-off". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
