# Reach out to creators who sell

Channel: TikTok Shop · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Reach out to creators who sell" (id: tiktok-shop-creator-outreach, TikTok Shop).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Looks at the creators who already sell for you, finds what they share, and drafts a short message to each one worth working with again. A person always presses send.

What to read: Your creator results
What to give me: A shortlist of creators worth working with again, and a draft message to each

Synthesis tools to use:
- `tiktok_metric metric=shop_video_performance`
- `tiktok_metric metric=shop_product_performance`
- `tier_creators`
- `export_docx`

Steps:
1. Call `tiktok_metric` with `metric=shop_video_performance` and `limit=30` to rank creators and videos by sales.
2. Call `tiktok_metric` with `metric=shop_product_performance` and `limit=10` to tie each creator to the product they sell.
3. Pass the top creators to `tier_creators` with their followers and engagement to sort them by size.
4. Note what the best ones share: size, product, video style.
5. Draft one short message per creator and save them with `export_docx` as creator-drafts.docx.

Checks before answering:
- Rank by sales, not views. If sales are missing for a creator, say so.
- If the creator read is empty, say no creator data was found. Never draft from nothing.
- Say plainly that new creators cannot be found yet. The list only covers people who already worked with you.

Output:
- One line first: how many creators are worth contacting and why.
- A Word file, creator-drafts.docx: creator, size tier, sales, product, draft message.

Never:
- Never send a message. It goes out in your name, so a person sends it.
- Never promise a fee or a free product in a draft unless a person asked for it.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: tiktok-shop-creator-outreach". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): Drafts work today. Finding new creators needs a creator search source we do not have yet. Do the parts you can and say plainly what is missing.
