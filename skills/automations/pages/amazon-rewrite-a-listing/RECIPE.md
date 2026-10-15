# Rewrite a listing to sell more

Channel: Amazon · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Rewrite a listing to sell more" (id: amazon-rewrite-a-listing, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Writes a new title, bullets and backend keywords for one product.
It uses the searches the listing is missing and the complaints in its reviews.
It keeps Amazon's length and claim rules, and a person uploads the file in Seller Central.

What to read: Search query performance, search terms, your reviews, rival listings
What to give me: Your old and new listing side by side, and the upload file

Synthesis tools to use:
- `amazon_metric metric=listing_details`
- `amazon_metric metric=search_term_gaps`
- `amazon_metric metric=review_voice`
- `scrape_amazon_search`
- `export_xlsx`

Steps:
1. Call `amazon_metric` with `metric=listing_details` and the product's `asin` to read the current title, bullets and price.
2. Call `amazon_metric` with `metric=search_term_gaps` and `limit=20` to find searches with sales where the listing does not show.
3. Call `amazon_metric` with `metric=review_voice` and the `asin` to pull the top praise and the top complaints in shoppers' own words.
4. Call `scrape_amazon_search` with the product's main search and `k=10` to see how the top rivals word their titles.
5. Write the new title, bullets and backend terms, then call `export_xlsx` with `filename=listing_rewrite.xlsx`: one sheet side by side, one sheet in upload layout.

Checks before answering:
- If the listing read is empty, say the listing could not be read. Never write a rewrite against a guessed current listing.
- Count characters. Title, each bullet and backend terms must sit inside Amazon's limits.
- Every claim in the new copy must be one the brand already makes. Check with the brand before adding a new one.

Output:
- A side-by-side table: field, now, new, why.
- The file listing_rewrite.xlsx. A person checks it and uploads it in Seller Central.
- One line on which search to watch to see if it worked, and when.

Never:
- Nothing goes live in any account. A person uploads the file.
- Never add a health or results claim the brand does not already make.
- Never copy a rival's wording.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-rewrite-a-listing". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): The data and the writing are ready. We still need to build the step that fills Amazon's listing upload file, and record which brands let us read their listing. Do the parts you can and say plainly what is missing.
