# Know when someone changes your listing

Channel: Amazon · Level: On a schedule · Status: Ready after we build it
Schedule: daily 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Know when someone changes your listing" (id: mkt-amazon-listing-change-detector, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Other sellers and Amazon's catalog can rewrite your product page. A wrong count or a lost claim can cut sales for weeks before anyone notices.
This compares each day's page with yesterday's and flags any change.

What to read: Your product page title, bullets, images and brand field, compared with the last saved copy
What to give me: An alert when a page changes without you, from another seller or Amazon's catalog, with the before and after

Synthesis tools to use:
- `amazon_metric metric=listing_details`
- `shelf_history marketplace=amazon days=30`

Steps:
1. For each top product, call `amazon_metric metric=listing_details asin=<product id>`. Keep the run to your top 20 products.
2. Compare title, bullets, image count and brand with the last saved copy.
3. Call `shelf_history marketplace=amazon days=30 asin=<product id>` to see whether price or rating moved at the same time.
4. Alert with the before and after, side by side.

Checks before answering:
- Ask the person whether anyone on their team changed the page before calling it unauthorized.
- Amazon sometimes reorders bullets with no change in words. Compare text, not order.

Output:
- One alert per changed product: field, before, after, date found.
- Nothing if nothing changed.

Never:
- Never edit the page or open a case without the person.
- Never call a change unauthorized before the person confirms.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-listing-change-detector". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (daily 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

Not fully ready yet (ready after we build it): Only price, rank, rating and review count are saved daily. Title, bullets and images are read live and no past copy is kept, so a change cannot be detected yet. Needs a daily saved copy of each page's content. Runs from your own Claude Code, so only while your computer is on. Do the parts you can and say plainly what is missing.
