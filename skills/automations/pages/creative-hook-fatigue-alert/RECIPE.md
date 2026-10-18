# Hook fatigue alert

Channel: Creative · Level: On a schedule · Status: Ready now
Schedule: Every Monday

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Hook fatigue alert" (id: creative-hook-fatigue-alert, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Watches the hooks that make you money and warns you when one starts to tire.
It compares this week with last week and points at the ad to refresh before the return falls.

What to read: Your winning hooks this week and last, and each top ad's fatigue curve
What to give me: A short alert when a winning hook's thumb-stop or return drops week over week, with the ad to refresh

Synthesis tools to use:
- `winning_hooks`
- `meta_metric metric=creative_fatigue_curve`
- `meta_metric metric=hook_rate`

Steps:
1. Call `winning_hooks` with `days=7` and `read_new=false` for this week's winners.
2. Call `winning_hooks` with `days=14` and `read_new=false`, and compare each winner's thumb-stop and return.
3. For each winner whose thumb-stop or return fell by a tenth or more, call `meta_metric` with `metric=creative_fatigue_curve` and the top ad's `ad_id`.
4. Call `meta_metric` with `metric=hook_rate` to confirm the drop is in the opening.
5. Name the ad to refresh and what to keep.

Checks before answering:
- Use closed days only. A week still settling on Amazon reads low; say so beside the number.
- Too little spend this week is "too early to tell", never "tired".
- No winner dropped: say "no winning hook is tiring this week" in one line.

Output:
- One headline line: how many winning hooks are tiring.
- For each: the hook, this week against last, the ad to refresh, and what to keep.

Never:
- Nothing is paused. You decide.
- Never call a hook tired on one day of data.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-hook-fatigue-alert". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (Every Monday). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
