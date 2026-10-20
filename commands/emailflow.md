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
4. Write each email as saved HTML. Host images on your store's Files page. Every animated image starts on its finished frame, because some inboxes show only frame 1.
5. Scan the body, preheader and the words inside every image for the claims you said never to make. Fix any hit before building.
6. Use Klaviyo in your real signed-in browser. The built-in browser pane is often logged out. Name the flow "<type> - <trigger> - Claude". Leave it in Draft.
7. Set the trigger. Placed Order carries no product code, so the filter keys off the product NAME. Use a "contains" filter on the part every pack size shares, copied exactly from step 3, symbols included. Trigger only on website, shop and social shop orders. Never email marketplace buyers. Exclude cancelled orders.
8. Add each email and wait. Drag and drop often drops only at the top, so add steps with "+ Step" in order. Branches cannot rejoin, so plan the order before you add a split.
9. If the flow replaces old content, first save each old email as a template named "BACKUP <old name>".
10. Show the whole flow: trigger, filters, each email's subject, timing and offer. Sending a test email is a message on their behalf. Send one only if they ask, and only to their own inbox.
11. On "Turn it on", set each email to Live. When Klaviyo asks about a live A/B test, choose "Continue", never "End and publish new test". Start any A/B test before turning the flow on. A flow switched on with a draft A/B test sends version A only.
12. Reload the flow. Read back that every email is Live and the trigger filters are as approved. After 48 hours, call `klaviyo_metric` with `metric=flow_step_performance` and check sends are above zero.

Checks before answering:
- Safe test when asked: build the flow as "CLAUDE TEST flow - do not send" in Draft with a trigger filter no order can match. Never set it Live.
- Spend: a flow costs nothing to build, but every send counts toward your Klaviyo plan. Say about how many people a day the trigger will reach: entries a day into a live flow with the same trigger. With none, use website orders a day from `shopify_metric` `metric=daily_revenue` `days=28` as the most it can be, and say so. Decline any upgrade Klaviyo offers.
- If the trigger product name does not match a name in step 3, stop. The flow would never send.

Output:
- One line: the flow name, how many emails, Draft or Live.
- The trigger and its filters, as set.
- Each email: subject, delay, offer, Live or Draft.
- What to check in 48 hours, and that renaming the product in your store will silently stop this flow.

Never:
- Never email marketplace buyers.
- Never send a test email without a yes.
- Never turn on a flow with a draft A/B test.
- Never edit a shared footer without saying it changes every email at once.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-klaviyo-build-flow". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
