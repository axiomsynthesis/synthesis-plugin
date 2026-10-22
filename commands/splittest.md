---
description: "Run a split test on a page: A 50/50 profit-per-visitor test on one page, set up in your split-test app after your yes, read on its date, then the winner built into the page"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Run a split test on a page

Channel: Website · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Run a split test on a page" (id: do-website-split-test, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Sets up a 50/50 split test on one page, judged on profit per visitor.
It reads the result on the agreed date, then ends the test and builds the winner into the page itself.
House rules, as defaults: test one thing at a time. A change that removes a decision tends to win; one that adds a decision tends to lose. On one live brand a 4-pack picked by default gave 23% more buyers, while a pack picker that asked a question cost 22%. A free gift can eat a paid add-on.

What to read: Your page's visitors and sales, your pack and gift costs, your split-test app's results
What to give me: A 50/50 profit-per-visitor test on one page, set up in your split-test app after your yes, read on its date, then the winner built into the page

Synthesis tools to use:
- `cost_rules for=do-website-split-test`
- `ga4_metric metric=landing_pages days=28`
- `operator_inputs section=cogs`
- `first_order_contribution_margin`
- `web_fetch`
- `measurable_test direction=higher_is_better`
- `log_decision kind=other`

Steps:
1. Ask in one message: the one big change to test, the page, start now or later. For a readout, ask which test. Say which house rule predicts the result.
2. One test per page or buy box at a time. Ask what is running, including any readout on that buy box such as an add-on take rate. Stop on an overlap, or read that readout from the control side only.
3. Call `ga4_metric` with `metric=landing_pages` and `days=28` for visitors and buy rate. If it says Google Analytics is not connected, ask for the split-test app's last test on that page or Shopify's sessions report, and say which you used. Visitors a side = 16 x p x (1 - p) divided by d squared. p is the buy rate. d is the lift to detect in points of buy rate, for example 0.013 for 6.4% to 7.7%. This sizes buy rate. Profit per visitor needs more. At least 2 full weeks. Give the read date.
4. Call `operator_inputs` with `section=cogs`. Every gift and pack needs a cost. Ask for any missing one. Never assume one. Call `first_order_contribution_margin` with `price` and `cogs`, shipping and packing per order as `misc` and `referral_fee_pct=2.9` for card fees.
5. Check the app's plan end date against the read date. If the plan or trial ends first, say so and stop. The person buys any plan.
6. The test version is built with the live page shortcut on its own template, never the control's. Call `web_fetch` on the control. Check the test version on its preview link in the browser. Both show the right prices.
7. Open the split-test app in its own tab, for example app.intelligems.io. Its window inside Shopify admin ignores clicks. At a login, ask the person to sign in. Choose a template test or a style and script test, 50/50, profit per visitor as the main metric.
8. In the app, pull product costs from Shopify, so gifts count in profit. The code editor adds closing brackets by itself. Read the code back after typing.
9. Save it as a draft. Show the setup. On a yes, press Start. If the safety check blocks Start, ask the person to press it.
10. Call `measurable_test` with the claim, the metric, the read date and `direction=higher_is_better`. Thresholds are dollars of profit per visitor, so 0.10 means 10 cents.
11. Read back after the app refreshes. The first visitors can all land in control. Load the page as several fresh visitors. Check both sides appear and the cart carries the test tag.
12. Readout: open the app's results. Report profit per visitor, buy rate and order size per side, with visitors per side. Ask; default stop early when one side is more than 30% behind on buy rate at about 1,000 visitors a side.
13. Ending: on a yes, end the test. Build the winner into the theme with the live page shortcut. Never rely on the app's own roll-out. Call `log_decision` with `kind=other`, the winner, `made_on` and `measure=page`.

Checks before answering:
- Safe test run: when the person asks to test the shortcut, create the test as a draft, never started. Read its setup back.
- Spend: the test spends nothing by itself. A paid app plan needs the person's own words to buy it. Never buy one.
- Express-pay and untagged buys may be missing from the app's counts. Say so.
- Never call a winner before the read date unless the stop rule fires.
- A lab speed warning is not proof. Check real browser timing before calling a page slower.

Rounds (relook before you answer):
1. **Enough to call.** Re-read visitors and orders per side. Fails when: the read date has not come, the stop rule has not fired, or a side has under 1,000 visitors. Fix: say "too early" and give the next read date.
2. **Profit range, not just buy rate.** Fails when: the profit per visitor range for the winner still crosses zero, even if buy rate wins. Fix: call it a lead, not a winner, and ask whether to keep running or roll out on buy rate.
3. **Store tags agree with the app.** Count store orders by the test tag for the same days. Fails when: the app's orders per side differ from tagged orders by more than 10%, or untagged express buys exceed 10% of orders. Fix: add untagged buys to the side whose page they came from, and say so.
4. **Gift and add-on costs.** Read every gift and add-on's cost in Shopify and the app. Fails when: any is $0 or blank, so the app's profit reads high. Fix: enter the cost, refresh, re-read.
5. **Free gift eats the paid add-on.** Compare the paid add-on's take on each side. Fails when: it fell by a third or more on the gift side. One live brand fell from 17.5% to 5.7%. Fix: count that lost profit in the call.
6. **Second window.** Split the test days in half. Fails when: the winner loses the later half, or its lead shrinks by half or more. Fix: keep running a week, or call it even.

Output:
- Setup: one line with the change, the page, 50/50, the metric and the read date.
- Readout: one line per side with visitors, buy rate, order size and profit per visitor.
- The call and the date the winner went into the page.

Never:
- Never run two tests on the same page or buy box.
- Never buy an app plan.
- Never roll out a winner with the app alone.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-website-split-test". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
