# Check my ads

Channel: Growth · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Check my ads" (id: ads-health-check, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs one health check across every ad platform the brand has connected, instead of one platform at a time.
It reads which platforms are connected and current, then runs 15 fixed checks: wasted searches on Amazon and Google, efficient Amazon campaigns out of budget, ads on products about to run out or without the Buy Box, Meta purchase tracking, ad sets too small to learn, new-ad cadence, ads Meta rates below average, spend not aimed at a sale, frequency by campaign role, non-brand Google searches, the TikTok connection, tired TikTok ads, and platform spend against the books.
The server decides every result as pass, fail, unknown or not applicable, with the dollars a month and the numbers and dates behind it.
Failures come ranked by dollars, with a coverage line per platform instead of a score.

What to read: Every connected ad platform (Amazon ads, Meta, Google Ads, TikTok ads), stock, the Buy Box, online store orders and the books
What to give me: One health check across every ad account: what failed, ranked by dollars a month, what could not be read, and the three fixes to make first

Synthesis tools to use:
- `cost_rules for=ads-health-check`
- `ad_health_check`

Steps:
1. Call `ad_health_check` with no arguments. It takes 20 to 45 seconds and reads every connected platform.
2. To recheck one platform after a fix, call `ad_health_check` with `only=["meta"]`, or another platform: amazon_ads, google_ads, tiktok_ads or books.
3. For each of the top three fixes it returns, open the recipe it names to build the change list.

Checks before answering:
- Use the result as the server decided it. Never turn an unknown into a pass, and never re-judge a fail.
- Unknown means the data was missing, empty, stale or too thin. Say which checks could not be read and why, in one line each.
- Where a platform says "not enough data to judge", give no verdict for that platform.
- Each dollar figure says what it measures: some are money wasted, some are spend exposed to a problem. Never add them up as savings.
- Not applicable means the platform is not connected or the thing checked does not exist for this brand. Do not list those as passes.

Output:
- One line first: the headline the tool returned.
- A table of failures in the order returned: platform, check, dollars a month, what the number measures, why.
- The coverage line, then one line per platform with its verdict.
- The top three fixes, each with the recipe that builds its change list.
- Under 20 lines in total.

Never:
- Never give a 0 to 100 score or a grade. The coverage line replaces it.
- Never change anything in an ad account. A person does that.
- Never say an ad account is healthy when checks could not be read.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ads-health-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
