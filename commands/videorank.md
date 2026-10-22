---
description: "Rank my videos by cost per Amazon order and rebuild the best for the website: Every Amazon-bound video ranked by Meta dollars per Amazon order, which are already running as website ads, and a build plan to rebuild the rest of the best as website sales ads, each sent only to its own product's page"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Rank my videos by cost per Amazon order and rebuild the best for the website

Channel: Meta · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Rank my videos by cost per Amazon order and rebuild the best for the website" (id: meta-video-rank-by-amazon-orders, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds the videos that sell best on Amazon and plans to reuse them for website sales.
It reads the same source, spend and weeks as "Meta to Amazon read" and "Which Meta ads for Amazon to keep, cut or move up", so the three agree on one ad.
An ad cannot be moved from an Amazon traffic campaign to a website sales campaign. The plan rebuilds each winner as a new ad.

What to read: Meta spend and Amazon Attribution orders for every Amazon-bound video over the last settled weeks, each video's product, hook rate and Amazon profit per order, and the website ads already running with their pages and keep line
What to give me: Every Amazon-bound video ranked by Meta dollars per Amazon order, which are already running as website ads, and a build plan to rebuild the rest of the best as website sales ads, each sent only to its own product's page

Synthesis tools to use:
- `cost_rules for=meta-video-rank-by-amazon-orders`
- `meta_metric metric=amazon_ads period=weekly weeks=6`
- `meta_metric metric=ad_destinations days=28`
- `amazon_metric metric=daily_revenue`
- `amazon_metric metric=contribution_by_asin months=3`
- `meta_metric metric=creative_leaderboard limit=100`
- `meta_metric metric=ad_returns limit=200`
- `brand_brain action=moves`
- `ad_health_check`

Steps:
1. Call `meta_metric` with `metric=amazon_ads`, `period=weekly` and `weeks=6`. Read every `result_page`. If a week says rows kept N of M, say which videos may be missing. If it says no_linked_ads or error, stop. A `gated` stamp over real rows is wrong: use the rows.
2. Call `meta_metric` with `metric=ad_destinations` and `days=28`. Take out the "not linked to Amazon" line and any ad whose destination is dtc or walmart.
3. Call `amazon_metric` with `metric=daily_revenue` and `days=49`. A day over 1.5 times the median is a sale day (Prime, Black Friday). Rank on the 4 newest settled weeks: ended 14 or more days ago, no sale day. The newest settled week is the 7-day check. The 2 newest weeks show as still settling only.
4. Group rows by video: strip audience prefixes and " - Copy" so copies add up. Cost per Amazon order = Meta spend over Amazon orders on both windows. Rank only videos with 10 or more orders; list the rest as too few.
5. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3` for profit per Amazon order, plus the 10% referral bonus when the brand gets it. A video above that cost per order loses money on Amazon.
6. Call `meta_metric` with `metric=creative_leaderboard` and `limit=100` for each top video's 3-second hook rate. Missing: say "hook rate not measured".
7. Already on the website: call `meta_metric` with `metric=ad_returns` and `limit=200`, read the ad set list once from page 1, and `brand_brain` with `action=moves`. A website ad from the same creator and video is "already running" with its cost per website sale. Never plan it again.
8. Plan the next 3 to 6 not yet running: video, product, page, ad set and daily budget. Budget from saved decisions; else ask once, default $50 a day for this run only. New 4:5 feed version, website link, no Amazon logo.
9. Call `ad_health_check` with `ads={"ad_ids": ["<id>"]}` and `only=["right_product","creator_tag"]` on each original. Carry any creator tag into the new name.

Checks before answering:
- A video for one product goes only to that product's page. Two products: hold.
- A video cheap per Amazon order is a guess for the website. The new ads are a test, judged by the website keep line.
- Never stop the Amazon original to make room.

Rounds (relook before you answer):
1. **Second window.** Fails when: a top-3 video on 28 days falls out of the top 10 on the settled week. Fix: drop it from the plan, name it as fading.
2. **Already running.** Fails when: a planned video matches a live website ad by creator and video name in step 7. Fix: move it to "already running".
3. **Profit per order.** Fails when: a planned video's cost per Amazon order is over the profit per order from step 5. Fix: say it loses money on Amazon; plan it only as a website test.
4. **Product match.** Fails when: ad_health_check flags right_product, or the video's name names another product than its page. Unknown: say "watch it first". Fix: change the page or hold.
5. **Hook check.** Fails when: a planned video's hook rate is under half the account median. Not measured: the round cannot run; say so and hold any video whose two windows disagree. Fix: move it below a stronger one.
6. **Spend check.** Fails when: the new daily total is over the saved or approved amount. Fix: cut the plan to fit.

Output:
- One line first: videos ranked, the top cost per Amazon order, how many already run on the website, how many go into the plan.
- The ranking: video, product, 28-day and 7-day cost per order, profit per order, orders, hook rate.
- Already running on the website, with cost per website sale. Then the build plan, one row per new ad.
- Videos held and why. "Not checked:" videos the tool cut off, hook rates not measured.

Never:
- Never build, pause or change an ad. A person or "Add new videos as Meta ads" does that.
- Never send a video to another product's page.
- Never switch off a campaign an outside agency runs.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-video-rank-by-amazon-orders". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
