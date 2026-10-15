# Make the Google Ads changes for me

Channel: Google · Level: Push live · Status: Needs access we don't have yet

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Make the Google Ads changes for me" (id: grw-google-bid-budget-push, Google).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Turns the Google recipes' advice into one exact change list: budget moves, negative keywords, product exclusions. Today a person applies it in Google Ads. With write access it would apply only the approved lines and log each one.

What to read: Google Ads campaigns and the moves other Google recipes recommend
What to give me: A prepared change list, applied in Google Ads once you approve it

Synthesis tools to use:
- `google_ads_metric metric=campaign_performance days=30 limit=50`
- `google_ads_metric metric=search_terms days=30 limit=200`

Steps:
1. Collect the moves from the Google recipes in this session.
2. Pull `google_ads_metric metric=campaign_performance days=30 limit=50` so each line carries today's value.
3. Write each line as campaign id, field, from, to, reason, check date.
4. For negative keywords, pull `google_ads_metric metric=search_terms days=30 limit=200` and confirm each term has spend and no conversions.
5. Hand the list over for approval.

Checks before answering:
- Every line keys on an id.
- No budget line rises more than 30% in one step.

Output:
- A table and, when asked, a spreadsheet via `export_xlsx` named google-ads-changes-<date>.xlsx.

Never:
- Nothing changes in any live account. A person on your team makes every change.
- Never apply any line a person has not approved.
- Never fill a missing, gated or empty number with an estimate. Say what is missing and why.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: grw-google-bid-budget-push". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (needs access we don't have yet): Write access to Google Ads is not connected to Synthesis. Today a person applies the list. Do the parts you can and say plainly what is missing.
