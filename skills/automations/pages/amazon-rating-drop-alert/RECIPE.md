# Know when a star rating slips

Channel: Amazon · Level: On a schedule · Status: Ready now
Schedule: every Monday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Know when a star rating slips" (id: amazon-rating-drop-alert, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Watches your star ratings and review flow each week. When a product slips, it says when, by how much, and what the new complaints say. It tells a real quality problem apart from a normal wobble.

What to read: Reviews and ratings
What to give me: Which products slipped, by how much, and what the new complaints say

Synthesis tools to use:
- `amazon_metric metric=rating_watch`
- `amazon_metric metric=review_velocity`
- `amazon_metric metric=review_voice`
- `review_themes`
- `find_product`

Steps:
1. Call `amazon_metric` with `metric=rating_watch` and `days=30` to find products whose star rating stepped down and the likely cause.
2. Call `amazon_metric` with `metric=review_velocity` and `days=30` to see whether new reviews slowed down.
3. For each product that slipped, call `amazon_metric` with `metric=review_voice`, its `asin`, `sentiment=negative` and `limit=50` for the newest complaints.
4. Pass those reviews to `review_themes` to group the complaints into themes with counts.
5. Use `find_product` to name each product the way the brand does.

Checks before answering:
- If the rating tools return nothing, say the review data could not be read. Never say "no drops" from an empty result.
- A 0.1 star move on a small review count can be noise. Say how many reviews it rests on.
- A new complaint needs more than one review to count as a theme.

Output:
- One line first: which products slipped and by how much.
- A table: product, old rating, new rating, date, new reviews this week, top new complaint.
- Two or three quoted complaints, and one move: the fix to look at first.

Never:
- Never reply to a review or change a listing. A person does that.
- Never invent a complaint the reviews do not contain.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-rating-drop-alert". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every Monday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
