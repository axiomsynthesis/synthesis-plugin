# Which creators earn their pay?

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Which creators earn their pay?" (id: creators-creator-and-affiliate-payout-check, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Puts what each creator or affiliate was paid next to the sales they drove, so you can see who earns their pay and who does not. It reads each program on its own basis and never adds them into one total.

What to read: Levanta, Growi, TikTok creators
What to give me: What each creator or affiliate was paid next to the sales they drove, and who to review first

Synthesis tools to use:
- `growi_top_creators`
- `growi_creator_payouts`
- `levanta_metric metric=top_creators`
- `levanta_metric metric=commission_economics`
- `cruva_metric metric=creator_leaderboard`

Steps:
1. Call `growi_top_creators` with `limit=50` for sales, retainer and commission per creator, and `growi_creator_payouts` with `months=6` for cash actually paid.
2. Call `levanta_metric` with `metric=top_creators`, `months=6` and `limit=50`, then `metric=commission_economics` with `months=6` for commission owed less the referral bonus.
3. Call `cruva_metric` with `metric=creator_leaderboard`, `days=180` and `limit=50` for TikTok Shop creators.
4. For each creator, work out sales per dollar paid and flag anyone paid more than the sales they drove.
5. Rank by dollars paid with the weakest return first.

Checks before answering:
- Cash paid and commission owed are different bases. Show each on its own line, never summed.
- Only read the programs that are connected. A missing program is missing, not zero.
- Sales per dollar paid is a sales ratio, not profit. Never call a creator profitable without product cost.
- A creator with one post is not a trend. Say how many months each figure covers.

Output:
- One line first: dollars paid to creators who drove less in sales than they were paid.
- A table: creator, program, paid, basis, sales, sales per dollar paid, months.
- One move: which creator to review first and what to change in the deal.

Never:
- Never change a creator's deal or stop a payment. A person does that.
- Never fill a missing payout with zero.
- Never add sales from creators, ads and attribution together.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creators-creator-and-affiliate-payout-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
