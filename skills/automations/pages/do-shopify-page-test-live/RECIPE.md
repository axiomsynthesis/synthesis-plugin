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
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-shopify-page-test-live". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
