# Does your agency's report hold up?

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Does your agency's report hold up?" (id: strategy-agency-check, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks the numbers in your agency's report against your own data. It shows where they agree, where they do not, and why, such as a different date range, credit window or sales definition.

What to read: Ads data, the agency's report
What to give me: Your agency's numbers checked against your own data: where they agree, where they don't, and why

Synthesis tools to use:
- `cost_rules for=strategy-agency-check`
- `search_files`
- `read_file`
- `meta_metric metric=roas`
- `amazon_metric metric=acos_tacos`
- `mer`
- `attribution_lenses`

Steps:
1. Call `search_files` with the agency's name or "agency report" to find the uploaded report, then `read_file` with its `file_id`.
2. Pull each headline number from the report with its date range and definition.
3. Call `meta_metric` with `metric=roas` and `amazon_metric` with `metric=acos_tacos`, each with `month` set to the report's month (`YYYY-MM`), for our own numbers. Both read whole months only, so for a report that covers part of a month, say the periods differ.
4. Call `mer` for the same period to get total sales against total ad spend.
5. Call `attribution_lenses` with the platform return and the blended return to show the gap between them.

Checks before answering:
- Match the date range and credit window before calling a number wrong.
- If the report is missing or unreadable, say so and stop. Never check against a guess of what it said.
- If our own read is empty, say that number is missing.

Output:
- One line first: whether the agency's headline holds up, and the size of any gap.
- A table: measure, agency number, our number, gap, likely reason.
- One move: the one question to put to the agency.

Never:
- Never send anything to the agency. A person does that.
- Never say the agency is wrong without naming the reason for the gap.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: strategy-agency-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
