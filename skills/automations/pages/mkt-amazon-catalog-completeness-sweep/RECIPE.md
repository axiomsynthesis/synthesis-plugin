# Fix your weakest product pages first

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Fix your weakest product pages first" (id: mkt-amazon-catalog-completeness-sweep, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Scores every product page for the basics: title length, bullets, description, main image and number of images. It ranks the gaps by sales, so the fix list starts where it pays.

What to read: A completeness score for every product page you sell, weighed by how much each product sells
What to give me: The pages missing the most basics, ranked by sales at stake, with the exact pieces missing

Synthesis tools to use:
- `cost_rules for=mkt-amazon-catalog-completeness-sweep`
- `amazon_metric metric=pnl_by_asin limit=40`
- `amazon_metric metric=listing_score`
- `amazon_metric metric=conversion_funnel days=30 limit=40`

Steps:
1. Call `amazon_metric metric=pnl_by_asin limit=40` to get your products by sales.
2. For each of the top 20 by sales, call `amazon_metric metric=listing_score asin=<product id>`. Stop at 20 unless asked.
3. Call `amazon_metric metric=conversion_funnel days=30 limit=40` to put conversion next to each score.
4. Rank by monthly sales times the number of failed checks. List the exact missing pieces per product.

Checks before answering:
- The score is structure only. It does not judge whether the words are good.
- A+ pages can show an unverifiable description. Never count that as missing.
- If a product shows no sales, check it is active before calling it a priority.

Output:
- One line: how many pages fail basics and the one to fix first.
- A table: product, monthly sales, score, failed checks, conversion rate.

Never:
- Never edit listings.
- Never score more than 20 pages in one run without asking.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-catalog-completeness-sweep". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
