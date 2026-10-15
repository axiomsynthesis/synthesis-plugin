# Your best scroll-stopping opening lines

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Your best scroll-stopping opening lines" (id: grw-hook-library, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ranks your video ads by how many viewers stay past the first seconds. It groups the winners into patterns like question, bold claim, before and after, or a face to camera, so the next scripts start strong.

What to read: Meta and TikTok video hook rates by ad
What to give me: A library of the opening lines that stop people scrolling, with patterns to reuse

Synthesis tools to use:
- `meta_metric metric=hook_rate`
- `meta_metric metric=creative_engagement limit=40`
- `tiktok_metric metric=creative_fatigue limit=30`
- `benchmark_metric channel=meta metric=hook_rate`

Steps:
1. Pull `meta_metric metric=hook_rate` and `meta_metric metric=creative_engagement limit=40`.
2. Pull `tiktok_metric metric=creative_fatigue limit=30` for TikTok videos.
3. Keep videos with at least 5,000 impressions.
4. Ask the person for the first line of each top video if names do not show it, and tag a pattern.
5. Check the top hook rates with `benchmark_metric channel=meta metric=hook_rate value=<percent>`.

Checks before answering:
- Pass percents as whole numbers to the benchmark.
- A high hook rate with poor sales is a hook that attracts the wrong people. Show cost per purchase beside it.

Output:
- Table: ad, platform, hook rate, hold rate, cost per purchase, pattern, first line. Then three patterns to reuse.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-hook-library". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
