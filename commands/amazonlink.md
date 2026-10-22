---
description: "Make a tracked Amazon link for each ad: One tracked Amazon link per ad, on your own link address, so Amazon can credit each sale to the ad that sent it"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Make a tracked Amazon link for each ad

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Make a tracked Amazon link for each ad" (id: do-amazon-ad-link, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Makes one tracked Amazon link for each ad that sends people to Amazon. Each link sits on your own link address and carries its own Amazon Attribution tag. Amazon then credits each sale to the one ad that sent it. Putting a link into a live ad is the job of the ad launch shortcut.

What to read: Your Meta ads that send people to Amazon, the links they use today, your own link address
What to give me: One tracked Amazon link per ad, on your own link address, so Amazon can credit each sale to the ad that sent it

Synthesis tools to use:
- `cost_rules for=do-amazon-ad-link`
- `meta_metric metric=ad_destinations days=14 active_only=true`
- `create_ad_links kind=meta`
- `meta_metric metric=amazon_ads period=week`

Steps:
1. Ask the product page or its product code. Ask which ads the links are for.
2. Call `meta_metric` with `metric=ad_destinations`, `days=14` and `active_only=true`. Read every page with `result_page`. If a page holds no rows but rows are still missing, say the list is incomplete. Ask which ads to cover, or try `days=7`. Keep only ads whose `effective_status` is ACTIVE.
3. List ads that go to Amazon with no link of their own. An empty link with basis rule or inference has no link Synthesis can see. List it as needs a link, never as shared. Links shared by two or more ads go on a second list.
4. An ad with no name cannot get a link. Say to name it in Ads Manager first.
5. Build one row per ad: creator handle or short ad name, month, year, version and product. Read the product from the old link's last word, like twopacknha or 9pack. If there is no link, ask the product.
6. Call `create_ad_links` with `kind=meta` and the rows, WITHOUT `create`. This is a preview and writes nothing. Show every link name and product code. Wait for yes.
7. Call `create_ad_links` again with the same rows and `create=true`.
8. Read back: call `create_ad_links` once more with the same rows and no `create`. Each row must return the same link, never a new one. Confirm each link name and its product.
9. Hand over each link next to its ad name. The link goes in the ad's website address. Leave the ad's URL parameters box empty, so the tag is not doubled.

Checks before answering:
- Safe test: when the person asks for a test run, make one link named claudetest that points at your main product page. Never use it in an ad.
- Spend: making a link spends nothing and changes no ad. Never edit, publish or turn on an ad here.
- One link per ad. Never give two ads the same link, or their sales cannot be told apart.
- One ad lives in one campaign. A copy of an ad in a second campaign gets its own link.
- Meta cannot see Amazon purchases. Judge these ads on the Amazon credit for each link, never on Meta's own results.
- If the answer says the Meta to Amazon add-on or your own link address is missing, say so and stop.
- If an ad account's last day is weeks old, say its ads are missing from this list.
- A new link in a live ad resets Meta's learning on it. Say so. The swap needs its own yes, at a quiet hour.

Rounds (relook before you answer):
1. **Name match.** Re-read each link name against its ad name before `create=true`. Fails when: a link name lacks the creator handle or short ad name that is in the ad name. Spend and Amazon sales are later joined by that name. Fix: rename the row and preview again.
2. **One link, one ad.** Two days after the person pastes the links, call `meta_metric` with `metric=ad_destinations`, `days=14` and `active_only=true` again. Fails when: an ad does not point at its own new link, or two ads still share one. Fix: list each ad still wrong.
3. **Clicks arrive.** Call `meta_metric` with `metric=amazon_ads` and `period=week`. Fails when: a new link shows 0 Amazon clicks while its ad spent over $50 since the swap. Fix: say the link was not pasted, or the tag is doubled in the URL parameters box.
4. **Clicks look right.** Same read. Fails when: Amazon clicks are under half or over 1.5x the ad's own link clicks. On one live brand they ran about 1.2x. Fix: name the ad and check its link and URL parameters by hand.

Output:
- One line first: how many links made, and how many old shared links were found.
- A table: ad name, product, link name, the link.

Never:
- Never reuse a link that another ad already uses.
- Never invent a product code the tool did not return.
- Never change a live ad. Use the ad launch shortcut, with its own yes.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-amazon-ad-link". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
