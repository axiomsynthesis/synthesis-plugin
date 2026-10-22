---
description: "Turn approved Trybe videos into Meta ads for me: Each approved video built into a Meta ad in the right product's ad set, creator tag kept, launched paused and then switched on, every ad read back"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Turn approved Trybe videos into Meta ads for me

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Turn approved Trybe videos into Meta ads for me" (id: do-trybe-build-creator-ads, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds approved Trybe creator videos into Meta ads, using Trybe's own Build Ads screen.
It sorts each video by the product it shows and builds it into your existing creator test campaign.
It launches paused, checks every ad, then switches them on.

What to read: Newly approved Trybe creator videos and their scripts, your existing creator test campaign, and each new ad read back live after launch
What to give me: Each approved video built into a Meta ad in the right product's ad set, creator tag kept, launched paused and then switched on, every ad read back

Synthesis tools to use:
- `cost_rules for=do-trybe-build-creator-ads`
- `trybe_creator_program view=performance days=30`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. Ask which submissions, or "all newly approved", and the daily budget for each new ad set. House defaults the brand can override: about $50 a day per batch, at most 3 test batches live, off at about 2x the order value spent with no sale, each test set closed after 7 days. Winners move up through do-meta-graduate-winners.
2. Ask the house setup. Default: build into the existing creator test campaign, not a new one. Copy the house text and headline from your live creator ads in Ads Manager. Read each target ad set's end date with `ad_health_check`, `ads={"adset_id": "<id>"}` and `only=["schedule_budget"]`. If it ends within 7 days, build into a new ad set with a later end date.
3. Call `trybe_creator_program` with `view=performance` and `days=30` for program totals. It lists no videos. The approved list comes from Trybe, Submissions.
4. In the browser, open Trybe, Submissions. Open each video and read its script. Watch it and sort it by the product it shows. A video for a product with no ad set yet is held.
5. Show the plan: each video, its product, its target ad set, and every new ad set's budget. Wait for the yes on new budgets.
6. In Build Ads, select the videos. Leave about 400 ms between row clicks. The header box selects every row.
7. Configure: copy the existing ad set for that product. A copy keeps the old end date and every ad in it, so set the end date now and delete down to the new videos. Identity: the brand's own page. Name template: keep trybe=<id> in every ad name, because the creator is paid by it. End each name "- Claude".
8. Copy: the house text and headline. Landing page: the product's page. Ask the link tags. Keep trybe=<id> in the link too. Default: utm_source=facebook, utm_medium=paid_social, utm_campaign={{campaign.name}}, utm_content={{ad.name}}.
9. Give each video a 4:5 feed version. Turn the Shop destination off. Choose Launch as Paused. Each build takes about 30 seconds. Clicks are ignored while one says "Setting up".
10. In Ads Manager, check every copied end date reads the agreed date before publishing. A missed one stops spend with no error.
11. Publish each ad from its own preview. Batch review wrongly flags tall videos as Stories only.
12. Keep the Meta tab in front while it works. Hidden tabs slow down.
13. Switch on only the new ads. Paused copies already in the ad set stay off. Check every ad set row, not just the campaign. A batch can arrive with an ad set "Ads off".
14. Call `ad_health_check` with `ads={"adset_id": "<new ad set>"}` and find each new ad by its trybe=<id>. It checks links, tags, switches, end dates and shape. Trybe's own ad count is not proof an ad ran.
15. Call `log_decision` with `kind=campaign`, the ads built, and the date to judge them.

Checks before answering:
- Every approved video is either built in the right product's ad set or listed as held, with why.
- Every new ad name keeps trybe=<id>.
- Spend check: state each new ad set's daily budget and the new daily total for the campaign. Never above what was approved.
- Safe test, when asked for one: build one video with Launch as Paused and stop there. Read it back by its trybe=<id>.
- Tomorrow, every new ad set should show spend above $0.

Rounds (relook before you answer):
1. **Product, script then video.** For each video, read the script, then watch it. Fails when: the script and the video show different products, or the target ad set's page sells another product. Fix: hold it and say why.
2. **Claims frame by frame.** Fails when: any spoken or on-screen line makes a claim the brand's live ads do not make. Fix: hold the video and quote the line.
3. **Caps.** Count live test batches and new daily spend. Fails when: more than 3 test batches would be live, or the new daily total is over the approved ceiling. Fix: build paused and ask.
4. **Creator tag.** Read every new ad name and link. Fails when: any lacks trybe=<id>. Fix: add it before switch-on, or the creator is not paid.
5. **Did the money reach them.** After a full closed day, read the new ad sets. Fails when: a set or a video in it shows $0 spend. Fix: say it is starved; a daily creator loop shortcut handles the ongoing promote and cut.

Output:
- One line first: videos built, held, and the new daily spend live.
- One row per ad: creator, product, ad set, status read back.
- Anything that differs from the plan.

Never:
- Never put a product's video into another product's ad set.
- Never drop the trybe=<id> tag from a name.
- Never start a new campaign when the person asked for the existing one.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-trybe-build-creator-ads". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
