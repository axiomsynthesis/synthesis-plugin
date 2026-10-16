# What if your top creator walks?

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What if your top creator walks?" (id: grw-creator-concentration, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows how dependent your creator channel is on a few people. If one creator drives a third of creator sales, losing them is a real revenue event, so you need a bench.

What to read: Creator revenue by creator on each creator platform
What to give me: The share of creator sales from your top five, and the risk if one leaves

Synthesis tools to use:
- `growi_metric metric=top_creators limit=25`
- `levanta_metric metric=top_creators months=6 limit=25`
- `cruva_metric metric=creator_leaderboard limit=25`

Steps:
1. Pull the leaderboard from each connected creator platform: `growi_metric metric=top_creators limit=25`, `levanta_metric metric=top_creators months=6 limit=25`, `cruva_metric metric=creator_leaderboard limit=25`.
2. Per platform, compute the top 1 and top 5 share of creator revenue.
3. List creators ranked 6 to 20 with rising revenue. They are the bench.

Checks before answering:
- Creator sales are the platform's own attribution. They will not tie to your order records, and they are a slice of the shop, not all of it.
- Overlapping sources are shown side by side, never added together.
- Some leaderboards are lifetime-to-date and carry no date. Never compare them to a dated month.
- Skip platforms that are not connected and say which.

Output:
- Answer first. Per platform: top 1 share, top 5 share. Then a short bench list.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-creator-concentration". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
