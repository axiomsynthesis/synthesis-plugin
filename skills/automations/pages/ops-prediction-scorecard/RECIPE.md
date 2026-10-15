# How often are our predictions right?

Channel: Leadership · Level: On a schedule · Status: Ready now
Schedule: monthly, 1st business day 9am

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How often are our predictions right?" (id: ops-prediction-scorecard, Leadership).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Keeps score on the brand's own forecasts. Each month it shows how often each kind of prediction came true and which are due to be checked. Over time it tells the founder which kinds of forecast deserve trust.

What to read: Every forecast and prediction registered for your brand, and the measured outcomes
What to give me: How often past predictions came true, by type, and which ones are due to be checked this month

Synthesis tools to use:
- `track_record include_cases=true cases_limit=30`
- `recall_decisions`
- `resolve_prediction`
- `get_calibration_for_claim`

Steps:
1. Call `track_record include_cases=true cases_limit=30` for resolved predictions by type, with hit rates and ranges.
2. Call `recall_decisions` for decisions linked to predictions.
3. List predictions whose horizon has passed and are still open.
4. For each due one, pull the measured value with the metric tool named in the prediction, then record it with `resolve_prediction` as correct, wrong or unmeasurable, with the value.
5. Call `get_calibration_for_claim` for the forecast types used most, to show the confidence they have earned.

Checks before answering:
- Resolve only against closed, settled periods. An estimate month cannot resolve a prediction.
- If the measured metric's definition differs from the prediction's, mark it unmeasurable rather than forcing a verdict.
- Fewer than five resolved cases in a type is too few for a hit rate. Say so.

Output:
- Table: Prediction type | Resolved | Right | Wrong | Hit rate | Range.
- A list of predictions due this month with their verdicts.
- One line on which forecast type to trust least.

Never:
- Never resolve a prediction on an unsettled number.
- Never delete or edit a past prediction.
- Never mark a prediction right without the measured value.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-prediction-scorecard". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (monthly, 1st business day 9am). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
