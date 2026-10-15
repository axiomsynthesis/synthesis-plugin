# Rank and size your big bets

Channel: Strategy · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Rank and size your big bets" (id: ops-rank-big-bets, Strategy).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Ranks a handful of big decisions on expected value, then adds two things a plain ranking misses: how much of each to commit given the spread of outcomes, and whether it can be undone. Reversible bets should be tested fast; one-way bets deserve staging.

What to read: Your list of large decisions with their cost, payoff, chance of success and whether they can be undone
What to give me: Your bets ranked by expected value, how much to commit to each given its risk, and which are cheap to undo

Synthesis tools to use:
- `strategy_framework framework=rank_decision_options`
- `strategy_framework framework=kelly_sizing`
- `strategy_framework framework=decision_type`
- `strategy_framework framework=decision_weight`

Steps:
1. Ask for each bet: cost, payoff if it works, chance it works, and cost to reverse. Size cost and payoff from measured bases where possible.
2. Run `strategy_framework framework=rank_decision_options options=[{name, cost, payoff, p_good}]` with the list, chance as 0 to 1.
3. For each, run `strategy_framework framework=decision_type decision_text=<the bet> reversible=<true or false> cost_to_reverse=<cost>`.
4. For bets with a clear win and loss, run `strategy_framework framework=kelly_sizing win_prob=<chance> win_loss_ratio=<payoff over cost>` for the share to commit.
5. Run `strategy_framework framework=decision_weight question=<the bet in one sentence>` to flag which ones deserve a deep run.

Checks before answering:
- Chances and payoffs supplied by the person are judgement. Label them.
- Sizing is sensitive to the chance. Show how the answer moves if the chance is 10 points lower.
- A bet with no measurable payoff is "not sized".

Output:
- Table: Bet | Expected value | Reversible | Share to commit | Rank.
- Two lines: what to do first and what to stage.

Never:
- Never commit money or make the decision.
- Never present judged chances as measured.
- Never skip the reversibility check on a large bet.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-rank-big-bets". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
