---
description: "Whole-business profit, every channel: Every channel side by side, ad spend and fixed costs, down to one net profit, with every missing cost named"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Whole-business profit, every channel

Channel: Money · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Whole-business profit, every channel" (id: money-whole-business-profit, Money).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Puts every channel on one page for one month: Amazon, the website, TikTok Shop, Walmart, stores and wholesale. Each shows its sales and its profit after its own costs. Ad spend that cannot be pinned to one store sits in its own row. Your fixed costs come off last, down to one net profit. Every channel or cost with no data is named, so the net is never read as more complete than it is.

What to read: Every sales channel's profit as the Profit page counts it, ad spend by platform, and your entered fixed costs
What to give me: Every channel side by side, ad spend and fixed costs, down to one net profit, with every missing cost named

Synthesis tools to use:
- `cost_rules for=money-whole-business-profit`
- `business_profit month=YYYY-MM`
- `amazon_metric metric=pnl_waterfall month=YYYY-MM`

Steps:
1. Call `business_profit` with `month=` set to last month.
2. Read `data_quality_flags` before anything else. Sort them into three groups: channels left out, channels with sales but no profit yet, and costs not counted.
3. Read `columns`. List each sales channel with its sales, profit and margin, then each ad platform's spend.
4. If Amazon is the largest channel and the month is still settling, call `amazon_metric` with `metric=pnl_waterfall` for the month before as well, and say which month is settled.
5. Read `fixed_costs`. If none are entered, say net profit is before rent, salaries and software.

Checks before answering:
- If `gated` is true, there is no net to state. Give the reason.
- A channel with sales and no profit is not in the net. Say how much it sold, so the gap is visible.
- Never add an ad platform's spend to one channel. It is its own row.
- A margin above 70% on any product channel almost always means a cost is missing. Say so beside it.
- Use a closed month.

Output:
- One line first: net profit for the month, its share of sales, and how many channels or costs are missing.
- A table: channel, sales, profit, margin, what is not counted.
- Two lines: the channel that makes the most per dollar of sales, and the one missing cost that would change the net most.
- One move: the cost to enter or the feed to connect first.

Never:
- Never fill a missing channel or cost with an estimate of your own.
- Never call the net complete while a flag says otherwise.
- Never move budget between channels. A person does that.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Before step 1, call cost_rules. If it returns questions, ask them in one message as written (dollars, choices, what skip does) and save each answer with set_cost_rule. On a scheduled run, use the defaults and list the questions at the end. End the answer with its used_line.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: money-whole-business-profit". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
