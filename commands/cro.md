---
description: "Ideas to make a landing page sell more, and the next test: A ranked list of page changes, from headline and buy box to fonts and colours, each with its likely lift, cost and how to test it, then a phone mock-up of the top one ready for a split test"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Ideas to make a landing page sell more, and the next test

Channel: Website · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Ideas to make a landing page sell more, and the next test" (id: website-cro-test-ideas, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads one landing page as a phone shopper sees it, ranks every change worth testing by profit per visitor times confidence, and hands over the top one ready to run.
House rules, as defaults: what removes a decision wins. One change at a time. The phone first screen matters most: on one live brand 6 in 10 buyers bought from the top box.

What to read: The live page on a phone, its visitors and profit per visitor, scroll and click maps, past test results, pack costs, reviews and approved claims
What to give me: A ranked list of page changes, from headline and buy box to fonts and colours, each with its likely lift, cost and how to test it, then a phone mock-up of the top one ready for a split test

Synthesis tools to use:
- `cost_rules for=website-cro-test-ideas`
- `recall_decisions`
- `brand_brain action=moves`
- `shopify_metric metric=profit`
- `ga4_metric metric=landing_pages days=28`
- `meta_metric metric=ad_destinations days=28`
- `web_fetch`
- `shopify_metric metric=aov_levers months=3`
- `amazon_metric metric=review_voice limit=12`
- `operator_inputs section=cogs`
- `first_order_contribution_margin`
- `brand_facts`
- `measurable_test direction=higher_is_better`
- `get_skill`

Steps:
1. Past tests. Call `recall_decisions`, then `brand_brain` with `action=moves`, `kind=ads` and `since` 60 days ago: a campaign named for this page or a split is a past test. If neither shows one, ask for the split-test app's history: an empty log is not "no past tests". Ask the page link and the saved profit per visitor goal. None saved: ask once, else grade against break-even.
2. Money. Call `shopify_metric` with `metric=profit` for last month and for this month to date: profit and ad cost per paid visit, website ad spend. If this month's ad spend is over twice last month's, lead with this month as a part month. Call `meta_metric` with `metric=ad_destinations` and `days=28` only to find this page's ads: it lists the top 40, so its totals are not website spend.
3. Visitors. Call `ga4_metric` with `metric=landing_pages` and `days=28`. If not connected, use the split-test app's or Shopify's count and say which.
4. Read the page. Call `web_fetch` on the link. View it 390 wide or ask for a phone screenshot. Note the first screen: headline, image, price, default pack, button, proof.
5. Maps. Ask for the heatmap's scroll and click maps: who leaves before the buy box, dead clicks.
6. Basket. Call `shopify_metric` with `metric=aov_levers` and `months=3`. Call `operator_inputs` with `section=cogs`, then `first_order_contribution_margin` per pack with `price`, `cogs` for the whole pack, and `misc` = shipping cost minus shipping the shopper pays per order. Name the pack with the most profit per order.
7. Doubts. Call `amazon_metric` with `metric=review_voice`, `sentiment=negative` and `limit=12`. An unanswered top doubt is an idea.
8. Claims. Call `brand_facts` with `query=claim`. Flag every claim on the live page that no fact backs, or that a fact marks open, disputed or banned. Each is a must-fix before any test.
9. The list. One idea or more per area: headline, buy box and default pack, price display, offer, copy, fonts, colours, images, proof, speed, checkout. Each: change, lift range in profit per visitor, build cost, confidence, and the test: `get_skill` with `name=/splittest`, or `name=/pagetest` for a new page.
10. Confidence: high when this page's own past test backs it, medium for a house rule or a map finding, low otherwise. Score = profit per visitor x middle of lift x 0.8, 0.5 or 0.2.
11. Mock up the top idea on the phone first screen beside today's, in the browser only.
12. Size it: visitors a side = 16 x p x (1 - p) / d squared, 2 full weeks at least. If it crosses a big sale (Prime days, Black Friday), end before it or leave those days out. Call `measurable_test` with the claim, profit per visitor, the read date and `direction=higher_is_better`. Hand it to `get_skill` with `name=/splittest`.

Checks before answering:
- An idea below the first screen reaches only shoppers who scroll. Cut its lift by that share.
- A gift or pack with no cost cannot be ranked. Ask. Never assume a cost.
- Speed: use real phone load time, not a lab score.
- Never stack two ideas into one test.

Rounds (relook before you answer):
1. **Profit, not buy rate.** Re-score the top 3 with pack and gift costs. Fails when: an idea ranks top on buy rate but its profit per order falls more than the buy rate rises. Fix: re-rank.
2. **Already tested.** Re-read step 1's two sources. Fails when: a top-5 idea repeats a past loser with no reason it would now win, or the move log shows a test on this page whose result is not logged. Fix: drop it, or cut it to low confidence and ask for that result.
3. **First screen.** Re-read step 4 at 390 wide. Fails when: the top idea changes nothing seen before scrolling, while a first-screen idea scored within 20% of it. Fix: lead with the first-screen idea.
4. **Removes or adds a decision.** Fails when: the top idea adds a choice and no past test on this page backs it. Fix: swap in the best idea that removes one.
5. **Enough visitors.** Re-check step 12. Fails when: the test needs over 6 weeks at today's visitors, or its window holds a big sale. Fix: a bigger expected lift, a Meta page test, or end before the sale.
6. **Overlap.** Call `brand_brain` with `action=moves` and `since` 30 days ago, then ask. Fails when: a campaign or split names this page, or another test touches its buy box or first screen. Fix: queue behind that test's read date.
7. **Ready to run.** Fails when: the top idea lacks its mock-up, shortcut, split, days, metric, winner line or dollars a month. Fix: add it.

Output:
- First line: profit per visitor today against the goal or break-even, and the next test with its read date.
- Ranked table: idea, area, lift range, build cost, confidence, score, how to test. Top 10.
- Must-fix claims. The mock-up beside today's.
- The next action: shortcut, 50/50, days, profit per visitor, winner line, dollars a month = gain per visitor x monthly visitors. What was not checked.

Never:
- Never change the live page, theme or prices.
- Never invent a lift from nothing. Say the evidence behind every range.
- Never use a claim that is not in `brand_facts`.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-cro-test-ideas". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
