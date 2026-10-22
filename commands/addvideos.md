---
description: "Add new videos as Meta ads: Each file live as a new website ad in the ad set you name, with your team's text, link and tags, read back one by one"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Add new videos as Meta ads

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Add new videos as Meta ads" (id: do-meta-add-videos, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Takes the creator videos or statics you send and adds each one as a new website ad in the ad set you name.
It copies your team's live text and link, fixes Meta's upload traps, and reads every new ad back.

What to read: The videos or statics you send, a working ad in the ad set you name
What to give me: Each file live as a new website ad in the ad set you name, with your team's text, link and tags, read back one by one

Synthesis tools to use:
- `cost_rules for=do-meta-add-videos`
- `meta_metric metric=ad_destinations`
- `ad_health_check`
- `meta_metric metric=ad_returns`

Steps:
1. Ask in one message: the files or share links, the target ad set (ask, default your main website ad set), and whether to switch them on now.
2. Watch or read each file first. Never judge the product from the file name alone. Send each file to the campaign and page for the product it shows. Hold any file whose product matches no ad set. Flag caption claims the brand does not already make.
3. Call `meta_metric` with `metric=ad_returns` and read every page with `result_page`. If one ad takes over half the target set's 7-day spend, warn that new ads will likely starve. Offer a separate ad set, which needs its own budget yes.
4. Call `meta_metric` with `metric=ad_destinations`, passing only `days` and `active_only`. It has no ad set filter, so pick a working website ad in the target set by its ad set name. Skip any ad whose type is SHARE: it is an existing post and its media cannot be swapped.
5. Call `ad_health_check` with `ads={"ad_ids": ["<that ad>"]}` to read its tags and Meta's switches. Read its text and headline in Ads Manager. If it carries no utm tags, copy the tags from an ad that does, or use source facebook, medium paid_social, and campaign, content and term set to the campaign, ad and ad set names.
6. Browser uploads stop at 10 MB. Shrink bigger files first, to about 8.5 MB at 720x1280. Use any video tool you can run here, else ask for a smaller export. Never stop at the limit.
7. In Ads Manager, quick-duplicate the working ad inside the target ad set. Remove media, Add media, Add video, upload. Wait until it no longer says Processing.
8. Swap the file into all 3 placement groups and crop. Set the thumbnail to Manual in every group before publish. A fresh upload left on automatic is switched off by Meta with an "Image Not Found" error.
9. Name each ad after its file plus " - site - Claude". Keep any creator tag such as trybe=<id> in the name and in the link, or the creator is not paid. The first rename after a page load often fails, so re-check it.
10. Turn off AI creative enhancements, standard enhancements, Add music, promo codes and any email sign-up offer. Meta turns some back on after a media swap, so re-check them. No Amazon logo or stars on a website ad.
11. Publish from the ad's own preview, not the global Review and publish. The first Publish click sometimes does not take. If Meta asks to raise the budget, decline.
12. An ad copied from an Amazon-traffic campaign cannot be pasted into a sales ad set. Rebuild it by duplicate and swap instead.
13. Read back: call `ad_health_check` with `ads={"adset_id": "<id>"}` and read every page. Each new ad must be on, carry the right video, link and tags. Promo codes and the email offer read unknown there, so check them by eye.
14. Next day, call `meta_metric` with `metric=ad_returns` and flag any new ad still at $0 spend.

Checks before answering:
- Safe test run: when asked to test the shortcut, add one file as "TEST upload check - site - Claude" in an ad set that is off, publish it off and read it back. Leave it off.
- Spend: the person's "add these" is the yes for ads in the named ad set at its current budget. A different ad set or any budget change needs its own yes with the number.
- If two browsers are connected, drafts live in only one. Check which before building.
- An ad set with many ads may never spend on new ones. Judge by spend share, not by being on.

Rounds (relook before you answer):
1. **Frame-by-frame claims.** Watch each video to the end and read every caption and on-screen line. Fails when: any line makes a claim the brand's live ads do not already make, such as a lab, award or health claim. Fix: hold the file and quote the line.
2. **Product to page.** Fails when: the product shown is not the product on the ad's page link. Fix: move it to the right product's ad set, or hold it.
3. **Switches after the swap.** Open each new ad's edit screen once more after publish. Fails when: AI enhancements, music, promo codes, the email offer or an automatic thumbnail read on. Fix: turn it off and publish that ad alone.
4. **Did the money reach them.** After a full closed day, read `ad_returns`. Fails when: a new ad has $0 spend, or under 5% of the ad set's spend while one old ad takes over half. Fix: say it is starved and offer an ad set of its own, which needs a budget yes.

Output:
- One line: how many added, to which ad set, live or off.
- Each ad: name, on or off, link and tags right, thumbnail set.
- Files held back and why, and caption claims flagged.

Never:
- Never edit or replace a live winning ad. Always build a new ad.
- Never change the ad set's budget.
- Never publish an ad with the wrong product's page.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-add-videos". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
