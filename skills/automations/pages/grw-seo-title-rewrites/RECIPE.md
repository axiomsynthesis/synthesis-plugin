# Rewrite search titles that lose clicks

Channel: Website · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Rewrite search titles that lose clicks" (id: grw-seo-title-rewrites, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds pages Google shows often that people skip. It drafts new titles and descriptions built on the words searchers used, for a person to review and publish.

What to read: Pages with many Google impressions and low click rate for their position
What to give me: New page titles and descriptions for pages that are seen on Google but not clicked

Synthesis tools to use:
- `search_console_organic view=pages days=28 limit=50`
- `search_console_organic view=opportunities days=28 limit=50`

Steps:
1. Pull `search_console_organic view=pages days=28 limit=50`.
2. Pull `search_console_organic view=opportunities days=28 limit=50` for pages clicking below what their position normally earns.
3. Pick the 10 pages with the biggest click gap.
4. For each, list the top three searches that show it and draft a title under 60 characters and a description under 155, using those words.

Checks before answering:
- A page ranked beyond 10 gets few clicks for position reasons. Do not blame its title.
- Never draft a claim the page does not make.

Output:
- Answer first. Table with columns page, impressions, click rate, expected click rate, new title, new description.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- A person publishes any change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-seo-title-rewrites". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
