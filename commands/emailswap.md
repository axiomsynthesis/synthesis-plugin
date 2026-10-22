---
description: "Swap images or wording in my live Klaviyo emails: New images, subject lines or offer wording swapped into your live Klaviyo emails or sign-up form after your yes, and read back"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Swap images or wording in my live Klaviyo emails

Channel: Email · Level: Does it for you · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Swap images or wording in my live Klaviyo emails" (id: do-klaviyo-swap-email-content, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Edits live Klaviyo emails or a sign-up form. It swaps images, subject lines or offer wording in your own signed-in Klaviyo. It changes only what you approved and reads every email back. Our Klaviyo key only reads, so all changes go through your browser.

What to read: Klaviyo flow, step and template results
What to give me: New images, subject lines or offer wording swapped into your live Klaviyo emails or sign-up form after your yes, and read back

Synthesis tools to use:
- `klaviyo_metric metric=flow_step_performance limit=60`
- `klaviyo_metric metric=template_performance`

Steps:
1. Ask: which flow or form, which emails, and the new wording or images. Ask for the new preheader too, or say it stays. Ask which claims your brand never makes in email. Ask your brand font for any rebuilt image.
2. Call `klaviyo_metric` with `metric=flow_step_performance` and `limit=60`. It gives each flow email's subject, template and results. Use `metric=template_performance` only for campaign emails. The order shown is by people reached, not the real order. Confirm each email by its place in the flow in Klaviyo, most of all when two share a subject.
3. Rebuild images so only the old wording pixels change. Keep the same size and layout. Upload them to your store's Files page. Keep the old images there for rollback.
4. Scan every new subject, preheader and image text for the claims you said never to make, and for any disease or medical claim. Those never go in email or SMS, because a sent email cannot be pulled back. Fix any hit first.
5. Use Klaviyo in your real signed-in browser. The built-in browser pane is often logged out. Before any edit, read each email's old image links and every link in it, and save the email as a template named "BACKUP <old name>".
6. Show the exact list: each email, the old and new subject, preheader and image link, and every link read in step 5. Uploading anything customers will receive needs a yes. A live flow edit sends at once, so offer the safe test copy first.
7. To replace an image, wait until the replace dialog stops sliding before you click. A click mid-slide picks the wrong image.
8. Click off each field after editing. Klaviyo saves an edit only then. Do not click "+ Step", because it adds a new step.
9. If the email is an A/B arm, edit both arms the same day. When Klaviyo asks about a live A/B test, choose "Continue".
10. If the change sits in shared footer content, say first that it changes every email at once.
11. Reload each email. Read back that the image link and subject equal the new ones, the links are unchanged and the preview renders.

Checks before answering:
- Safe test when asked: copy one email to a template named "CLAUDE TEST - copy of <name>" and make the swap there only.
- Spend: this changes no budget and sends nothing new. Decline any upgrade Klaviyo offers.
- Every link in each edited email must match its link before the edit.
- If an email cannot be read back, say it is unconfirmed. Never call it done.

Rounds (relook before you answer):
1. **Only the approved change.** Diff each email's subject, preheader and image links against step 6's list. Fails when: anything changed that is not on the list, or an approved change is missing. Fix: put it right and re-read.
2. **Links unchanged.** Re-read every link in each edited email. Fails when: one link differs from step 5's copy. Fix: restore it from the backup template.
3. **Claim sweep, pictures too.** Read the words inside every new image, not just the text. Fails when: a disease or medical claim, or a claim the person banned, appears. Fix: rebuild the image.
4. **Both A/B arms.** Open each arm. Fails when: one arm has the new content and the other does not. Fix: edit the other arm the same day.
5. **It renders.** Open the preview on a phone width. Fails when: an image is blank, an animated image's first frame is not its finished frame, or text overflows. Fix: re-upload and re-read.

Output:
- One line: how many emails or forms changed, Live.
- Each one: name, what changed, old and new, read back yes or no.
- Where the old images and the backup templates are kept, for rollback.

Never:
- Never change links.
- Never edit only one A/B arm.
- Never delete old images.
- Never send a test email without a yes.

Rules:
- This one makes the change for me, in my own browser where I am already signed in (Claude in Chrome or another browser tool). Before changing anything, show me the exact change in one list: every object by name, every budget, price, link and date. Wait for my clear yes. Then change only what I approved. Never delete, never buy, never raise spend or a price beyond what I approved, and decline every platform suggestion that would. If a platform's safety check stops a step, quote my approval once and stop if it still refuses. When it is done, read every changed object back and tell me what is live, what is off and anything that differs from the plan. If no browser tool is available here, give me the exact click-by-click steps instead.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-klaviyo-swap-email-content". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
