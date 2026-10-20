---
name: start-here
description: >-
  Load first on any business question answered with Synthesis, and whenever a message says "deep". Picks how deep to go, grounds the answer in what this brand already knows, opens the Brand Brain map for what matters and what changed, runs a deep synthesis when asked, and files what was learned. Asked to make a dashboard, report, deck or page: open writing-it-up too.
---

# Start here

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

**Asked to MAKE something** (a dashboard, report, deck, chart, spreadsheet, page or file)? Open the writing group now: `../writing-it-up/pages/exports-and-deliverables/PAGE.md`, and fetch its method. A bare "make me a dashboard" with no detail gets the default dashboard that page describes, built first. Do not answer with questions and nothing built; offer to adjust after it exists. Use the pages below as well for grounding. Call `brand_kit` before building: `source: agency` means work for the client to read wears the agency's look and "Prepared by" the agency, never the client's look.

| Page | Open it when |
|---|---|
| `pages/synthesis-operating-protocol/PAGE.md` | On every real question about your business that Synthesis can answer, from "what was revenue last month" or "chart sales by week" to "should we expand", "why is repeat down" or "what is our biggest risk". |
| `pages/synthesis-reasoning-method/PAGE.md` | For a strategic, why or should-we question ("should we cut ad spend", "why is revenue falling", "what's driving repeat down", "give me a strategy to scale this product", "what is our biggest constraint") once the operating… |
| `pages/invoke-deep-synthesis/PAGE.md` | When your message contains the word "deep" in any spelling about a business question ("@deepsynthesis", "deepsynthesis", "deep synthesis on why repeat fell", "go deep on this", "deep dive into our ad spend"), or when a deep run's… |
| `pages/ground-in-brand-knowledge/PAGE.md` | At the start of any analysis of your brand, when you mention a document, deck, file or spreadsheet ("what does our research say", "check the brief we uploaded"), before quoting a stored brand fact, when you say you added a file… |
| `pages/brand-context-lenses/PAGE.md` | Before leaning on your brand's stored archetype, revenue stage, channel gravity, seasonality class, market posture or death-mode scores ("what kind of brand are we", "what should our repeat rate be", "are we Amazon-dependent",… |
| `pages/write-back-conclusions/PAGE.md` | At the end of a substantive answer, when you attach a file, when a forward-looking number is stated ("we should hit 20% repeat by March"), when a stored fact about your brand turns out wrong, or when you commit to a decision or… |
| `pages/operating-state-tools-retired/PAGE.md` | Before calling or quoting any of the six state-diagnosis tools (diagnose_operating_state, diagnose_state_gated, diagnose_state_map, check_state_transition, run_state_formula, apply_growth_investment_override), or whenever a… |
| `pages/brand-brain-map/PAGE.md` | At the start of any open review of your business ("what should I focus on", "what needs a look this week", "walk me through this week"), and for connective questions one metric cannot answer: what a product, channel, rival or… |

## When a page names another skill

Pages sometimes say "load <some-skill>". Those skills are pages in this
plugin's groups: every name is listed in `../start-here/INDEX.md`, and
`get_skill` takes the name directly, with or without the `ssi-` prefix.

## Shortcuts the person can type

The person types these; you never run them yourself. When your answer covered
what one of them does, end with ONE line naming it, for example:
"Next time, type /stockout." Only when it truly matches, never more than one,
and never at the end of a shortcut's own run. When the answer matched an
automation that has no word of its own, name it as /go and its title instead,
for example "Next time, type /go win-back list and email."

If the person's message starts with one of these words, or with /go and an
automation's title, and it reached you as plain text because the command did
not run, run it anyway: call get_skill with that word (or the /go text) and
follow the instructions it returns. Never answer that the command does not exist.

When the person is new, or asks what they can do or which shortcut to use,
tell them to type /start: it shows the shortcuts for their job and runs the first.

- `/start` The shortcuts for your job, and the first one run on your data
- **Amazon:** `/adloss` Find ads that lose money after product cost · `/amazonblock` Block Amazon searches that cost money and never sell · `/amazonlink` Make a tracked Amazon link for each ad · `/bids` Build the keyword bid change sheet · `/deals` Did that deal make money? · `/incremental` Are your ads buying sales you'd get anyway? · `/pricemove` Size an Amazon price or Subscribe and Save change · `/rivals` Who's stealing your search shoppers? · `/saleready` Get ready for the next big Amazon sale
- **Creative:** `/adcopy` Write ad copy for every buyer stage · `/scout` Scout creators and rival ads for me · `/static` Make static ads in my house style
- **Customers:** `/bundles` Find bundles buyers already want · `/ltv` Which first product makes the best customers? · `/payback` How fast does a new customer pay back? · `/returning` Is website growth from new or old customers? · `/reviews` Turn reviews into selling lines · `/winback` Win back customers who stopped buying
- **Data:** `/health` Is all my data fresh?
- **Email:** `/emailflow` Build a Klaviyo email flow for me · `/emailswap` Swap images or wording in my live Klaviyo emails · `/flows` Where your email flows lose people
- **Google:** `/googlewatch` Check Google Ads data is landing
- **Growth:** `/adcheck` Check my ads · `/ideas` Find your next product in search demand · `/mer` Is all your marketing paying, together? · `/nextdollar` What each channel must return to earn the next dollar
- **Inventory:** `/afford` Test a purchase order (needs your cash balance) · `/reorder` What to reorder, and the purchase order to send · `/stock` Send me the inventory report every Monday · `/stockout` Warn me before we run out
- **Meta:** `/adaudit` Audit my whole Meta account · `/addvideos` Add new videos as Meta ads · `/adroi` Which Meta ads lose or make money · `/budget` Change a Meta budget for me · `/creativetest` Run this week's Meta creative test · `/feedcut` Make feed-shape copies of my top ads · `/graduate` Move winning test ads into the main campaign · `/halo` Does Meta grow your Amazon sales? · `/newads` Check the ads I just launched · `/pagetest` Test a new landing page on Meta · `/toggle` Switch Meta ads on or off for me · `/trybe` Turn approved Trybe videos into Meta ads for me
- **Money:** `/allprofit` Whole-business profit, every channel · `/amazonprofit` Amazon profit after every fee and cost · `/costup` A cost went up. Now what? · `/fees` Check for Amazon fee jumps · `/mix` Was it price, volume or mix? · `/price` What happens if you change the price? · `/profit` Which Amazon products actually make money? · `/shopifyprofit` Website profit after every cost · `/tiktokprofit` TikTok Shop profit after every fee · `/walmartprofit` Walmart profit after every fee · `/whyprofit` Why did profit move this month?
- **Retail:** `/coupon` Is this Walmart store coupon worth running again?
- **Strategy:** `/risk` What if we lost our biggest one?
- **Subscriptions:** `/cancels` Why subscribers cancel, and what to change · `/subcheck` Are subscriptions worth it, product by product?
- **TikTok Ads:** `/tiktokwatch` Check TikTok is still connected and sending data
- **TikTok Shop:** `/gmvtest` Plan and read a TikTok GMV Max pause test
- **Website:** `/addon` Add an add-on or after-payment upsell · `/codes` Set up a discount code or offer · `/landingpage` Build a landing page from the kit · `/offeritem` Set up the product behind an offer · `/pagelive` Make a test version of a live page · `/ppv` Profit per website visit · `/splittest` Run a split test on a page
