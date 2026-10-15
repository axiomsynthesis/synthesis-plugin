# Write the A+ content brief

Channel: Amazon · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Write the A+ content brief" (id: amazon-a-plus-content-brief, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Writes a brief for your product page images and A+ modules. It uses what your buyers praise and worry about, what rival buyers complain about, and the words people search with. A designer can work straight from it.

What to read: Reviews, rival pages, searches
What to give me: A module-by-module brief for your page images and A+ content, built from what buyers praise, worry about and search for

Synthesis tools to use:
- `find_product`
- `amazon_metric metric=listing_details`
- `amazon_metric metric=review_voice`
- `competitor_review_voice`
- `amazon_metric metric=search_query_performance`
- `export_docx`

Steps:
1. Use `find_product` to pick the product, then call `amazon_metric` with `metric=listing_details` and its `asin` for the current title, bullets and images.
2. Call `amazon_metric` with `metric=review_voice`, the `asin` and `limit=100` for what your buyers praise and complain about.
3. Call `competitor_review_voice` with `limit=100` for what rival buyers complain about.
4. Call `amazon_metric` with `metric=search_query_performance`, `grain=week`, `periods=4` and `top=15` for the words shoppers use.
5. Map each worry or search to one module, then call `export_docx` with `filename=a_plus_brief.docx`.

Checks before answering:
- Every module claim must trace to a real review or search. Quote it.
- If reviews come back empty, say so and build the brief from searches only.
- Do not lean on a theme that shows up in only one or two reviews.

Output:
- A Word file named `a_plus_brief.docx`, one or two pages.
- One section per module: the job of the module, the headline, the proof to show, and the review or search it answers.
- A person hands it to the designer and uploads the finished A+ content.

Never:
- Never upload or change A+ content or the listing. A person does that.
- Never write a health or results claim the brand cannot prove.
- Never quote a review that the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-a-plus-content-brief". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
