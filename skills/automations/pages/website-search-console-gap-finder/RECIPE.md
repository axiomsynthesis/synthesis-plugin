# Google searches you almost win

Channel: Website · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Google searches you almost win" (id: website-search-console-gap-finder, Website).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds Google searches where you almost rank, usually positions 8 to 20, and says which page to write or fix to win them. Each idea comes with the clicks you could gain.

What to read: Search Console
What to give me: Searches where you rank just off page one, and briefs for the pages that could win them, ranked by clicks

Synthesis tools to use:
- `search_console_organic view=opportunities`
- `search_console_organic view=pages`
- `search_console_organic view=hidden_traffic`
- `export_docx`

Steps:
1. Call `search_console_organic` with `view="opportunities"`, `days=90`, `limit=50` and `min_impressions=200` to list near-miss searches.
2. Call `search_console_organic` with `view="pages"` and `days=90` to see which page ranks for each one today.
3. Call `search_console_organic` with `view="hidden_traffic"` and `days=90` so the answer says how much traffic Google does not show by term.
4. Group searches that share a meaning, and estimate the clicks a top 5 spot would bring.
5. Write one short brief per group: the search, the page to write or fix, what it must answer. Save with `export_docx`, `filename="search-page-briefs.docx"`.

Checks before answering:
- Use 90 days so one odd week does not move a ranking.
- The term list is a floor. Never scale it up to guess total organic traffic.
- If Search Console returns nothing or an error, say it could not be read. Never say there are no gaps.
- Searches with your brand name are not gaps. Leave them out.

Output:
- One line first: the clicks a month the top three briefs could win.
- A table: search, position now, searches a month, page today, clicks to gain.
- File: search-page-briefs.docx with up to 5 briefs.

Never:
- Never publish or edit a page. A person does that.
- Never invent a search volume the tool did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: website-search-console-gap-finder". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
