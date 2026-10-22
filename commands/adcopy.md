---
description: "Write ad copy for every buyer stage: Ad copy for one product written five ways, from people unaware of the problem to people ready to buy"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Write ad copy for every buyer stage

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Write ad copy for every buyer stage" (id: grw-awareness-ladder-copy, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
People meet your ad at different stages. Some do not know they have the problem, some know the problem, some compare products, some know you and need a nudge. This first finds which stage your current ads leave out, by the money behind each stage. Then it writes one ad for each stage, in your customers' words, with every claim checked against your product facts, and a plan to test them.

What to read: Your non-branded search terms, review language, ad comments, product facts and the opening lines of your best ads
What to give me: Ad copy for one product written five ways, from people unaware of the problem to people ready to buy

Synthesis tools to use:
- `winning_hooks read_new=false`
- `amazon_metric metric=search_query_performance periods=1 grain=week top=30`
- `search_console_organic view=branded_split days=90`
- `amazon_metric metric=review_voice limit=50`
- `meta_metric metric=ad_comment_themes days=90`
- `brand_facts`

Steps:
1. Pick one product.
2. Call `winning_hooks` with `read_new=false`. It spends nothing and gives the opening lines of the top ads with their spend and return.
3. Tag each top hook to one of the five stages and add up spend per stage. The gap is the stage with the least spend.
4. Call `amazon_metric metric=search_query_performance periods=1 grain=week top=30`. Read `nonbranded_top` and `top_opportunities` for problem words and product words.
5. Call `search_console_organic view=branded_split days=90`. Use the non-branded terms only.
6. Call `amazon_metric metric=review_voice limit=50` for the language buyers use.
7. Call `meta_metric metric=ad_comment_themes days=90` for the doubts people raise under the ads. These are the objections to answer.
8. Call `brand_facts` with `query` set to the product, for every claim you plan to make.
9. Write five versions: unaware (lead with a moment or story), problem aware (name the pain), solution aware (why this kind of fix), product aware (why yours, with proof), most aware (the offer).

Checks before answering:
- Each version names the stage and the words it borrowed from data.
- Every claim must match a product fact from step 8. If no fact backs it, cut the claim.
- Mark the stage your current ads miss, with the spend behind each stage from step 3.
- If the hook read has no hooks yet, say the stage gap could not be measured. Never guess it from ad names.
- If the comment read says a surface was not read, say which one. The objections then come from what was read only.
- This cannot check a claim against the ad platform's own rules. A person checks policy before the ads run.

Rounds (relook before you answer):
1. **Claim list.** Re-check every line against `brand_facts`. Fails when: any claim has no matching product fact. Fix: cut the claim.
2. **Their words.** Fails when: a version uses none of the words pulled from searches, reviews or comments. Fix: rewrite its headline from those words.
3. **Top objection.** Re-read the comment themes. Fails when: the top objection by count is answered in none of the five versions. Fix: answer it in the product aware version.
4. **Is the gap real?** Fails when: the stage called missing already has a hook in the top 10 by spend. Fix: name the next-thinnest stage instead.
5. **House voice.** Compare with the top 3 hooks from step 2. Fails when: a hook line is over twice their median word count, or opens on the brand name. Fix: cut it to their length and open on the buyer.

Output:
- One line first: the stage your ads leave out, and the share of spend each stage gets now.
- Five blocks: stage, headline, 40-word body, hook line for video, where it runs, and the objection it answers.
- One line: run all five at equal budget, judge each after 3x the keep cost per sale, on thumb-stop first and cost per sale second. Thumb-stop is the share of viewers who watch past the first 3 seconds.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never copy text from any book or course. Write in plain words.
- Never write a disease or cavity claim, even if an old ad used one.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-awareness-ladder-copy". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
