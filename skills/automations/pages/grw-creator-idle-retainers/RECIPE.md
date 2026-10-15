# Creators you pay who don't post

Channel: Creators · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Creators you pay who don't post" (id: grw-creator-idle-retainers, Creators).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Lists creators under contract who did not post, or posted far below the videos they owe, set against what they are paid each cycle. These are the easiest dollars to recover in a creator program.

What to read: Creator roster, contracts, posting against quota, and retainers
What to give me: Creators on retainer who posted nothing or missed quota, with the money at stake

Synthesis tools to use:
- `growi_roster_health months=6`
- `growi_post_compliance`
- `growi_top_creators limit=50`

Steps:
1. Pull `growi_roster_health months=6` for the enrolled, contracted, posted and earning funnel.
2. Pull `growi_post_compliance` for posted vs not posted per window against contracted quota and retainer.
3. Pull `growi_top_creators limit=50` for each creator's retainer and contract status.
4. List contracted creators with no post in 30 days, and those under half their quota in 90 days, with retainer per cycle.

Checks before answering:
- Posting windows overlap. Never add the 7, 30 and 90 day counts.
- Lifetime, dated and per-cycle figures never divide into each other. Only compare numbers over the same dates.
- A blank or zero cost field means the cost is not stored there, never that nothing was paid.
- If the creator platform is not connected, say so. Never report zero creators.

Output:
- Answer first: retainer dollars per cycle tied to idle creators. Table: creator, contract status, quota, posts in 30 days, posts in 90 days, retainer per cycle, move.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never contact a creator or end a contract. A person does.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-creator-idle-retainers". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
