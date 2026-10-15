---
description: "Write ad copy for every buyer stage: Ad copy for one product written five ways, from people unaware of the problem to people ready to buy"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Write ad copy for every buyer stage

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Write ad copy for every buyer stage" (id: grw-awareness-ladder-copy, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
People meet your ad at different stages. Some do not know they have the problem, some know the problem, some compare products, some know you and need a nudge. This writes one ad for each stage, in your customers' words.

What to read: Your search terms, review language and best ads
What to give me: Ad copy for one product written five ways, from people unaware of the problem to people ready to buy

Synthesis tools to use:
- `amazon_metric metric=search_query_performance periods=4 grain=week top=30`
- `search_console_organic view=queries days=90 limit=50`
- `amazon_metric metric=review_voice limit=50`
- `meta_metric metric=creative_leaderboard limit=10`

Steps:
1. Pick one product.
2. Pull `amazon_metric metric=search_query_performance periods=4 grain=week top=30` and `search_console_organic view=queries days=90 limit=50` for problem words and product words.
3. Pull `amazon_metric metric=review_voice limit=50` for the language buyers use.
4. Pull `meta_metric metric=creative_leaderboard limit=10` to see which stage your winning ads already speak to.
5. Write five versions: unaware (lead with a moment or story), problem aware (name the pain), solution aware (why this kind of fix), product aware (why yours, with proof), most aware (the offer).

Checks before answering:
- Each version names the stage and the words it borrowed from data.
- Every claim must be one your reviews or product facts support.
- Mark the stage your current ads miss.

Output:
- Five blocks: stage, headline, 40-word body, hook line for video, where it runs. Plus one line on the gap.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never copy text from any book or course. Write in plain words.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-awareness-ladder-copy". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
