---
description: "Build the keyword bid change sheet: A ready-to-upload sheet of bid cuts and raises by keyword, each tied to the product's real break-even"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Build the keyword bid change sheet

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build the keyword bid change sheet" (id: mkt-amazon-keyword-bid-sheet, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A bid sheet a person can upload. Each keyword's target bid comes from what its product can afford. It cuts keywords losing money and raises keywords leaving sales on the table.

What to read: Every Sponsored Products keyword, product target and automatic target with its current bid, spend, clicks and sales over a mature window, plus each product's break-even ad cost
What to give me: A ready-to-upload sheet of bid cuts and raises by keyword, each tied to the product's real break-even

Synthesis tools to use:
- `cost_rules for=mkt-amazon-keyword-bid-sheet`
- `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact match_type=EXACT`
- `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact match_type=PHRASE`
- `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact match_type=BROAD`
- `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact`
- `amazon_metric metric=breakeven_acos_ltv months=12 limit=12`
- `amazon_metric metric=ppc_purchase_latency days=60 limit=10`
- `export_xlsx`

Steps:
1. Call `amazon_metric metric=ppc_purchase_latency days=60 limit=10` to see how long sales take to land after a click.
2. Call `amazon_metric metric=ppc_keyword_bids days=60 min_clicks=20 limit=80 shape=compact` four times: with `match_type=EXACT`, `match_type=PHRASE`, `match_type=BROAD`, then with match type unset. The last pass adds product and automatic targets. From it keep only target ids not already in hand. Its `totals.spend` is the whole window's spend. Leave dates unset, so the window's sales have landed. Rows come cuts first. Keep the campaign, ad group and target ids. If `paging` says more rows exist, call again with `offset` set to where the next page starts. Stop paging once `action` reaches below_evidence_floor: those go to the skipped tab.
3. Call `amazon_metric metric=breakeven_acos_ltv months=12 limit=12`. If it is split into pages, call again with the next result_page the result names. Use the first-order break-even for one-time products and the 3-month figure for products people rebuy. Say which you used.
4. Each keyword's target is the most it can pay per click and still make money: `max_profitable_cpc`, which is revenue per click x the product's break-even ad cost share. Compare it with the cost paid per click (spend over clicks), never with the bid. Cut where the paid cost is over 15% above target. Raise only where it is over 25% below target AND the keyword has orders. A keyword paying more than its target is never raised. The tool's `suggested_bid` only cuts, so work out raises yourself.
5. Build the sheet with `export_xlsx`: a "changes" tab (campaign id, ad group id, target id, keyword, match type, current bid, new bid, reason) and a "skipped" tab for thin or uncosted keywords.

Checks before answering:
- Keywords under 20 clicks go to "skipped". Too few clicks to set a bid.
- A product with no entered cost has no real break-even. Leave its keywords out and list it as missing a cost.
- Say how much of the window's spend the sheet covers, in dollars and percent of `totals.spend` from the call with no match type. If a read says it was cut, the sheet is partial: say so in the first line.
- This sheet changes base bids only. It cannot yet see a bid robot's goal or placement premiums. Where paid cost per click runs well above the bid, something else sets the price: say so first, with the dollars a bid upload cannot reach.
- Never set a bid below Amazon's minimum. Cap any single change at 30%, so one sheet cannot swing the account.

Rounds (relook before you answer):
1. **Three kinds of search.** Sort every row into your own name, a rival's brand name, or a plain product search. Fails when: a raise lands on an own-name keyword. Those shoppers mostly find you anyway. Fix: move it to skipped. Judge rival-name searches as their own group, never mixed in with plain ones.
2. **Rank push.** Call `amazon_metric` with `metric=organic_rank` and `days=30`. Fails when: a cut lands on a search where your organic rank rose in the last 30 days while the ads ran. Sometimes you lose on ads to gain organic rank, but not always. Fix: ask if it is a planned push. If yes, keep the bid with a loss cap and an end date.
3. **Room to grow.** Call `amazon_metric` with `metric=search_query_performance`, `periods=4` and `scope=nonbranded`. Fails when: a raise lands on a search where your share of views is already above your share of purchases. Fix: hold the raise. Where your share of views is under your share of purchases, shoppers who see you buy, so that raise stays.
4. **Repeat value.** Fails when: a product people rebuy was judged on the first-order break-even. Fix: redo its rows on the 3-month figure from step 3.
5. **Size of the sheet.** Fails when: the sheet covers under 60% of spend, or the changes move monthly spend more than 15%. Fix: say so in the first line, and split a bigger change over two weeks.
6. **Three weeks later.** Re-read step 2 for the changed keywords. Fails when: their cost per click moved less than 5%. Fix: say something else sets the price, such as a bid tool or placement premium, and stop uploading bid sheets on them.

Output:
- One line: number of cuts, number of raises, and the monthly dollar effect at today's clicks.
- File `bid_changes_<week>.xlsx` with the two tabs above.
- One line on how we will know: recheck return per dollar on these keywords in 3 weeks.

Never:
- Never upload or change bids in the account. A person uploads the file.
- Never guess a missing product cost.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-keyword-bid-sheet". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
