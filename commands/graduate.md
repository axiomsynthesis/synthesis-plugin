---
description: "Move winning test ads into the main campaign: Proven test winners copied into your main or winners ad set as existing-post ads, or a raise on the winner's own ad set, read back after"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Move winning test ads into the main campaign

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Move winning test ads into the main campaign" (id: do-meta-graduate-winners, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds test ads that have earned a bigger budget and moves them where the money is.
It copies each winner into your main campaign or winners ad set, or raises the winner's own ad set instead.
It also moves a mis-filed ad to the right campaign. Then it reads every copy back.

What to read: Recent cost per sale and sales for every live test ad, your main campaign and winners ad set
What to give me: Proven test winners copied into your main or winners ad set as existing-post ads, or a raise on the winner's own ad set, read back after

Synthesis tools to use:
- `cost_rules for=do-meta-graduate-winners`
- `meta_metric metric=ad_returns`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. Call `meta_metric` with `metric=ad_returns` and read every page with `result_page`. Winners are ads it marks winning: enough sales under the brand's own keep line. House default: 4 or more sales at or under the keep line, never fewer. If the brand has no keep line, ask for one. Never borrow another brand's.
2. Drop any winner already copied into the target or main set, by the same name plus " - Copy" or the same post. Report that copy's spend and cost per sale instead of copying again.
3. For the main ad set's 7-day cost per sale, use its row in the same result's ad set list. A winner should beat it or match it.
4. Look at the target set's earlier copies. If one has near zero spend, or the set is over the keep line, warn that new copies will likely starve.
5. Call `ad_health_check` with `ads={"ad_ids": ["<winner id>"]}` to read each winner's ad set end date. If it ends within 2 days, raising in place is not an option. Copy instead.
6. Ask in one message: which ads, the target ad set, and copy or raise in place. Raising the winner's own ad set about 20% often works better than a copy, and goes through the budget yes.
7. To copy, use "Use existing post" with the original ad's post id, so likes and comments carry. Switch the post picker off the Partner Content tab first. A creator's post that is only a partner post may not show at all. Then use step 9.
8. Existing-post ads drop the ad's tracking tags. Re-add the brand's tracking template on every copy. If you use Meta's Copy and paste instead, do both in one page session.
9. Copies between campaigns with different goals or catalog setups are refused. Quick-duplicate an ad inside the target set and swap media instead. Meta refuses new copies of tall-only 9:16 videos under all placements, so use the existing post or a 4:5 version.
10. Name copies with the original name plus " - Copy". Do not add a second " - Claude". Keep any creator tag such as trybe=<id> in the name and the link. An ad that sent people to Amazon gets the website page link and tags.
11. Turn off Meta's standard enhancements, promo codes and any email sign-up offer on each copy. Keep the originals running unless the person says otherwise.
12. Publish from the ad's own preview. Never the global Review and publish. Decline any budget raise Meta offers.
13. Read back: call `ad_health_check` with `ads={"ad_ids": ["<new id>"]}`. Each copy on, in the target set, tags present. An existing-post copy hides its link from the data, so check the link by eye.
14. Call `log_decision` with `kind=campaign`, `measure` and `made_on`: which ads moved, where, and a spend-share check in 2 days.

Checks before answering:
- Safe test run: when asked to test the shortcut, copy one winner into an ad set that is off, publish it off and read back its post id and tags. Leave it off.
- Spend: a copy into an existing ad set adds no budget. A raise needs the person's yes on the new dollar figure, shown beside the old one.
- A winner on 3 days of data may be luck. Say how many sales it rests on.
- After 2 days, check each copy's spend share. A copy with near zero spend did not graduate.

Rounds (relook before you answer):
1. **Second window.** Put each winner's 7-day result beside its `last3_spend` and `last3_sales`. Fails when: it pays over 1.5x the keep line a sale in the last 3 days, or sold nothing in them. Fix: leave it in test and say why.
2. **Right product, right page.** Watch the first seconds of each winner and open the target set's page. Fails when: the video's product is not the product on that page. Fix: send it to the ad set for its own product, or hold it.
3. **Already there.** Read the target set's ads by post id and name. Fails when: the same post or a " - Copy" of it is already in the target set or the main set. Fix: drop the copy and report the one that exists.
4. **Did the money reach it.** Two days later, read `ad_returns` again. Fails when: the copy has under 5% of the target set's spend. Fix: it did not graduate; propose raising the winner's own ad set about 20% instead.
5. **Did the original hold.** Fails when: after the copy went live, the original's cost per sale rose over the keep line on the last 3 days. Fix: say the two compete and ask which to keep.

Output:
- One line: how many ads moved, where, and the route used.
- Each ad: sales and cost per sale that earned it, the copy's status, tags present.
- Ads left in test and why.

Never:
- Never move an ad that has not met the brand's keep line.
- Never switch off the original unless the person asked.
- Never raise a budget past the number the person approved.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-graduate-winners". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
