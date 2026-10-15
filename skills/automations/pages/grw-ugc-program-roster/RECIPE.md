# Is your UGC program healthy?

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is your UGC program healthy?" (id: grw-ugc-program-roster, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads your user-generated content creator program: how many creators are active, who joined, who left, and what they earned. On a new program the roster is the only signal with weight.

What to read: UGC creator program roster, joins, departures and earnings
What to give me: Whether your UGC program is growing, keeping creators and producing

Synthesis tools to use:
- `trybe_creator_program view=roster days=90 limit=50`
- `trybe_creator_program view=performance days=90 limit=50`

Steps:
1. Pull `trybe_creator_program view=roster days=90 limit=50`.
2. Pull `trybe_creator_program view=performance days=90 limit=50`.
3. Report active creators, joins and departures by month, and earnings concentration.

Checks before answering:
- Left the program is inferred from creators missing from the platform list. Say it is an inference.
- Earnings take weeks to move. On a program under 60 days old, read the roster only.
- If the program is not connected, say so.

Output:
- Answer first. Table by month: joined, left, active, earnings.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-ugc-program-roster". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
