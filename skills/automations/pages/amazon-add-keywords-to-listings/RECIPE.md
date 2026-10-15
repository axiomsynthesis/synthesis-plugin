# Add the searches your listings miss

Channel: Amazon · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Add the searches your listings miss" (id: amazon-add-keywords-to-listings, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lists the searches with sales where your products do not show.
It places each one where Amazon reads it: title, bullets or backend terms.
It checks nothing goes over the length limits, and a person uploads the file.

What to read: Search query performance, search terms
What to give me: Searches that sell where your products don't show, placed in title, bullets or backend, with the upload file

Synthesis tools to use:
- `amazon_metric metric=search_term_gaps`
- `amazon_metric metric=keyword_opportunities`
- `amazon_metric metric=listing_details`
- `find_product`
- `export_xlsx`

Steps:
1. Call `amazon_metric` with `metric=search_term_gaps` and `limit=50` to get searches with sales where each product barely appears.
2. Call `amazon_metric` with `metric=keyword_opportunities` and `grain=week` to add search terms that already convert in ads but are not in the listing. It reads the latest closed weeks of search data, so say which weeks.
3. For each product, call `amazon_metric` with `metric=listing_details` and its `asin` to read the current title, bullets and backend terms.
4. Use `find_product` to group pack sizes of one product, so one keyword is not placed twice.
5. Place each keyword and call `export_xlsx` with `filename=keyword_plan.xlsx`: one sheet with the plan, one sheet in upload layout.

Checks before answering:
- If the search data is empty, say Brand Analytics may not be on. Never say "no missing searches".
- Count characters after adding. Drop the lowest-value keyword if a field goes over.
- Skip any search already in the listing.

Output:
- A table: product, keyword to add, where it goes, sales on that search a month.
- The file keyword_plan.xlsx. A person checks it and uploads it in Seller Central.

Never:
- Nothing goes live in any account. A person uploads the file.
- Never add a rival's brand name as a keyword.
- Never guess search volume the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-add-keywords-to-listings". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): The data is ready. We still need to build the step that fills Amazon's listing upload file, the same as the listing rewrite. Do the parts you can and say plainly what is missing.
