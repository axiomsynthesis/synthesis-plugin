# How is this ad set going?

Channel: Creative · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "How is this ad set going?" (id: creative-how-is-this-ad-set-going, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads one ad set and tells you whether to keep it, fix it or switch it off.
It shows where the funnel breaks against your own average and which ad inside it is tiring.

What to read: One Meta ad set's spend and return, its ads' funnel and fatigue, your hook ranking
What to give me: Keep, fix or kill for one ad set, with where its funnel breaks and which ad is tiring

Synthesis tools to use:
- `meta_metric metric=adset_performance`
- `meta_metric metric=creative_fatigue_curve`
- `meta_metric metric=ad_microfunnel`
- `winning_hooks`

Steps:
1. Ask which ad set. If none is named, call `meta_metric` with `metric=adset_performance` and offer the three biggest by spend.
2. Read the chosen ad set's spend, sales and return from `meta_metric` with `metric=adset_performance`.
3. Call `meta_metric` with `metric=ad_microfunnel` for its ads' stop, hold, click and buy rates.
4. Call `meta_metric` with `metric=creative_fatigue_curve` for each of its ads to see which is tiring.
5. Call `winning_hooks` with `read_new=false` for the account average and each ad's hook.
6. Say keep, fix or kill, and the one change that would move it.

Checks before answering:
- Use closed days only. Today is still filling in.
- An ad set sending shoppers to Amazon cannot be judged on Meta purchases. Say so and use the Amazon return from `winning_hooks`.
- Too little spend to judge is "too early", never "losing".

Output:
- One headline line: keep, fix or kill, with spend and return against your average.
- Where the funnel breaks, in one line.
- The tiring ad, if any, and the one change to make.

Never:
- Nothing is changed in Ads Manager. You make the change.
- Never compare against another brand's numbers. Your own average is the bar.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-how-is-this-ad-set-going". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
