# Find searches where you're not on the shelf

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Find searches where you're not on the shelf" (id: mkt-amazon-off-the-shelf-searches, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lists searches where shoppers in your category buy and you are not one of the top three. The split matters: never shown needs reach, shown but skipped needs a better offer.

What to read: Category searches where none of your products is in the top three clicked, split into never shown and shown but skipped
What to give me: The searches you are missing, the products winning them, and whether the fix is ads, listing words or the product

Synthesis tools to use:
- `amazon_metric metric=search_term_gaps weeks=8 limit=40`
- `amazon_metric metric=ppc_search_terms days=60 limit=100`

Steps:
1. Call `amazon_metric metric=search_term_gaps weeks=8 limit=40`. Note each term's kind and the rival products leading it.
2. Call `amazon_metric metric=ppc_search_terms days=60 limit=100` to see whether you already pay for any of these terms.
3. For never shown terms you do not bid on: suggest ads plus listing words. For shown but skipped: compare your product with the leaders and name the missing claim, size or price.

Checks before answering:
- A never shown term has no share for you. It is unmeasured, never 0%.
- Make sure the term is truly in your category. Drop terms for products you do not make.
- Check the weeks are closed. Never use the in-progress week.

Output:
- One line: how many gaps, split by kind, and the largest one.
- A table: search, monthly searches if known, kind, rival leaders, do you bid on it, suggested fix.

Never:
- Never add keywords or edit listings in any account.
- Never claim a rival's sales.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-off-the-shelf-searches". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
