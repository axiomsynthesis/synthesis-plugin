# This week's Google rank winners and losers

Channel: Website · Level: On a schedule · Status: Ready now
Schedule: weekly Monday 8am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "This week's Google rank winners and losers" (id: grw-seo-rank-movement, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Every week, lists the Google searches where your organic rank moved most, up and down, with the page that ranks. It catches a page dropping off page one before the traffic loss shows up in sales.

What to read: Google Search Console rank change against the prior equal window
What to give me: The organic searches you gained and lost this week, and the pages behind them

Synthesis tools to use:
- `search_console_organic view=movement days=7 limit=50 min_impressions=50`
- `search_console_organic view=pages days=28 limit=20`

Steps:
1. Pull `search_console_organic view=movement days=7 limit=50 min_impressions=50`.
2. Split into gainers and losers. A positive change means the term improved.
3. Pull `search_console_organic view=pages days=28 limit=20` to attach each term's page and its click trend.
4. Highlight terms that crossed into or out of the top 10.

Checks before answering:
- Terms missing from one window are turnover, not movement. List them apart.
- Search Console runs about 2 to 3 days behind. Use the closed window only.
- If the tool reports no Search Console connection, say so. Never report zero movement.

Output:
- Answer first. Two tables of up to 10 rows: term, page, position before, after, clicks change.

Never:
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never rewrite a page automatically.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-seo-rank-movement". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (weekly Monday 8am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
