---
description: "Find your next product in search demand: Searches for things you could make but don't sell, on a weak shelf, sized in yearly revenue"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Find your next product in search demand

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find your next product in search demand" (id: growth-new-product-ideas-from-search, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds searches where shoppers want something you do not sell and the products that win are weak. It keeps only ideas the brand could make, sizes each in yearly revenue, and ranks them.

What to read: Amazon search data, the winners on each search, rival reviews, what the brand makes
What to give me: Searches for things you could make but don't sell, on a weak shelf, sized in yearly revenue

Synthesis tools to use:
- `amazon_metric metric=search_term_gaps limit=15 kind=NOT_SURFACING weeks=12`
- `amazon_metric metric=search_query_performance scope=nonbranded top=25`
- `brand_facts`
- `competitor_review_voice`
- `scrape_amazon_search`

Steps:
1. Call `amazon_metric` with `metric=search_term_gaps`, `limit=15`, `kind=NOT_SURFACING` and `weeks=12`. These are searches near your products where Amazon never shows you. Searches for a rival's brand name and off-category searches are already set aside.
2. Call `amazon_metric` with `metric=search_query_performance`, `scope=nonbranded` and `top=25`. For each gap, find the nearest search you do show on. Take its purchases per search (market purchases divided by searches).
3. Shelf strength, free, from the gap rows: add the top 3 winners' click shares. Under 30% is open, 30% to 60% is contested, over 60% is locked. Winnable share: 5% if open, 2% if contested, 0 if locked. Say these shares are rules of thumb.
4. Trend, free: call `amazon_metric` with `metric=search_term_gaps`, `kind=NOT_SURFACING` and `weeks=4`. A term whose best rank in the last 4 weeks matches its 12-week best is holding or rising. Much worse means fading.
5. Fit: call `brand_facts`. Mark FIT yes only if the idea is a format or formula the brand already makes, or its supplier lists. Otherwise FIT no, and say why.
6. Size each FIT yes idea: weekly searches x 52 x purchases per search x winnable share x price. For price, use the brand's own price for its nearest product.
7. Call `competitor_review_voice` with `asin` set to each winner of the top 2 ideas. It only works for products on your watchlist. Say so when one is not.
8. Only if the person asks, call `scrape_amazon_search` with that `keyword` and `k=20` for the top idea's shelf prices and ratings. It is paid.

Checks before answering:
- Search counts are the biggest single week, not a month. Call them searches a week, rounded, as estimates.
- A gap with no search count stays unsized. Never fill it. This cannot yet estimate volume from search rank alone.
- Leave out searches for products you already sell.
- A search for a part or refill that fits another brand's device is an add-on play. List it on its own.
- Revenue is sized before costs. Margin, launch and stock costs are not in it. Say so.
- Duplicate rival reviews across two listings count once.

Rounds (relook before you answer):
1. **Real fit.** Re-read `brand_facts` for each FIT yes. Fails when: no fact names that format, formula or supplier. Fix: mark it FIT no.
2. **Still there.** Fails when: the top idea is fading in step 4. Fix: move the next holding idea to the top.
3. **A reason to switch.** Re-read the winners' reviews. Fails when: they show no repeated complaint the brand would fix. Fix: say the shelf is weak on shares but buyers are happy, and rank it lower.
4. **Brand-name leak.** Fails when: a sized search holds any brand name. Fix: drop it.
5. **Size sanity.** Fails when: an idea's yearly size is over the brand's own best product's yearly sales, or over 10% of all purchases on that search. Fix: recheck the winnable share and say which input drove it.

Output:
- One line first: the single best FIT yes idea, its yearly revenue size, and why the shelf is open.
- A table of up to 10 ideas: search, searches a week (estimate), top-3 click share, trend, fit, yearly size.
- Then FIT no ideas in one line each.

Never:
- Never launch, list or order anything. A person decides.
- Never make up a search count, a share or a rival's rating.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: growth-new-product-ideas-from-search". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
