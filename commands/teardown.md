---
description: "Winning ads teardown: Your ads taken apart: winning hooks, words, visuals and creators, which ads stop, warm or close, and three moves"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Winning ads teardown

Channel: Creative · Level: Advise · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Winning ads teardown" (id: creative-winning-ads-teardown, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Takes every Meta ad of the last 30 days apart beside its results.
Copies and re-edits of one ad count as one idea, so the idea really carrying the account shows up.
You get the winning hooks, the words, visuals and creator types that sell, which ads stop, warm and close, two traits that win together, what predicts a sale, why the losers lose, a cut list and three moves.

What to read: Every Meta ad of the last 30 days beside its results, its hook and hold rate, and the script the video model wrote down
What to give me: Your ads taken apart: winning hooks, words, visuals and creators, which ads stop, warm or close, and three moves

Synthesis tools to use:
- `winning_hooks view=teardown`
- `winning_hooks view=strategist`
- `brand_facts`
- `ad_idea_bank action=save`

Steps:
1. Call `winning_hooks` with `view=teardown`. If `more_to_read` is above 0, call it again, at most twice more: the biggest spenders are read first.
2. If the top idea or a line that sells has no script yet, say so: the next run reads it, biggest spenders first.
3. Read the concentration first: the top idea's share of sales and what the rest of the account returns without it.
4. Read what predicts a sale: hook rate, hold rate, length, format and product named, each pooled.
5. For each line that sells, write what is seen, said and written in the first seconds, the beats, the offer and why it sells. For the biggest losers, say where each breaks.
6. Call `winning_hooks` with `view=strategist`. From each lens take its `leaders`: the winning hooks, phrases (words said or shown in 3+ creatives), visuals, creator types, storylines and offers at each job: stop, warm, close. Read `hidden_connections`: two traits that do a job better together than either alone. Name the website ads in `fills_carts_others_close`.
7. Write five new versions of the top idea: same format, new first line, built from the winning words, visual and creator type. Check every claim with `brand_facts`, then save each with `ad_idea_bank` and `action=save`.

Checks before answering:
- Amazon-bound ads are judged on Amazon sales per $1, website ads on cost per order. Never add the two.
- An idea started in the last 14 days is not judged on Amazon yet. Say so.
- A strong hook rate with a weak sale is attention without a sale, never a winner.
- If under half the spend has a script, say how much and read the rest as numbers only.
- Words, visuals and creator types cover only the share of spend in each lens's `labelled_spend_pct`. Say that share.
- A job index compares an ad with the brand's own average for the same destination. A stopper with a low return is doing its job; never cut it on return alone.
- A hidden connection is the case for a test, not proof: it rests on as few as 2 creatives.
- Every number comes from a tool result above.

Output:
One page in the house look, in this order:
- The answer: the idea carrying the account, its share of sales, and what the rest returns.
- Winning hooks, words, visuals and creator types: one row each, with its job and how far above the brand's average it sits.
- Two that win together: each pair, what it does alone and together.
- What predicts a sale: one bar per band, with a line at $1.00 back per $1.
- The lines that sell: opening line, where it sends, result, hook rate, spend.
- The winners taken apart: the opening on a phone-shaped card, the numbers, what happens, why it sells, a watch link.
- Why the losers lose: pattern, opening line, hook rate, result.
- What the winners share, three moves with what to measure, and what not to do.
- How it was measured, in plain words.

Never:
- Never pause or change an ad. The cut list is for a person, or for whoever runs those ads.
- Never copy a health or results claim from an old ad unless `brand_facts` has it on file.
- Never call a pattern proof: ads differ in budget, audience and timing.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-winning-ads-teardown". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- If you could not finish, open your answer with "Stuck:" and what I need to do. If your answers are not saved for you automatically, save this one with the Synthesis tool `capture_turn`: my request as `question`, your answer as `answer`, and `context` starting with "automation: creative-winning-ads-teardown".

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
