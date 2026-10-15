# Why did Meta get more expensive?

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Why did Meta get more expensive?" (id: grw-meta-cost-decomposition, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Cost per purchase is media price times clicks needed times visitors needed. This splits a rise into those three parts so you fix the right thing: creative for clicks, the site for conversion, or nothing when the whole market got pricier.

What to read: Meta CPM, click rate, conversion rate and cost per purchase by week
What to give me: Which of the three parts moved your cost per purchase, and the fix for that part

Synthesis tools to use:
- `meta_metric metric=weekly_trend weeks=12`
- `meta_metric metric=cpm month=<YYYY-MM>`
- `meta_metric metric=funnel days=28`
- `meta_metric metric=account_daily`

Steps:
1. Run `meta_metric metric=account_daily` and stop if stale.
2. Pull `meta_metric metric=weekly_trend weeks=12`.
3. For the last 4 closed weeks against the 4 before, compute the change in CPM, click rate and purchases per click.
4. Attribute the cost per purchase change to each part using log shares, so the three add up to the total change.
5. Pull `meta_metric metric=cpm` for the same month last year if the data exists, to tell a seasonal price rise from a real one.
6. Name the part that moved most and one fix for it.

Checks before answering:
- Run `meta_metric metric=account_daily` first. An ACCOUNT STALE flag means recent zero spend is missing data, not a pause. Stop and say so before reading any trend.
- Compute rates from summed counts across the weeks, never by averaging weekly rates.
- The three parts must multiply back to the reported cost per purchase within 2%. If not, say the inputs disagree and show both.
- Exclude the current partial week.

Output:
- Answer first in one sentence. Then a 3-row table: part, before, after, share of the change.
- One fix and how we will know in two weeks.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-cost-decomposition". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
