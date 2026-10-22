---
description: "Build a Klaviyo email flow for me: A new Klaviyo flow built as drafts, shown to you, then switched on after your yes and read back"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Build a Klaviyo email flow for me

Channel: Email · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build a Klaviyo email flow for me" (id: do-klaviyo-build-flow, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds a Klaviyo flow, such as an after-purchase series, an abandoned checkout or a welcome series. It builds every email as a draft in your own signed-in Klaviyo and switches it on only when you say "Turn it on".

What to read: Klaviyo flow and step results, the exact product names in your store
What to give me: A new Klaviyo flow built as drafts, shown to you, then switched on after your yes and read back

Synthesis tools to use:
- `klaviyo_metric metric=flow_funnel`
- `klaviyo_metric metric=flow_step_performance limit=60`
- `shopify_metric metric=product_attach limit=20`
- `shopify_metric metric=daily_revenue days=28`

Steps:
1. Ask: flow type, trigger product or event, number of emails and their timing, A/B test or not, and any offer. Ask whether any code in it may stack with a welcome code. Ask which claims your brand never makes in email. Ask the guarantee length per product, and whether email follows the page or the checkout when they differ.
2. Call `klaviyo_metric` with `metric=flow_funnel`, then again with `metric=flow_step_performance`, to see what flows run. These show only steps that have sent. Open each live flow with the same trigger in Klaviyo and list its unsent steps before building, so the new one does not double up.
3. Call `shopify_metric` with `metric=product_attach`, `anchor=<a word from the product title>` and `limit=20` for the exact current names of every pack size. `top_products` is all-time and misses new products.
4. After-purchase timing follows run-out, not the calendar. Ask how long each pack lasts. Days to run out = units x days each lasts. Default plan from one live brand, a pack lasting about 8 weeks: welcome day 0, why it works day 4, subscribe-or-stock-up test day 12, add-on day 21, running low day 42, last call day 56. Skip the last two for anyone who already reordered.
5. Every email nudges one size up from what was bought, for example 2 to 4 to 6, never the same size at a discount. Each link opens that exact pack at the price the email states.
6. No disease or medical claims in email or SMS. A sent email cannot be pulled back, unlike a page. Ask which milder claims the brand allows.
7. Write each email as saved HTML. Host images on your store's Files page. Every animated image starts on its finished frame, because some inboxes show only frame 1.
8. Scan the body, preheader and the words inside every image for the claims you said never to make. Fix any hit before building.
9. Use Klaviyo in your real signed-in browser. The built-in browser pane is often logged out. Name the flow "<type> - <trigger> - Claude". Leave it in Draft.
10. Set the trigger. Placed Order carries no product code, so the filter keys off the product NAME. Use a "contains" filter on the part every pack size shares, copied exactly from step 3, symbols included. Trigger only on website, shop and social shop orders. Never email marketplace buyers. Exclude cancelled orders.
11. Add each email and wait. Drag and drop often drops only at the top, so add steps with "+ Step" in order. Branches cannot rejoin, so plan the order before you add a split.
12. If the flow replaces old content, first save each old email as a template named "BACKUP <old name>".
13. Show the whole flow: trigger, filters, each email's subject, timing and offer. Sending a test email is a message on their behalf. Send one only if they ask, and only to their own inbox.
14. On "Turn it on", set each email to Live. When Klaviyo asks about a live A/B test, choose "Continue", never "End and publish new test". Start any A/B test before turning the flow on. A flow switched on with a draft A/B test sends version A only.
15. Reload the flow. Read back that every email is Live and the trigger filters are as approved. After 48 hours, call `klaviyo_metric` with `metric=flow_step_performance` and check sends are above zero.

Checks before answering:
- Safe test when asked: build the flow as "CLAUDE TEST flow - do not send" in Draft with a trigger filter no order can match. Never set it Live.
- Spend: a flow costs nothing to build, but every send counts toward your Klaviyo plan. Say about how many people a day the trigger will reach: entries a day into a live flow with the same trigger. With none, use website orders a day from `shopify_metric` `metric=daily_revenue` `days=28` as the most it can be, and say so. Decline any upgrade Klaviyo offers.
- If the trigger product name does not match a name in step 3, stop. The flow would never send.

Rounds (relook before you answer):
1. **Run-out timing.** Re-work days to run out for every pack the trigger catches. Fails when: the running-low email lands after the run-out day minus 14, or before half the pack's life. Fix: move the delay.
2. **Claim sweep.** Re-read every subject, preheader, body, image text and alt text. Fails when: any disease or medical claim appears, or a claim the person said never to make. Fix: cut it before anything goes Live.
3. **Size-up and links.** Open every link. Fails when: a link opens a pack the same size or smaller than the one bought, the cart price differs from the email's price, or a code in it stacks with the welcome code. Fix: relink or reword.
4. **Trigger catches the right orders.** Re-read the trigger against step 3's names. Fails when: one pack size's name is missed, marketplace orders get in, or cancelled orders are not excluded. Fix: change the filter.
5. **No double sends.** Fails when: another live flow with the same trigger would email the same buyer within 2 days of this one. Fix: add a filter or change the timing.
6. **It actually sends.** After 48 hours call `klaviyo_metric` with `metric=flow_step_performance`. Fails when: the first email shows 0 sends while `daily_revenue` shows matching website orders. Fix: re-check the trigger name and that every email is Live.

Output:
- One line: the flow name, how many emails, Draft or Live.
- The trigger and its filters, as set.
- Each email: subject, delay, offer, Live or Draft.
- What to check in 48 hours, and that renaming the product in your store will silently stop this flow.

Never:
- Never email marketplace buyers.
- Never put a disease or medical claim in an email or text.
- Never send a test email without a yes.
- Never turn on a flow with a draft A/B test.
- Never edit a shared footer without saying it changes every email at once.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-klaviyo-build-flow". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
