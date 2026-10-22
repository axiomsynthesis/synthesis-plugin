---
description: "New landing page, start to finish: A five-reasons page built from your reviews and searches and revised over several versions, every claim and price proved, then tested on Meta in its own campaign after your yes, and called keep, kill or next version"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# New landing page, start to finish

Channel: Website · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "New landing page, start to finish" (id: website-new-page-start-to-finish, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs the whole new-page job, from the page it must beat to the keep or kill call. Reasons come from buyers' complaints and shoppers' searches, claims only from the approved list, and the page is revised in rounds before any test spends.

What to read: Your best current page, your reviews, what shoppers search for, your approved claims, creator videos, pack costs and cart prices, your proven Meta ads
What to give me: A five-reasons page built from your reviews and searches and revised over several versions, every claim and price proved, then tested on Meta in its own campaign after your yes, and called keep, kill or next version

Synthesis tools to use:
- `cost_rules for=website-new-page-start-to-finish`
- `recall_decisions`
- `brand_brain action=moves`
- `ga4_metric metric=landing_pages days=28`
- `meta_metric metric=ad_destinations days=28`
- `web_fetch`
- `amazon_metric metric=review_voice limit=20`
- `amazon_metric metric=search_query_performance scope=nonbranded grain=month`
- `brand_facts`
- `first_order_contribution_margin`
- `amazon_metric metric=buybox_watch`
- `get_skill`
- `log_decision kind=campaign`

Steps:
1. Call `recall_decisions` for an earlier run, and `brand_brain` with `action=moves` and `since` 30 days ago for tests on its pages. Daily test budget and days come from saved decisions. Ask once: product, page to beat, and budget or days not saved (default $100 a day, 10 days, this run only).
2. The bar. Call `ga4_metric` with `metric=landing_pages` and `days=28`, and `meta_metric` with `metric=ad_destinations` and `days=28`. Name the page to beat, its sales per visitor and its Meta cost per sale. Read it with `web_fetch`: its format, every pack price, default pack, guarantee and gifts. If it is already the format you planned, say so and test its default pack or offer instead.
3. Reviews, the /reviews job. Call `amazon_metric` with `metric=review_voice` and `sentiment=negative`, then `sentiment=positive`. Top 5 complaints and praises, with counts and one real quote each. No marketplace: ask for site reviews.
4. Angle, the /ideas read. Call `amazon_metric` with `metric=search_query_performance`, `scope=nonbranded`, `grain=month`, `periods=1`, `top=40` and `min_volume=5000`, and read every result page until none is left. Lead with the most searched pain matching a complaint.
5. Draft five reasons. Default headline "5 reasons to switch to" the product. Each answers a top complaint, proved by a real number or dated review. Claims only from `brand_facts`, never one another fact marks open or disputed: search it with `query=clinical` and `query=open` first. Buy button after reasons 1 and 4. Order: offer bar, hero with buy box, proof, reasons, reviews and videos, FAQ, final buy box, sticky phone bar.
6. Videos. For every creator video, watch it or ask for its script, and list every on-screen and spoken claim. A claim not in `brand_facts` cuts the video. Say which videos no one checked.
7. Build, the /landingpage job. Call `get_skill` with `name=/landingpage` and follow it. For a version of a live page use `name=/pagelive`. Never edit the page being beaten.
8. Prices. Read every pack's page price with `web_fetch` on the live page, then check the cart against it in the browser, with and without each add-on. Call `amazon_metric` with `metric=buybox_watch`: show any pack sold cheaper on the marketplace. Call `first_order_contribution_margin` per pack with `price`, `cogs` (one unit's cost times units in the pack), `misc` and `cac` at today's Meta cost per sale.
9. Run the Rounds. Each round that changes the page makes a new version. Show preview, versions and test plan. Wait for a yes to the page and to the total dollars.
10. Test, the /pagetest job. Call `get_skill` with `name=/pagetest` and follow it: own campaign, the same top ads as the page being beaten.
11. First look day 3 or 4: stop only a disaster, like twice the order value spent with no sale. Call at $700 to $1,000 spent with `get_skill` and `name=/testread`: keep, kill or next version. Call `log_decision` with `kind=campaign`, the page, the call, `measure` and `made_on`.

Checks before answering:
- Safe test run: build only on the hidden preview theme and leave the Meta test built but off.
- A claim in a creator video is our claim. No unproven health claim, rival names or fear claims.
- A crossed-out price must be a real earlier price. A gift or pack with no cost: ask.
- Never test on the page being beaten or its template, or run an on-site split on it during the Meta test.
- A small test campaign catches disasters, not close calls: on one live brand the same page cost twice as much per sale there.
- Closed days only. If the test window crosses a big sale (Prime days, Black Friday), move it or label those days.

Rounds (relook before you answer):
1. **Complaint coverage.** Re-read `review_voice` with `sentiment=negative`. Fails when: one of the top 3 complaints by mentions has no reason answering it. Fix: rewrite or swap a reason.
2. **Claim audit.** Every line, caption and video line against `brand_facts`. Fails when: a claim has no matching fact, or a fact marks it open. Fix: cut the line or video.
3. **Angle.** Re-read the searches. Fails when: a search tied to a top complaint has 3 times the volume of the one the headline leads with. Fix: lead with that pain. If not every result page was read, write "not checked", never a pass.
4. **Phone first screen.** Preview 360 wide. Fails when: price, default pack and buy button are not all visible before scrolling, or the page scrolls sideways. No browser or screenshot: write "not checked", never a pass.
5. **Money and prices.** Re-run the cart check and margins. Fails when: a cart price differs from the page by a cent, a pack costs more than on the marketplace with no stated reason, or the default pack keeps less than today's Meta cost per sale. Fix: test the default pack before a new page, or stop.
6. **Argue for the old page.** Read the page being beaten beside the new one. Fails when: the old page has a proof, guarantee or offer the new one dropped. Fix: put it back.

Output:
- First line: version number, angle, product, the page it must beat.
- Five reasons, one line each with the complaint it answers. Prices proved, one line per pack.
- The test: campaign, budget, end, first look and call dates. What was not checked. Under 25 lines.

Never:
- Never put a claim on the page, or in a video on it, that is not in `brand_facts`.
- Never switch the test on before the page is live and the person said yes to the dollars.
- Never call a winner from a close margin in a small test.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-new-page-start-to-finish". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
