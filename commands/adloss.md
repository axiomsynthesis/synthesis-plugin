---
description: "Find ads that lose money after product cost: Product families whose ads lose money on the sales they are credited with, and the dollars"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Find ads that lose money after product cost

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find ads that lose money after product cost" (id: mkt-amazon-ad-profit-after-cost, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ad dashboards stop at sales. This goes to profit, and it asks what the ads themselves earn.
Ad profit is the sales the ads are credited with, times the product's profit rate before ads, minus the ad spend.
A product can make money after its ad bill and still have ads that lose money, because its organic sales pay for them. This names those ads.

What to read: Each advertised product's settled sales, Amazon fees, product cost, its ad-credited sales and its own ad spend for the last three closed months
What to give me: Product families whose ads lose money on the sales they are credited with, and the dollars

Synthesis tools to use:
- `cost_rules for=mkt-amazon-ad-profit-after-cost`
- `amazon_metric metric=ppc_profit_by_asin month=YYYY-MM limit=40`
- `amazon_metric metric=ad_spend_monthly month=YYYY-MM`
- `operator_inputs section=cogs`
- `amazon_metric metric=ppc_branded_split start_date=YYYY-MM-DD end_date=YYYY-MM-DD`
- `amazon_metric metric=breakeven_acos_ltv months=12 limit=12`

Steps:
1. Call `amazon_metric metric=ppc_profit_by_asin month=YYYY-MM limit=40` three times, once for each of the last three months whose `settlement_status.fully_settled` is true. If the newest month is still settling, show it only as the estimate range the tool returns.
2. For each product row, work out ad profit: `ad_sales` x (`contribution_before_ads` / `sales`) minus `ad_spend_reported`. Add the rows up by `family`. Compare the three months by family to see whether the loss is new or steady.
3. Call `amazon_metric metric=ad_spend_monthly month=YYYY-MM` for the latest settled month. Use its Sponsored Products and Display spend in `by_ad_product` for the spend check below.
4. Call `operator_inputs section=cogs` and list any advertised product that has no cost entered.
5. Sort families by ad dollars lost. Also work out margin after ads: `profit_after_ads` over `sales`, by family. For each losing family, give one move: cut ad spend, raise price, or stop advertising it.
6. Call `amazon_metric metric=ppc_branded_split start_date=YYYY-MM-DD end_date=YYYY-MM-DD` over the same settled months. Searches for your own name and all other searches are different jobs: never average them. On one live brand, own-name searches ran at 11.5% ad cost of sales and the rest at 61.8%. A loss almost always sits in the other searches, so the move is to cut those, not the whole family.
7. Call `amazon_metric metric=breakeven_acos_ltv months=12 limit=12`. For a product people rebuy, also compare its ad cost share with the 3-month break-even. Say which you used.

Checks before answering:
- Use a fully settled month: the latest month whose `settlement_status.fully_settled` is true. If the newest month is still settling, show it only as the estimate range the tool returns. A month that has ended but is still settling has all its ad spend and only part of its sales, so it shows false losses.
- A product that is profitable after ads can still have ads that lose money. Never call the ads fine because the product row is positive.
- Credited sales are the most the ads can claim. Some of those buyers would have bought anyway. So a loss on credited sales is a real loss, and a small ad profit may be smaller still.
- Sum `ad_spend_reported` across rows and compare it with the Sponsored Products and Display spend from `ad_spend_monthly` for the month. Say how much is unmatched. The Profit page's advertising line also holds Sponsored Brands and outside traffic sent to Amazon, so never tie to it.
- Zero is not the only line. Flag any family under 10% margin after ads as "ads eat the margin", even when it is above zero.
- A product with incomplete cost is flagged by the tool. Never call it a loser or a winner.
- One bad month is not a pattern. Use the 3-month view before recommending a stop.
- This answer cannot yet show the return on the last dollar spent, or a tested lift. Say so if someone asks whether a smaller budget would earn more.

Rounds (relook before you answer):
1. **Own name or not.** Re-read step 6. Fails when: own-name and other searches differ in ad cost share by more than 2x, or searches no rule could label hold over 10% of spend. Fix: split each losing family's move into a cut on other searches and a keep on own-name ones, and say how much spend is unlabelled.
2. **Repeat value.** Re-read step 7 for each losing family. Fails when: a family loses on the first order but sits at or under its 3-month break-even. Fix: relabel it "pays back on repeat", take it off the losers and give the months to pay back.
3. **Rank push.** Ask once whether a losing family is in a planned push for organic rank. Sometimes you lose on ads to gain organic share, but not always. Fails when: the answer is yes and the draft says stop. Fix: give a loss budget a month and an end date instead.
4. **Three months, not one.** Re-read the step 1 table. Fails when: a losing family made an ad profit in any of the three months. Fix: call it mixed, no stop, recheck next month.
5. **Outside traffic.** Ads on Meta or TikTok that send shoppers to Amazon make them search your name, and Amazon ads then claim the sale. Fails when: own-name ad spend rose over 20% month on month while those ads ran. Fix: say own-name ad credit is inflated and never count it as earned.
6. **Spend tie.** Re-check the step 3 sum. Fails when: over 10% of Sponsored Products and Display spend is unmatched to a product. Fix: put the unmatched dollars in the first line as not judged.

Output:
- One line: the dollars the ads lost last month on the sales they are credited with, and the number of families.
- A table by family: ad spend, credited sales, ad profit on credited sales, product profit after ads, margin after ads, 3-month direction, move.
- A list of advertised products with no cost entered.

Never:
- Never estimate a missing product cost.
- Never change ads or prices in any account.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-ad-profit-after-cost". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
