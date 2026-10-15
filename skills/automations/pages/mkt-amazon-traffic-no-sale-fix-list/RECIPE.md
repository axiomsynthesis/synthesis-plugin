# Fix pages that get visits but no sales

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Fix pages that get visits but no sales" (id: mkt-amazon-traffic-no-sale-fix-list, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds product pages that get the visits and lose the sale. It checks the usual reasons one by one: buy box, price, reviews and page content.

What to read: Sessions and conversion for each product, what buyers complain about in reviews, and price against the shelf
What to give me: Products with plenty of visits but poor conversion, the likely reason for each, and what a fix is worth

Synthesis tools to use:
- `amazon_metric metric=conversion_funnel days=30 limit=40`
- `amazon_metric metric=review_voice sentiment=negative limit=10`
- `amazon_metric metric=shelf_position days=30 limit=30`
- `amazon_metric metric=buybox_health days=30 limit=40`

Steps:
1. Call `amazon_metric metric=conversion_funnel days=30 limit=40`. Flag products with above-median sessions and conversion under half your account median.
2. For each flagged product, call `amazon_metric metric=buybox_health days=30 limit=40`. Lost buy box kills conversion first.
3. Call `amazon_metric metric=shelf_position days=30 limit=30` for price and rating against rivals.
4. Call `amazon_metric metric=review_voice asin=<product id> sentiment=negative limit=10` for what buyers complain about.
5. Size the prize: sessions times the gap to your median conversion times average price.

Checks before answering:
- Compare like with like. A single unit and a 6-pack convert differently. Compare against the product's own family when you can.
- Buy box under 90% explains low conversion on its own. Check it before blaming the page.
- Promo weeks inflate conversion. Use a window without a big deal in it, or say one was in it.

Output:
- One line: the product with the biggest prize and its reason.
- A table: product, sessions, conversion, account median, buy box share, price gap, top complaint, monthly prize.

Never:
- Never edit listings or prices.
- Never quote review text beyond a short phrase.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-traffic-no-sale-fix-list". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
