---
description: "Score and rewrite a product page to sell more: Your products ranked by money at stake, a 0-100 score for each page in 6 parts, a rewrite that sells inside your approved claims, the lines that need your approval, and an Amazon A/B test to prove it"
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
Finds the products where a better page makes the most money, scores each page 0-100 in six parts, and rewrites it to sell, not to score.
It reads the jobs, people and worries behind a search, as Amazon's search and shopping assistant now do. For keywords across the catalog use /go add the searches your listings miss; for the A+ brief use /go write the A+ content brief.

What to read: Profit per product, your real searches and share, reviews, rivals on the same searches, approved claims
What to give me: Your products ranked by money at stake, a 0-100 score for each page in 6 parts, a rewrite that sells inside your approved claims, the lines that need your approval, and an Amazon A/B test to prove it

Synthesis tools to use:
- `cost_rules for=amazon-listing-optimizer`
- `amazon_metric metric=contribution_by_asin`
- `amazon_metric metric=keyword_opportunities`
- `amazon_metric metric=search_term_gaps`
- `amazon_metric metric=search_competitors grain=week`
- `amazon_metric metric=listing_score`
- `amazon_metric metric=review_voice`
- `amazon_metric metric=full_reviews`
- `competitor_review_voice`
- `winning_hooks read_new=false`
- `amazon_metric metric=shelf_position`
- `amazon_metric metric=conversion_funnel`
- `brand_facts`
- `brand_kit`
- `amazon_metric metric=organic_rank`
- `brand_brain action=moves`
- `propose_brand_fact`
- `measurable_test`

Steps:
1. Triage. `brand_brain` with `action=moves` for a page change already being read. `amazon_metric` with `metric=contribution_by_asin` and `months=3`; for the top 5 by profit, `metric=keyword_opportunities` with the `asin` and `top=10`: rank by profit times purchase share gap. Skip a product low on stock or off the Buy Box.
2. Score the live page: `metric=listing_score` with the `asin`. That is the before score, never one you work out. If Amazon refuses, ask me to paste the page or upload my category listing file and pass it as `listing`; one `scrape_amazon_product` only with my yes. `metric=shelf_position` for price. Say which parts were read, pasted or not seen and the A+ read. A live title over 75 characters: "Amazon will rewrite this; review it in Review Listing Changes within 14 days".
3. Why people buy. `metric=review_voice` with `limit=200`, `metric=full_reviews` with the `asin`, `competitor_review_voice` with `limit=60`, `winning_hooks` with `read_new=false`. Name the #1 reason people buy: the top search by purchases plus the most-praised review theme. `brand_kit` for the voice.
4. Rivals. `metric=search_competitors` with `grain=week` and `term=` each top 3 search: who wins and what their titles cover that ours does not.
5. Write to sell, inside `brand_facts`. Title of 75 or fewer: product type, top search, #1 reason. Item highlights of 125 or fewer. 5 bullets of 255 or fewer, the #1 reason first; each header a benefit in buyer words, never a review-theme or worry name; then the proof. Answer each worry with its true upside ("rich paste, a pea-size is enough"), never by conceding it. Keep every strong live line unless a rule forbids it: a line no saved fact backs stays, marked "needs your approval", and on my yes `propose_brand_fact` saves it. Backend: new words only, no misspellings (Amazon matches those). Then description, field values, A+ outline, 7 image slots.
6. Score the draft: `metric=listing_score`, the `asin`, the draft as `listing` with `rival_brands` and the live page as `live_copy` inside it. Fix each `policy.blocking_failed` and each `copy_checks` warning; score again. The draft was written to the score, so the score is not proof it sells.
7. Test it. Brand-registered: give the exact Manage Your Experiments test (Brands > Manage Experiments): one of title, bullets or main image, live vs draft, 8-10 weeks, winner on units sold per unique visitor, and the read date. Otherwise `measurable_test`: organic spot (`metric=organic_rank`), purchase share and buy rate (`metric=conversion_funnel`) 14 and 28 days after I apply it.

Checks before answering:
- Never score a part you did not read; mark it "not seen".
- Search shares are already percents. Weekly search data is never added into months.
- A rival's name is never a keyword or a backend term.
- Full review text: its words, never its counts.
- Say whether the read window holds a big sale event.

Rounds (relook before you answer):
1. **Claims.** Check each claim with `brand_facts`. Fails when: a line states a result, a health benefit or a number no saved fact backs and is not marked "needs your approval", or treats or prevents a condition. Fix: mark it, or cut a rule-breaker.
2. **Top searches.** Fails when: any of the top 10 searches by purchases is in neither the copy nor a written "skipped because". Fix: place it or say why.
3. **Real buyer words.** Fails when: a buyer reason used has no review, comment or search behind it. Fix: cut it.
4. **Amazon rules.** Fails when: `policy.blocking_failed` is not empty, or backend terms repeat a front-copy word. Fix: fix each; cut lowest-purchase words first.
5. **Nothing lost.** Fails when: a search where we hold purchase share above our average loses its word. Fix: put it back.
6. **Read it as a shopper.** Fails when: `copy_checks` holds a warning, a header is a label, a bullet opens with a caveat, or a live benefit is gone with no rule named and no approval question. Fix: rewrite that line.
7. **Argue for the old page.** Fails when: the old page wins a search with more purchases than the new one gains, or sells the #1 reason harder. Fix: keep the old line.

Output:
- One line first: the product, its score now and after, and the money at stake a month.
- Triage table: product, profit a month, share gap, score.
- Score card: six parts, the evidence, what was not seen.
- Before and after, field by field, with why; counts; `policy`; `copy_checks`.
- Needs your approval: each exact line and why.
- Rivals; the test and its read date.
- A person applies it in Seller Central or with their own Claude.

Never:
- Never change the page, an experiment, an ad or any account. A person applies it.
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
- If you could not finish, open your answer with "Stuck:" and what I need to do. If your answers are not saved for you automatically, save this one with the Synthesis tool `capture_turn`: my request as `question`, your answer as `answer`, and `context` starting with "automation: amazon-listing-optimizer".

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
