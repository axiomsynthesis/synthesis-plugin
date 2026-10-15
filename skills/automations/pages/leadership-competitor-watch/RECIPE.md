# Weekly rival watch

Channel: Leadership · Level: On a schedule · Status: Ready after we build it
Schedule: every Monday 9am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Weekly rival watch" (id: leadership-competitor-watch, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each week it writes one page on your rivals: who moved price, who gained search share, and what their customers are saying. It ends with whether you need to respond.

What to read: Search data, rival listings
What to give me: A one-page update on rival price, search and review moves, and whether to respond

Synthesis tools to use:
- `amazon_metric metric=search_competitors`
- `amazon_metric metric=search_query_performance`
- `shelf_history`
- `competitor_review_voice`
- `export_pdf`

Steps:
1. Call `amazon_metric` with `metric=search_competitors` with `grain=week` and `periods=4` for who is winning clicks and sales on your top searches.
2. Call `amazon_metric` with `metric=search_query_performance` with `grain=week`, `periods=8` and `scope=nonbranded` for your own share on those searches.
3. Call `shelf_history` with `marketplace="amazon"` and `days=30` for rival price, rank and review moves.
4. Call `competitor_review_voice` with `limit=50` for what rival customers praise and complain about.
5. Write one page and save with `export_pdf`, `filename="competitor-watch.pdf"`.

Checks before answering:
- Keep branded and non-branded search share apart. Never blend them.
- A one-week move is a watch item, not a trend. Say how many weeks a move has lasted.
- If the listing history is empty, say scans have not run. Never say rivals did not move.

Output:
- One page. First line: the one rival move that matters and whether to respond.
- A table: rival, price change, share change, review change, weeks.
- File: competitor-watch.pdf.

Never:
- Never change your price or ads in response. A person decides.
- Never invent a rival's price or share.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: leadership-competitor-watch". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every Monday 9am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

Not fully ready yet (ready after we build it): Repeats by itself only in Claude Code on a computer that is on at that time. In the Claude app or website, run it by hand each time, or use a scheduled task if your Claude offers one. Search data is ready, but regular scans of rival listings still need to be scheduled for each brand. Do the parts you can and say plainly what is missing.
