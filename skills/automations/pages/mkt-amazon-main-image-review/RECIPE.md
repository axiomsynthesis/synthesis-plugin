# Is your main image losing clicks?

Channel: Amazon · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is your main image losing clicks?" (id: mkt-amazon-main-image-review, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
The main image decides the click. This compares your main image with the shelf around it and checks your click share to see if the image is the problem.

What to read: The main image of your product and of the rivals beside it on your top search, plus your click share on that search
What to give me: Whether your main image is costing clicks, with three specific fixes and a test to prove the new one works

Synthesis tools to use:
- `amazon_metric metric=listing_details`
- `scrape_amazon_search k=10`
- `amazon_metric metric=search_query_performance grain=week periods=4 scope=nonbranded top=20`

Steps:
1. Call `amazon_metric metric=search_query_performance grain=week periods=4 scope=nonbranded top=20` and find the gap between view share and click share on your top searches.
2. Call `amazon_metric metric=listing_details asin=<product id>` to get your main image link.
3. Call `scrape_amazon_search keyword=<main search> k=10` once to get the rivals on that shelf and their images.
4. Look at the images yourself, in your own AI app. Judge white background, how much of the frame the product fills, whether it reads at thumbnail size, and whether pack count is clear.
5. Write three fixes and a test: change only the main image, recheck click share after 4 closed weeks.

Checks before answering:
- If view-to-click is not the biggest gap, say the image is probably not the main problem.
- Scraped shelf data is a snapshot. Label it with the date. Ask before more than one scrape.
- Synthesis' own server image grader is not on customer connections. The picture review is done by your AI app.

Output:
- One line: is the image costing clicks, yes or no, with the share numbers.
- Three fixes, one line each.
- The test: what changes, which number, which date.

Never:
- Never upload or change images.
- Never claim a click-rate lift before the test runs.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-main-image-review". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
