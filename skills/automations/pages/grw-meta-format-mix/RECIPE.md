# Video, image or carousel: which sells?

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Video, image or carousel: which sells?" (id: grw-meta-format-mix, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Compares video, static image and carousel ads on cost per purchase and on how many winners each format produces. It tells your creative team where the next production dollar does the most.

What to read: Meta results by creative format, video retention and creative quality
What to give me: Which ad format earns your money, and where to shift production effort

Synthesis tools to use:
- `meta_metric metric=creative_quality_dist`
- `meta_metric metric=video_efficiency limit=30`
- `meta_metric metric=creative_leaderboard limit=40`

Steps:
1. Pull `meta_metric metric=creative_leaderboard limit=40` and label each ad's format.
2. Pull `meta_metric metric=video_efficiency limit=30` for video watch depth against cost.
3. Pull `meta_metric metric=creative_quality_dist` for the spread of results within each format.
4. For each format: spend, purchases, cost per purchase from summed counts, and the share of ads that became winners (cost per purchase within target on 10 or more purchases).

Checks before answering:
- Rows under $25 of spend, or with fewer than 10 purchases, are noise. List them, never rank them as winners or losers.
- Use summed spend over summed purchases per format, never an average of ad ROAS.
- Meta's purchase numbers come from its own tag. It cannot see Amazon or retail checkouts, so say that beside any ROAS.

Output:
- Answer first. Table with columns format, ads run, spend, cost per purchase, winner rate.
- One line on the production mix for next month.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-format-mix". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
