---
description: "Audit my whole Meta account: One change list ranked by money at stake: each ad or ad set by name and id, what it is now, what to change, the undo"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Audit my whole Meta account

Channel: Meta · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Audit my whole Meta account" (id: meta-whole-account-audit, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Reads the whole live Meta account and hands over one change list.
It covers placements, links, duplicates, who the spend really reaches, and return by ad for ads that send people to Amazon.
It changes nothing. Each change on the list is then made one yes at a time, with the budget or switch-on-off automations.

What to read: Every live Meta ad: placements, links and tracking tags, duplicates across campaigns, who the money really reaches, and return by ad for ads that send people to Amazon
What to give me: One change list ranked by money at stake: each ad or ad set by name and id, what it is now, what to change, the undo

Synthesis tools to use:
- `cost_rules for=meta-whole-account-audit`
- `ad_health_check only=[meta]`
- `meta_metric metric=ad_destinations`
- `meta_metric metric=breakdown dimension=age_gender`
- `meta_metric metric=amazon_ads`
- `meta_metric metric=ad_returns`

Steps:
1. Ask which account (your own or an agency's) and which lens, if not all: placements, links, returns or structure.
2. Call `ad_health_check` with `only=["meta"]` for the account-level checks and their dollars at stake.
3. Call `meta_metric` with `metric=ad_destinations`, `active_only=true` and `days=14` for links. It covers the top 40 spenders only, so say how much spend that is. Flag site-bound and Amazon-bound ads mixed in one ad set.
4. For each live campaign, call `ad_health_check` with `ads={"campaign_id": "<id>"}` and `only=["placement_fit","tracking_tags"]`. Flag tall-only videos and links with no tags.
5. Call `meta_metric` with `metric=breakdown` and `dimension=age_gender`. It is all-time and takes no days, so say so. Recent reach is could not check.
6. Call `meta_metric` with `metric=amazon_ads` and page with `result_page`. Ask the bar per product, default 1.0 on `roi_after_bonus`. This week and `roas_last_week` must both miss before a cut. Amazon credits sales for 14 days, so re-read new ads later. Leave out the "Ads not linked to Amazon yet" line and big sale days.
7. Call `meta_metric` with `metric=ad_returns` and `limit=50` for site-bound winners and losers. Page with `result_page` until every ad is read.
8. Find the same ad running in more than one campaign. One ad should live in one campaign. A copy in an agency's campaign may be on purpose, so mark it for the agency's word. An ad with no name or campaign is checked in Ads Manager.
9. Write one row per change: ad or ad set name and id, now, proposed, money at stake a week, undo.

Checks before answering:
- Totals tie to the account's spend for the same window. Never mix a 7-day and a 14-day total. Say the gap.
- A large read can hit Meta's reading limit. A read that failed or came back partial is "could not check", never "nothing found".
- An empty Amazon return read can mean the attribution link is missing. Say which.
- Same-day video numbers are still filling in. Use closed days.
- Safe test: nothing is written, so a test run is the same read. Run it on one ad account first if asked.
- Spend check: every proposed raise or switch-on shows its added daily spend. The list never raises total spend without saying so.
- An agency's own return figure may use a different formula. Compare like with like.

Output:
- One line first: live ads read, spend covered, and money a week at stake on the list.
- The change list, ranked by money at stake, about 5 to 15 rows.
- What could not be checked, one line each.
- Next step: which rows to send to the budget or switch-on-off automation first.

Never:
- Never change anything in the account. This one only reads.
- Never change an agency's account without a yes from the person.
- Never cut an Amazon-bound ad on Meta's own sales figure.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-whole-account-audit". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
