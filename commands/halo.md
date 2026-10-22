---
description: "Does Meta grow your Amazon sales?: A rough range for Amazon profit per $1K on Meta, and the state test that settles it"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Does Meta grow your Amazon sales?

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Does Meta grow your Amazon sales?" (id: meta-does-meta-grow-amazon-sales, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Answers whether your Meta spend lifts Amazon sales, even though Meta cannot see Amazon orders. It lines up Meta spend with searches for your brand on Amazon and with Amazon sales. Then it gives a rough range for the lift in sales and in profit, says plainly how sure we are, and designs the state test that would settle it. Only that test gives a firm number.

What to read: Meta spend, Amazon branded search, attribution, Amazon sales by state and Amazon margin per product
What to give me: A rough range for Amazon profit per $1K on Meta, and the state test that settles it

Synthesis tools to use:
- `cost_rules for=meta-does-meta-grow-amazon-sales`
- `meta_metric metric=weekly_trend`
- `amazon_metric metric=search_query_trend`
- `amazon_metric metric=attribution_sources`
- `amazon_metric metric=offamazon_share`
- `amazon_metric metric=daily_revenue`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=geo_penetration months=3 limit=51`
- `meta_metric metric=creative_geo`

Steps:
1. Call `meta_metric` with `metric=weekly_trend` and `weeks=26` for weekly Meta spend.
2. Call `amazon_metric` with `metric=search_query_trend`, `grain=week` and `periods=26`, with no keyword. Read `branded_series.query_volume` for weekly branded searches. Read every page of the result. A keyword returns one row per search with no weekly branded total.
3. Call `amazon_metric` with `metric=daily_revenue` and `days=180`, rolled up to weeks, for Amazon sales.
4. Call `amazon_metric` with `metric=attribution_sources` and `days=90` for sales Amazon tracked back to Meta links.
5. Call `amazon_metric` with `metric=offamazon_share` and `days=90` for how much of Amazon is driven from outside Amazon.
6. Fit the trend in Amazon sales over the 8 or more weeks before Meta spend rose, and project it forward. Count only sales above that line, with a one to two week lag. Then compare weeks of high and low spend the same way, for a low and a high figure for sales added per $1K.
7. Call `amazon_metric metric=contribution_by_asin months=3` for the margin of the products the ads point to. Turn added sales into added profit. A lift that earns less profit than the $1K it cost is a loss, even if it is positive. Work out the break-even: the extra Amazon orders a day the spend needs to pay for itself, so the reader can see the bar.
8. Propose a state holdout. Call `amazon_metric metric=geo_penetration months=3 limit=51`. Pick about 20% of states matched on Amazon sales and customers. Switch Meta off there for 4 to 6 weeks, then compare Amazon sales by state against the rest.

Checks before answering:
- Deal weeks and holidays move both lines at once. Take them out before comparing.
- Fewer than about 12 weeks of spend changes is too little. Say low confidence.
- Tracked Meta links undercount the lift. Never treat them as the whole answer.
- If any series is empty, say which one. Never treat a failed read as no lift.
- Amazon sales credited to Meta links can include creator and agency links that share the same publisher. Say when one week's credited sales are far above what its Meta spend could buy, and leave it out.
- There is no model here with controls or a confidence range. The range from step 6 is a by-eye read. Always say low confidence until the state test runs.
- If a product has no cost entered, its margin is blank. Give the lift in sales only for it and say why.

Rounds (relook before you answer):
1. **Pre-trend.** Re-read Amazon sales for the 8 weeks before the spend rise from step 3. Fails when: sales were already climbing fast enough to explain half or more of the lift. Fix: count only sales above the projected trend and cut the range.
2. **Break-even bar.** Fails when: the high end of the range adds less Amazon profit per $1K than $1K, or fewer extra orders a day than the break-even from step 7. Fix: the headline says the lift does not pay yet, whatever its size.
3. **Second window, sale days out.** Drop deal and holiday weeks and re-run step 6 on the last 13 weeks only. Fails when: the low or high figure moves by more than half, or flips sign. Fix: say low confidence and give the wider range.
4. **Dose by state.** Call `meta_metric` with `metric=creative_geo`, `grain=region`, `days=90` and `limit=500`, and add spend up by state. Set it beside Amazon sales growth by state from `geo_penetration`. Fails when: the heaviest-spend third of states did not grow faster than the lightest third after their own trend. Fix: say the state read does not back the lift.
5. **Argue the other side.** Write the strongest case that the lift is bigger (tracked links only count clicks, and sales campaigns reach the best buyers) and that it is smaller (sales were rising anyway, creator links share the same tag). Fails when: either case rests on a number this run did not read. Fix: read it, or list it as not checked. Only the state test settles it.

Output:
- One line first: whether to keep, cut or test Meta spend aimed at Amazon, with the range of Amazon profit added per $1K and the confidence.
- A short table: week, Meta spend, branded searches, Amazon sales.
- The state test: which states go dark, for how long, and what result would mean keep or cut.

Never:
- Never change a Meta budget or campaign. A person does that.
- Never state the lift as proven without a test.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-does-meta-grow-amazon-sales". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
