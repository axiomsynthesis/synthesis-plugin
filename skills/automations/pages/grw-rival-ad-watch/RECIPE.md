# See what rivals are running on Meta

Channel: Creative · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "See what rivals are running on Meta" (id: grw-rival-ad-watch, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ads that run for months are usually profitable. This would list rivals' longest-running ads and new launches each week, with the angles they use, beside your own.

What to read: Rivals' active ads in Meta's public Ad Library
What to give me: New rival ads, the ones running longest, and the angles they lean on

Synthesis tools to use:
- `meta_metric metric=creative_leaderboard limit=20`

Steps:
1. When a reader exists: pull each rival's active ads, start date and text.
2. Rank by days live and group by angle.
3. Compare with your own winners from `meta_metric metric=creative_leaderboard limit=20`.

Checks before answering:
- Days live is a hint of profit, not proof.
- Never copy a rival's ad.

Output:
- Table: rival, ad start date, days live, format, angle.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-rival-ad-watch". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): An Ad Library sync exists but no governed customer tool reads it. A reader tool is needed. Do the parts you can and say plainly what is missing.
