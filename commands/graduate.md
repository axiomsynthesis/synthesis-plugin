---
description: "Move winning test ads into the main campaign: Proven test winners copied into your main or winners ad set as existing-post ads, or a raise on the winner's own ad set, read back after"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Move winning test ads into the main campaign

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Move winning test ads into the main campaign" (id: do-meta-graduate-winners, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Finds test ads that have earned a bigger budget and moves them where the money is.
It copies each winner into your main campaign or winners ad set, or raises the winner's own ad set instead.
It also moves a mis-filed ad to the right campaign. Then it reads every copy back.

What to read: Recent cost per sale and sales for every live test ad, your main campaign and winners ad set
What to give me: Proven test winners copied into your main or winners ad set as existing-post ads, or a raise on the winner's own ad set, read back after

Synthesis tools to use:
- `cost_rules for=do-meta-graduate-winners`
- `meta_metric metric=ad_returns`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. Call `meta_metric` with `metric=ad_returns` and read every page with `result_page`. Winners are ads it marks winning: enough sales under the brand's own keep line. If the brand has no keep line, ask for one. Never borrow another brand's.
2. Drop any winner already copied into the target or main set, by the same name plus " - Copy" or the same post. Report that copy's spend and cost per sale instead of copying again.
3. For the main ad set's 7-day cost per sale, use its row in the same result's ad set list. A winner should beat it or match it.
4. Look at the target set's earlier copies. If one has near zero spend, or the set is over the keep line, warn that new copies will likely starve.
5. Call `ad_health_check` with `ads={"ad_ids": ["<winner id>"]}` to read each winner's ad set end date. If it ends within 2 days, raising in place is not an option. Copy instead.
6. Ask in one message: which ads, the target ad set, and copy or raise in place. Raising the winner's own ad set about 20% often works better than a copy, and goes through the budget yes.
7. To copy, use "Use existing post" with the original ad's post id, so likes and comments carry. Switch the post picker off the Partner Content tab first. A creator's post that is only a partner post may not show at all. Then use step 9.
8. Existing-post ads drop the ad's tracking tags. Re-add the brand's tracking template on every copy. If you use Meta's Copy and paste instead, do both in one page session.
9. Copies between campaigns with different goals or catalog setups are refused. Quick-duplicate an ad inside the target set and swap media instead. Meta refuses new copies of tall-only 9:16 videos under all placements, so use the existing post or a 4:5 version.
10. Name copies with the original name plus " - Copy". Do not add a second " - Claude". Keep any creator tag such as trybe=<id> in the name and the link. An ad that sent people to Amazon gets the website page link and tags.
11. Turn off Meta's standard enhancements, promo codes and any email sign-up offer on each copy. Keep the originals running unless the person says otherwise.
12. Publish from the ad's own preview. Never the global Review and publish. Decline any budget raise Meta offers.
13. Read back: call `ad_health_check` with `ads={"ad_ids": ["<new id>"]}`. Each copy on, in the target set, tags present. An existing-post copy hides its link from the data, so check the link by eye.
14. Call `log_decision` with `kind=campaign`, `measure` and `made_on`: which ads moved, where, and a spend-share check in 2 days.

Checks before answering:
- Safe test run: when asked to test the shortcut, copy one winner into an ad set that is off, publish it off and read back its post id and tags. Leave it off.
- Spend: a copy into an existing ad set adds no budget. A raise needs the person's yes on the new dollar figure, shown beside the old one.
- A winner on 3 days of data may be luck. Say how many sales it rests on.
- After 2 days, check each copy's spend share. A copy with near zero spend did not graduate.

Output:
- One line: how many ads moved, where, and the route used.
- Each ad: sales and cost per sale that earned it, the copy's status, tags present.
- Ads left in test and why.

Never:
- Never move an ad that has not met the brand's keep line.
- Never switch off the original unless the person asked.
- Never raise a budget past the number the person approved.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-graduate-winners". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
