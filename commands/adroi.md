---
description: "Which Meta ads lose or make money: Ad sets and ads losing money, ads ready for more budget, and what to watch, each with its cost per sale against the most you can pay for a sale"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Which Meta ads lose or make money

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which Meta ads lose or make money" (id: meta-ad-returns, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads Meta directly, so it is current to the hour, and puts every live ad set and ad that buys website sales against the brand's own money lines.
Each gets a verdict: losing, winning, fine, watch, too early, or no keep line. Fine means under the keep line, but not far enough under it to add budget. It is the same read as the four-hourly ROI alerts and the Ad returns page.
Ad sets that send people to Amazon are left out and counted, because Meta cannot see their sales.

What to read: Live Meta ad sets and ads that buy website sales, with spend and sales over the last 3 and 7 closed days, against the brand's own money lines
What to give me: Ad sets and ads losing money, ads ready for more budget, and what to watch, each with its cost per sale against the most you can pay for a sale

Synthesis tools to use:
- `cost_rules for=meta-ad-returns`
- `meta_metric metric=ad_returns`
- `meta_metric metric=creative_action_breakdown days=7`

Steps:
1. Call `meta_metric` with `metric=ad_returns` and `limit=50`.
2. If it returns status error, stop: say the Meta read failed and to try again later. Never report it as no sales.
3. For each winner, the move is to raise its own ad set budget by about 20%. Do not copy it into a big ad set, because a copy there competes with every ad and can get almost no spend. If its ad set is losing as a whole, move the ad into a small ad set of its own instead.
4. For each losing ad, call `meta_metric` with `metric=creative_action_breakdown`, `ad_id` set to that ad and `days=7`. Divide purchase value by purchases for its order value.

Checks before answering:
- Use the verdicts as the server decided them. "Too early" is not losing.
- If the brand has no money lines, show spend, sales and cost per sale only, and say the lines need to be set. Never borrow another brand's lines.
- Say how many ad sets were left out as Amazon-bound.
- The windows are closed days ending yesterday. Today is not in it.
- The verdicts judge cost per sale only. They ignore order size and margin. An ad at a high cost per sale with a big order can still make money, and a "fine" ad with a small order can lose. Say this when an order value is far from the others.
- A verdict on a handful of sales is shaky. On 4 sales the true cost per sale could be less than half or more than double. Say how many sales each losing call rests on.
- Ad sets switched off during the window are not in the totals, even if they spent. Say the totals cover live ad sets only.
- The order value comes from the synced table, which runs a day behind the live read. Say so. Ad sets get no order value here. Say that plainly.
- If the result says status ok, it is a full answer, even if it also carries a gated or no-data stamp.

Rounds (relook before you answer):
1. **Second window.** Put each verdict's 7-day figures beside its own 3-day columns, `last3_spend` and `last3_sales`. Fails when: a winner or fine row pays over 1.5x its keep line a sale in the last 3 days, or a loser sold at or under the line in them. Fix: mark it "turning", hold its move and say which window the call rests on.
2. **Argue the losing case.** For each ad ready for more budget, write the case against it: how many sales, how many days live, and its share of its ad set's spend. Fails when: it rests on fewer than 4 sales, or most of its sales came in the last 3 days of a 7-day read. Fix: move it to watch.
3. **Profit, not cost per sale.** Set each named ad's cost per sale against its order value from step 4. Fails when: the cost per sale is over half the order value (the house default; the brand's own profit kept per order overrides it). Fix: say it loses money on the first order even if the verdict says fine.
4. **Starved, not judged.** Read every ad set's spend in the result. Fails when: one ad set takes over half of all spend while a newer ad set spent under $5 in 3 days. Fix: list the newer one as starved, not losing.
5. **Ties to the total.** Add up the ad set spend. Fails when: it differs from the total spend by more than 5%, or ad sets were left out as Amazon-bound and the answer does not count them. Fix: state the gap and the count. Amazon-bound ads are judged by the Meta-to-Amazon keep and cut shortcut, not here.

Output:
- One line first: spend, sales and cost per sale over 7 days, against the keep line.
- Losing: each ad set or ad, its spend, sales, the line it crossed and its order value, with one move.
- Ready for more budget: each ad with its cost per sale, sales and the budget move from step 3.
- Watch: one line.
- Under 15 lines in total.

Never:
- Never change budgets or switch ads off. A person does that.
- Never call an Amazon-bound ad set losing on Meta's own sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-ad-returns". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
