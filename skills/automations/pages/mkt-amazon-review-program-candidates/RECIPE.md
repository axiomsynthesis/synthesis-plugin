# Which products need more reviews?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which products need more reviews?" (id: mkt-amazon-review-program-candidates, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Some products lose because they have too few reviews to be trusted. Amazon runs programs that put free product in front of vetted reviewers.
This finds the products where reviews are the binding problem and gives advice on whether a program is worth it. It is advice only.

What to read: Review count, rating and review pace per product, against the shelf on each product's main search
What to give me: Products held back by too few reviews, and which of Amazon's review programs fits each

Synthesis tools to use:
- `amazon_metric metric=review_velocity days=90 limit=30`
- `compare_to_shelf`
- `amazon_metric metric=pnl_by_asin limit=40`

Steps:
1. Call `amazon_metric metric=review_velocity days=90 limit=30` for review counts and pace per product.
2. For the products with the fewest reviews relative to their sales, call `compare_to_shelf our_asin=<product id> keyword=<main search>` once each, up to three.
3. Call `amazon_metric metric=pnl_by_asin limit=40` to weigh each by sales.
4. A product qualifies when its review count is far below the shelf median and its rating and price are in line. For each, say the likely program, the units to give and the cost, and remind the person to check current terms in Seller Central.

Checks before answering:
- Review programs change terms often. Never state a fee or limit as current. Tell the person to confirm in Seller Central.
- A product with a low rating does not need more reviews first. It needs the product fixed.
- Shelf data is scraped and draws on a shared monthly allowance. Ask before more than three calls.

Output:
- One line: which products, if any, need review help.
- A table: product, reviews, shelf median, rating, monthly sales, advice.

Never:
- Never enroll products in any program.
- Never suggest paying for reviews, review swaps or incentives outside Amazon's own programs.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-review-program-candidates". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
