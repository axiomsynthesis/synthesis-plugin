---
description: "Daily Meta ads: Nine simple questions with our recommended answer for each, your routine's rules in plain words, and what it would do today. Practice only"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Daily Meta ads

Channel: Meta · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Daily Meta ads" (id: do-meta-routine-card, Meta).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Sets up your daily Meta ads routine from nine simple questions. Each question comes with our recommended answer and the reason, from your own numbers.
You answer them yourself. Then you see the rules your answers make and what they would do today. This is practice: nothing changes in your ad account.

What to read: Your order value and product costs, your Meta campaigns and ad sets, each live test ad's spend, sales, hook rate and hold rate
What to give me: Nine simple questions with our recommended answer for each, your routine's rules in plain words, and what it would do today. Practice only

Synthesis tools to use:
- `meta_metric metric=routine_card`

Steps:
1. Call `meta_metric` with `metric=routine_card`. If `status` or `practice.status` is `still_reading`, say its `message`, wait about a minute and make the same call again. That is not a failure.
2. Show every item in `questions` as one numbered list: the question, then "We recommend" with `we_recommend`, then `because`. Say: "Answer each one, or say 'yes' to take a recommendation." Wait for the answers.
3. If `we_recommend` is empty, say you have no recommendation and why. Never make one up.
4. Call `meta_metric` with `metric=routine_card`, `answers` set to what the person said by each question's `key`, and `practice=true`. Use numbers for money, counts and days.
5. Show the result: every line of `rules_in_words` as it is written, every line in `warnings`, what it would do today from `practice.note`, then the best ads from `practice.best` and the worst from `practice.worst` with `practice.worst_note` beside them, each with spend, cost per sale, hook rate and hold rate. Point out the checks that guard the switch-offs: more time for an ad that could be having a bad few days, winners copied to one place first, budget raises held when the whole store slows down, and new vs engaged shown for watching only. If `practice.note` says a read was missing, say so in those words.
6. Ask if they want to change any answer. Repeat step 4 for each change.
7. When they agree, call `meta_metric` with `metric=routine_card`, the same `answers` and `save=true`. Say it is saved and is still practice.

Checks before answering:
- If they asked for anything other than Meta ads after the command, say this only covers Meta ads today and stop.
- Only answers the person gave in this chat go in `answers`. A recommendation counts only after they say yes to it.
- Show every warning, in full.
- A read error is a failure. Say so and stop. Never show an empty card as a result.

Output:
- First the numbered questions, then, once answered, the rules, the warnings and what it would do today.
- End by saying nothing in the ad account changed.

Never:
- Never change, pause or build anything in the ad account from this job.
- Never answer a question for the person.
- Never say the routine is running. It is saved as practice.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-meta-routine-card". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
- If you could not finish, open your answer with "Stuck:" and what I need to do. If your answers are not saved for you automatically, save this one with the Synthesis tool `capture_turn`: my request as `question`, your answer as `answer`, and `context` starting with "automation: do-meta-routine-card".

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
