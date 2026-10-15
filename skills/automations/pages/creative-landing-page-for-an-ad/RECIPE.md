# Build a landing page for an ad

Channel: Creative · Level: Prepare · Status: Ready now

Follow these instructions when someone asks to run this automation.

---
Run the Synthesis automation "Build a landing page for an ad" (id: creative-landing-page-for-an-ad, Creative).

Use the Synthesis tools connected in this Claude for my brand's real numbers. Do not guess a number. If a figure is missing, say so plainly.
No Synthesis tools yet? Search your tools for "synthesis"; that waits for one still connecting. Still none: never say this does not exist, say "Synthesis is still loading in this chat. Wait a minute, then open a new chat and try again."

What it does:
Builds a page for one ad and one product, in your brand look.
It uses the offer, the proof and the worries found in your reviews.
It keeps health and results claims careful, and saves a page you can host anywhere.

What to read: Your brand kit, product facts, reviews
What to give me: A finished one-page site for one ad and one product, in your brand look, that works on a phone

Synthesis tools to use:
- `brand_kit`
- `brand_facts`
- `find_product`
- `amazon_metric metric=review_voice`

Steps:
1. Ask which ad and which product the page is for, and what the offer is.
2. Call `brand_kit` for colours, typefaces and logo, and `brand_facts` with `query` set to the product for the claims the brand already makes.
3. Use `find_product` to get the product's id, then call `amazon_metric` with `metric=review_voice` and that `asin` for praise and worries in shoppers' own words.
4. Write the page: hero, proof, how it works, answers to worries, offer.
5. Save it as `landing_page.html`, with all styles inside the file. If you can save files here, save it and tell me its name. If not, show it in full.

Checks before answering:
- Every claim on the page must come from the brand's own facts. Mark any line that needs the brand to confirm.
- If the review read is empty, leave out the review count. Never make one up.
- If the brand kit is empty, say the page uses a plain look until the kit is set.

Output:
- One HTML file, landing_page.html, one page long, that works on a phone.
- A short list of lines the brand should confirm before it goes live.

Never:
- Nothing goes live anywhere. A person hosts the page.
- Never write a health or results claim the brand does not already make.
- Never invent a review, a rating or a review count.

Rules:
- Nothing goes live in any account. Prepare the change; I apply it.
- Keep the answer short and follow the Output section above. Open with one headline line (the dollars, or a yes/no verdict). End with one move and what to measure and when, then one line naming what this run did not check. Keep each number's warning beside it. No other sections.
- On every Synthesis tool call, start `context` with "automation: creative-landing-page-for-an-ad". Synthesis then returns the data and its warnings without general notes.
- If you can save files here, save the result and tell me its name. If not, show it to me in full.
