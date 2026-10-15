# Which outside links sell on Amazon?

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which outside links sell on Amazon?" (id: grw-offsite-partner-ranking, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ranks every tagged outside link, such as an influencer post or a partner page, by the Amazon sales it produced. It is the list you use to decide who to renew, pay more or drop.

What to read: Amazon Attribution sales by publisher, campaign and ad group
What to give me: Partners and influencers ranked by the Amazon sales their links drove, to renew or drop

Synthesis tools to use:
- `amazon_metric metric=attribution_sources days=90 limit=50`
- `amazon_metric metric=attribution_trueup weeks=12`

Steps:
1. Pull `amazon_metric metric=attribution_sources days=90 limit=50`.
2. Pull `amazon_metric metric=attribution_trueup weeks=12` to see how much late-settling sales change recent weeks.
3. Rank sources by sales, and show click-to-order rate and active days.
4. Ask for each partner's cost if known, and compute sales per dollar.

Checks before answering:
- Recent weeks settle upward. Use the trueup to say how much the last two weeks may still grow.
- A source with under 10 orders is listed, not judged.
- Add Amazon's Brand Referral Bonus as 10% of attributed sales, not of spend, if the brand is enrolled.

Output:
- Answer first. Table: source, sales, orders, click-to-order rate, cost if known, sales per dollar, move.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-offsite-partner-ranking". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
