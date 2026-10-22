---
description: "Meta to Amazon read: A Meta to Amazon scorecard by campaign, ad set and ad over the last settled week and 28 days, with sales per $1 against each product's break-even and which ads to cut, trim, keep or scale, written so it can be sent to an outside agency"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Meta to Amazon read

Channel: Meta · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Meta to Amazon read" (id: meta-to-amazon-read, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A readout of how the brand's Meta ads sell on Amazon, ready to send to the agency that runs them.
It joins Amazon Attribution to Meta spend per ad, then rolls up to ad set and campaign.
It reads the same source, spend, weeks and bar as "Which Meta ads for Amazon to keep, cut or move up" and "Rank my videos by cost per Amazon order", so all three give one ad the same call.

What to read: Meta spend for every ad that sends shoppers to Amazon, the Amazon sales and orders Amazon Attribution credits to each ad, each ad's campaign, ad set and destination, Amazon sales by day for sale days, and product margins
What to give me: A Meta to Amazon scorecard by campaign, ad set and ad over the last settled week and 28 days, with sales per $1 against each product's break-even and which ads to cut, trim, keep or scale, written so it can be sent to an outside agency

Synthesis tools to use:
- `cost_rules for=meta-to-amazon-read`
- `meta_metric metric=amazon_ads period=weekly weeks=6`
- `meta_metric metric=ad_destinations days=28`
- `amazon_metric metric=contribution_by_asin months=3`
- `amazon_metric metric=daily_revenue`
- `meta_metric metric=weekly_trend weeks=58`
- `meta_metric metric=ad_daily_trend days=14`

Steps:
1. Call `meta_metric` with `metric=amazon_ads`, `period=weekly` and `weeks=6`. Read every `result_page`. If a week says rows kept N of M, say "ad list cut at N of M, X% of spend shown". Sales per $1 is `amazon_sales` over `spend`.
2. The result can say `gated` while its rows hold real spend, sales and orders. Then use the rows and say the stamp is wrong. Stop only when rows are empty or it says no_linked_ads.
3. Call `meta_metric` with `metric=ad_destinations` and `days=28`. It lists the top 40 ads only. Take out the "not linked to Amazon" line and any ad whose destination is dtc or walmart: the scorecard's spend includes them. Match the rest to campaign and ad set; no match goes in an "unmatched" line.
4. Call `amazon_metric` with `metric=daily_revenue` and `days=49`. A day over 1.5 times the median is a sale day (Prime, Black Friday). Settled weeks ended 14 or more days ago with no sale day. The 7-day read is the newest settled week, the 28-day read the 4 newest. The 2 newest weeks show as still settling only.
5. Call `amazon_metric` with `metric=contribution_by_asin` and `months=3`. Bar: 1 over the margin share, plus the 10% referral bonus when the result shows the brand gets it. Internal only.
6. Call `meta_metric` with `metric=weekly_trend` and `weeks=58` for last year's Amazon-bound spend only. Never set its Amazon sales beside this scorecard's: another source. No spend then: say there is no year-ago read.
7. Read saved answers in `recall_decisions`; ask once only for what is missing: agency campaigns, its bill, sale days, what the agency may see. Say a default holds for this run only.
8. Rules, as in /amazonrules: test ad (first ran in 28 days) cut at $150 with no order, too early under 3 days live. Scale at the bar on both windows with 10+ orders. Trim at 1.0 to the bar on both. Cut under 1.0 after $500 on both. Windows disagree: hold.
9. For each cut, call `meta_metric` with `metric=ad_daily_trend`, `ad_id=<id>` and `days=14`. Spend and return both climbing means hold.

Checks before answering:
- The agency's bill is its own line, never in spend or sales per $1.
- Ads sharing one Amazon link are one row.
- Say which source each number came from.

Rounds (relook before you answer):
1. **Second window.** Fails when: an ad's settled week and 28 days sit on opposite sides of the bar. Fix: hold.
2. **Still settling.** Fails when: a cut or scale rests on the 2 newest weeks. Fix: judge on settled weeks only.
3. **Bar vs margin.** Fails when: a family's bar (owner's or saved) is under its break-even from step 5. Fix: raise it and re-sort; never scale under break-even.
4. **Sale weeks out.** Fails when: a campaign's 28-day sales per $1 moves 0.2 or more with sale weeks out. Fix: lead with the number without them.
5. **Safe to send.** Fails when: the agency text shows cost, margin, break-even or profit the owner did not clear. Fix: cut them.
6. **Rollup adds up.** Fails when: campaign totals differ from ad rows plus unmatched by over 1%, or rows were cut off. Fix: find the rows, or state the share of spend shown.
7. **Full solution.** Fails when: a cut, trim or scale lacks its ad, dollars a week and what applies it. Fix: add them.

Output:
- One line first: settled week and 28-day spend, Amazon sales, orders and sales per $1.
- Campaign table, then ad sets, then ads, with the call on both windows. Then still settling, sale weeks out, last year, the agency bill.
- A send-ready summary of 3 to 5 lines the owner can paste to the agency.
- Below a line, owner only: each cut, trim, scale or hold with weekly spend, new budget and dollars a week after break-even. Name what applies it: /toggle, /budget, or the agency. Full keep and cut check: /amazonrules.
- "Not checked:" repeat buying after the first order, ad rows the tool cut off, and last year when there was no spend then.

Never:
- Never send the report. The owner does.
- Never change the agency's campaigns. The owner and the agency decide.
- Never share costs or margins outside without the owner's yes.
- Never judge an Amazon-bound ad on Meta's own sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-to-amazon-read". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
