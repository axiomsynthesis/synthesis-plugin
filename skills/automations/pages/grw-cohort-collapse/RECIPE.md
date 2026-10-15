# Are newer customers worth less?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are newer customers worth less?" (id: grw-cohort-collapse, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lines up every month's new customers by age and compares how many came back in month 1, 2, 3 and so on. A drop that starts at one month usually points to a change in offer, product or ad audience.

What to read: Monthly retention for each acquisition month on Amazon and on the website, at equal age
What to give me: Whether recent customer groups come back less than older ones, and when it started

Synthesis tools to use:
- `cohort_retention_table limit=24`
- `shopify_metric metric=cohort_retention`

Steps:
1. Pull `cohort_retention_table limit=24` for Amazon cohorts and `shopify_metric metric=cohort_retention` for website cohorts. Read each on its own.
2. Compare month 2 and month 3 retention for the newest complete cohorts against the year before.
3. Find the first cohort where retention stepped down and list what changed that month: offer, price, channel mix.

Checks before answering:
- Young cohorts are unfinished. Leave immature cells blank and never read them as low.
- Cohorts under 100 customers are flagged as low confidence.
- Never merge Amazon and website cohorts. Amazon buyers cannot be matched to website buyers.
- Each cell is the share ordering in that one month, not cumulative. Say so.

Output:
- Answer first. Table: cohort, customers, month 1, 2, 3, 6 retention. One line on the break point.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-cohort-collapse". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
