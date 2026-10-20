# Run this week's Meta creative test

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Run this week's Meta creative test" (id: do-meta-creative-test, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Runs a weekly creative test: one ad set per new creative at a small budget.
On day 4 it switches off the clear losers. On day 7 it moves winners into the main ad set and switches the test off.

What to read: The new creatives, your proven ads' copy and link, each test ad's spend and sales by day
What to give me: One small ad set per new creative, built in your Ads Manager, with day 4 and day 7 calls on what to switch off and what to move up

Synthesis tools to use:
- `cost_rules for=do-meta-creative-test`
- `meta_metric metric=ad_returns`
- `meta_metric metric=ad_destinations`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. If last week's test has ad sets ending this week, read them out first. Then ask in one message: the creatives, the budget per ad set (ask, there is no safe default), and the week start date. Show the total: ad sets times budget times 7.
2. Call `meta_metric` with `metric=ad_destinations`, `active_only=true` and `days=14` to pick a working website ad and its link. Call `ad_health_check` with `ads={"ad_ids": ["<that ad>"]}` for its link tags. No read returns ad text or headline, so copy them from that ad in Ads Manager.
3. In Ads Manager, make one campaign named the way the person names tests (ask, default "Creative Test - week of <date> - Claude"). Name ads "TEST <kind> - <name> - Claude".
4. Statics and videos go in separate ad sets. Meta's Creative testing button does not appear on new draft ad sets, so build by hand.
5. Finish one single-ad ad set first. Then use the tree menu Quick duplicate on that ad set only. A copy of a bigger ad set copies all its ads, so delete down to one before publishing. Then swap media in the 3 Edit group slots, set the thumbnail to Manual and rename.
6. Turn off AI enhancements, music, promo codes and email sign-up offers in each ad. No Amazon logo or stars on a website ad.
7. Draft ads show no ids and cannot be filtered by ad set. Read an ad's id from its Action menu link.
8. If the structure differs from what the person expected, say so before publishing.
9. Publish only these rows. Never the global Review and publish. Decline any budget raise Meta offers, then re-read every ad set budget.
10. Read back: call `ad_health_check` with `ads={"campaign_id": "<id>"}`. Every ad set on, one ad each, at the agreed budget, tags on, Meta's automatic changes off. Fix any fail before it spends. It cannot see promo codes or the email offer, so check those in the edit screen.
11. Day 4: call `meta_metric` with `metric=ad_returns` for closed days. Do not judge from the read-back, which counts today. Switch off an ad set that spent past the no-sale line with no sale. Read the line as `no_sale_cap` from `ad_health_check`, and ask only if it is missing. To switch it off, use `ad_change` then `ad_change_apply` when this connection offers them. Otherwise use the browser.
12. Day 7: an ad with 4 or more sales at or under the keep line moves up through do-meta-graduate-winners. If it is already copied into the main ad set, say so and do not copy it twice. Switch the rest of the test off.
13. Call `log_decision` with `kind=campaign` at launch and at each readout.

Checks before answering:
- Safe test run: when asked to test the shortcut, build one ad set and leave it off. Read it back.
- Spend: the yes covers the weekly total, ad sets times budget. If the person wants total spend flat, cutting the main ad set needs its own yes on that number.
- The keep line is `keep_line` from `ad_returns`. Ask only when `rules_set` is false. Never borrow another brand's.
- A creative with no spend by day 4 was starved, not judged. Say so.

Output:
- At launch: one line with ad sets, budget each, weekly total, live or off.
- Day 4 and day 7: each creative's spend, sales, cost per sale and the call made.
- What moved up and what was switched off.

Never:
- Never edit live winners in the main ad set.
- Never switch on more ad sets than the approved total covers.
- Never call a winner on fewer than 4 sales.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-creative-test". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
