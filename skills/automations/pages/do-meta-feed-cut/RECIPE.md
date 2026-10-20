# Make feed-shape copies of my top ads

Channel: Meta · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Make feed-shape copies of my top ads" (id: do-meta-feed-cut, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Makes new feed-shape (4:5) copies of your top tall videos.
In each copy, Feeds get the 4:5 file and Stories and Reels keep the original 9:16.
The copies go in their own ad set. Your live winners are never edited.

What to read: Your top ads by recent cost per sale, and where each one is spending by placement
What to give me: New 4:5 copies of your top tall videos in their own ad set: Feeds get the 4:5 file, Stories and Reels keep the original

Synthesis tools to use:
- `cost_rules for=do-meta-feed-cut`
- `meta_metric metric=ad_returns`
- `meta_metric metric=creative_by_placement`
- `ad_health_check`
- `log_decision kind=campaign`

Steps:
1. Call `meta_metric` with `metric=ad_returns` and read every page with `result_page`. First look for a live feed-shape ad set, with "feed 4:5" in its name. If one is live, report its result and fix its ads instead of building another. Otherwise take the top website ads by recent cost per sale.
2. For each top ad, call `meta_metric` with `metric=creative_by_placement`, `ad_id` and `days=7`. Skip any ad that already spends most of its money on Feeds.
3. Ask in one message: which ads (ask, default the top 2 first, then up to 6), the target ad set, its daily budget if new, and a yes to download the source videos. A creator video that exists only as a partner post may have no file to download. Then ask for the file.
4. Crop each video to 4:5 with any video tool you can run here. Pick the crop per video so the captions stay inside it. A center crop trims about 15% top and bottom. Show the person a frame from each crop first. If no video tool exists, ask for 4:5 exports.
5. Keep each file under 10 MB, the browser upload limit. Re-encode first rather than stop.
6. In Ads Manager, duplicate the source ad into the target ad set. Remove media, Add video, pick the 4:5 file, Crop. Then use Vertical "Replace" to put the original 9:16 back for Stories and Reels.
7. Do not use the "up to 10 media" route with placement exclusions. It fails at publish.
8. Per-placement files have run in a campaign with ad set budgets. If publish refuses them, use a campaign with a campaign budget.
9. Set the thumbnail to Manual in every group. Name each copy "<ad> - feed 4:5 - Claude". Keep any creator tag such as trybe=<id>. Add the brand's tracking tags, since duplicate and swap drops them. Turn off enhance CTA, inline comments, standard enhancements, AI enhancements, music, promo codes and email sign-up offers.
10. Publish from each ad's own preview. Review and publish re-ticks every draft, so untick held drafts if you must use it. Decline any budget raise Meta offers, then re-read the budget.
11. Read back: call `ad_health_check` with `ads={"adset_id": "<id>"}`. Each copy on, video fits each placement, link and tags right, Meta's changes off.
12. Call `log_decision` with `kind=campaign`, `measure` and `made_on`. After 3 days, call `meta_metric` with `metric=creative_by_placement` and `ad_id` for each copy. If under half its spend is on Feeds, say the test failed to test feed shape.

Checks before answering:
- Safe test run: when asked to test the shortcut, build one copy named "<ad> - feed 4:5 - Claude TEST" in an ad set that is off, publish it off and read it back. Leave it off.
- Spend: a new ad set is new spend. Show daily budget times days and get a yes on the number.
- Meta may still send most spend to Stories. Then the test is a second budget for that ad, not proof 4:5 works. Say so.
- Downloading source videos needs the person's yes.

Output:
- One line: how many copies, which ad set, daily budget, live or off.
- Each copy: name, which file serves Feeds and which serves Stories and Reels.
- The date to read the placement split.

Never:
- Never edit a live winning ad. Only new copies.
- Never crop off captions or the product.
- Never raise a budget past the number the person approved.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-feed-cut". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
