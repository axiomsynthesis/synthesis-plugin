# Make the Amazon ad changes for me

Channel: Amazon · Level: Push live · Status: Needs access we don't have yet

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Make the Amazon ad changes for me" (id: amazon-change-ads-for-me, Amazon).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Today it prepares the exact bid, budget and keyword changes as a list.
Nothing is pushed, because the safe way to apply changes does not exist yet.
Once built, it would show the changes first, apply them only after you approve, never spend past your cap, and keep an undo for each one.

What to read: Amazon Ads
What to give me: Your ad changes made in the account, with a one-click undo

Synthesis tools to use:
- `amazon_metric metric=ppc_keyword_bids`
- `amazon_metric metric=ppc_budget_utilisation`
- `amazon_metric metric=ppc_account_changes`
- `propose_operator_action`

Steps:
1. Call `amazon_metric` with `metric=ppc_keyword_bids` and `days=30` to find bids above break-even or starved of impressions.
2. Call `amazon_metric` with `metric=ppc_budget_utilisation` and `days=30` to find campaigns that run out of budget or never spend it.
3. Call `amazon_metric` with `metric=ppc_account_changes` and `days=30` to skip anything a person changed in the last two weeks.
4. Call `propose_operator_action` for each change with `platform=amazon_ads`, the amount and the reason, to check it against the brand's caps.
5. Hand the person the change list to apply in the ad console.

Checks before answering:
- If a bid or budget read is empty, say it could not be read. Never propose a change from a missing number.
- A change that would raise monthly spend past the brand's cap is marked and left out.
- Judge bids on at least 30 days of clicks, not one week.

Output:
- A change list: campaign, target, current, proposed, reason, monthly dollar effect.
- One line on the total effect on monthly spend.

Never:
- Nothing is pushed to any account. A person applies the changes.
- Never raise spend past the brand's cap.
- Never guess a number the tools did not return.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: amazon-change-ads-for-me". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (needs access we don't have yet): We have access to change Amazon ads but have never used it. Before we do, we need a monthly spending cap, a one-step undo and a guard so the same change cannot apply twice. Do the parts you can and say plainly what is missing.
