# Answer the top objection with an ad

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Answer the top objection with an ad" (id: creative-answer-top-objection, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds the doubt your customers raise most under your ads, then writes an ad that answers it.
The answer uses only claims you have on file, and the concept is saved to your ideas list.

What to read: The comments under your ads, Reddit threads about your category, your brand facts
What to give me: The most-liked unanswered objection in your ad comments, and one ad concept that answers it with claims on file

Synthesis tools to use:
- `meta_metric metric=ad_comment_themes`
- `reddit_mentions`
- `brand_facts`
- `ad_idea_bank action=save`

Steps:
1. Call `meta_metric` with `metric=ad_comment_themes`, `days=90` and `quotes=5` for objections with their likes and quotes.
2. Pick the objection with the most likes that no ad answers yet.
3. Call `reddit_mentions` with `about=category` and `query` set to the objection's words, to see if buyers ask it elsewhere.
4. Call `brand_facts` with `query` set to the objection for the claims that answer it.
5. Write one concept that opens on the objection in the customer's words and answers it.
6. Save it with `ad_idea_bank`, `action=save`, `source=comment`, and the quote in `source_detail`.

Checks before answering:
- If the comment read is empty, say the ad comments are not collected yet. Never invent an objection.
- A question naming a disease is never answered with a disease claim. Say the brand cannot claim it.
- Reddit not collected is "not connected yet", never "no one asks".

Output:
- One headline line: the objection, with its comment count and likes.
- One concept: hook, script, brief, claims used.
- The saved idea id.

Never:
- Never reply to a comment for the brand. This writes an ad, not a reply.
- Never use a claim that is not on file.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-answer-top-objection". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
