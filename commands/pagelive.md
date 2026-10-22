---
description: "Make a test version of a live page: A copy of one live page with only the tested thing changed, shown on a hidden preview first, then pushed live after your go, with every price proved against the cart"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Make a test version of a live page

Channel: Website · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Make a test version of a live page" (id: do-shopify-page-test-live, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Makes a new test version of one live landing page.
It copies today's live section, changes only the one thing being tested, shows it on a hidden preview, then pushes it live on your go.
Then it proves the live page shows the change at the cart's prices.

What to read: Your live landing page, its store prices, your landing page results, the claims your brand already makes
What to give me: A copy of one live page with only the tested thing changed, shown on a hidden preview first, then pushed live after your go, with every price proved against the cart

Synthesis tools to use:
- `cost_rules for=do-shopify-page-test-live`
- `ga4_metric metric=landing_pages days=28`
- `web_fetch`
- `brand_facts`
- `search_files`
- `first_order_contribution_margin`
- `log_decision kind=other`

Steps:
1. Ask in one message: which live page to copy, the one thing to change (often the default pack in the buy box), the new page link, and preview only or live. The new link must differ from the live one, or there is no control.
2. Call `ga4_metric` with `metric=landing_pages` and `days=28` for the page's sales per visitor. The new version must beat it. If not connected, say so and use the split-test app's sales per visitor instead. Never skip the bar.
3. In Claude Code, pull that page's section and template from the LIVE theme with Shopify's command-line tool. Copy them under new names ending "-claude". Never edit the live page's own files.
4. Change only the tested thing, by exact text replacement. Never redesign. Keep today's main buy box unless it is the test.
5. Claims only from `brand_facts`. If it times out, retry with one claim word and `limit=10`, then try `search_files` with `query=claims`. If neither answers, keep only live-page claims and say they were not re-checked. Flag every health claim. Keep each product's guarantee wording. Name no marketplace on a site page. A crossed-out price must be a real earlier price of that same pack.
6. Keep the section's schema name at 25 characters or fewer, or the push fails silently. Load images eagerly, or phones may show none.
7. Push only the new files to a hidden preview theme. The store may be at Shopify's 20-theme limit, so reuse an existing preview theme. Never duplicate one.
8. Check the preview in a real browser at 360, 768 and 1440 wide: centred, no sideways scroll, sticky buy bar showing. Add every pack, with and without each add-on and the subscription box, to the cart. Cart price must equal page price. Empty the cart after. Call `web_fetch` on the preview for Liquid error text.
9. After about 40 fast loads the store blocks you. Wait.
10. Ask each pack's cost. Call `first_order_contribution_margin` with `price`, `cogs`, `misc` for shipping, warehouse and card fees, and `cac` at today's ad cost per sale. Send the preview screenshots, prices and money kept per pack. Wait for the go for this page.
11. Back up the live files. Push only the new files to the live theme, allowing the live theme and deleting nothing. The tool asks to proceed. Answer it.
12. In admin, Online Store, Pages, create the page or pick the new template. Switching the template on a live page needs its own yes.
13. Read back. Pull the live section again and compare it to the build, since a code sync can undo a push. Open the live link in a fresh window and call `web_fetch` on it. Confirm the change shows and prices match the cart.
14. Call `log_decision` with `kind=other`, the page, the change, the undo, `measure` and `made_on`.

Checks before answering:
- Safe test run: when the person asks to test the shortcut, push only to the preview theme with new "-claude" files. Create no page in admin and touch nothing live.
- Spend: this spends nothing. Ads pointed at the page are a separate step and a separate yes.
- One page price that differs from the cart blocks the live push.
- If the browser sticks in preview, clear it with a blank preview value before the live check.

Rounds (relook before you answer):
1. **Only one thing changed.** Compare the new "-claude" files with the live copies line by line. Fails when: any line differs besides the tested thing. Fix: put the extra change back.
2. **Control untouched.** Pull the control page's section and template again. Fails when: either differs from the backup, or the test version uses the control's own template. Fix: restore the backup, give the test its own template.
3. **Every price against the cart.** Re-add every pack, with and without each add-on and the subscription box. Fails when: any cart line is 1 cent off the page, or a crossed-out price is not a real earlier price of that pack. Fix: correct the page, re-run.
4. **Claim sweep.** Re-read the page text, image words and video captions against `brand_facts`. Fails when: one claim has no entry, a disease claim appears, a rival or a marketplace is named. Fix: cut or reword it.
5. **Screens.** Re-open at 360, 768 and 1440 wide. Fails when: sideways scroll, a blank image on a phone, or no sticky buy bar. Fix: fix and push to preview again.
6. **Push stuck.** The next day, pull the live section again. Fails when: it differs from the build, since a code sync can undo a push. Fix: push again and say so.

Output:
- One line: preview or live, the page link, the one thing changed.
- Prices proved, one line per pack.
- The undo: push the backup, or set the template back.

Never:
- Never change the current live page when asked for a new version.
- Never push to live without the go for this page in this conversation.
- Never show a price the cart does not charge.
- Never delete a theme or a file.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-shopify-page-test-live". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
