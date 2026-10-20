---
description: "Test a new landing page on Meta: A Meta test for one landing page, built in your Ads Manager, switched on after your yes, with every link and budget read back"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Test a new landing page on Meta

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Test a new landing page on Meta" (id: do-meta-page-test, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Launches a Meta test for one new landing page in its own campaign.
It copies your proven campaign, puts the same top ads in one ad set and points every ad at the new page.
It switches on after your yes, then reads every link, budget and switch back.

What to read: Your proven Meta campaign, your top ads by recent cost per sale, the new page
What to give me: A Meta test for one landing page, built in your Ads Manager, switched on after your yes, with every link and budget read back

Synthesis tools to use:
- `cost_rules for=do-meta-page-test`
- `web_fetch`
- `meta_metric metric=ad_returns`
- `meta_metric metric=ad_destinations`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. Read your existing test names first and offer the next free number. Then ask in one message: the page link, daily budget (ask, default $100), end date (ask, default about 10 days out), how many ads (ask, default your top 5) and the test number.
2. Call `web_fetch` on the page link. Stop if it does not open, shows the wrong product, or its price differs from the store price (ask if you cannot read it). Stop if it is the page your control campaign already links to: then the test has no difference to measure.
3. Call `meta_metric` with `metric=ad_returns`. The result comes in pages and is ordered by verdict, not cost per sale. Read every page with `result_page`, keep only the control ad set's rows and sort them yourself. Reuse those ads, so the page is the only difference.
4. Call `meta_metric` with `metric=ad_destinations`. An ad whose type is SHARE is an existing post. Its link and media cannot be changed, so rebuild it as a new ad. Its likes will not carry.
5. In Ads Manager, duplicate the proven campaign with Advantage+ recommendations unticked. Keep goal, pixel, audience, placements and attribution. Check the ad set goal did not switch to Messages. The copy carries every ad in the set, so delete all but the picked ads first.
6. Name it the way the person names tests (ask, default "Test N - <page> page - Claude"). Everything you build ends in "- Claude".
7. Edit each ad's Website URL one at a time, never bulk edit. Use the page link plus the tags from an ad that the ad check shows carrying them. If none does, use source facebook, medium paid_social, and campaign, content and term set to the campaign, ad and ad set names.
8. In each ad, untick "Personalize buyer journey" and "Show existing reactions". Turn off Shop destination, promo codes, any email sign-up offer and Meta's standard enhancements. No Amazon logo or stars on a website ad.
9. Set the ad set budget and end date. One campaign per page, never an on-site split.
10. Publish by ticking only the new campaign's rows. Never use the global Review and publish, it re-ticks every draft. If "Publish draft items?" appears, choose Close.
11. Meta often raises the budget on publish. Decline, then re-read the ad set budget and any campaign budget and set them back.
12. Switch on only once the page is live and the person said yes to the page and the dollar figure. Then do not ask again.
13. Read back: call `ad_health_check` with `ads={"campaign_id": "<new id>"}`. Every ad on, every link the new page with tags, end date set, only the picked ads left.
14. Call `log_decision` with `kind=campaign`, `measure`, `made_on`, the page, budget, end date and readout dates: first look about day 4, decision about day 10.

Checks before answering:
- Safe test run: when asked to test the shortcut, build the full copy and leave it off. Read it back and leave it off for the person to delete.
- Spend: the budget read back must equal the agreed number. Show daily budget times days before the yes.
- If the safety check blocks a budget edit, ask for the dollar figure in chat.
- If the page already runs an on-site split test, say so. Meta traffic will be split by it.
- If the structure differs from the proven campaign, say so before publishing.
- Small tests can be twice off on luck. They catch disasters, not small wins.

Output:
- One line: live or off, campaign name, daily budget, end date.
- Each ad: on or off, link right or wrong.
- Anything Meta changed that you set back, and the readout dates.

Never:
- Never touch other campaigns, other people's drafts or live winners.
- Never accept Meta's budget raise.
- Never switch on before the page is live.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-page-test". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
