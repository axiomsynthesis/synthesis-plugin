# Watch my competitors every day

Channel: Creative · Level: On a schedule · Status: Ready now
Schedule: Every day, morning

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Watch my competitors every day" (id: creative-watch-my-competitors, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads the ads your tracked rivals are running and tells you what is new.
An ad that keeps running for 30 days or more is very likely paying, so those are called out first.
New ads and changes since the last digest come next.

What to read: Your tracked rivals' live Meta and TikTok ads, and this week's top TikToks in your category
What to give me: A short daily digest: rival ads that just passed 30 days running, ads that started this week, and what changed

Synthesis tools to use:
- `competitor_ads`
- `competitor_ads view=tiktok_trends`

Steps:
1. Call `competitor_ads` with `min_days=30` for the rival ads that have run 30 days or more.
2. Call `competitor_ads` with `new_days=1` for ads that started since yesterday, then with `new_days=7` for the week.
3. Call `competitor_ads` with `view=tiktok_trends` for this week's most-liked category videos.
4. Compare with the last digest if you have it in this chat. Name what crossed 30 days, what is new and what stopped.
5. For each long runner, write one line: the rival, the hook, the format, days running and the ad link.

Checks before answering:
- Read `status` first. If the watch is not switched on, has not run or failed, say that. It is never "no new ads".
- The rival pull refreshes once a week. On days with no new pull, say "no new pull since <date>" instead of "nothing new".
- Ad libraries show no spend. Never state a rival's spend or results.

Output:
- One headline line: how many long runners and how many new ads.
- Up to 5 long runners and up to 5 new ads, one line each with the ad link.
- One line on what to test from it, and the hook it would beat.

Never:
- Never copy a rival's claim into an idea. Use the angle, not the words.
- Never guess spend, results or targeting for a rival ad.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-watch-my-competitors". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- This is meant to repeat (Every day, morning). Run it once now. If you can set up a repeating task here, do it. If not, tell me how to run this again each time it is due.
