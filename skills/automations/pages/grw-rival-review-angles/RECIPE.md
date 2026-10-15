# Ad angles from rivals' unhappy customers

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Ad angles from rivals' unhappy customers" (id: grw-rival-review-angles, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads what customers of rival products complain about, and what your customers praise. Where a rival's weakness meets your strength, it drafts an ad angle and a listing line.

What to read: Competitor reviews on Amazon and your own review insights
What to give me: Ad and listing angles built on what rival buyers complain about and what yours praise

Synthesis tools to use:
- `competitor_review_voice limit=100`
- `amazon_metric metric=review_voice sentiment=positive limit=50`
- `review_themes`

Steps:
1. Pull `competitor_review_voice limit=100` for your competitor watchlist.
2. Run `review_themes` on the rival reviews and keep the top complaints.
3. Pull `amazon_metric metric=review_voice sentiment=positive limit=50` for your praised topics.
4. Match rival complaints to your praised topics. Draft one ad hook and one listing line per match.

Checks before answering:
- If the competitor watchlist is empty, say so and ask for rival products.
- Quote only short phrases from reviews. Never name a rival in ad copy.
- Every claim must match something your own reviews say.

Output:
- Table: rival complaint, how often, your matching strength, ad hook, listing line. 5 to 8 rows.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never make a comparative claim about a named rival.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-rival-review-angles". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
