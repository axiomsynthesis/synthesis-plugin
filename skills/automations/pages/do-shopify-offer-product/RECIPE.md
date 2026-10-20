# Set up the product behind an offer

Channel: Website · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Set up the product behind an offer" (id: do-shopify-offer-product, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Creates or edits the product behind an offer: an add-on, a gift, a pack box, a crossed-out price or stock.
It enters the item's cost so profit-per-visitor tests are right.
It checks the item adds to the cart at the right price, then checks the first real order ships.

What to read: Your store's products, prices and costs
What to give me: One add-on, gift or pack product created or edited in your Shopify admin after your yes, with its cost entered so profit tests are right

Synthesis tools to use:
- `cost_rules for=do-shopify-offer-product`
- `find_product`
- `first_order_contribution_margin`
- `web_fetch`

Steps:
1. Ask in one message: product name, price, crossed-out price, which real warehouse SKU, cost per item, stock rule and which page it is for.
2. Call `find_product` only for the product's family name. It reads the Amazon catalog, not the store. Read the real item it copies, its variant and its warehouse SKU in Shopify admin. Store sales rankings are all-time and miss new products, so never use them to find it.
3. Ask the cost. Never assume one. Call `first_order_contribution_margin` with `price` and `cogs` passed by hand, and shipping, warehouse and card fees as `misc`. Show profit per order. For an add-on, also show the change in shipping when it moves the order across a shipping tier.
4. A crossed-out price must be a real earlier price. Ask, and say so.
5. In Shopify admin, Products, create or edit it. New offer products: Unlisted, Online Store channel only, the same warehouse SKU as the real item, stock not tracked. Untick sell only as a subscription so one-time buys work.
6. Never reprice an existing $0 free-send product. Price and stock changes need the number named in chat.
7. Enter the cost per item in the product or the bulk editor. If a split-test app reads costs from Shopify, run its cost refresh after. Then read the app's cost setting back, since a flat per-order cost there ignores the product cost.
8. Save. Reload and read back: status, channel, SKU, price, crossed-out price, cost and tracking.
9. Add it to the cart on the storefront and read the cart price. Call `web_fetch` on the page that sells it.
10. After the first real order of a new SKU, check it shows Fulfilled with tracking. A new box SKU not mapped in the warehouse system can sit unshipped, and nothing else checks this. Nothing reminds anyone, so give the date and ask who will check.

Checks before answering:
- Safe test run: when the person asks to test the shortcut, create a Draft product "CLAUDE TEST ITEM - do not sell" at $999, no channels, SKU TEST-CLAUDE. Read it back and leave it as Draft. It stays in the catalog. Say so, since this shortcut never deletes or archives.
- Spend: this spends nothing, but a wrong price or a $0 item sells at a loss. Show the price and profit per order before the yes.
- A stock sync from another system can reset stock to 0. Re-read stock a day later when stock matters.
- Check the product is not swept into a smart collection that a discount code covers.
- If the cost in Shopify differs from the cost the person gave, say both. Never pick one quietly.

Output:
- One line: the product, price, status and channel.
- Cost entered and profit per order.
- Cart check, and the date to check the first order shipped.

Never:
- Never delete or archive a product.
- Never change a price or stock level without the number in chat.
- Never put an offer product in search or the shop's menus.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-shopify-offer-product". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
