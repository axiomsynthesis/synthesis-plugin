# Cut Meta placements that don't sell

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Cut Meta placements that don't sell" (id: grw-meta-placement-waste, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits Meta spend across Feed, Reels, Stories and the audience network. It shows where money goes without purchases and which ads win on each surface, so the next edit fits the placement.

What to read: Meta results by placement and by creative per placement
What to give me: Placements that eat budget without sales, and the ads that win on each

Synthesis tools to use:
- `meta_metric metric=breakdown dimension=placement limit=30`
- `meta_metric metric=creative_by_placement limit=30`

Steps:
1. Pull `meta_metric metric=breakdown dimension=placement limit=30`.
2. Rank placements by spend and mark any with cost per purchase more than 1.5 times the account average.
3. Pull `meta_metric metric=creative_by_placement limit=30` and find, for each big placement, the ad with the best cost per purchase.
4. Write one move per wasteful placement: exclude it, or make a format that fits it (for example a vertical cut for Reels).

Checks before answering:
- Check the breakdown dates. If the placement table's newest date is weeks behind the ad table, say it is stale and do not advise on it.
- Rows under $25 of spend, or with fewer than 10 purchases, are noise. List them, never rank them as winners or losers.
- Placement totals should sum close to account spend for the same window. If they are off by more than 5%, say the cut is incomplete.
- Meta's purchase numbers come from its own tag. It cannot see Amazon or retail checkouts, so say that beside any ROAS.

Output:
- Answer first. Then a table with columns placement, spend, share, purchases, cost per purchase, best ad on it, move.
- Under 12 rows.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.
- Never recommend excluding a placement on less than $25 of spend.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-meta-placement-waste". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
