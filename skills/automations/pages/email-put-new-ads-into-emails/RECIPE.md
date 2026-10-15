# Turn winning ads into email blocks

Channel: Email · Level: Prepare · Status: Ready after we build it

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Turn winning ads into email blocks" (id: email-put-new-ads-into-emails, Email).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Takes your best still-image Meta ads and turns each one into a ready email block: a headline, two lines of copy and a button. An ad that already sells on Meta is a safer bet in an email than a brand-new idea.

What to read: Meta creative results
What to give me: Your best-selling Meta images turned into email blocks with headline, copy and button

Synthesis tools to use:
- `meta_metric metric=creative_leaderboard`
- `meta_metric metric=creative_fatigue_curve`
- `klaviyo_metric metric=template_performance`
- `export_docx`

Steps:
1. Call `meta_metric` with `metric=creative_leaderboard` and `limit=10` to rank your ads by return on spend. It always covers the last 30 days.
2. Call `meta_metric` with `metric=creative_fatigue_curve` for the top ads, so a tired ad is not chosen.
3. Call `klaviyo_metric` with `metric=template_performance` to see which email layouts earn the most clicks. This read has no date setting, so say the dates the result covers.
4. Keep the top three still-image ads that are not fatiguing. Write a headline, two short lines and a button label for each, in the ad's own words.
5. Use `export_docx` with `filename=email-blocks.docx` to hand over the blocks, one per page, with the ad name and its results.

Checks before answering:
- If the Meta read is empty or fails, say so. Never pick "best ads" from nothing.
- One week of good results is not a winner. Use at least 14 days and real spend.
- Say plainly that the image still has to be added by hand until the image step is built.

Output:
- One line first: which three ads were picked and why.
- A Word file, email-blocks.docx: per block, the ad name, spend, return, headline, two lines, button label.

Never:
- Never send or schedule an email. A person builds and sends it in Klaviyo.
- Never invent a result for an ad the tools did not return.
- Never reuse an ad that Meta flags as fatigued without saying so.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: email-put-new-ads-into-emails". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (ready after we build it): The copy part is ready today. Putting the ad image into the block needs the image step from the creative automations, which is not built yet. Do the parts you can and say plainly what is missing.
