# Split next quarter's marketing budget

Channel: Growth · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Split next quarter's marketing budget" (id: ops-marketing-budget-allocation, Growth).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Splits the next quarter's marketing budget across channels by where the next dollar earns most, not by last quarter's habit. Each channel's returns flatten as spend grows, so the right split moves money from flattened channels to ones with room.

What to read: Spend and return by channel, where each channel's returns flatten, margin and total budget
What to give me: A recommended split across channels, the expected effect, and the chance the shift loses money

Synthesis tools to use:
- `cost_rules for=ops-marketing-budget-allocation`
- `allocate_budget revenue=<annual_revenue> stage=<stage>`
- `meta_metric metric=efficiency_curve`
- `media_response_model`
- `amazon_metric metric=acos_tacos month=YYYY-MM`
- `google_ads_metric metric=impression_share days=30`
- `run_scenario scenario_type=budget_shift`
- `export_xlsx filename=marketing-budget.xlsx`

Steps:
1. Ask for the total budget and any fixed commitments.
2. Run `allocate_budget revenue=<annual_revenue> stage=<stage>` for a starting reference only.
3. Meta: call `meta_metric metric=efficiency_curve` and `media_response_model` for where returns flatten.
4. Amazon: call `amazon_metric metric=acos_tacos month=YYYY-MM` for efficiency and total-sales effect.
5. Google: call `google_ads_metric metric=impression_share days=30` for spend lost to budget versus to rank.
6. Draft a split that moves money toward channels with room. Run `run_scenario scenario_type=budget_shift amount_monthly=<amount> from_channel=<from> to_channel=<to> contribution_margin_pct=<margin>` for each move.
7. Write it with `export_xlsx filename=marketing-budget.xlsx`.

Checks before answering:
- Platform-reported returns are not incremental. Use the response model or blended figures where possible, and say which.
- The reference split is a rule of thumb, not a target. Label it.
- Use the measured contribution margin, not a default.
- A channel with under 8 weeks of data has no reliable curve. Hold its budget flat.

Output:
- Spreadsheet: Channel | Current monthly | Proposed monthly | Expected return on the change | Chance of loss.
- Three lines in chat: the main move, its expected effect, and the step plan.

Never:
- Never change a budget in any ad account. A person applies the split.
- Never use the rule-of-thumb split as the answer.
- Never move more than half a channel's budget in one step.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: ops-marketing-budget-allocation". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
