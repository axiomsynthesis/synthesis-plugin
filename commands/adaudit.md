---
description: "Audit my whole Meta account: One change list ranked by money at stake: each ad or ad set by name and id, what it is now, what to change, the undo"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Audit my whole Meta account

Channel: Meta · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Audit my whole Meta account" (id: meta-whole-account-audit, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads the whole live Meta account and hands over one change list.
It covers placements, links, duplicates, who the spend really reaches, and return by ad for ads that send people to Amazon.
It changes nothing. Each change on the list is then made one yes at a time, with the budget or switch-on-off automations.

What to read: Every live Meta ad: placements, links and tracking tags, duplicates across campaigns, who the money really reaches, and return by ad for ads that send people to Amazon
What to give me: One change list ranked by money at stake: each ad or ad set by name and id, what it is now, what to change, the undo

Synthesis tools to use:
- `cost_rules for=meta-whole-account-audit`
- `ad_health_check only=[meta]`
- `meta_metric metric=ad_destinations`
- `meta_metric metric=breakdown dimension=age_gender`
- `meta_metric metric=amazon_ads`
- `meta_metric metric=ad_returns`

Steps:
1. Ask which account (your own or an agency's) and which lens, if not all: placements, links, returns or structure.
2. Call `ad_health_check` with `only=["meta"]` for the account-level checks and their dollars at stake.
3. Call `meta_metric` with `metric=ad_destinations`, `active_only=true` and `days=14` for links. It covers the top 40 spenders only, so say how much spend that is. Flag site-bound and Amazon-bound ads mixed in one ad set.
4. For each live campaign, call `ad_health_check` with `ads={"campaign_id": "<id>"}` and `only=["placement_fit","tracking_tags"]`. Flag tall-only videos and links with no tags.
5. Call `meta_metric` with `metric=breakdown` and `dimension=age_gender`. It is all-time and takes no days, so say so. Recent reach is could not check.
6. Call `meta_metric` with `metric=amazon_ads` and page with `result_page`. Ask the bar per product, default 1.0 on `roi_after_bonus`. This week and `roas_last_week` must both miss before a cut. Amazon credits sales for 14 days, so re-read new ads later. Leave out the "Ads not linked to Amazon yet" line and big sale days.
7. Call `meta_metric` with `metric=ad_returns` and `limit=50` for site-bound winners and losers. Page with `result_page` until every ad is read.
8. Find the same ad running in more than one campaign. One ad should live in one campaign. A copy in an agency's campaign may be on purpose, so mark it for the agency's word. An ad with no name or campaign is checked in Ads Manager.
9. For each site-bound campaign, set cost per sale against order value. House defaults, overridable: cost per sale under half the order value, click-through 3% or more, cost per click under $1.50. Name which part fails: the ad (clicks), the page (sales per visit) or the order size.
10. Write one row per change: ad or ad set name and id, now, proposed, money at stake a week, undo. Agency bills for creators are a cost of their own, outside Meta spend.

Checks before answering:
- Totals tie to the account's spend for the same window. Never mix a 7-day and a 14-day total. Say the gap.
- A large read can hit Meta's reading limit. A read that failed or came back partial is "could not check", never "nothing found".
- An empty Amazon return read can mean the attribution link is missing. Say which.
- Same-day video numbers are still filling in. Use closed days.
- Safe test: nothing is written, so a test run is the same read. Run it on one ad account first if asked.
- Spend check: every proposed raise or switch-on shows its added daily spend. The list never raises total spend without saying so.
- An agency's own return figure may use a different formula. Compare like with like.

Rounds (relook before you answer):
1. **Money moves, it does not vanish.** For each cut, check its ad set's budget. Fails when: a row counts savings from switching ads off but leaves the ad set budget the same. Fix: pair it with a budget cut, or count the saving as $0, since Meta moves the money to the other ads.
2. **Starved, not judged.** From `ad_returns`, find ad sets where a few ads take the money. Fails when: in an ad set with 10 or more ads, the top 5 take over 60% of spend. Fix: add a row to give the new ads an ad set of their own.
3. **Second window.** Re-read every cut row on the other window: 7 days if it was judged on 14, or 14 if on 7. Fails when: a row's call flips. Fix: drop it to watch.
4. **Like with like.** Set each agency return figure beside ours for the same days and the same formula. Fails when: the two differ by more than 10%. Fix: show both and say which formula each uses before any row rests on it.
5. **Would a second account break this?** Re-read the list for any line that assumes one brand's products, pages or limits. Fails when: a row uses a keep line, bar or page the brand never set. Fix: ask for the brand's own, or mark the row unjudged. Amazon-bound keep and cut calls go to the Meta-to-Amazon keep and cut shortcut.

Output:
- One line first: live ads read, spend covered, and money a week at stake on the list.
- The change list, ranked by money at stake, about 5 to 15 rows.
- What could not be checked, one line each.
- Next step: which rows to send to the budget or switch-on-off automation first.

Never:
- Never change anything in the account. This one only reads.
- Never change an agency's account without a yes from the person.
- Never cut an Amazon-bound ad on Meta's own sales figure.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-whole-account-audit". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
