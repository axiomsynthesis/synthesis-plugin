---
description: "Keyword flywheel: what your ad spend really buys in organic rank: For each big search: the ad cost you see, the organic sales the ads really create, the true ad cost with both, and keep, raise, trim or cut, with one test to prove it"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Keyword flywheel: what your ad spend really buys in organic rank

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Keyword flywheel: what your ad spend really buys in organic rank" (id: mkt-amazon-keyword-flywheel, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Tests the rule that you sometimes lose on ads to win organic rank. Per big search, it sets ad spend beside organic share week by week: does spend build organic sales the ad report never shows, how sure, and the true ad cost.

What to read: Ad spend, clicks and orders per search by week, exact and phrase apart, beside the same weeks of Amazon's search report, daily organic rank and break-even
What to give me: For each big search: the ad cost you see, the organic sales the ads really create, the true ad cost with both, and keep, raise, trim or cut, with one test to prove it

Synthesis tools to use:
- `cost_rules for=mkt-amazon-keyword-flywheel`
- `brand_brain action=moves`
- `amazon_metric metric=ppc_keyword_roi days=60 limit=25`
- `amazon_metric metric=ppc_keyword_roi limit=25 start_date=<week-start> end_date=<week-end>`
- `amazon_metric metric=search_query_trend keyword=<search> periods=26`
- `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact match_type=EXACT`
- `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact match_type=PHRASE`
- `amazon_metric metric=organic_rank days=60 limit=60`
- `amazon_metric metric=search_term_gaps weeks=8 limit=30`
- `amazon_metric metric=ppc_organic_vs_paid days=28 limit=15`
- `breakeven_roas asin=<asin>`
- `measurable_test`

Steps:
1. Call `brand_brain` with `action=moves` and `recall_decisions` for searches already pushed on purpose for rank, with their loss cap and end date.
2. Call `amazon_metric metric=ppc_keyword_roi days=60 limit=25`. Keep the 8 to 10 plain searches with most spend and market data. Leave out your own name and product targets.
3. Build the weekly panel. For each of the last 12 closed Sunday-to-Saturday weeks, call `amazon_metric metric=ppc_keyword_roi limit=25 start_date=<week-start> end_date=<week-end>`. Its search report columns are then that same week. Weeks under 30 days old still gain ad sales: mark them.
4. For each kept search, call `amazon_metric metric=search_query_trend keyword=<search> periods=26`. Read only rows of exactly that wording; never add wordings. Take your clicks and purchases per week.
5. Organic per week, all counted in clicks: your clicks in the search report minus ad clicks on that search, same week. Organic orders = organic clicks times your click-to-purchase rate there. Never subtract ad orders from search-report purchases: ad orders count 30 days and other searches, so they run higher.
6. Call `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact` with `match_type=EXACT`, then `match_type=PHRASE`. Give each search's ad cost for exact and phrase apart, with current bids.
7. Call `amazon_metric metric=organic_rank days=60 limit=60` for rank now, before and days checked.
8. Spillover: call `amazon_metric metric=search_term_gaps weeks=8 limit=30` and step 4 rows sharing root words or product. Count the rise in your purchases on those with no ads.
9. Flywheel test per search: spend in a week against organic clicks and share 1 to 4 weeks later. Across searches: did bigger spend rises bring bigger organic rises? Natural tests: weeks spend fell by half. Control: flat-spend searches. Under 8 weeks: `run_bayesian`.
10. True ad cost = spend / (ad sales + organic sales the test supports). Organic sales count only when step 9 passed; else zero. Break-even per search from step 3, checked with `breakeven_roas asin=<asin>` for the main product.

Checks before answering:
- An absent search in the search report is unmeasured, not zero. Shares there are already percentages.
- Fewer than 28 days of rank readings: rank is a snapshot, not a lag test. Use search report share as the long series and say so.
- A bid robot's spend drop is not a planned test. Say which.

Rounds (relook before you answer):
1. **Same basis.** Compare ad clicks with your search-report clicks for every search and week. Fails when: ad clicks exceed your clicks by over 10% in any week. Fix: organic is unmeasured there, never negative; say the wording differs or all traffic is paid.
2. **Settled sales.** Fails when: a week under 30 days old sets a true ad cost. Fix: use settled weeks; show the newest as still landing.
3. **Control group.** Re-read step 3 for flat-spend searches. Fails when: their organic share rose within 1 point of the spending searches. Fix: the market moved, not the ads. Set organic sales to zero.
4. **Pause test.** Fails when: in a week spend fell by half, organic clicks held or rose. Fix: the ads were taking sales you had anyway. Move that search to cut, sized at the spend saved.
5. **Sale weeks and stock-outs.** Fails when: a week driving the call holds a big sale or a week your purchases on the search fell near zero while views held. Fix: drop it and re-run step 9.
6. **Adds up.** Call `amazon_metric metric=ppc_organic_vs_paid days=28 limit=15`. Fails when: organic sales credited to ads across searches exceed the family's organic sales growth over the same weeks. Fix: scale every credit down to fit and say so.

Output:
- Headline: dollars a month of ad spend that pays once organic is counted, and dollars that should be cut.
- Per search, in this shape: "You're paying X% ad cost on <search> (exact X%, phrase X%), but it is creating Y% organic share (rank A→B, organic orders +N a week), which spills into <related searches, total share, sales>. True ad cost with the organic lift is Z% against break-even W%: keep, raise, trim or cut." Add how sure: strong, some or none, and the weeks behind it.
- Rank investment: searches kept below break-even on purpose, each with a monthly loss cap, end date and stop rule: stop when organic share has not risen for 4 weeks.
- Cut list: searches where ads take sales an already high organic rank wins, sized in dollars a month.
- Bid list for the bid sheet or the search blocker: search, match type, current bid, new bid, reason.
- One `measurable_test`: pause exact on one search where you rank in the top 3 for 2 weeks, beside a matched search left on. Measure your purchases on both in the search report.

Never:
- Never treat ad-credited orders, or a link without the control and pause tests, as proof.
- Never change bids or budgets. A person does that.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-keyword-flywheel". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
