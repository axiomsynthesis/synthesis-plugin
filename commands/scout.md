---
description: "Scout creators and rival ads for me: A ranked hit list of creators to approach and rival ads worth learning from, with where each was found and why it ranks"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Scout creators and rival ads for me

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Scout creators and rival ads for me" (id: creative-ad-library-creator-scout, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Scouts the Meta Ad Library for creators and rival ads in your category.
It returns a ranked hit list of people to approach and ads worth learning from.
It only reads. Any message to a creator is drafted, never sent.

What to read: Rival brands' running ads in the Meta Ad Library, the creators and experts who front them, and how long each ad has run
What to give me: A ranked hit list of creators to approach and rival ads worth learning from, with where each was found and why it ranks

Synthesis tools to use:
- `competitor_ads source=meta min_days=30`
- `competitor_ads source=meta new_days=7`
- `web_search`

Steps:
1. Ask the product, how many names, and which rival brands to include.
2. Ask the ranking rule. Default: real licensed experts in the category first, then creators whose ads have run longest.
3. Call `competitor_ads` with `source=meta` and `min_days=30` for rival ads that have run a month or more. Read `status` first. A partial run means a rival has no matched page, so that rival's zero is not real. Name it.
4. Call `competitor_ads` with `source=meta` and `new_days=7` for rival ads started this week.
5. The rival-ads tool returns the brand's page, not the creator. Creator names come only from the Ad Library page text. In the browser, open the Meta Ad Library. Search each rival and each category phrase. Read the page text for the page name, start date and who fronts the ad. Keep to the rivals asked and about 30 searches in all.
6. Before the first search, run one query you know has results. Run it again about every 30 searches. The Ad Library silently returns nothing after about 40 searches. A zero after that is not a real zero.
7. Facebook clears saved page data between pages. Copy results out after each search.
8. Use `web_search` to check each expert's credential is real. It costs credits. Say how many searches and get a yes first.
9. Rank the list and note the source and date for each name.

Checks before answering:
- If `competitor_ads` is not in the tool list, stop and say the rival-ads tool is not available on this connection. Never fall back to memory.
- The known query still returned results at the end of the run. If not, say the run was cut short and how many searches were trusted.
- Drop pages with fake credentials or a claimed government approval.
- Never pass on a rival's health-scare claim or a "better than" claim as something to copy.
- A captcha or login wall goes back to the person. Never get past it.
- Safe test, when asked for one: run it on one query with 10 names.
- Spend check: the reads and the browser spend nothing. Credential searches cost credits and need a yes on the count. Outreach drafts never promise money or free product the person has not agreed.

Rounds (relook before you answer):
1. **Coverage.** Re-read the `status` and the known-query checks. Fails when: an asked rival shows zero ads with a partial status, or the known query came back empty. Fix: name the rival as not read, never as quiet.
2. **Credential.** For each top-10 expert, look for a license, practice or school that can be found. Fails when: none can be found, or the page claims a government approval. Fix: move them to the creator list or drop them.
3. **Proven run.** Fails when: a ranked rival ad has run under 30 days. A long run is the proof an ad pays. Fix: move it to a watch list.
4. **Clean to copy.** Fails when: a rival ad picked to learn from leans on a fear claim, a fake countdown, a "better than" claim or a fake ranking site. Fix: drop it.
5. **Free to work with.** Fails when: a creator fronts a direct rival in an ad still running. Fix: flag them as likely tied up and rank them lower.

Output:
- One line first: names found, from how many rivals, and how many searches were trusted.
- The hit list: name, page, why they rank, ad running since, where found.
- Up to 3 rival ads worth learning from, one line each.
- Outreach drafts, only if asked, using only facts the brand has confirmed and no sales figures.

Never:
- Never send a message, fill a form or follow a creator.
- Never bypass a captcha or a login.
- Never state a brand claim the brand has not confirmed.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-ad-library-creator-scout". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
