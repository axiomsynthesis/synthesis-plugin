---
description: "Check the ads I just launched: Every new ad checked one by one: what to fix before it spends, what to fix while it runs, and what could not be checked"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Check the ads I just launched

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Check the ads I just launched" (id: meta-ad-launch-check, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks each Meta ad made in the last few days, one by one, the way a careful media buyer would before it spends.
It checks that the video and the landing page sell the same product, the page opens, the link carries tracking and creator tags, the name follows the brand's rule, the video fits each placement, Meta's automatic add-ons are off, the ad, ad set and campaign are all on, the ad set has not ended, no video runs twice, cost per sale sits inside the brand's own lines, and Amazon-bound links carry their attribution tags.
The server decides every result as pass, fail, unknown or not applicable, with the exact fix.

What to read: Each new Meta ad's video, link, landing page, tracking and creator tags, name, placements, switches, end date and sales so far
What to give me: Every new ad checked one by one: what to fix before it spends, what to fix while it runs, and what could not be checked

Synthesis tools to use:
- `cost_rules for=meta-ad-launch-check`
- `ad_health_check`

Steps:
1. Call `ad_health_check` with `ads={}` to check every ad made in the last 3 days, or `ads={"adset_id": "<id>"}` for one ad set, or `ads={"campaign_id": "<id>"}` for one campaign.
2. If someone gave ad ids, call it with `ads={"ad_ids": ["<id>", "<id>"]}` instead (up to 60).
3. If the ad's edit screen is open in a browser, read the "email sign-up offer" and "promo codes" boxes and the product the video shows, and pass only what was actually seen in `ads.seen_in_tab`.

Checks before answering:
- Use each result as the server decided it. Never turn an unknown into a pass.
- An unknown product means the video's name and title say nothing about it. Say so and ask someone to watch the first seconds; never guess from the ad copy.
- "Too early" on sales is not a failure.
- A brand with no money lines gets cost per sale shown, not judged. Do not judge it with another brand's numbers.

Rounds (relook before you answer):
1. **Watch the first seconds.** For every ad whose product reads unknown, watch it in the browser if one is open. Fails when: the product shown differs from the page the ad links to. Fix: list it under fix before it spends.
2. **Claims.** Read every caption and on-screen line of each new ad. Fails when: a line makes a claim the brand's other live ads do not make. Fix: list it under fix before it spends, with the line quoted.
3. **Did it spend.** After a full closed day, run `ad_health_check` on the same ads again. Fails when: an ad marked ready still has $0 spend. Fix: say it is starved and name the ad set it competes in.

Output:
- One line first: how many ads, how many to fix before they spend, how many ready.
- Each ad to fix before it spends, with its exact fix.
- The smaller fixes, grouped by kind.
- What could not be checked and how to check it, one line each.
- Under 20 lines in total.

Never:
- Never change, publish or switch on an ad. A person does that.
- Never say an ad is ready when one of its checks read unknown.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-ad-launch-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
