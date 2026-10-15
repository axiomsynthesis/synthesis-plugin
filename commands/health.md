---
description: "Is all my data fresh?: Every connected source checked, and a short list of anything stale or broken, with the fix"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Is all my data fresh?

Channel: Data · Level: On a schedule · Status: Ready now
Schedule: every weekday 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Is all my data fresh?" (id: data-health-check, Data).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Each morning it checks every connected source and lists anything stale or broken, with the fix. If all is well it says so in one line.

What to read: All connectors
What to give me: Every connected source checked, and a short list of anything stale or broken, with the fix

Synthesis tools to use:
- `data_freshness`
- `data_freshness_sweep`
- `warehouse_freshness`

Steps:
1. Call `data_freshness` for the newest data date of each connected source.
2. Call `data_freshness_sweep` with `stale_days=3` for every built table and whether it is stale.
3. Call `warehouse_freshness` for the last sync of each mirrored table and any error on the last run.
4. List each problem with the source, the last good date, and the fix: reconnect, wait for a delayed sync, or tell us.

Checks before answering:
- Judge by the newest data date, not the time a table was written. A rebuilt table can look fresh with old data.
- A source with no sales for days may just be quiet. Check its newest record before calling it broken.
- If a check itself fails, say the check failed. Never report "all healthy" from an empty read.

Output:
- One line first: all current, or how many sources need attention.
- A short list: source, last good date, days behind, fix.

Never:
- Never reconnect or change a connection. A person does that.
- Never hide a stale source because the rest look fine.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: data-health-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (every weekday 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
