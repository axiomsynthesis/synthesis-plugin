# Make static ads with Higgsfield

Channel: Creative · Level: Prepare · Status: Needs access we don't have yet

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Make static ads with Higgsfield" (id: creative-static-ads-with-higgsfield, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Would turn a creative brief into finished static ads in your sizes and your brand look.
Higgsfield is not connected, so today it prepares the brief, ready to paste into Higgsfield or hand to a designer.
You pick the images to use.

What to read: Your brand kit, the brief
What to give me: Ready-to-paste prompts for static ads in your sizes and brand look

Synthesis tools to use:
- `brand_kit`
- `meta_metric metric=creative_leaderboard`
- `export_docx`

Steps:
1. Call `brand_kit` to read the brand's colours, typefaces and logo.
2. Take the brief from the Meta or email automations, or call `meta_metric` with `metric=creative_leaderboard` to base it on the current winners. It always covers the last 30 days.
3. Write one image prompt per size: square, portrait and story, each with the headline and the brand colours.
4. Call `export_docx` with `filename=static_ad_prompts.docx` holding the brief and the prompts.

Checks before answering:
- If the brand kit is empty or still proposed, say so and use it as a draft only.
- Every headline must use a claim the brand already makes.

Output:
- One prompt per size, with headline, layout and colours.
- The file static_ad_prompts.docx.

Never:
- Nothing goes live in any account. A person picks and uploads the images.
- Never write a health or results claim the brand does not already make.
- Never use another brand's logo or product in an image.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-static-ads-with-higgsfield". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.

Not fully ready yet (needs access we don't have yet): Higgsfield is not connected. We would need its API access and your Higgsfield account. Until then the design add-on can make simple static ads as images. Do the parts you can and say plainly what is missing.
