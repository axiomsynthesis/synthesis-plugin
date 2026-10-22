---
description: "Make feed-shape copies of my top ads: New 4:5 copies of your top tall videos in their own ad set: Feeds get the 4:5 file, Stories and Reels keep the original"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Make feed-shape copies of my top ads

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Make feed-shape copies of my top ads" (id: do-meta-feed-cut, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Makes new feed-shape (4:5) copies of your top tall videos.
In each copy, Feeds get the 4:5 file and Stories and Reels keep the original 9:16.
The copies go in their own ad set. Your live winners are never edited.

What to read: Your top ads by recent cost per sale, and where each one is spending by placement
What to give me: New 4:5 copies of your top tall videos in their own ad set: Feeds get the 4:5 file, Stories and Reels keep the original

Synthesis tools to use:
- `cost_rules for=do-meta-feed-cut`
- `meta_metric metric=ad_returns`
- `meta_metric metric=creative_by_placement`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. Call `meta_metric` with `metric=ad_returns` and read every page with `result_page`. First look for a live feed-shape ad set, with "feed 4:5" in its name. If one is live, report its result and fix its ads instead of building another. Otherwise take the top website ads by recent cost per sale.
2. For each top ad, call `meta_metric` with `metric=creative_by_placement`, `ad_id` and `days=7`. Skip any ad that already spends most of its money on Feeds.
3. Ask in one message: which ads (ask, default the top 2 first, then up to 6), the target ad set, its daily budget if new, and a yes to download the source videos. A creator video that exists only as a partner post may have no file to download. Then ask for the file.
4. Crop each video to 4:5 with any video tool you can run here. Pick the crop per video so the captions stay inside it. A center crop trims about 15% top and bottom. Show the person a frame from each crop first. If no video tool exists, ask for 4:5 exports.
5. Keep each file under 10 MB, the browser upload limit. Re-encode first rather than stop.
6. In Ads Manager, duplicate the source ad into the target ad set. Remove media, Add video, pick the 4:5 file, Crop. Then use Vertical "Replace" to put the original 9:16 back for Stories and Reels.
7. Do not use the "up to 10 media" route with placement exclusions. It fails at publish.
8. Per-placement files have run in a campaign with ad set budgets. If publish refuses them, use a campaign with a campaign budget.
9. Set the thumbnail to Manual in every group. Name each copy "<ad> - feed 4:5 - Claude". Keep any creator tag such as trybe=<id>. Add the brand's tracking tags, since duplicate and swap drops them. Turn off enhance CTA, inline comments, standard enhancements, AI enhancements, music, promo codes and email sign-up offers.
10. Publish from each ad's own preview. Review and publish re-ticks every draft, so untick held drafts if you must use it. Decline any budget raise Meta offers, then re-read the budget.
11. Read back: call `ad_health_check` with `ads={"adset_id": "<id>"}`. Each copy on, video fits each placement, link and tags right, Meta's changes off.
12. Call `log_decision` with `kind=campaign`, `measure` and `made_on`. After 3 days, call `meta_metric` with `metric=creative_by_placement` and `ad_id` for each copy. If under half its spend is on Feeds, say the test failed to test feed shape.

Checks before answering:
- Safe test run: when asked to test the shortcut, build one copy named "<ad> - feed 4:5 - Claude TEST" in an ad set that is off, publish it off and read it back. Leave it off.
- Spend: a new ad set is new spend. Show daily budget times days and get a yes on the number.
- Meta may still send most spend to Stories. Then the test is a second budget for that ad, not proof 4:5 works. Say so.
- Downloading source videos needs the person's yes.

Rounds (relook before you answer):
1. **Crop frames.** Look at the first, middle and last frames of each 4:5 file. Fails when: any caption word, face or the product is cut off. Fix: move the crop or ask for a 4:5 export.
2. **Wiring read-back.** Fails when: `ad_health_check` or the preview shows Feeds serving the tall file, or Stories and Reels serving the 4:5. Fix: redo the Replace step on that ad.
3. **Day 3: did it test the shape.** Call `meta_metric` with `metric=creative_by_placement` per copy. Fails when: under half a copy's spend is on Feeds. Fix: say the test is not testing feed shape and offer to end it.
4. **Day 7: same days, enough sales.** Set each copy's cost per sale beside its original's for the same days. Fails when: either side has under 10 sales, or the days differ. Fix: hold the call and give the next read date.

Output:
- One line: how many copies, which ad set, daily budget, live or off.
- Each copy: name, which file serves Feeds and which serves Stories and Reels.
- The date to read the placement split.

Never:
- Never edit a live winning ad. Only new copies.
- Never crop off captions or the product.
- Never raise a budget past the number the person approved.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-feed-cut". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
