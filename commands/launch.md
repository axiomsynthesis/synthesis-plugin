---
description: "Launch a Meta campaign: A whole new campaign planned, written and built in your Ads Manager, launched on your yes, read back, then judged on day 3 and day 7"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Launch a Meta campaign

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Launch a Meta campaign" (id: do-meta-launch-campaign, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Launches a whole new Meta campaign from start to finish: the plan, the ads, the build in your own Ads Manager, the launch on your yes, and the read-back.
Then it judges the new ads on day 3 and day 7 and switches off what does not sell.
Meta has not given Synthesis write access, so the build happens in your own browser where you are signed in, or through the ad tools this connection offers.

What to read: Your past campaigns and ad sets, your working ads and their links, your costs, each new ad's spend and sales by day
What to give me: A whole new campaign planned, written and built in your Ads Manager, launched on your yes, read back, then judged on day 3 and day 7

Synthesis tools to use:
- `cost_rules for=do-meta-launch-campaign`
- `meta_metric metric=campaign_performance`
- `meta_metric metric=adset_performance`
- `meta_metric metric=ad_destinations`
- `meta_metric metric=ad_returns`
- `ad_health_check`
- `propose_operator_action`
- `log_decision kind=campaign`

Steps:
1. Ask in one message: the product, where the sale happens (your website or Amazon), the budget per day and the dates, the creatives to use (or "pick from my best"), and any audience to keep out. Default to a 7-day launch with an end date set. Show the total: daily budget times days.
2. Call `meta_metric` with `metric=campaign_performance` to see which campaign types have paid for this brand. It covers each campaign's whole life, so say that. Call `meta_metric` with `metric=adset_performance` to pick the audiences and budgets to copy, and say the dates it covers.
3. Call `meta_metric` with `metric=ad_destinations`, `active_only=true` and `days=14` to pick a working ad and its link for the same product and destination. Call `ad_health_check` with `ads={"ad_ids": ["<that ad>"]}` for its link tags, pixel and settings. No read returns ad text, so copy the proven ad's text from Ads Manager.
4. Write the plan before building anything: the campaign goal and name, each ad set with audience and daily budget, and each ad with its creative, primary text, headline and link. Up to 3 ad sets and 3 ads each unless the person asks for more. New text follows the proven ad's claims only.
5. Call `propose_operator_action` with `platform=meta`, the total budget and the dates, to check the plan against the brand's spending caps. Over the cap: cut the plan, never the check.
6. Show the whole plan with the total spend and wait for the yes. The yes covers that total and nothing more.
7. If your tools include `ad_change` and it offers `change=meta_tool`, build through it. First call `ad_change` with `action=meta_catalog` and `names` set to the Meta tools named here, and follow their argument rules: budgets are in cents. Make the campaign with ads_create_campaign, each ad set with ads_create_ad_set copying the proven ad set by its source_adset_id, upload media with ads_creative_upload_media, and make each ad with ads_create_ad with the proven ad as source_ad_id. Create everything paused. Then propose one launch with ads_activate_entity and every new id in object_ids, and apply it with `ad_change_apply` only after the yes.
8. Otherwise build it in Ads Manager in the person's browser, where they are already signed in. Make the campaign with the agreed name (default "<Product> - Launch - <date> - Claude"). Finish one ad set with one ad first, then use Quick duplicate on that ad set only and change what the plan says. Turn off Meta's AI enhancements, music, promo codes and sign-up offers in each ad. No Amazon logo or stars on a website ad.
9. Publish only the new campaign's rows. Never the global Review and publish. Decline any budget raise Meta offers, then re-read every ad set budget.
10. Read back: call `ad_health_check` with `ads={"campaign_id": "<id>"}`. Every ad set on at the agreed budget, the right ads in each, link tags on, pixel right, Meta's automatic changes off. Fix any fail before it spends. Tell the person what is live, with the ids.
11. Call `log_decision` with `kind=campaign` at launch, with the plan, the total and the ids.
12. Day 3: call `meta_metric` with `metric=ad_returns` for closed days only. Switch off an ad set that spent past the no-sale line with no sale (read `no_sale_cap` from `ad_health_check`; ask only if it is missing). Switch off through `ad_change` and `ad_change_apply` when offered, otherwise in the browser.
13. Day 7: keep ads with 4 or more sales at or under the keep line, and switch the rest off. Log the readout with `log_decision`.

Checks before answering:
- Safe test run: when asked to test the shortcut, build one ad set with one ad, leave it off, and read it back.
- Spend: the yes covers the agreed total. A bigger budget, more days or more ad sets needs its own yes on the new number.
- The keep line is `keep_line` from `ad_returns`. Ask only when `rules_set` is false. Never borrow another brand's.
- Amazon sales from Meta ads arrive late. Judge an Amazon-bound ad on closed days, leaving out the last 2.
- If there is no past campaign to copy, say so plainly and ask for the audience and budget. Never invent one.

Rounds (relook before you answer):
1. **Plan against the cap.** Before the yes, put the total spend beside the brand's cap from `propose_operator_action`. Fails when: the total is over the cap, or the plan has no end date. Fix: cut budget or days until it fits, with an end date set.
2. **Logo and claim pass.** Look at every creative full size, every frame of a video, and every line of text. Fails when: a website ad shows a marketplace logo or stars, or text makes a claim the brand's live ads do not already make. Fix: crop or rewrite it, or hold that ad.
3. **Same setup as the proven ads.** Read the new campaign back with `ad_health_check` beside the source ad. Fails when: pixel, page, link tags or placements differ from the source without a reason in the plan. Fix: correct it before it spends.
4. **Day 3: starved or judged.** Fails when: an ad set spent under half its budget so far. Fix: call it starved, not losing, and leave it to day 7.

Output:
- Before the yes: the plan as one list with campaign, ad sets, budgets, ads and the total spend.
- At launch: one line with what is live, the ids and the total, then the read-back result.
- Day 3 and day 7: each ad set's spend, sales, cost per sale and the call made.

Never:
- Never spend past the agreed total or the brand's cap.
- Never launch anything before the person's yes on the exact plan.
- Never edit or pause the brand's existing campaigns. Only the new campaign's rows.
- Never call a winner on fewer than 4 sales.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-launch-campaign". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- If you could not finish, open your answer with "Stuck:" and what I need to do. If your answers are not saved for you automatically, save this one with the Synthesis tool `capture_turn`: my request as `question`, your answer as `answer`, and `context` starting with "automation: do-meta-launch-campaign".

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
