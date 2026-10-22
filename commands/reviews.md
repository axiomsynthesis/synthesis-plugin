---
description: "Turn reviews into selling lines: What buyers love and complain about, written as FAQ answers, listing bullets and ad angles in their own words"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Turn reviews into selling lines

Channel: Customers · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Turn reviews into selling lines" (id: customers-review-mining, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Turns your reviews into words you can use. It finds the top praise and complaints, then writes FAQ answers, listing bullets and ad angles in your buyers' own words.

What to read: Reviews
What to give me: What buyers love and complain about, written as FAQ answers, listing bullets and ad angles in their own words

Synthesis tools to use:
- `find_product`
- `amazon_metric metric=review_voice`
- `review_themes`
- `amazon_metric metric=rating_watch`
- `amazon_metric metric=search_competitors grain=week`
- `competitor_review_voice limit=40`
- `export_docx`
- `brand_facts`

Steps:
1. Use `find_product` to pick your top products and their IDs.
2. Call `amazon_metric` with `metric=review_voice`, each `asin` and `limit=200` for the review text. Run it once per product family, and check a second product. It already returns topic counts, praise or complaint, quotes and a themes block.
3. Use `review_themes` only if raw review text with star ratings is available. The quotes from step 2 carry no ratings, so it adds nothing to them.
4. Call `amazon_metric` with `metric=rating_watch` and `days=90` to see whether any theme moved the star rating.
5. Call `amazon_metric` with `metric=search_competitors` and `grain=week` to name the two rivals that contest most of your searches. Call `competitor_review_voice` with each rival's `asin` and `limit=40`. Mark each theme as ours only, shared with rivals, or a rival weakness. A shared complaint is a category problem, not your fault.
6. Write FAQ answers, bullets and ad angles from the top themes. Ad angles come first from rival weaknesses you do not share.
7. If the person asks for a file, call `export_docx` with `filename=review_mining.docx`. Otherwise show the table and lines in chat.

Checks before answering:
- Every line must trace to real reviews. Show the count behind each theme.
- If reviews come back empty, say so. Never write lines from a guess of what buyers say.
- A theme in one or two reviews is not a theme.
- The review read covers a small part of all reviews, and few carry a star rating. Say how many it read. It cannot rank complaints by their effect on the rating yet, because Amazon's topic score is the same for praise and complaint. Rank by count only, and say so.
- Rival reviews exist only for products on your rival watch list. If a rival returns nothing, say so.
- Rival reviews are Amazon's featured few, not a sample. Use their words, never their counts or shares.

Rounds (relook before you answer):
1. **Count behind each line.** Re-read the theme table. Fails when: any FAQ, bullet, reason or angle traces to under 3 reviews. Fix: cut it or merge it into a bigger theme.
2. **Complaints answered head-on.** Fails when: any of the top 3 complaints by count has no direct answer in the FAQ or the five reasons. Fix: write the answer in the buyer's words.
3. **Claim check.** Call `brand_facts` for each line. Fails when: a line states a result or benefit no brand fact backs. Fix: cut the claim, keep the feeling.
4. **Second product.** Re-run step 2 on another product family. Fails when: a theme called brand-wide shows up on only one product. Fix: label it for that product only.
5. **Rival lens.** Fails when: a "rival weakness" angle is also one of our own top 5 complaints. Fix: drop the angle, it invites the same attack.

Output:
- One line first: the strongest ad angle and the complaint to fix first.
- A theme table: theme, praise or complaint, reviews, ours only or shared or rival weakness, a short quote.
- Ready-to-use lines: five FAQ answers, five listing bullets, five ad angles.
- Five reasons to switch, for a landing page: the top praise as reasons, and the top 2 complaints answered head-on, each with its review count.
- A Word file named `review_mining.docx`, two pages at most, only if asked.
- A person edits and publishes them.

Never:
- Never post or change a listing, ad or FAQ. A person does that.
- Never turn a review into a health or results claim the brand cannot prove.
- Never quote a reviewer's name.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-review-mining". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
