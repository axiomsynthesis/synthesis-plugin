# Are newer customers worth less?

Channel: Customers · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Are newer customers worth less?" (id: grw-cohort-collapse, Customers).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Takes each month's new customers and the share who came back within 3 months. It compares each month with the same month a year earlier, so sales events and seasons do not fool it. A real drop that starts at one month usually points to a change in offer, product or ad audience.

What to read: The share of each month's new customers who reordered within 3 months, on Amazon and on the website, against the same month a year earlier
What to give me: Whether recent customer groups come back less than the same month a year before, with error bars, and when it started

Synthesis tools to use:
- `cohort_retention_table limit=24`
- `shopify_metric metric=cohort_retention limit=24`

Steps:
1. Pull `cohort_retention_table limit=24` for Amazon cohorts and `shopify_metric metric=cohort_retention limit=24` for website cohorts. Read each on its own.
2. For each cohort, read `retained_3mo_pct`: the share who reordered at least once in months 1 to 3. Compare it with the same calendar month a year earlier.
3. Put a range on each rate. Use the Wilson interval at 95%, from the rate and `cohort_size`. Call it a step down only when the two ranges do not overlap.
4. Website cohorts under 300 customers: pool three months into a quarter before comparing.
5. Find the first cohort that stepped down and list what changed that month: offer, price, first product, channel mix.

Checks before answering:
- Never compare single-month cells like month 2 against month 2. Sales events land at different ages and swamp them.
- Young cohorts are unfinished. A null cell is not yet readable, never low.
- A cohort marked as a brand sale cohort is judged on its own, not against full-price months.
- Never merge Amazon and website cohorts. Amazon buyers cannot be matched to website buyers.
- Two website table builders define the 3-month rate differently. If the website rate looks out of line with month 1 to 3 cells, say the table may be on the other rule.
- This cannot split a drop by first product or ad channel yet. Say what would need checking.

Output:
- Answer first: is there a real step down, and from which month.
- Table: cohort, customers, reordered within 3 months with its range, same month a year earlier with its range, step down yes or no.
- One line on the break point and what changed.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-cohort-collapse". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
