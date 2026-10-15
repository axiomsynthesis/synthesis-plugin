# Turn reviews into selling lines

Channel: Customers · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Turn reviews into selling lines" (id: customers-review-mining, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Turns your reviews into words you can use. It finds the top praise and complaints, then writes FAQ answers, listing bullets and ad angles in your buyers' own words.

What to read: Reviews
What to give me: What buyers love and complain about, written as FAQ answers, listing bullets and ad angles in their own words

Synthesis tools to use:
- `find_product`
- `amazon_metric metric=review_voice`
- `review_themes`
- `amazon_metric metric=rating_watch`
- `export_docx`

Steps:
1. Use `find_product` to pick your top products and their IDs.
2. Call `amazon_metric` with `metric=review_voice`, each `asin` and `limit=200` for the review text.
3. Pass the reviews to `review_themes` for themes, counts and positive or negative lean.
4. Call `amazon_metric` with `metric=rating_watch` and `days=90` to see whether any theme moved the star rating.
5. Write FAQ answers, bullets and ad angles from the top themes, then call `export_docx` with `filename=review_mining.docx`.

Checks before answering:
- Every line must trace to real reviews. Show the count behind each theme.
- If reviews come back empty, say so. Never write lines from a guess of what buyers say.
- A theme in one or two reviews is not a theme.

Output:
- A Word file named `review_mining.docx`, two pages at most.
- A theme table: theme, praise or complaint, reviews, a short quote.
- Ready-to-use lines: five FAQ answers, five listing bullets, five ad angles.
- A person edits and publishes them.

Never:
- Never post or change a listing, ad or FAQ. A person does that.
- Never turn a review into a health or results claim the brand cannot prove.
- Never quote a reviewer's name.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: customers-review-mining". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
