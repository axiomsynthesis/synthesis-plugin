# What's working on Meta, and what to cut

Channel: Meta · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "What's working on Meta, and what to cut" (id: meta-ads-strategy-review, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Says what is working on Meta, what to cut, and where the next dollar should go.
It reads results the way Meta cannot, including the sales Meta drove on Amazon.
It ranks campaigns by real return and names one budget move and one creative test.

What to read: Meta ads, Amazon sales, website orders
What to give me: Keep, cut or grow for every campaign, counting the sales Meta drove on Amazon, plus one test

Synthesis tools to use:
- `cost_rules for=meta-ads-strategy-review`
- `meta_metric metric=campaign_performance`
- `meta_metric metric=creative_leaderboard`
- `amazon_metric metric=attribution_sources`
- `mer`
- `attribution_lenses`

Steps:
1. Call `meta_metric` with `metric=campaign_performance` to get spend and Meta-reported return by campaign. It covers each campaign's whole life, not the last 30 days, so say that.
2. Call `amazon_metric` with `metric=attribution_sources` and `days=30` to add the Amazon sales tracked back to Meta.
3. Call `mer` for the latest closed month to get the blended return on all ad spend.
4. Call `attribution_lenses` with the platform return and the blended return to see how much Meta's own number overstates.
5. Call `meta_metric` with `metric=creative_leaderboard` to find the creative that should get the test. It always covers the last 30 days.

Checks before answering:
- Meta's last 7 days are still filling in. Judge on closed days.
- If the Amazon tracking read is empty, say Amazon sales from Meta could not be counted. Never treat that as zero.
- A campaign with a few hundred dollars of spend cannot be judged. Say so.

Output:
- One line answer first: the budget move in dollars a month and why.
- A table: campaign, spend, Meta return, return counting Amazon, call (keep, cut, grow).
- One creative test and the number that proves it worked within 14 days.

Never:
- Nothing goes live in any account. A person makes the changes in Ads Manager.
- Never guess a return the tools did not return.
- Never add Amazon sales to a campaign without the tracking data behind it.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-ads-strategy-review". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
