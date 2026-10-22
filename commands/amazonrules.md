---
description: "Which Meta ads for Amazon to keep, cut or move up: Keep, trim, cut and move-up lists for Amazon-bound Meta ads, each ad with its spend, return, orders and the dollars a week at stake, judged against each product's break-even"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Which Meta ads for Amazon to keep, cut or move up

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which Meta ads for Amazon to keep, cut or move up" (id: meta-amazon-keep-cut-promote, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Judges every Meta ad that sends shoppers to Amazon by Amazon's own orders, not Meta's.
It reads the same source, spend, weeks and bar as "Meta to Amazon read" and "Rank my videos by cost per Amazon order", so all three give one ad the same call.
Changes go through "Switch Meta ads on or off for me" and "Change a Meta budget for me".

What to read: Meta spend for every ad that sends shoppers to Amazon, the Amazon orders and sales Amazon Attribution credits to each, over the last settled weeks, each ad's destination, each product's Amazon margin and each ad's campaign and daily budget
What to give me: Keep, trim, cut and move-up lists for Amazon-bound Meta ads, each ad with its spend, return, orders and the dollars a week at stake, judged against each product's break-even

Synthesis tools to use:
- `cost_rules for=meta-amazon-keep-cut-promote`
- `meta_metric metric=amazon_ads period=weekly weeks=6`
- `meta_metric metric=ad_destinations days=28`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=daily_revenue`
- `brand_brain action=moves`
- `meta_metric metric=ad_daily_trend days=14`
- `ad_health_check`

Steps:
1. Call `meta_metric` with `metric=amazon_ads`, `period=weekly` and `weeks=6`. Read every `result_page`. If a week says rows kept N of M, say what share of spend was shown. Return is Amazon sales over Meta spend.
2. If it says no_linked_ads or error, or its rows are empty, stop and say why. A `gated` stamp over rows that carry spend, sales and orders is wrong: use the rows and say so.
3. Call `meta_metric` with `metric=ad_destinations` and `days=28` (top 40 ads only). Take out the "not linked to Amazon" line and any ad whose destination is dtc or walmart.
4. Call `amazon_metric` with `metric=daily_revenue` and `days=49`. A day over 1.5 times the median is a sale day (Prime, Black Friday). Settled weeks ended 14 or more days ago with no sale day. 7-day read: the newest settled week. 28-day read: the 4 newest. The 2 newest weeks are "still settling" only.
5. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3`. Each family's bar is its break-even: 1 over its margin share, plus the 10% referral bonus when the brand gets it. Never a flat number.
6. Read saved answers in `recall_decisions`; ask once only for what is missing: which campaigns an outside agency runs, and its bill. Say a default holds for this run only.
7. Call `brand_brain` with `action=moves` for ads already switched off, cut or moved up. Call `ad_health_check` with `ads={"ad_ids": ["<id>"]}` and `only=["schedule_budget","switched_on"]` for each ad you would cut, trim or move up. An ad already off is "already off", no action.
8. The rules, same as /metaamazon, each overridable by the owner:
   - Test ad (first ran in 28 days): cut at $150 with no Amazon order; under 3 days live is too early.
   - Move up: at or above the bar on both windows, $300+ spent, 10+ orders.
   - Trim: 1.0 or more but under the bar on both windows. Lower its ad set budget by the share under the bar.
   - Cut: under 1.0 after $500 spent on both windows. Windows disagree: hold.
9. For each cut, call `meta_metric` with `metric=ad_daily_trend`, `ad_id=<id>` and `days=14`. Spend and return both climbing: hold as ramping.
10. Dollars at stake: for a cut or trim, its weekly spend minus the Amazon profit it brings.

Checks before answering:
- Agency or influencer bills are their own cost line, never in Meta spend or the return.
- Savings are real only if the budget comes down. Say so on every cut.
- Agency campaigns go in their own list. The owner decides.
- Ads that share one Amazon link are one row.

Rounds (relook before you answer):
1. **Second window.** Fails when: an ad's 7-day return sits on the other side of the bar from its 28-day return. Fix: hold.
2. **Still settling.** Fails when: a cut or move-up rests on the 2 newest weeks. Fix: judge on settled weeks only.
3. **Bar vs margin.** Fails when: an owner's or saved bar is under that family's break-even from step 5. Fix: raise it and re-sort.
4. **Order count.** Fails when: a move-up rests on fewer than 10 orders. Fix: back to keep.
5. **Argue the losing case.** For the biggest cut, make the case to keep it. Fails when: spend rose in the last 7 days and the newest week's return is above the week before. The daily trend has no Amazon return. Fix: hold as ramping.
6. **Money adds up.** Fails when: the cut savings exceed those ads' spend, or the budget is not lowered. Fix: say no money is saved yet.

Output:
- One line first: 28-day spend, Amazon sales and return, the bar, and the dollars a week at stake.
- Cut: each ad, spend, orders, return on both windows, the rule, and the budget to lower.
- Trim: each ad set, the share under the bar and the new budget.
- Move up: each ad as a copy into its own ad set at a stated daily budget. One ad inside a shared budget cannot be budgeted.
- Keep, hold, already off and agency lists: one line each.

Never:
- Never change, pause or raise an ad. A person does that.
- Never put an outside agency's campaign on the cut list without the owner's word.
- Never judge an Amazon-bound ad on Meta's own sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-amazon-keep-cut-promote". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
