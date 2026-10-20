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
4. Scan every new subject, preheader and image text for the claims you said never to make. Fix any hit first.
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
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-klaviyo-swap-email-content". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
