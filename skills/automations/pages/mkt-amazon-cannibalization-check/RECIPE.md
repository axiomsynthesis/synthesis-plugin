# Is the new product eating the old one?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is the new product eating the old one?" (id: mkt-amazon-cannibalization-check, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A launch that only moves buyers from your other products adds nothing. This splits the new product's sales into truly new and moved over.

What to read: Weekly units for a new product and its sister products before and after launch, and which of your products buyers switched from
What to give me: How much of the new product's sales are new to the business and how much moved over from your own products

Synthesis tools to use:
- `amazon_metric metric=velocity_momentum weeks=20 limit=40`
- `product_customers definition=gateway`
- `product_customers definition=all`
- `find_product`

Steps:
1. Call `find_product query=<family name>` to list the sister products.
2. Call `amazon_metric metric=velocity_momentum weeks=20 limit=40`. Compare sister products' weekly units after launch with their trend before.
3. Call `product_customers asin=<new product id> definition=gateway` for buyers whose first ever order was the new product, and `definition=all` for every buyer.
4. Cannibalized units = fall in sisters below trend. Net gain = new product units minus that.

Checks before answering:
- Sister products move for other reasons too: stockouts, price changes, events. Check those weeks before blaming the launch.
- Event weeks are tagged. Leave them out of the trend.
- Gateway and all-buyers counts are different groups. Always show both with their names.

Output:
- One line: net weekly gain from the launch.
- A table: product, weekly units before, after, change from trend.
- Two lines: share of new product buyers new to you, and share of its sales moved from your own products.

Never:
- Never blame a sister product's fall on the launch without checking stock and price.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-cannibalization-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
