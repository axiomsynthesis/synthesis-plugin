# Are you winning share in your category?

Channel: Retail · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are you winning share in your category?" (id: retail-category-share-recap, Retail).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads your syndicated category data and says what share you hold, which way it is moving, and who is gaining or losing. It answers first with your share and the change, then names the one rival to watch.

What to read: SPINS or Nielsen
What to give me: Your share, which way it's moving, and who is gaining or losing

Synthesis tools to use:
- `list_files`
- `search_file_content`
- `read_file`
- `estimate_market_share`

Steps:
1. Call `list_files` with `limit=50` and `search_file_content` with `query="category share SPINS Nielsen"` and `k=8` to find the newest syndicated files.
2. Open each with `read_file` and pull dollar share by brand for the last 52 weeks, in the periods the file uses.
3. Work out your share and each rival's share for the latest period, the period before, and a year ago.
4. If the file gives more than one share signal, pass them to `estimate_market_share` with `signals` set to those percentages for a single figure with its confidence.
5. Rank the brands by share points gained or lost.

Checks before answering:
- Use the file's own periods. Never mix a 4-week and a 12-week read.
- Share of a segment and share of the whole category are different. Say which one.
- If no syndicated file is found, say the data is missing. Never report a share of zero.
- One period's move is not a trend. Show at least three periods.

Output:
- One line first: your share, the change in points, and the period.
- A table: brand, share now, share last period, share a year ago, change in points.
- One move and how we will know it worked next period.

Never:
- Never invent a rival's share the file does not hold.
- Never call a segment share a category share.
- Nothing changes in any account. This is a read.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: retail-category-share-recap". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): A connected SPINS feed lands in our warehouse, but no customer tool reads it yet, so a category share tool has to be built. An uploaded SPINS or Nielsen file works today. Do the parts you can and say plainly what is missing.
