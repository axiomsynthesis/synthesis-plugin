# Go deep on one big decision

Channel: Strategy · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Go deep on one big decision" (id: ops-deep-decision-run, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
For a decision too big for a quick answer (a large stock bet, a price move across the range, a new channel), this runs the deep synthesis chain: it pulls the data, has separate analysts look at it, challenges the draft, and simulates outcomes. The result is a written recommendation the founder can read and forward.

What to read: Everything relevant in your connected data, run through the multi-step deep synthesis chain
What to give me: A checked recommendation on one high-stakes question, with the evidence, the strongest case against, and a range of outcomes

Synthesis tools to use:
- `deep_synthesis step=start question=<question>`
- `deep_synthesis step=result job_id=<job>`
- `run_scenario`
- `export_docx`

Steps:
1. Help the person state the decision as one question with the options and the amount at stake.
2. Call `deep_synthesis step=start question=<question>` as the first action. Do not pull data separately first.
3. Follow the chain's steps as it asks, then call `deep_synthesis step=result job_id=<job>`.
4. If the chain did not simulate the decision, run `run_scenario` with the matching type (inventory_bet, price_change, budget_shift or spend_scale) on inputs the chain produced.
5. Write the recommendation with `export_docx`: question, answer, evidence, the case against, the range of outcomes, and how we will know.

Checks before answering:
- Count the analysts that actually ran against those planned. If some failed, say the answer is partial.
- If the challenge step did not run, say the answer was not challenged.
- Every number in the write-up must come from the run or a tool call. No figure from memory.
- Deep runs take minutes and cost more than a normal answer. Use them for big decisions only.

Output:
- A Word document of one to two pages with the sections above.
- Three lines in chat: the answer, the main risk, and the measure to watch.

Never:
- Never carry out the decision.
- Never skip the chain by assembling the answer from separate tools when the person asked for a deep run.
- Never present a partial run as complete.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-deep-decision-run". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
