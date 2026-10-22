---
description: "Make static ads in my house style: Finished static ad files in your house look, or an Amazon static cleaned for website ads, ready to load as ads"
argument-hint: "[anything to add for this run]"
disable-model-invocation: true
---

# Make static ads in my house style

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Make static ads in my house style" (id: do-creative-static-ads, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Makes static ads in your house look, from your real product photo.
It can also clean an Amazon static for website use: cut the Amazon logo and stars and refit it to 4:5.
Nothing is uploaded to an ad account. The files load as ads through the add videos shortcut.

What to read: Your brand kit, your proven static ads, your real product photo, the message you want
What to give me: Finished static ad files in your house look, or an Amazon static cleaned for website ads, ready to load as ads

Synthesis tools to use:
- `brand_kit`
- `meta_metric metric=creative_leaderboard limit=50`
- `meta_metric metric=amazon_ads`
- `list_files file_type=image`
- `get_upload_link`
- `render_report format=ad`
- `brand_facts`

Steps:
1. Ask in one message: the message or headline, website-bound or Amazon-bound, how many looks, and the source static if cleaning one.
2. Copy the house style first. Call `brand_kit` for colours, type and logo. If its state is proposed, say the colours are not confirmed. The ad maker then takes colours from the pack photo. If the person keeps finished ads in an image tool, open their latest ones and copy that look.
3. See which statics sold. Call `meta_metric` with `metric=creative_leaderboard` and `limit=50`. It takes no days. Statics that send shoppers to Amazon show no website sales there, so judge them with `meta_metric` and `metric=amazon_ads`, by sales per dollar spent.
4. Free path first. Call `list_files` with `file_type=image` for a product photo already held. Only if none, get one with `get_upload_link`.
5. Call `render_report` with `format=ad`, the headline, `product_file` set to the photo's file id, `size=4:5` for feeds, and a layout. Do not rely on `asin` for the photo: it is refused when the listing does not name the brand. Use `layout=quote` for a customer's own words, else shout or glow. Make one file per look. Each file is saved in the brand's file store. Say so.
6. Read every word on the returned preview picture. Small text is where errors hide.
7. Only if the free path cannot make the look, offer a paid image tool in the browser. Say the credit cost per image and the total, and wait for a yes. In that tool, use a finished house ad as the style image and the real photo as the product image. Ask it to keep the style and change only the copy. Use its high-quality setting for text-heavy ads, since cheaper models misspell small text.
8. To clean an Amazon static for the website, no Synthesis tool crops a picture. Use an image editor the person has, or rebuild the look with the free ad maker from the same words. Fetch the original without sign-in cookies, cover the Amazon logo and star row, refit to 4:5, and save it as "<name> - 4x5 no amazon". Then read the whole file again for any Amazon mark, star or rating left.
9. Show the person every file before anything else happens. Loading files as ads is the add videos shortcut and needs its own yes.

Checks before answering:
- Safe test run: when asked to test the shortcut, make one file with the free ad maker and upload it nowhere.
- Spend: the free ad maker costs nothing. Any paid image credit needs a yes on the total first.
- No Amazon wordmark, stars or "Verified Amazon Buyer" on a website-bound file. They belong only on Amazon-bound ads.
- Review quotes must be word for word from a real review. "Verified buyer" only where the review says so.
- Claims only from what the brand already says. Flag anything new.
- Statics often sell less than video on ads that send people to Amazon, except customer-quote cards. Warn before making many.

Rounds (relook before you answer):
1. **House style.** Put each file beside the latest finished house ad. Fails when: colours, headline weight or product size plainly differ from it. Fix: remake it with that ad as the style reference.
2. **Word by word.** Read every word on each preview against the agreed copy. Fails when: any word, price or mark differs, even by one letter. Fix: remake that file.
3. **Destination marks.** Fails when: a website-bound file shows any marketplace logo, wordmark, star row or rating. Fix: cut it or remake it.
4. **Quote and claim.** Call `brand_facts` for each claim. Fails when: a quote is not word for word from a review, or a claim has no fact behind it. Fix: cut it.
5. **Variation set.** Fails when: all files share one look. The house method is one message made in at least 3 looks. Fix: add the missing looks.
6. **Feed crop.** Fails when: the headline or product sits in the outer tenth of the 4:5 frame, where feeds crop. Fix: refit to the centre.

Output:
- One line: how many files, which looks, free or paid.
- Each file with its preview, size and where it is meant to run.
- Any word or claim to check.

Never:
- Never redraw or invent the product. Use the real photo.
- Never spend paid credits without a yes on the total.
- Never upload a file into an ad account from this shortcut.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- This job is worked in rounds; the first pass is never the answer. First call recall_decisions and look for an earlier run of this job: if one exists, start from where it ended, not from zero. After the Steps, run every round in Rounds in order. Each round re-reads the data it needs, says what it found wrong and fixes the draft. Log one line per round: what changed and why, or 'no change' if its check passed. Never invent a change. Stop mid-way only for a choice only I can make. Show the final draft, then the round log, then 2 or 3 next rounds I could ask for. Treat my feedback as a new round: re-run every check it touches, and never quietly undo an earlier fix. At the end, save where this run stopped with log_decision so the next run picks it up.
- Read every number that drives the call in layers and over several windows, never one. Layers, where they apply: volume (orders, sales), then profit after every cost, then return on the money spent against break-even, then what a customer is worth later on profit. Windows by how fast the number moves: fast ones (clicks, buy rate, cost per sale) over the last 7 closed days and the 7 before; sales, spend and return over 28 days, never under 4 weeks; slow ones (repeat, lifetime value, share) over 90 days to 12 months, comparing only customers of the same age. Set each against the same weeks last year, not last week. Closed days only; a young cohort is unfinished, not low. Before calling a change, rule out a deal, a stock-out or a part month. Show one small grid: each key number by window, with return on spend. When windows disagree, say so plainly: a fall in a slow number outranks a wobble in a fast one, a trend needs 4 steady weeks, and mixed signals mean no clear signal yet, not a verdict.
- Before trusting a number, compare it the way an expert would. Against itself: its own usual level and the same weeks last year. Against its peers: the other products, ads, pages or channels doing the same job, ranked side by side. Against the line that matters: break-even and any goal the brand set. An outside benchmark only shows room to grow, never a grade. Against a control: a holdout, the page being beaten, or a past natural test such as a pause or a stock-out. Break every move into its parts (price times units times mix, or rate times count) and name the part that moved. Look at the spread, not just the average: the top and bottom few, and how much rides on one item. Size each finding in dollars a month. Name the number that would flip the call.
- Go deeper with the tools built for it, picking the ones this job needs and saying which you ran and which you skipped. Start from the map: brand_brain with action=what_matters, then action=links_here on the thing at hand to find what it is tied to, and action=explain_link to check a link was tested and is not chance. Incrementality: attribution_lenses to set what the platform claims beside what was likely extra, plus any past pause, stock-out or spend jump as a natural test; never treat a platform's own credit as extra sales. Models: media_response_model or diminishing_returns for what the next dollar returns; run_monte_carlo for a range of outcomes, never one point; run_bayesian when the sample is small; explain_metric_move for why a number moved; backtest_rule to check the call would have held in the brand's own past. List what is working and what is breaking, both sides. Check find_contradictions against earlier conclusions. Close every recommendation with measurable_test: the number, the date and the line that says it worked.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-creative-static-ads". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
