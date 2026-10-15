# One-page strategy: the problem and the plan

Channel: Strategy · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "One-page strategy: the problem and the plan" (id: ops-strategy-kernel, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Writes a strategy in three linked parts: what the real challenge is, the approach for dealing with it, and a handful of actions that reinforce each other. Its job is to cut a long list of initiatives down to the few that fit the diagnosis.

What to read: Operating condition of each key metric, the biggest constraint, and the current list of initiatives
What to give me: A sharp diagnosis of your main challenge, one guiding approach, and a few actions that support each other

Synthesis tools to use:
- `diagnose_state_map metrics=[...]`
- `strategy_framework framework=binding_constraint`
- `strategy_framework framework=priority_score`
- `export_docx`

Steps:
1. Call `diagnose_state_map metrics=[...]` with revenue, new customers, repeat share and margin series to find the weakest areas.
2. Run `strategy_framework framework=binding_constraint` with the brand's scored dimensions to name the constraint that caps the rest.
3. Write the diagnosis in two sentences with the numbers.
4. Ask for the current initiatives list. Run `strategy_framework framework=priority_score items=[{name, death_prox, rev_impact, time_sens, ease}]` on it.
5. Keep three to five actions that directly address the diagnosis and do not compete for the same cash or people.
6. Write it with `export_docx` as one page.

Checks before answering:
- The diagnosis must name a specific challenge with a number, not a goal ("grow 30%" is a goal).
- Each action must link to the approach in one sentence. Drop any that does not.
- Scores in the priority step are judgement. Label them.

Output:
- One-page Word document: Diagnosis, Approach, Actions, What we stop doing.
- Two lines in chat: the diagnosis and the first action.

Never:
- Never copy any book's text. Use plain words for the method.
- Never list more than five actions.
- Never start an initiative.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-strategy-kernel". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
