# Monday creative brief

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Monday creative brief" (id: creative-monday-brief, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Gives you this week's creative brief on demand.
It reads the stored Monday research, the hooks that sell in your own ads, and the ideas you already have.
Every concept builds on a hook that already sells and uses only claims you have on file.

What to read: This week's stored research run, your hook ranking, your saved ideas
What to give me: Five ad concepts to brief this week, each built on a hook that sells, with its claims checked

Synthesis tools to use:
- `ad_idea_bank action=weekly_research`
- `winning_hooks`
- `ad_idea_bank action=list`
- `brand_facts`

Steps:
1. Call `ad_idea_bank` with `action=weekly_research` for the newest stored run.
2. Call `winning_hooks` with `read_new=false` for the hooks that sell and the account average.
3. Call `ad_idea_bank` with `action=list` so no concept repeats an idea already saved.
4. Write five concepts: hook, script, brief for the shoot, why it should work, and claims used.
5. Check each claim with `brand_facts`. Drop any claim not on file and say which.

Checks before answering:
- If the stored run is empty, say the brief has not run yet. Build only from the hook ranking and say so.
- Every number in a concept must come from a tool result above.
- Five concepts must differ in hook family or layout.

Output:
- One headline line: the hook the batch doubles down on, and its return against your average.
- Five concepts, each: title, hook, script, brief, why, claims checked.
- One line on how to test them and when to read the result.

Never:
- Never write a health or results claim the brand does not already make.
- Nothing is launched. A person briefs and launches the ads.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-monday-brief". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
