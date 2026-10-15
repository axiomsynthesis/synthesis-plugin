# Know when a listing gets taken down

Channel: Amazon · Level: On a schedule · Status: Ready now
Schedule: daily 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Know when a listing gets taken down" (id: mkt-amazon-suppressed-listing-alert, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
A suppressed or inactive listing sells nothing and Amazon does not always tell you. Every morning this reads Amazon's own reports of which listings it has suppressed and which have gone inactive, and names each product with the sales a day at stake. We can also email this alert every morning from our server, only on days something is wrong: ask us to add the addresses.

What to read: Amazon's own suppression report and listing report, pulled every morning, with each product's sales before it went down
What to give me: A morning alert when a selling listing is suppressed or goes inactive, with Amazon's reason, since when, and the dollars a day at stake

Synthesis tools to use:
- `amazon_metric metric=listing_takedowns limit=50`

Steps:
1. Call `amazon_metric metric=listing_takedowns limit=50`.
2. Open with its `headline`, word for word: how many listings are down and the dollars a day at stake, or why the check could not run.
3. For each product in `takedowns`, give its `product_name`, what Amazon says (`reasons` and the first of `issues` when Amazon gave them, or that every listing is inactive), `since_words`, `sales_at_stake_per_day`, and `stock_note`.
4. If `state` is `partial` or `could_not_check`, say first what could not be seen, from `problems`.
5. End with `where_to_look`.

Checks before answering:
- Quote when Amazon's reports were read, from `check.checked_at_words`. If `check.fresh` is false, say the check is not from today.
- An empty list is an all-clear only when `state` is `clear`. Never say "nothing is down" on `partial` or `could_not_check`.
- Stock is Amazon's live count, refreshed when asked. Quote Amazon's update time, and name any product the answer left out because its numbers did not add up. Check it before saying stock is on hand.
- A listing with no stock reads inactive. Products set aside for that, or because they are selling again, are in `set_aside` with the reason; mention them only if asked.
- A product with no sales before it went down is listed but not sized. Say "not sized", never $0.

Output:
- One headline line: how many listings are down and the dollars a day at stake.
- Then three lines per product: what Amazon says, since when, the dollars a day at stake.
- Nothing more on a clear day.

Never:
- Never edit the listing to fix it. A person does that in Seller Central.
- Never call a listing suppressed unless Amazon's suppression report says so. A listing that is only inactive is "inactive".

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-suppressed-listing-alert". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (daily 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
