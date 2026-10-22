---
description: "Check my ads: One health check across every ad account: what failed, ranked by dollars a month, what could not be read, and the three fixes to make first"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Check my ads

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Check my ads" (id: ads-health-check, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs one health check across every ad platform the brand has connected, instead of one platform at a time.
It reads which platforms are connected and current, then runs 15 fixed checks: wasted searches on Amazon and Google, efficient Amazon campaigns out of budget, ads on products about to run out or without the Buy Box, Meta purchase tracking, ad sets too small to learn, new-ad cadence, ads Meta rates below average, spend not aimed at a sale, frequency by campaign role, non-brand Google searches, the TikTok connection, tired TikTok ads, and platform spend against the books.
The server decides every result as pass, fail, unknown or not applicable, with the dollars a month and the numbers and dates behind it.
Failures come ranked by dollars, with a coverage line per platform instead of a score.

What to read: Every connected ad platform (Amazon ads, Meta, Google Ads, TikTok ads), stock, the Buy Box, online store orders and the books
What to give me: One health check across every ad account: what failed, ranked by dollars a month, what could not be read, and the three fixes to make first

Synthesis tools to use:
- `cost_rules for=ads-health-check`
- `ad_health_check`
- `aov_dtc`
- `meta_metric metric=cpa`
- `meta_metric metric=creative_leaderboard limit=50`
- `meta_metric metric=campaign_performance`

Steps:
1. Call `ad_health_check` with no arguments. It takes 20 to 45 seconds and reads every connected platform.
2. To recheck one platform after a fix, call `ad_health_check` with `only=["meta"]`, or another platform: amazon_ads, google_ads, tiktok_ads or books.
3. For each of the top three fixes it returns, open the recipe it names to build the change list.

Checks before answering:
- Use the result as the server decided it. Never turn an unknown into a pass, and never re-judge a fail.
- Unknown means the data was missing, empty, stale or too thin. Say which checks could not be read and why, in one line each.
- Where a platform says "not enough data to judge", give no verdict for that platform.
- Each dollar figure says what it measures: some are money wasted, some are spend exposed to a problem. Never add them up as savings.
- Not applicable means the platform is not connected or the thing checked does not exist for this brand. Do not list those as passes.
- These are housekeeping checks. None of them judges whether a platform's return beats break-even, the return at which ads stop making money. So "0 failed" on a platform never means its spend is profitable. Say this plainly.
- The expert bars are our own reads, not server checks. Keep them in their own lines, never mixed into the server's pass and fail counts.
- A dollar figure on a failure is often spend exposed to a problem, not money lost. Say "spend exposed" when that is what it measures.

Rounds (relook before you answer):
1. **Expert bars.** Defaults unless the brand set its own: website order value at least 2x the main product's single price, cost per new buyer under 50% of order value, thumb-stop at least 50%, outbound click rate at least 3%, cost per click under $1.50. Read `aov_dtc`, then `meta_metric` with `metric=cpa`, `metric=creative_leaderboard` for spend-weighted `thumb_stop_rate_30d` and `outbound_ctr_30d`, and `metric=campaign_performance` for cost per click. Never use the account hook rate: it counts static ads and reads far lower. Fails when: any bar is missed. Fix: add it to the fixes, with the spend it covers.
2. **Where the ad sends people.** Fails when: an ad that sends shoppers to Amazon is judged on website sales or website cost per buyer. Fix: judge it on Amazon sales only.
3. **New ads starved.** From the leaderboard. Fails when: the top 5 ads take over 80% of spend and ads under 14 days old got under $50 each. Fix: name the starved ads as a fix.
4. **Unread share.** Fails when: checks marked unknown cover over 30% of spend. Fix: the headline says the check is partial.
5. **After the fix.** Re-run `ad_health_check` with `only=` the platform fixed. Fails when: the same check still fails. Fix: say the fix did not take.

Output:
- One line first: the headline the tool returned.
- A table of failures in the order returned: platform, check, dollars a month, what the number measures, why.
- The coverage line, then one line per platform with its verdict.
- One line: this check cannot yet say what share of last month's ad spend had its return judged against break-even. Point to /adloss for Amazon ad profit and /adroi for Meta website ads.
- Expert bars: one line each for order value, cost per new buyer, thumb-stop, click rate and cost per click, our number beside the bar, with the spend it covers.
- The top three fixes, each with the recipe that builds its change list.
- Under 20 lines in total.

Never:
- Never give a 0 to 100 score or a grade. The coverage line replaces it.
- Never change anything in an ad account. A person does that.
- Never say an ad account is healthy when checks could not be read.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ads-health-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
