# What makes your best ads work (Motion)

Channel: Creative · Level: Advise · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What makes your best ads work (Motion)" (id: grw-motion-creative-tags, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Motion labels each creative by format, talent, message and more. This would rank those labels by results, so briefs build on what works. The connector exists but customers have no reading tool yet.

What to read: Motion creative tags, hooks and results across ads
What to give me: Which creative elements, like format, talent or message, go with better results

Synthesis tools to use:
- `meta_metric metric=creative_leaderboard limit=40`
- `score_creative_metrics`

Steps:
1. When a reader exists: pull creatives with tags and results, grouped by creative not by ad.
2. Today, use `meta_metric metric=creative_leaderboard limit=40` and `score_creative_metrics` for an untagged read.

Checks before answering:
- Motion money figures come from Meta's tag. Never add them to real revenue.
- Several ads can share one creative. Group by creative.

Output:
- Table: tag, creatives, spend, hook rate, cost per purchase.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-motion-creative-tags". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): The Motion connector syncs but no governed customer tool reads it. No governed customer tool reads this yet. The raw warehouse query is founder-only, so customers cannot run it. Do the parts you can and say plainly what is missing.
