# Too many ad sets to learn?

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Too many ad sets to learn?" (id: grw-meta-adset-learning, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Meta's delivery needs a steady flow of purchases per ad set to learn. This finds budgets split so thin that most ad sets never get there, and proposes a merged structure.

What to read: Meta ad set spend and weekly purchases
What to give me: Ad sets too small for Meta to learn from, and a simpler setup

Synthesis tools to use:
- `meta_metric metric=adset_performance limit=50`
- `meta_metric metric=campaign_performance limit=25`

Steps:
1. Pull `meta_metric metric=adset_performance limit=50`.
2. For each live ad set, compute purchases per week over the last 4 closed weeks.
3. Count ad sets under 50 purchases a week and their share of spend.
4. Pull `meta_metric metric=campaign_performance limit=25` and group the thin ad sets by campaign and goal.
5. Propose merges: ad sets with the same goal and overlapping audiences become one, with the summed budget.

Checks before answering:
- Only count live ad sets. Paused ones with old spend do not count.
- Fifty a week is a rule of thumb, not a law. Say so.
- Run `meta_metric metric=account_daily` first. An ACCOUNT STALE flag means recent zero spend is missing data, not a pause. Stop and say so before reading any trend.

Output:
- Answer first: how many ad sets, how many are too thin, their share of spend.
- Table of proposed merges: from ad sets, into, combined weekly purchases.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-adset-learning". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
