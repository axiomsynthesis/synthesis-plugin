---
name: start-here
description: >-
  Load first on any business question answered with Synthesis, and whenever a message says "deep". Picks how deep to go, grounds the answer in what this brand already knows, opens the Brand Brain map for what matters and what changed, sends a deep question to /deep, and files what was learned. Asked to make a dashboard, report, deck or page: open writing-it-up too.
---

# Start here

This skill is a group of pages. Before you answer, read the ONE page below
that fits the question, then follow it. Read a second page only when the
question truly spans both. The paths are relative to this skill's folder.

**Every page is a pointer.** It says what it covers and how to fetch its
method from the server with `get_skill`. Make that call before you answer;
the page alone is not the method.

**A deep answer runs here, on this Claude, through `/deep`.** A message asking to go deep without the command gets one line: type `/deep` and the question. Open `pages/invoke-deep-synthesis/PAGE.md` only when the person asks for the server-run deep synthesis by name, or a server run's result arrives.

**Asked to MAKE something** (a dashboard, report, deck, chart, spreadsheet, page or file)? Open the writing group now: `../writing-it-up/pages/exports-and-deliverables/PAGE.md`, and fetch its method. A bare "make me a dashboard" with no detail gets the default dashboard that page describes, built first. Do not answer with questions and nothing built; offer to adjust after it exists. Use the pages below as well for grounding. Call `brand_kit` before building: `source: agency` means work for the client to read wears the agency's look and "Prepared by" the agency, never the client's look.

| Page | Open it when |
|---|---|
| `pages/synthesis-operating-protocol/PAGE.md` | On every real question about your business that Synthesis can answer, from "what was revenue last month" or "chart sales by week" to "should we expand", "why is repeat down" or "what is our biggest risk". |
| `pages/synthesis-reasoning-method/PAGE.md` | For a strategic, why or should-we question ("should we cut ad spend", "why is revenue falling", "what's driving repeat down", "give me a strategy to scale this product", "what is our biggest constraint") once the operating… |
| `pages/invoke-deep-synthesis/PAGE.md` | When someone asks for the deep analysis that runs on the Synthesis server, when a deep run's status, result or error arrives, or to collect a deep run started in another session. |
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

When a plain question asks for a plan, list, check, report or decision, call
get_skill with `question` set to their words before building the answer yourself,
and act on the first match by its `what_to_do`. It searches every ready automation,
not only the words below. Run at most one per question, with the question as the
extra instruction, and open the answer with one line naming it, for example
"Ran /repeat for this." A question about one number or a definition gets a normal
answer. When the fit is only a maybe, answer normally and end with one line offering
it, for example "Want me to run the stockout check now?"

A shortcut under "Runs once, then offers the repeat" runs from a plain question
with get_skill `once` true: answer now, set up nothing, and end by asking in one line
if they want it repeated.

Never start a shortcut under "Ask first" from a plain question, and never
/deep: they change a live account or run long. When one fits, answer what you can
without it and end by asking in one line, for example "Want me to run /budget? It
changes live budgets after your yes." Run it only after a clear yes. When a stock read
carries `_automation_next_step`, follow its `what_to_do`.

If the person's message starts with one of these words, or with /go and an
automation's title, and it reached you as plain text because the command did
not run, run it anyway: call get_skill with that word (or the /go text) and
follow the instructions it returns. Never answer that the command does not exist.
A slash word that is not on this list goes to get_skill too. When it returns
`no_match`, list the shortcuts in `closest` and ask which one the person meant.
Never pick a job yourself from a word that did not match.

When the person is new, or asks what they can do or which shortcut to use,
tell them to type /start: it shows the shortcuts for their job and runs the first.

- `/start` The shortcuts for your job, and the first one run on your data

Runs when it fits:

- **Agency:** `/clientupdate` Client performance update · `/fbaplan` FBA ship plan for a client · `/marketanalysis` Market analysis deck for a new Amazon product
- **Amazon:** `/adloss` Find ads that lose money after product cost · `/amazonlink` Make a tracked Amazon link for each ad · `/bids` Build the keyword bid change sheet · `/deals` Did that deal make money? · `/incremental` Are your ads buying sales you'd get anyway? · `/keywordflywheel` Keyword flywheel: how much to spend on each search · `/listing` Score and rewrite a product page to sell more · `/pricemove` Size an Amazon price or Subscribe and Save change · `/rivals` Who's stealing your search shoppers? · `/saleready` Get ready for the next big Amazon sale
- **Creative:** `/adcopy` Write ad copy for every buyer stage · `/scout` Scout creators and rival ads for me · `/static` Make static ads in my house style · `/teardown` Winning ads teardown
- **Customers:** `/bundles` Find bundles buyers already want · `/ltv` Which first product makes the best customers? · `/payback` How fast does a new customer pay back? · `/repeat` Repeat buying and lifetime value, product by product · `/returning` Is website growth from new or old customers? · `/reviews` Turn reviews into selling lines · `/winback` Win back customers who stopped buying
- **Email:** `/flows` Where your email flows lose people
- **Google:** `/googlewatch` Check Google Ads data is landing
- **Growth:** `/adcheck` Check my ads · `/ideas` Find your next product in search demand · `/mer` Is all your marketing paying, together? · `/nextdollar` What each channel must return to earn the next dollar
- **Inventory:** `/afford` Test a purchase order (needs your cash balance) · `/reorder` What to reorder, and the purchase order to send · `/shipcost` Is real shipping cost per box above what your profit numbers assume?
- **Meta:** `/adaudit` Audit my whole Meta account · `/adroi` Which Meta ads lose or make money · `/amazonrules` Which Meta ads for Amazon to keep, cut or move up · `/daily` Daily Meta ads · `/halo` Does Meta grow your Amazon sales? · `/metaamazon` Meta to Amazon read · `/newads` Check the ads I just launched · `/videorank` Rank my videos by cost per Amazon order and rebuild the best for the website
- **Money:** `/allprofit` Whole-business profit, every channel · `/amazonprofit` Amazon profit after every fee and cost · `/costup` A cost went up. Now what? · `/fees` Check for Amazon fee jumps · `/mix` Was it price, volume or mix? · `/pnlmatch` Match our profit to your profit app · `/price` What happens if you change the price? · `/profit` Which Amazon products actually make money? · `/shopifyprofit` Website profit after every cost · `/tiktokprofit` TikTok Shop profit after every fee · `/walmartprofit` Walmart profit after every fee · `/whyprofit` Why did profit move this month?
- **Retail:** `/coupon` Is this Walmart store coupon worth running again?
- **Strategy:** `/risk` What if we lost our biggest one?
- **Subscriptions:** `/cancels` Why subscribers cancel, and what to change · `/subcheck` Are subscriptions worth it, product by product?
- **TikTok Ads:** `/tiktokwatch` Check TikTok is still connected and sending data
- **TikTok Shop:** `/gmvtest` Plan and read a TikTok GMV Max pause test
- **Website:** `/buildlandingpage` Build a landing page from the kit · `/cro` Ideas to make a landing page sell more, and the next test · `/headlines` Rank selling angles by ad results, write headlines, and test them on the page · `/landingpage` Check a landing page like a shopper · `/pageprofit` Profit per order after ads, page by page · `/ppv` Profit per website visit · `/testread` Read a running test and make the call

Runs once, then offers the repeat:

- `/health` Is all my data fresh? · `/monday` Your Monday one-pager · `/morningchecklist` Amazon daily check · `/orderwatch` Are orders still coming in right after a site change? · `/stock` Send me the inventory report every Monday · `/stockout` Warn me before we run out

Ask first:

- `/addon` Add an add-on or after-payment upsell · `/addvideos` Add new videos as Meta ads · `/amazonblock` Block Amazon searches that cost money and never sell · `/amazonops` Run my Amazon ads each morning · `/budget` Change a Meta budget for me · `/codes` Set up a discount code or offer · `/creativetest` Run this week's Meta creative test · `/emailflow` Build a Klaviyo email flow for me · `/emailswap` Swap images or wording in my live Klaviyo emails · `/feedcut` Make feed-shape copies of my top ads · `/graduate` Move winning test ads into the main campaign · `/launch` Launch a Meta campaign · `/metaops` Run my Meta ads each morning · `/newpage` New landing page, start to finish · `/offeritem` Set up the product behind an offer · `/pagelive` Make a test version of a live page · `/pagetest` Test a new landing page on Meta · `/splittest` Run a split test on a page · `/toggle` Switch Meta ads on or off for me · `/trybe` Turn approved Trybe videos into Meta ads for me · `/trybeloop` Run my creator video tests each morning
