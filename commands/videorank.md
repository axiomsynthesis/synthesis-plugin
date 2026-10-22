---
description: "Rank my videos by cost per Amazon order and rebuild the best for the website: Every Amazon-bound video ranked by Meta dollars per Amazon order, and a build plan to rebuild the top ones as website sales ads, each sent only to its own product's page"
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
It ranks every Amazon-bound video by Meta dollars spent per Amazon order over 14 days, and checks the order holds on 7 days.
An ad cannot be moved from an Amazon traffic campaign to a website sales campaign. The plan rebuilds each winner as a new ad instead.

What to read: Meta spend and Amazon Attribution orders for every Amazon-bound video over the last two closed weeks, each video's product and hook rate, and the brand's website ads with their pages and keep line
What to give me: Every Amazon-bound video ranked by Meta dollars per Amazon order, and a build plan to rebuild the top ones as website sales ads, each sent only to its own product's page

Synthesis tools to use:
- `cost_rules for=meta-video-rank-by-amazon-orders`
- `meta_metric metric=amazon_ads period=weekly weeks=3`
- `meta_metric metric=video_efficiency`
- `meta_metric metric=ad_destinations days=14`
- `meta_metric metric=ad_returns`
- `ad_health_check`

Steps:
1. Call `meta_metric` with `metric=amazon_ads`, `period=weekly` and `weeks=3`. The two newest closed weeks are the 14-day read, the newest alone is the 7-day read.
2. If it says unavailable, no_linked_ads or error, stop and say why. Never rank from missing data.
3. Group rows by video: strip audience prefixes and " - Copy" so copies of one video add up. Ads that share one Amazon link stay one row.
4. Cost per Amazon order = Meta spend over Amazon orders, per video, on both windows. Rank on 14 days. Only rank videos with 10 or more orders on 14 days. List the rest as too few.
5. Call `meta_metric` with `metric=video_efficiency` and `limit=50` for each top video's hook and hold rate.
6. Call `meta_metric` with `metric=ad_destinations` and `days=14`. Find the product each top video shows and the website page for that product.
7. Call `meta_metric` with `metric=ad_returns` and `limit=50` for the website keep line and the test ad set to build into.
8. Plan the top 3 to 6 videos: video, product, website page, target ad set and daily budget. Default: the brand's test ad set at $50 a day. Rebuild as a new website sales ad with a 4:5 feed version. Website link and tags, no Amazon logo.
9. Call `ad_health_check` with `ads={"ad_ids": ["<id>"]}` and `only=["right_product","creator_tag"]` on each original ad. Carry any creator tag into the new name.

Checks before answering:
- A video sells one product. A video for one product goes only to that product's page. A video showing two products is held.
- Amazon orders are not website orders. A video cheap per Amazon order is a guess for the website. Say the new ads are a test, judged by the website keep line.
- Never stop the Amazon original to make room. It keeps running unless the person says otherwise.
- Amazon keeps crediting orders for 14 days after a click. Say when the newest week has not settled.

Rounds (relook before you answer):
1. **Second window.** Re-rank on the 7-day week alone. Fails when: a top-3 video on 14 days falls out of the top 10 on 7 days. Fix: drop it from the plan, name it as fading.
2. **Still settling.** Fails when: the newest week has not settled and a top video's rank rests on it alone. Fix: rank on the older week and say so.
3. **Product match.** Watch each planned video against its page. Fails when: a video shows a different product than its target page, or ad_health_check flags right_product. Fix: change the page or hold it.
4. **Hook check.** Fails when: a planned video's hook rate is under half the account's median. It may sell on Amazon from a warm crowd only. Fix: move it below one with a stronger hook.
5. **Argue the losing case.** For the top video, ask why it would fail on the website. Fails when: it leans on an Amazon badge, Amazon price or Amazon-only offer that the website page does not carry. Fix: hold it or plan a new cut.
6. **Spend check.** Fails when: the new daily total is over what the person approved. Fix: cut the plan to fit.

Output:
- One line first: videos ranked, the top cost per Amazon order, and how many go into the plan.
- The ranking: video, product, 14-day and 7-day cost per order, orders, hook rate.
- The build plan: one row per new ad with page, ad set and budget.
- Videos held, and why.

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
