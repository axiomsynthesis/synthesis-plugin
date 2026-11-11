---
description: "Client performance update: The finished client update as a PDF, a Word copy for your notes and a spreadsheet: every number against the period before and what needs a person"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Client performance update

Channel: Agency · Level: Prepare · Status: Ready now
Schedule: Twice a month on the 3rd and 18th, or every Monday for a weekly client, once switched on

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Client performance update" (id: agency-client-update, Agency).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Hands back the update an agency sends its client, finished: the same fixed page for every brand, as a PDF, with a Word copy for the team's notes and a spreadsheet of every table. Twice a month covers the 1st to 15th or the 16th to month end; weekly covers Sunday to Saturday. Every figure is set against the period just before. Buyers who came back are read from orders up to yesterday. Profit and product cost are never in it.

What to read: Amazon sales, visits and Buy Box by day and product, sponsored ads, search share, rank, stock, orders, Subscribe and Save, returns
What to give me: The finished client update as a PDF, a Word copy for your notes and a spreadsheet: every number against the period before and what needs a person

Synthesis tools to use:
- `switch_brand`
- `amazon_metric metric=client_update_report cadence=semimonthly period_end=YYYY-MM-DD`

Steps:
1. Call `switch_brand` with no arguments. If it is not the client named, call `switch_brand` with that client's brand id.
2. Pick the period. "Oct 16 to 31" is `period_end=2026-10-31`; "Oct 1 to 15" is `period_end=2026-10-15`; a week ends on its Saturday with `cadence=weekly`. Leave `period_end` out for the last complete period.
3. Call `amazon_metric` with `metric=client_update_report`, the `cadence` and the `period_end`.

Checks before answering:
- If the result has `error`, say it in plain words and stop. No file was made.
- If `partial` is true, say traffic is still filling in and when to run it again (two days after the period ends).
- The server wrote every word and number on the page. Do not rebuild the tables or reword the page.
- Read `not_in_this_update` out as it is. A section that could not run is never "nothing to report".

Output:
- One line first: the result's `summary`.
- The five lines of `to_look_at`, as a short list.
- The PDF link (`download_url`), the Word copy (`word_url`) and the spreadsheet (`spreadsheet_url`).
- One line naming what is not in this update, from `not_in_this_update`.

Never:
- Never send the update to the client. It is a draft for the agency's team, who add what they changed and send it.
- Never add profit, margin or product cost to it.
- Never fill a missing section with a guess.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: agency-client-update". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- If you could not finish, open your answer with "Stuck:" and what I need to do. If your answers are not saved for you automatically, save this one with the Synthesis tool `capture_turn`: my request as `question`, your answer as `answer`, and `context` starting with "automation: agency-client-update".

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
