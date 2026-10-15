# Launch Meta ads for me

Channel: Meta · Level: Push live · Status: Needs access we don't have yet

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Launch Meta ads for me" (id: meta-launch-ads-for-me, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Would build the campaign, ad sets and ads, and put them live after you approve.
Nothing is pushed today, because our Meta access only reads.
Today it prepares the full launch plan as a list a person builds in Ads Manager.

What to read: Meta ads
What to give me: Live ads with a spend cap and undo, once you approve

Synthesis tools to use:
- `meta_metric metric=campaign_performance`
- `meta_metric metric=adset_performance`
- `propose_operator_action`

Steps:
1. Call `meta_metric` with `metric=campaign_performance` to see which campaign types return best for this brand. It covers each campaign's whole life, not a recent window, so say that.
2. Call `meta_metric` with `metric=adset_performance` to pick the audiences and budgets to copy. This read has no date setting, so say the dates the result covers.
3. Write the launch plan: campaign goal, each ad set with audience and daily budget, and each ad with its creative and copy.
4. Call `propose_operator_action` with `platform=meta`, the total budget and duration, to check it against the brand's caps.
5. Hand the person the plan to build in Ads Manager.

Checks before answering:
- If past results are empty, say there is no history to copy. Never invent a budget from nothing.
- The plan's total spend must sit inside the brand's cap.

Output:
- A launch plan: campaign, ad set, audience, daily budget, ad, creative, copy.
- One line on total spend and the number that shows it worked after 14 days.

Never:
- Nothing is pushed to any account. A person builds and launches the ads.
- Never plan spend past the brand's cap.
- Never guess a result the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: meta-launch-ads-for-me". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (needs access we don't have yet): Our Meta connection is read-only. Meta has to approve write access, which usually takes weeks, and we also need a spending cap and an undo first. Do the parts you can and say plainly what is missing.
