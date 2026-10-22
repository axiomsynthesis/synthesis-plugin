---
description: "Profit per website visit: What each website visit earns before ads, and what a paid visit earns against what this brand's ads pay for one"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Profit per website visit

Channel: Website · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Profit per website visit" (id: website-profit-per-visitor, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Answers one question: does a visit to the website make money? A visit here is one session, so one shopper who comes back twice counts twice. It takes the website's own orders' profit after product cost, fees and shipping, divides it by the month's visits, and does the same for paid visits. It sets paid visits against what this brand's own ads pay for one. Orders another marketplace sent into the store never visited the website, so they are left out.

What to read: Website profit after product cost, fees and shipping, the website's visits, and ad spend that sends shoppers there
What to give me: What each website visit earns before ads, and what a paid visit earns against what this brand's ads pay for one

Synthesis tools to use:
- `cost_rules for=website-profit-per-visitor`
- `shopify_metric metric=profit month=YYYY-MM`

Steps:
1. Call `shopify_metric` with `metric=profit` and `month=` set to last month, and again for the month before.
2. Read `profit_per_visitor`, `visitors`, `own_store_profit`, `visitors_note` and `profit_per_visitor_note` for each month.
3. If `profit_per_visitor` is missing, say why from `visitors_note` or `no_headline_reason`, and stop.
4. Read `paid_visitors`, `profit_per_paid_visitor`, `website_ad_spend`, `ad_cost_per_paid_visit` and `ad_cost_per_ad_click`. `website_ad_spend` is Meta, Google and TikTok spend that points at the website. If `ad_cost_per_paid_visit` is missing, give the reason in `paid_note` and use `ad_cost_per_ad_click`, saying clicks run above visits so it reads low. If both are missing, give no gap.
5. Compare `profit_per_paid_visitor` with `ppv_marks.break_even`. That mark is this brand's own ad cost for a paid visit this month. It is not a target the owner set. Never set a budget from it alone.

Checks before answering:
- Profit per visit is before ads. Say so in the same sentence as the number.
- The tool fields say visitor, but the count is sessions. Call it a visit, never a visitor or a person.
- Visits include free ones from search, email and direct. The fair test is profit per paid visit against ad cost per paid visit. Never set ad cost against all visits.
- Paid visits are the visits tagged as paid. Profit per paid visit takes a paid order to be an average order. Say so.
- Own-site orders are split from marketplace orders order by order, with the books' shipping cost per order. If they cannot be split, there is no figure. Never guess one.
- Read `data_quality_flags`. Each cost not connected makes profit per visit read high. Name them.
- If visits cover fewer days than the month, the figure reads high. Say so.
- Subscription renewals are profit with no visit behind them. If the store sells subscriptions, say they lift the figure. This answer does not measure that lift yet.
- Use closed months.

Rounds (relook before you answer):
1. **Second month.** Re-read the month before. Fails when: the paid-visit verdict flips between the two months, or profit per visit moved more than 25%. Fix: say the call is not settled and name what changed.
2. **Missing costs.** Re-read `data_quality_flags`. Fails when: any cost is not connected, such as shipping, product cost or card fees. Fix: say which, and that profit per visit reads high by about that cost per order.
3. **Fair comparison.** Fails when: the answer sets ad cost against all visits, or uses `ad_cost_per_ad_click` without saying it reads low. Fix: compare paid visits with paid visits only.
4. **The lever is the bigger gap.** Split profit per paid visit into buy rate times profit per order. Fails when: the move named is not the one with the bigger gap to break-even. On one live brand ad visitors bought at about the same rate as a stronger rival, and the gap was order size. Fix: name the other lever.
5. **Goal, not just break-even.** Ask the owner's own target per visit. One live brand set $1.50 against about $0.82 today. Fails when: the answer calls a visit "fine" because it beats break-even while it misses the owner's target. Fix: give both gaps.

Output:
- One line first: does a paid website visit pay for what ads spend to bring it? Profit per paid visit before ads for last month against ad cost per paid visit, the gap in cents, profit per visit, and the change from the month before.
- A small table: month, visits, paid visits, website profit, profit per visit, profit per paid visit, ad cost per paid visit.
- One move: the lever that would close the gap most, with what to measure next month.

Never:
- Never count orders another marketplace sent into the store as website visits' profit.
- Never call the break-even mark the owner's target, and never use another brand's mark.
- Never change budgets or prices. A person does that.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-profit-per-visitor". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
