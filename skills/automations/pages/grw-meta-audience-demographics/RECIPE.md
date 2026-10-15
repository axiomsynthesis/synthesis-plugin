# Who actually buys from your Meta ads

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Who actually buys from your Meta ads" (id: grw-meta-audience-demographics, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Shows which age and gender groups and which regions turn Meta spend into purchases. It sets that beside where your website sales actually come from, so targeting and creative casting match your real buyers.

What to read: Meta results by age, gender and region
What to give me: The ages, genders and regions that buy cheaply, and the ones that don't

Synthesis tools to use:
- `meta_metric metric=breakdown dimension=age_gender limit=30`
- `meta_metric metric=breakdown dimension=region limit=30`
- `shopify_metric metric=state_revenue`

Steps:
1. Pull `meta_metric metric=breakdown dimension=age_gender limit=30`.
2. Pull `meta_metric metric=breakdown dimension=region limit=30`.
3. Pull `shopify_metric metric=state_revenue` for where website revenue comes from.
4. Flag groups with at least $500 spend and cost per purchase 40% better or worse than the account.
5. Compare each region's share of Meta spend with its share of website revenue and list the biggest gaps.

Checks before answering:
- Rows under $25 of spend, or with fewer than 10 purchases, are noise. List them, never rank them as winners or losers.
- Meta's region names and the shop's state names must be matched by state, not by city.
- If the breakdown table is stale against the ad table, say so and stop.
- Meta's purchase numbers come from its own tag. It cannot see Amazon or retail checkouts, so say that beside any ROAS.

Output:
- Answer first. Two short tables: age and gender (group, spend, cost per purchase, verdict) and regions (region, share of Meta spend, share of website revenue, gap).
- Close with one casting or targeting move.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never infer a person's traits beyond the groups Meta reports.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-audience-demographics". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
