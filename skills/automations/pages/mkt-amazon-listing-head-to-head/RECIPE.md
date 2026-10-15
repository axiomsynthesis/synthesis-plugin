# Your listing vs the top rivals

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Your listing vs the top rivals" (id: mkt-amazon-listing-head-to-head, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Puts your product page next to the pages that beat you on the same search. It finds the gaps a shopper sees in the first five seconds.

What to read: Your product page and up to five rival pages side by side, with price, rating and review count on the live shelf for your main search
What to give me: Where your page loses to the products beside it on the shelf, and the one lever that decides that shelf

Synthesis tools to use:
- `amazon_metric metric=compare_listings`
- `compare_to_shelf`
- `amazon_metric metric=listing_details`

Steps:
1. Ask the person for the main search term and the product. Resolve the product with `find_product` if they give a name.
2. Call `compare_to_shelf our_asin=<your product id> keyword=<main search>`. This is a live scrape: one call, not a loop.
3. Pick the top two or three rivals from that shelf. Call `amazon_metric metric=compare_listings asins=[...]` with yours and theirs.
4. For any field that looks off, call `amazon_metric metric=listing_details asin=<product id>` to read the actual title and bullets.
5. Name the one lever that decides the shelf: price, rating, review count, images or copy.

Checks before answering:
- Shelf data is scraped live. Label it scraped, with the date. It draws on a shared monthly allowance, so ask before repeating it.
- The listing score measures completeness, not copy quality. Never say "your copy is worse" from the score alone.
- A product with A+ content can show an empty description. That is a known flag, not a missing description.

Output:
- One line: the lever that decides this shelf.
- A table: product, price, rating, reviews, title length, image count, listing score.
- Three specific fixes, in order.

Never:
- Never edit the listing.
- Never copy a rival's text.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-listing-head-to-head". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
