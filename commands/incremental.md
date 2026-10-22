---
description: "Are your ads buying sales you'd get anyway?: Products where ads likely buy sales you would get anyway or cost more than they earn, with a test"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Are your ads buying sales you'd get anyway?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are your ads buying sales you'd get anyway?" (id: mkt-amazon-ads-incrementality-by-product, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
High ad-credited sales can mean ads are working. It can also mean ads are paying for buyers who were already looking for you, or bidding more than the product can afford.
This first checks which of the two fits this account. Then it shortlists products and sets up a small test to find out.

What to read: Ad-credited sales against total sales for each product, branded and non-branded ad spend, and organic sales over time
What to give me: Products where ads likely buy sales you would get anyway or cost more than they earn, with a test

Synthesis tools to use:
- `cost_rules for=mkt-amazon-ads-incrementality-by-product`
- `amazon_metric metric=ppc_branded_split start_date=YYYY-MM-DD end_date=YYYY-MM-DD`
- `amazon_metric metric=ppc_organic_vs_paid days=60 limit=30`
- `amazon_metric metric=breakeven_acos_ltv months=3 limit=30`
- `amazon_metric metric=velocity_momentum weeks=16 limit=30`
- `measurable_test`
- `amazon_metric metric=ppc_trend weeks=26`
- `amazon_metric metric=attribution_publishers days=60`

Steps:
1. Call `amazon_metric metric=ppc_branded_split start_date=YYYY-MM-DD end_date=YYYY-MM-DD` for the 60 days ending 30 days ago, so ad-credited sales have landed. Say which dates you used. Note branded spend as a share of all ad spend.
2. Call `amazon_metric metric=ppc_organic_vs_paid days=60 limit=30`. Note each product's paid share of units, its `acos` (ad spend over ad-credited sales, as a fraction) and its spend.
3. Call `amazon_metric metric=breakeven_acos_ltv months=3 limit=30` for each product's first-order break-even ad cost share. It comes as a percent, so multiply `acos` by 100 before comparing.
4. Pick the test. If branded is 15% of spend or more, shortlist products with high paid share and heavy branded spend. If branded is under 15%, the waste is not on your own name: shortlist products whose `acos` is above break-even, largest spend first.
5. Call `amazon_metric metric=velocity_momentum weeks=16 limit=30` to look for past weeks when ads dropped and total units held.
6. Shortlist up to 3 products. For each, design one test with `measurable_test`: the cut, the window, and the total units level that would prove ads were needed.

Checks before answering:
- Organic units are total minus ad-credited. That is a floor, not a measurement. Say so.
- The branded split is account-wide. It cannot be read per product yet, so never write a branded share for one product.
- The product read cannot yet be set to a mature window. Its newest 30 days are still collecting ad-credited sales, so `acos` reads high and paid share reads low there. Say so.
- The momentum data has no ad spend beside it. A week where units held is a hint that ads dropped, not proof.
- A product with paid share over 100% means double counting across sizes. Read it at parent level instead.
- Promo weeks are flagged in the momentum data. Never use one as the "before" in a comparison.
- The test tool writes the plan in words. It cannot yet size the test from weekly swings in units, so say the thresholds are a judgment.
- Never call ads wasted on this read alone. It points to a test, not a verdict.

Rounds (relook before you answer):
1. **Outside traffic.** Call `amazon_metric` with `metric=attribution_publishers` and `days=60`. Fails when: ads off Amazon, such as Meta or TikTok, sent shoppers who bought on Amazon in the window while own-name ad spend rose. Those shoppers search your name and Amazon ads claim them. Fix: say own-name ad credit is partly bought by the outside ads, and never count it as earned by Amazon ads.
2. **Natural test.** Call `amazon_metric` with `metric=ppc_trend` and `weeks=26`. Find weeks where ad spend fell 30% or more against the 4 weeks before, with no sale event. Fails when: total units fell more than the product's paid share would predict. Fix: the ads were needed there, so drop that product from the shortlist.
3. **Repeat value.** Fails when: a shortlisted product is above its first-order break-even but at or under its 3-month value from step 3. Fix: take it off the cut list, or test a smaller cut.
4. **Can the test see it?** From step 5, take the normal week-to-week swing in total units for each product. Fails when: the test's failure line is smaller than that swing. Fix: lengthen the test to 6 weeks or deepen the cut, and say the thresholds are a judgment.
5. **One test per product.** Fails when: a price move, deal or other ad test sits on a shortlisted product in the test weeks. Fix: move the start date past it.

Output:
- One line: which problem this account has, branded buying or bids above break-even, how many products, and the monthly spend at stake.
- A table: product, paid share of units, ACoS vs break-even, spend, evidence from past weeks.
- One test per shortlisted product: change, length, success and failure thresholds.

Never:
- Never pause or cut ads in the account.
- Never present the organic figure as measured.
- Never run more than one test on the same product at once.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-ads-incrementality-by-product". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
