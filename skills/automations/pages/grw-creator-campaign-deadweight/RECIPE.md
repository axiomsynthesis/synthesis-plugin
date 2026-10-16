# Close creator campaigns that sell nothing

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Close creator campaigns that sell nothing" (id: grw-creator-campaign-deadweight, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Creator programs pile up campaigns. This finds the ones with enrolled creators and committed retainers that have produced no revenue, so you can close them or fix the brief.

What to read: Creator campaign enrolments, earnings and retainers by campaign
What to give me: Campaigns carrying creators and retainers with no sales, to close or fix

Synthesis tools to use:
- `growi_metric metric=campaign_performance limit=50`
- `growi_metric metric=creator_payouts months=6`

Steps:
1. Pull `growi_metric metric=campaign_performance limit=50`.
2. Flag campaigns with creators enrolled, retainers committed and no creator earning.
3. Pull `growi_metric metric=creator_payouts months=6` for what was actually paid against creator sales over the same dates.

Checks before answering:
- Lifetime, dated and per-cycle figures never divide into each other. Only compare numbers over the same dates.
- A blank or zero cost field means the cost is not stored there, never that nothing was paid.
- Retainers are per payout cycle and revenue is lifetime. Show them side by side, never as a return ratio.

Output:
- Answer first. Table: campaign, creators enrolled, earning creators, lifetime revenue, retainer per cycle, move.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-creator-campaign-deadweight". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
