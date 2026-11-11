---
description: "Check a landing page like a shopper: Every pack and add-on pressed through to checkout, plus pictures and motion on every screen size, with proof each check works"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Check a landing page like a shopper

Channel: Website · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Check a landing page like a shopper" (id: landing-page-check, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks a landing page the way a shopper meets it. Every pack and add-on goes through to Shopify's checkout, and the price, products and shipping must match the page.
Then it checks pictures, hidden parts and motion on four screen sizes. It breaks the page on purpose to prove each check can fail.

What to read: Your live or preview landing page, Shopify's real checkout, your store's shipping rates, every picture and animation on the page
What to give me: Every pack and add-on pressed through to checkout, plus pictures and motion on every screen size, with proof each check works

Synthesis tools to use:
- `cost_rules for=landing-page-check`
- `render_report format=landing_page page_format=check`
- `ga4_metric metric=landing_pages days=28`

Steps:
1. Ask which page, or call `ga4_metric` with `metric=landing_pages` and `days=28` and take the paid page with the most visitors. Use the live address; a preview address works too.
2. Call `render_report` with `format=landing_page` and `page_format=check`. In Claude Code, download the zip from `download_url` and unzip it.
3. In Claude Code, install the free test browser once, in that folder:
```bash
npm install playwright && npx playwright install chromium
```
4. Run the check. It writes `lpk-audit.md` and pictures in `lpk-shots/`:
```bash
node lpk.mjs audit "<page link>"
```
5. Run the proof. Each of the 7 breaks must say CAUGHT:
```bash
node lpk.mjs audit "<page link>" --prove
```
6. Open `lpk-shots/` and look at the phone and desktop pictures yourself before answering.

Checks before answering:
- A FAIL line is a real problem on the page. Quote it word for word with both prices.
- A blocked or error line means that row was not checked. Never call it a pass.
- The store's bot shield challenges a test browser after about 15 checkouts in a few minutes. Wait 10 minutes and run again; never run in a loop.
- A proof that says MISSED means that check is blind on this page. Say so; do not report its passes.
- Prices are checked only on a buy box built with the landing page kit: packs to pick, add-ons to tick, one buy button. Any other page, such as a theme's own product page, gets one error row, "prices to checkout: no buy box on this page". Its pictures and motion are still checked. Say plainly that its prices were not checked; never call that page a pass on price.

Rounds (relook before you answer):
1. **Every row ran.** Count the rows marked blocked, error or skip. Fails when: any blocked or error row remains, other than "no buy box" on a page not built with the kit. Fix: wait 10 minutes and run the check again, the checkout part or the screens part alone.
2. **Every break caught.** Re-read the proof. Fails when: any break says MISSED, or COULD NOT PROVE for a reason other than "break could not be planted: it is not on this page". On a page not built with the kit, the price and buy-box breaks cannot be planted: report those checks as unproven there. Fix: run that break again by name after a wait; if it still misses, report that check as unproven.
3. **Looked at it.** Open the phone picture at 390 wide. Fails when: something covers the buy button or the headline, or a picture is blank. Fix: add it to the answer as a FAIL.

Output:
- First line: the page, and passed, failed or could not check.
- Each FAIL with the page price and the checkout price, or the picture or motion that broke.
- The proof: 7 breaks, how many caught.
- What was not checked: the Shop Pay button needs a sign-in, so it is not pressed. Under 15 lines.

Never:
- Never place an order, type into checkout or use a real card.
- Never change the store or the page to make a check pass.
- Never call a blocked, errored or skipped row a pass.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: landing-page-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- If you could not finish, open your answer with "Stuck:" and what I need to do. If your answers are not saved for you automatically, save this one with the Synthesis tool `capture_turn`: my request as `question`, your answer as `answer`, and `context` starting with "automation: landing-page-check".

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
