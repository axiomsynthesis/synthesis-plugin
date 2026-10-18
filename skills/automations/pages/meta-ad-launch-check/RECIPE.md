# Check the ads I just launched

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Check the ads I just launched" (id: meta-ad-launch-check, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Checks each Meta ad made in the last few days, one by one, the way a careful media buyer would before it spends.
It checks that the video and the landing page sell the same product, the page opens, the link carries tracking and creator tags, the name follows the brand's rule, the video fits each placement, Meta's automatic add-ons are off, the ad, ad set and campaign are all on, the ad set has not ended, no video runs twice, cost per sale sits inside the brand's own lines, and Amazon-bound links carry their attribution tags.
The server decides every result as pass, fail, unknown or not applicable, with the exact fix.

What to read: Each new Meta ad's video, link, landing page, tracking and creator tags, name, placements, switches, end date and sales so far
What to give me: Every new ad checked one by one: what to fix before it spends, what to fix while it runs, and what could not be checked

Synthesis tools to use:
- `cost_rules for=meta-ad-launch-check`
- `ad_health_check`

Steps:
1. Call `ad_health_check` with `ads={}` to check every ad made in the last 3 days, or `ads={"adset_id": "<id>"}` for one ad set, or `ads={"campaign_id": "<id>"}` for one campaign.
2. If someone gave ad ids, call it with `ads={"ad_ids": ["<id>", "<id>"]}` instead (up to 60).
3. If the ad's edit screen is open in a browser, read the "email sign-up offer" and "promo codes" boxes and the product the video shows, and pass only what was actually seen in `ads.seen_in_tab`.

Checks before answering:
- Use each result as the server decided it. Never turn an unknown into a pass.
- An unknown product means the video's name and title say nothing about it. Say so and ask someone to watch the first seconds; never guess from the ad copy.
- "Too early" on sales is not a failure.
- A brand with no money lines gets cost per sale shown, not judged. Do not judge it with another brand's numbers.

Output:
- One line first: how many ads, how many to fix before they spend, how many ready.
- Each ad to fix before it spends, with its exact fix.
- The smaller fixes, grouped by kind.
- What could not be checked and how to check it, one line each.
- Under 20 lines in total.

Never:
- Never change, publish or switch on an ad. A person does that.
- Never say an ad is ready when one of its checks read unknown.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-ad-launch-check". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
