# Write ad copy for every buyer stage

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Write ad copy for every buyer stage" (id: grw-awareness-ladder-copy, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
People meet your ad at different stages. Some do not know they have the problem, some know the problem, some compare products, some know you and need a nudge. This first finds which stage your current ads leave out, by the money behind each stage. Then it writes one ad for each stage, in your customers' words, with every claim checked against your product facts, and a plan to test them.

What to read: Your non-branded search terms, review language, ad comments, product facts and the opening lines of your best ads
What to give me: Ad copy for one product written five ways, from people unaware of the problem to people ready to buy

Synthesis tools to use:
- `winning_hooks read_new=false`
- `amazon_metric metric=search_query_performance periods=1 grain=week top=30`
- `search_console_organic view=branded_split days=90`
- `amazon_metric metric=review_voice limit=50`
- `meta_metric metric=ad_comment_themes days=90`
- `brand_facts`

Steps:
1. Pick one product.
2. Call `winning_hooks` with `read_new=false`. It spends nothing and gives the opening lines of the top ads with their spend and return.
3. Tag each top hook to one of the five stages and add up spend per stage. The gap is the stage with the least spend.
4. Call `amazon_metric metric=search_query_performance periods=1 grain=week top=30`. Read `nonbranded_top` and `top_opportunities` for problem words and product words.
5. Call `search_console_organic view=branded_split days=90`. Use the non-branded terms only.
6. Call `amazon_metric metric=review_voice limit=50` for the language buyers use.
7. Call `meta_metric metric=ad_comment_themes days=90` for the doubts people raise under the ads. These are the objections to answer.
8. Call `brand_facts` with `query` set to the product, for every claim you plan to make.
9. Write five versions: unaware (lead with a moment or story), problem aware (name the pain), solution aware (why this kind of fix), product aware (why yours, with proof), most aware (the offer).

Checks before answering:
- Each version names the stage and the words it borrowed from data.
- Every claim must match a product fact from step 8. If no fact backs it, cut the claim.
- Mark the stage your current ads miss, with the spend behind each stage from step 3.
- If the hook read has no hooks yet, say the stage gap could not be measured. Never guess it from ad names.
- If the comment read says a surface was not read, say which one. The objections then come from what was read only.
- This cannot check a claim against the ad platform's own rules. A person checks policy before the ads run.

Output:
- One line first: the stage your ads leave out, and the share of spend each stage gets now.
- Five blocks: stage, headline, 40-word body, hook line for video, where it runs, and the objection it answers.
- One line: run all five at equal budget, judge each after 3x the keep cost per sale, on thumb-stop first and cost per sale second. Thumb-stop is the share of viewers who watch past the first 3 seconds.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never copy text from any book or course. Write in plain words.
- Never write a disease or cavity claim, even if an old ad used one.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-awareness-ladder-copy". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
