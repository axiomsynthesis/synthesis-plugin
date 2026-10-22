---
description: "Score and rewrite a product page to sell more: Your products ranked by money at stake, a 0-100 score for each page in 6 parts, a full rewrite inside your approved claims, a before and after score, and the searches to watch"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Score and rewrite a product page to sell more

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Score and rewrite a product page to sell more" (id: amazon-listing-optimizer, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds the products where a better page makes the most money, then scores each page 0-100 in six parts and rewrites it.
It builds on how Amazon's search and its shopping assistant now read a page: the jobs, people, places and worries behind a search, not just keywords.
It uses your own sales, searches, reviews and approved claims. It replaces the old one-product rewrite. For keywords across the whole catalog use /go add the searches your listings miss; for the A+ designer brief use /go write the A+ content brief; for whether ads on a search build organic rank use /keywordflywheel.

What to read: Profit per product, your real searches and share, reviews, rivals on the same searches, approved claims
What to give me: Your products ranked by money at stake, a 0-100 score for each page in 6 parts, a full rewrite inside your approved claims, a before and after score, and the searches to watch

Synthesis tools to use:
- `cost_rules for=amazon-listing-optimizer`
- `amazon_metric metric=contribution_by_asin`
- `amazon_metric metric=keyword_opportunities`
- `amazon_metric metric=search_term_gaps`
- `amazon_metric metric=search_competitors grain=week`
- `amazon_metric metric=listing_details`
- `amazon_metric metric=review_voice`
- `competitor_review_voice`
- `winning_hooks read_new=false`
- `amazon_metric metric=shelf_position`
- `amazon_metric metric=conversion_funnel`
- `brand_facts`
- `brand_kit`
- `amazon_metric metric=organic_rank`
- `brand_brain action=moves`
- `measurable_test`

Steps:
1. Triage. Check `brand_brain` with `action=moves` for a page change already being read. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3` for sales and profit after ads per product. For the top 5 by profit, call `amazon_metric` with `metric=keyword_opportunities`, the `asin` and `top=10`: rank by profit times the purchase share gap on its real searches. Skip a product low on stock or off the Buy Box: the page is not its problem.
2. Read the page. Call `amazon_metric` with `metric=listing_details` and the `asin`. If Amazon refuses (no Product Listing permission), use the title shown on your own row in step 5 and ask me to paste bullets, description and backend fields, or to upload my category listing file. Only with my yes, one `scrape_amazon_product` call. Call `amazon_metric` with `metric=shelf_position` and the `asin` for price, rating and review count. Say which parts were read, pasted or not seen.
3. Buyer language. Call `amazon_metric` with `metric=review_voice`, the `asin` and `limit=200`; `competitor_review_voice` with `limit=60`; `winning_hooks` with `read_new=false` for ad comments.
4. Score 0-100, six parts, each with sub-scores and its evidence: Search cover 25 (each real search weighted by purchases, plus `amazon_metric` `metric=search_term_gaps` `kind=NOT_SURFACING`; is its word in title, bullets or backend); Buyer-reason cover 20 (15 kinds: job, other uses, outcome, product type, what it replaces, occupation, who uses it, who buys, time, place, body part, activity, used with, goal, interests; 5 or fewer is keyword-era); Questions answered 20 (top 5 worries and questions, each answered with a fact); Backend fields 10 (list the blank ones); Images and trust 15 (7 images incl. lifestyle and chart, video, A+, rating 4.0 or more, reviews, stock; look at the images I share or the page, never guess them); Claims 10.
5. Rivals. Call `amazon_metric` with `metric=search_competitors`, `grain=week` and `term=` each of the top 3 searches: the 3 rivals that win them and what their titles cover that ours does not.
6. Rewrite inside `brand_facts` and `brand_kit`: title, item highlights, 5 bullets (benefit, proof, question answered), description, backend terms (no word already in front copy, under 249 bytes), backend field values, A+ module outline, the 7 image slots. Re-score it.
7. Measure. Call `amazon_metric` with `metric=organic_rank` for the top searches now. Then `measurable_test`: organic spot, purchase share and buy rate (`metric=conversion_funnel`) at 14 and 28 days after I apply it; Amazon can take days to index.

Checks before answering:
- Never score a part you did not read. Mark it "not seen" and score the rest out of what was read.
- Search shares are already percents. Weekly search data cannot be added into months.
- A rival's name is never a keyword or a backend term.
- Say whether the read window holds a big sale event.

Rounds (relook before you answer):
1. **Claims.** Check each claim with `brand_facts`. Fails when: a line states a result, a health benefit or a number no saved fact backs, or treats or prevents a condition. Fix: cut it, keep the feeling.
2. **Top searches.** Fails when: any of the top 10 searches by purchases is in neither the new copy nor a written "skipped because". Fix: place it or say why.
3. **Real buyer words.** Fails when: a buyer reason used has no review, comment or search behind it. Fix: cut it.
4. **Type first.** Fails when: the first 80 characters of the title do not say what the product is, or the title repeats a word 3 times. Fix: rewrite the opening.
5. **Backend limits.** Fails when: backend terms pass 249 bytes or repeat a front-copy word. Fix: cut the lowest-purchase words first.
6. **Nothing lost.** Fails when: a search where we hold purchase share above our average loses its word. Fix: put it back.
7. **Argue for the old page.** Fails when: the old page beats the new on a search with more purchases than the one it gains. Fix: keep the old line there.

Output:
- One line first: the product, its score now and after, and the money at stake a month.
- Triage table: product, profit a month, share gap, score.
- Score card: six parts, sub-scores, the evidence, and what was not seen.
- Before and after, field by field, with why; backend byte count.
- Rivals: who wins the top searches and what they cover that we do not.
- The test: searches, numbers to read, dates.
- A person applies it in Seller Central or with their own Claude.

Never:
- Never change the page, an ad or any account. A person applies it.
- Never invent a search volume, review, claim or blank field.
- Never copy a rival's wording.
- No `scrape_amazon_product`, `compare_to_shelf` or `keyword_rank_tracker` without my yes: each read is paid.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-listing-optimizer". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
