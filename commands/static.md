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
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: do-creative-static-ads". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

---

Anything the person typed after the shortcut is extra instruction for this run: $ARGUMENTS
