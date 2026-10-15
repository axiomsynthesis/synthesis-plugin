# Keep or kill each new ad after week one

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Keep or kill each new ad after week one" (id: grw-meta-new-ad-first-week, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads each ad launched in the last two weeks against your own account and against practitioner bands. It gives a plain keep, wait or kill call, so new creative gets a fair test and losers stop early.

What to read: Hook rate, hold rate, click rate and cost per purchase for ads launched in the last 14 days
What to give me: Keep, give it more time, or kill, for every new ad

Synthesis tools to use:
- `meta_metric metric=ad_performance limit=50`
- `meta_metric metric=hook_rate`
- `meta_metric metric=ad_daily_trend ad_id=<id>`
- `score_creative_metrics`
- `benchmark_metric channel=meta`

Steps:
1. Pull `meta_metric metric=ad_performance limit=50` and keep ads whose first spend day is within 14 days.
2. Pull `meta_metric metric=hook_rate` for hook rate and hold rate on those ads.
3. For each new ad, run `score_creative_metrics` with its hook rate, hold rate, click rate and frequency.
4. Run `benchmark_metric channel=meta metric=hook_rate value=<whole-number percent>` for context.
5. Call it: kill if hook rate is in the bottom band and spend passed 2 times your target cost per purchase with no purchase; keep if cost per purchase is within 20% of target on 5 or more purchases; otherwise wait and say the spend still needed.

Checks before answering:
- Pass percents as whole numbers to `benchmark_metric` (18 means 18%).
- An ad younger than 3 days or under $50 spend gets wait, never kill.
- Static images have no hook rate. Judge them on click rate and cost per purchase only.
- Run `meta_metric metric=account_daily` first. An ACCOUNT STALE flag means recent zero spend is missing data, not a pause. Stop and say so before reading any trend.

Output:
- Answer first: counts of keep, wait, kill.
- Table with columns ad id, name, days live, spend, hook rate, hold rate, purchases, cost per purchase, call, reason.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never judge an ad on a benchmark alone. Your own account average comes first.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-new-ad-first-week". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
