# Replace tired ads before they cost you

Channel: Meta · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Replace tired ads before they cost you" (id: meta-tired-ads-and-new-briefs, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Spots Meta ads that are wearing out and writes briefs for their replacements.
It finds ads whose cost per sale keeps climbing, and shows what the winners have in common.
The briefs are ready for a designer or an AI image tool.

What to read: Meta ad results by creative
What to give me: Meta ads wearing out, and three briefs for their replacements

Synthesis tools to use:
- `meta_metric metric=creative_fatigue_curve`
- `meta_metric metric=creative_leaderboard`
- `meta_metric metric=hook_rate`
- `export_docx`

Steps:
1. Call `meta_metric` with `metric=creative_fatigue_curve` to find ads whose cost per sale is rising as they are shown more. It tracks each ad from its launch day, with no date setting.
2. Call `meta_metric` with `metric=creative_leaderboard` to find the current winners. It always covers the last 30 days.
3. Call `meta_metric` with `metric=hook_rate` for the latest month to compare how well winners and tired ads stop the scroll.
4. Write three briefs from what the winners share: format, hook, proof and offer.
5. Call `export_docx` with `filename=meta_creative_briefs.docx` holding the tired-ad list and the three briefs.

Checks before answering:
- An ad needs real spend to be called tired. Skip ads under a few hundred dollars and say how many.
- If the creative read is empty, say it could not be read. Never say "nothing is tired".
- Rising cost in one week is not fatigue. Look for a climb across at least 3 weeks.

Output:
- A table: ad, cost per sale 4 weeks ago, cost per sale now, spend, call.
- Three briefs, each: goal, format and size, hook, proof, headline, what to avoid.
- The file meta_creative_briefs.docx.

Never:
- Nothing goes live in any account. A person pauses ads and uploads new ones.
- Never write a health or results claim the brand does not already make.
- Never guess a cost the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-tired-ads-and-new-briefs". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
