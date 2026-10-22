---
description: "Who's stealing your search shoppers?: The named rival products winning shoppers on your searches, and which of your searches each one threatens"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Who's stealing your search shoppers?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Who's stealing your search shoppers?" (id: mkt-amazon-search-rivals-named, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Search data shows your share and leaves the rest anonymous. This names the products taking the rest.
It ranks rivals by how many of your searches they win and whether they are rising.

What to read: Amazon's top clicked products on your own search terms, with their click share next to yours
What to give me: The named rival products winning shoppers on your searches, and which of your searches each one threatens

Synthesis tools to use:
- `amazon_metric metric=search_competitors periods=4 top=20`
- `scrape_amazon_product`
- `amazon_metric metric=shelf_position days=30 limit=40`
- `amazon_metric metric=search_query_performance periods=4 scope=nonbranded`

Steps:
1. Call `amazon_metric metric=search_competitors periods=4 top=20`. It reads by week when no grain is given. Rivals and terms come back over several pages. Call again with the next result_page the result names until all 20 rivals are in hand. Skip terms whose `search_relevance` is off_category. If the latest week holds a marketplace event, such as Prime Day, Big Deal Days or Black Friday, or its `contested_volume_change_pct` is above 25%, judge the change on the prior clean week. Say so in the first line.
2. Rank rivals by the number of your searches where they are in the top three clicked, then by click share.
3. Call `amazon_metric metric=shelf_position days=30 limit=40` first. It already holds price, rating and review count for tracked rivals, and shows whether they cut price recently.
4. Scrape only top-three rivals missing from it: call `scrape_amazon_product asin=<rival product id>` for live price, rating and reviews. Ask before more than three scrapes: they draw on a shared monthly allowance.

Checks before answering:
- Rival data comes from Amazon's top-three clicked list. A rival outside the top three is invisible here. Say so.
- Shares are percentages already. Never rescale.
- Click share is not dollars. This answer cannot yet say what a rival costs you in sales. Say so if asked "how much".
- A review count that jumps or falls by hundreds in a week is usually a change in how reviews are counted, not real reviews. Say so, never call it a trend.
- Scraped data is a snapshot from a third-party source. Label it scraped, with the date.
- If the tool returns no rivals, check whether search data is loaded before saying you have none.

Rounds (relook before you answer):
1. **Does it hold?** Call `amazon_metric` with `metric=search_competitors`, `periods=8` and `top=20`. Fails when: the rival to watch is in the top three on your searches in fewer than half of the 8 weeks. Fix: call it noise and pick the next rival that holds.
2. **Whose search is it?** Split the rival's searches into its own brand name, your brand name and plain product searches. Fails when: most of its lead comes from searches for its own name. That is its own buyers, not yours. Fix: count only your-name and plain searches. Rival-name searches are a chance for your ads, list them apart.
3. **Is it really taking yours?** Call `amazon_metric` with `metric=search_query_performance`, `periods=4` and `scope=nonbranded`. Fails when: on the searches the rival leads, your share of purchases held or rose over the 4 weeks. Fix: say it is rising but not yet taking your buyers.
4. **Fresh price.** Fails when: the shelf or scraped price and reviews for a top rival are over 7 days old. Fix: label the date, or ask before one more scrape.

Output:
- One line: the one rival to watch and why.
- A table: rival product, title, number of your searches it leads, its click share, yours, change over 4 weeks, price, rating, reviews.

Never:
- Never run scrapes in a loop over every rival.
- Never call a rival's sales figure. This data has clicks, not their sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-search-rivals-named". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
