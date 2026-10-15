# What we believe vs what we've proven

Channel: Leadership · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What we believe vs what we've proven" (id: ops-beliefs-and-tests-review, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reviews the brand's working beliefs: which have been tested and held, which failed, and which have sat untested. It keeps the team from building plans on a belief that was disproved last quarter.

What to read: Hypotheses Synthesis holds for your brand, their status and test results
What to give me: A monthly list of what has been confirmed, what failed, and what is still untested about how your business works

Synthesis tools to use:
- `get_hypotheses`
- `record_hypothesis_result`
- `propose_hypothesis`

Steps:
1. Call `get_hypotheses` for every hypothesis with status, evidence and last update.
2. Group them: confirmed, failed, under test, untested.
3. For any under test whose check date has passed, pull the measured value with the named metric and record it with `record_hypothesis_result`.
4. Flag untested beliefs older than 60 days that a current plan depends on.
5. For a belief the person states that is not yet held, file it with `propose_hypothesis` including how it would be falsified.

Checks before answering:
- A hypothesis marked confirmed on fewer than six data points is weak. Say so.
- A result recorded on an unsettled period should be re-checked.
- Never mark a belief failed because the data was missing. That is "not measurable".

Output:
- Four short lists: Confirmed, Failed, Under test, Untested. Each item one line with its evidence.
- One line naming the untested belief that matters most to current plans.

Never:
- Never delete a hypothesis.
- Never turn a hypothesis into a fact without a recorded test.
- Never act on a belief on the person's behalf.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-beliefs-and-tests-review". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
