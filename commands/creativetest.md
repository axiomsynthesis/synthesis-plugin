---
description: "Run this week's Meta creative test: One small ad set per new creative, built in your Ads Manager, with day 4 and day 7 calls on what to switch off and what to move up"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Run this week's Meta creative test

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Run this week's Meta creative test" (id: do-meta-creative-test, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs a weekly creative test: one ad set per new creative at a small budget.
On day 4 it switches off the clear losers. On day 7 it moves winners into the main ad set and switches the test off.

What to read: The new creatives, your proven ads' copy and link, each test ad's spend and sales by day
What to give me: One small ad set per new creative, built in your Ads Manager, with day 4 and day 7 calls on what to switch off and what to move up

Synthesis tools to use:
- `cost_rules for=do-meta-creative-test`
- `meta_metric metric=ad_returns`
- `meta_metric metric=ad_destinations`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. If last week's test has ad sets ending this week, read them out first. Then ask in one message: the creatives, the budget per ad set (ask; house default about $14 a day each, 7 to 10 creatives, about $100 a day in all, 7 days with an end date set), and the week start date, a Monday by default. Show the total: ad sets times budget times 7.
2. Call `meta_metric` with `metric=ad_destinations`, `active_only=true` and `days=14` to pick a working website ad and its link. Call `ad_health_check` with `ads={"ad_ids": ["<that ad>"]}` for its link tags. No read returns ad text or headline, so copy them from that ad in Ads Manager.
3. In Ads Manager, make one campaign named the way the person names tests (ask, default "Creative Test - week of <date> - Claude"). Name ads "TEST <kind> - <name> - Claude".
4. Statics and videos go in separate ad sets. Meta's Creative testing button does not appear on new draft ad sets, so build by hand.
5. Finish one single-ad ad set first. Then use the tree menu Quick duplicate on that ad set only. A copy of a bigger ad set copies all its ads, so delete down to one before publishing. Then swap media in the 3 Edit group slots, set the thumbnail to Manual and rename.
6. Turn off AI enhancements, music, promo codes and email sign-up offers in each ad. No Amazon logo or stars on a website ad.
7. Draft ads show no ids and cannot be filtered by ad set. Read an ad's id from its Action menu link.
8. If the structure differs from what the person expected, say so before publishing.
9. Publish only these rows. Never the global Review and publish. Decline any budget raise Meta offers, then re-read every ad set budget.
10. Read back: call `ad_health_check` with `ads={"campaign_id": "<id>"}`. Every ad set on, one ad each, at the agreed budget, tags on, Meta's automatic changes off. Fix any fail before it spends. It cannot see promo codes or the email offer, so check those in the edit screen.
11. Day 4: call `meta_metric` with `metric=ad_returns` for closed days. Do not judge from the read-back, which counts today. Switch off an ad set that spent past the no-sale line with no sale (house default about 2x the order value, $50 on a $25 order). Read the line as `no_sale_cap` from `ad_health_check`, and ask only if it is missing. To switch it off, use `ad_change` then `ad_change_apply` when this connection offers them. Otherwise use the browser.
12. Day 7: an ad with 4 or more sales at or under the keep line moves up through do-meta-graduate-winners. If it is already copied into the main ad set, say so and do not copy it twice. Switch the rest of the test off.
13. Call `log_decision` with `kind=campaign` at launch and at each readout.

Checks before answering:
- Safe test run: when asked to test the shortcut, build one ad set and leave it off. Read it back.
- Spend: the yes covers the weekly total, ad sets times budget. If the person wants total spend flat, cutting the main ad set needs its own yes on that number.
- The keep line is `keep_line` from `ad_returns`. Ask only when `rules_set` is false. Never borrow another brand's.
- A creative with no spend by day 4 was starved, not judged. Say so.

Rounds (relook before you answer):
1. **Logo and claim pass.** Before publishing, look at every creative full size, every frame of a video. Fails when: a site ad shows a marketplace logo or star badge, or text makes a claim the brand's live ads do not already make. Fix: crop or patch it out in a 4:5 copy, or hold the creative.
2. **Same setup as the proven ads.** Read the test campaign back with `ad_health_check` beside the source ad. Fails when: goal, pixel, audience, placements, page or link tags differ from the source. Fix: correct it before it spends; the creative must be the only difference.
3. **Day 4: starved or judged.** Fails when: an ad set spent under half its budget so far. Fix: call it starved, not losing, and leave it to day 7.
4. **Day 7: does the call survive.** Put each winner's 7-day result beside its last 3 days. Fails when: it has fewer than 4 sales, or pays over the keep line a sale in the last 3 days. Fix: hold it another week instead of moving it up.
5. **Did it hold in the main group.** Two days after a move, read `ad_returns` again. Fails when: the moved ad has under 5% of its new ad set's spend, or pays over the keep line there. Fix: give it an ad set of its own at its test budget, with a budget yes.

Output:
- At launch: one line with ad sets, budget each, weekly total, live or off.
- Day 4 and day 7: each creative's spend, sales, cost per sale and the call made.
- What moved up and what was switched off.

Never:
- Never edit live winners in the main ad set.
- Never switch on more ad sets than the approved total covers.
- Never call a winner on fewer than 4 sales.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-creative-test". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
