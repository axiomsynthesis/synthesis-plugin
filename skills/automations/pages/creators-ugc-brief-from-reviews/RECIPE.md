# Turn reviews into creator briefs

Channel: Creators · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Turn reviews into creator briefs" (id: creators-ugc-brief-from-reviews, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Turns what real customers say in reviews into three creator briefs, each with a hook, the shots to film and the proof to show. It checks the hooks against the ads that already work for you.

What to read: Reviews, best ads
What to give me: Three creator briefs with hooks, shots and proof, built from what real customers say

Synthesis tools to use:
- `amazon_metric metric=review_voice`
- `review_themes`
- `meta_metric metric=creative_leaderboard`
- `meta_metric metric=hook_rate`
- `export_docx`

Steps:
1. Call `amazon_metric` with `metric=review_voice` and `limit=200` for recent review text on your top products.
2. Pass that text to `review_themes` with `reviews` set to the list, to rank the praise and complaints that come up most.
3. Call `meta_metric` with `metric=creative_leaderboard` and `limit=10` to find your best ads by sales. It always covers the last 30 days, so say that.
4. Call `meta_metric` with `metric=hook_rate` for the latest month, then again with `month=` set to each of the two months before, to see which openings hold viewers.
5. Write three briefs, each built on one review theme, and save with `export_docx`, `filename="ugc-briefs.docx"`.

Checks before answering:
- Every hook must trace to real review words. Quote the review it came from.
- A theme needs at least 10 reviews behind it. One loud review is not a theme.
- If no reviews come back, say so. Never write hooks from guesses.
- Leave out any claim the product cannot legally make.

Output:
- One line first: the three themes and why they will sell.
- Three briefs, each with hook, three to five shots, proof line, call to action and the review quotes behind it.
- File: ugc-briefs.docx.

Never:
- Never send briefs to creators. A person does that.
- Never invent a customer quote.
- Never promise a health result the product does not claim.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creators-ugc-brief-from-reviews". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
