# Fill the holes in your ad lineup

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Fill the holes in your ad lineup" (id: grw-creative-coverage-matrix, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Maps your live ads onto a grid of funnel stage and format. Empty cells are audiences you have nothing for. It briefs the most valuable empty cells.

What to read: Live Meta and TikTok ads labelled by stage and format
What to give me: The funnel stages and formats with no live ad, and briefs to fill them

Synthesis tools to use:
- `build_creative_matrix`
- `meta_metric metric=creative_leaderboard limit=40`
- `tiktok_metric metric=campaign_leaderboard limit=20`

Steps:
1. Run `build_creative_matrix funnel_stages=[cold, warm, hot] formats=[short video, static, carousel, creator]`.
2. Pull `meta_metric metric=creative_leaderboard limit=40` and `tiktok_metric metric=campaign_leaderboard limit=20`.
3. Label each live ad's stage and format. Ask when unclear.
4. Mark empty cells and brief the top three.

Checks before answering:
- Unlabelled ads are listed, never guessed.
- This is coverage, not performance. Say so.

Output:
- A grid with ad counts per cell, then three briefs: cell, goal, angle, hook, proof, call to action.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-creative-coverage-matrix". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
