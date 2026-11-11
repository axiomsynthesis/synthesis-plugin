---
description: "Keyword flywheel: how much to spend on each search: For each big search: what Amazon credits per $1, the later sales the flywheel must bring to break even, what is measured so far (rank boost, repeat to date, projected long-term repeat), and raise, hold and test, or trim in steps, with the exact test"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Keyword flywheel: how much to spend on each search

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Keyword flywheel: how much to spend on each search" (id: mkt-amazon-keyword-flywheel, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Answers the flywheel question per search. Start from Amazon's own count: the ad-report sales per $1 and ACoS. The first order keeps only the margin before ads, so the flywheel (rank boost on other searches, repeat buying, long-term repeat) must bring the rest later. The call compares what is needed with what is measured, each in dollars of later sales per $1 of Amazon-credited sales.

What to read: Amazon's own ad-report sales and ACoS per search, the margin before ads, best-seller rank and other-search sales, repeat buying measured and projected to 12 and 24 months, and Amazon's search report as a check
What to give me: For each big search: what Amazon credits per $1, the later sales the flywheel must bring to break even, what is measured so far (rank boost, repeat to date, projected long-term repeat), and raise, hold and test, or trim in steps, with the exact test

Synthesis tools to use:
- `cost_rules for=mkt-amazon-keyword-flywheel`
- `brand_brain action=moves`
- `amazon_metric metric=keyword_incrementality top=10`
- `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact match_type=EXACT`
- `amazon_metric metric=organic_rank days=60 search=<search>`
- `breakeven_roas asin=<asin>`
- `measurable_test`

Steps:
1. Call `brand_brain` with `action=moves` and `recall_decisions` for searches pushed on purpose for rank, with their loss cap and end date.
2. Call `amazon_metric metric=keyword_incrementality top=10`. Lead with each row's `flywheel_call`: `sentence`, `needed_later_sales_per_dollar`, `measured_later_sales_per_dollar` and `measured_range_per_dollar`, the parts in `measured_parts_per_dollar` (rank boost, repeat to date, projected 12 and 24 months), `call` and `test`. Quote `repeat_projection_backtest` (error of the projection method on older products).
3. Then `flywheel_call.how_sure`: the search report's lower count, as how sure, never as the headline. Add `cost_of_losing_share` for any trim.
4. Call `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact match_type=EXACT`. Keyword rows whose text equals the search give its exact bid; none means "n/a".
5. For each search to trim or raise, call `amazon_metric metric=organic_rank days=60 search=<search>` for rank now and before.
6. Check the main product's break-even with `breakeven_roas asin=<asin>`.

Checks before answering:
- Projected repeat is a PROJECTION: say so beside its number, with the backtest error.
- Weeks marked `ad_group_allocated` are estimates: say so when they set a level.
- Own-name searches are not read here.

Rounds (relook before you answer):
1. **Amazon's count leads.** Fails when: a search's first line is the search report's lower count. Fix: lead with `flywheel_call.sentence`; the lower count goes in how sure.
2. **No cut on a straddle.** Fails when: a trim or cut is said where `measured_range_per_dollar` reaches `needed_later_sales_per_dollar`. Fix: hold and test, with the row's `test`.
3. **Line check.** Fails when: `breakeven_roas` differs from the row's `margin_before_ads_pct` by more than 5 points. Fix: use `breakeven_roas`, redo needed = 1 / (Amazon sales per $1 x margin) - 1 and say so.
4. **Trim in steps.** Fails when: a trim cuts more than a third of a search's spend at once. Fix: step down a third, read total orders and rank after 3 weeks, then step again.

Output:
- Per search, exactly: "Amazon credits $X of sales per $1 here (ACoS Y%). Each $1 of those sales keeps Z¢ up front, so the flywheel must bring $N more later. Measured so far: $M (rank boost $a, repeat to date $b, projected long-term repeat $c, range …). Call: … Test: …" Then the how-sure line in plain words.
- A table: search, spend a week, Amazon sales per $1, needed, measured (range), call.
- Bid list for the bid sheet: search, match type, current bid, new bid, reason.

Never:
- Never lead with "the search report says fewer sales", and never say "cut".
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
- If you could not finish, open your answer with "Stuck:" and what I need to do. If your answers are not saved for you automatically, save this one with the Synthesis tool `capture_turn`: my request as `question`, your answer as `answer`, and `context` starting with "automation: mkt-amazon-keyword-flywheel".

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
