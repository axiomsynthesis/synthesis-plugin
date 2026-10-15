# Protect your seller account

Channel: Amazon · Level: On a schedule · Status: Ready after we build it
Schedule: daily 7am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Protect your seller account" (id: mkt-amazon-account-health-watch, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
An account health problem can stop all your Amazon sales. Warnings often sit unread in Seller Central. This would watch them daily and raise anything new.

What to read: Amazon's account health rating, policy warnings, order defect rate, late shipment rate and listing compliance notices
What to give me: A daily alert when an account health number nears Amazon's limit or a new policy warning appears

Synthesis tools to use:
- `amazon_metric metric=return_reasons months=1`
- `amazon_metric metric=rating_watch days=30 limit=30`
- `data_freshness`

Steps:
1. Once the feed exists: read the account health rating, order defect rate, late shipment rate, cancellation rate and open policy warnings.
2. Compare each with Amazon's limit and with yesterday.
3. Call `amazon_metric metric=return_reasons months=1` and `amazon_metric metric=rating_watch days=30 limit=30` for early signs of defect-driven complaints.
4. Alert on any new warning or any number within 20% of its limit.

Checks before answering:
- Until the feed exists, never report an account health number. Say it cannot be read.
- Call `data_freshness` first. A stale Amazon sync must not read as "no warnings".

Output:
- Nothing if nothing changed.
- Otherwise: what changed, Amazon's limit, the deadline, and where in Seller Central.

Never:
- Never respond to Amazon or submit appeals.
- Never report "all clear" when the data could not be read.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: mkt-amazon-account-health-watch". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (daily 7am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.

Not fully ready yet (ready after we build it): No account health, policy warning or performance notification feed is synced. Needs Amazon's account health and notifications data added to the sync. Runs from your own Claude Code, so only while your computer is on. Do the parts you can and say plainly what is missing.
