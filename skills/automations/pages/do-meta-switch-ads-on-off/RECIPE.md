# Switch Meta ads on or off for me

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Switch Meta ads on or off for me" (id: do-meta-switch-ads-on-off, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Switches named Meta ads, ad sets or finished test campaigns on or off.
It works from the person's word, or from the stop rules agreed for a named test.
When most of an ad set goes off, it also proposes a lower budget, so the money does not just move to the rest.

What to read: Each named ad, ad set or campaign with its live status and spend and sales over the last 7 closed days, against the brand's stop rules
What to give me: The ads, ad sets or finished tests you named switched on or off, every row read back live, with leftover copies checked

Synthesis tools to use:
- `cost_rules for=do-meta-switch-ads-on-off`
- `meta_metric metric=ad_returns`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. If the person asks "is it live?", answer that first from a live read.
2. Ask which rows and on or off, or "apply the stop rules" to a named test. Ask the stop rules. Default: a test ad goes off at the no-sale line with no sale (`no_sale_cap` in `ad_health_check`). Default keep: at or under the keep line per sale after 4 sales.
3. Call `meta_metric` with `metric=ad_returns` and `limit=50` for 7-day spend, sales and cost per sale per row.
4. Call `ad_health_check` with `ads={"adset_id": "<id>"}` and `only=["switched_on","duplicates"]` for each ad set touched. It shows every copy that is on or off. A paused copy flagged "switch the ad on" is expected. Leave it off.
5. Show the plan: each row, on or off, spend, sales, why. Add the ad set budget cut when most of it goes off. Proposals still waiting for a yes are listed, not done.
6. For a test the person already agreed, stop-rule offs and the agreed switch-on count as approved. Anything else needs a yes.
7. If your tools include `ad_change`, use it to switch off: call it with `action=propose` and the `items` to pause. Propose changes nothing in the account, so it can run before the yes. Show its list, then call `ad_change_apply` with the plan id and hash after the yes. It can switch back on only what Synthesis switched off, through `action=undo`.
8. Otherwise use Ads Manager in the browser. Filter to the named campaign. Find each row by its ad id, not its name, because one video can run in many campaigns. Click its toggle. Check the ad set rows as well as the campaign, because a row can sit "Ads off" inside a live ad set.
9. A budget cut goes through the budget cell's own Publish, never the global Review and publish.
10. Leave copies off. Never delete anything.
11. Call `ad_health_check` with `ads={"adset_id": "<id>"}` for each changed ad set to read every row's live switches.
12. Call `log_decision` with `kind=campaign`, what changed, and the day to look again.

Checks before answering:
- Every switched row reads back in the state planned, including leftover copies.
- Spend check: switching on raises spend. State the daily budgets now live against before. Never switch on spend the person has not seen.
- If a platform safety check stops a switch-on the person agreed, quote that yes once, then stop.
- Safe test, when asked for one: switch off, then back on, an ad that is already off inside an off test ad set. Show both steps and the unchanged end state.
- Judge stop rules on closed days. Today is still filling in.
- A Meta read error is not zero sales. Never switch anything off from missing data.
- If the ad returns verdict disagrees with the stop rule, show both and ask.

Output:
- One line first: what is now on, what is now off, and the daily spend now live.
- One row per change: name, before, after, read back, 7-day spend and sales.
- Rows left alone and why, one line.
- Next look: the date to check the remaining ads.

Never:
- Never delete an ad, ad set or campaign. Leave it off.
- Never put a product's videos into another product's campaign.
- Never switch on anything outside what was approved or agreed.
- Never touch an agency's campaign without a yes.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-switch-ads-on-off". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
