# Synthesis for Claude Code

Your brand's real numbers, and the doctrine for reading them, inside your own
Claude Code.

Once installed, Claude answers questions about your business from your actual
warehouse instead of guessing — and it reads those numbers the way an operator
who knows your category would, not the way a platform dashboard presents them.

## Start here

1. Sign in: in Claude Code, type `/mcp`, press Enter twice, and sign in with
   your Synthesis key.
2. Type `/start` and say what you do, like "I run the ads". It picks the
   shortcuts for your job and runs the first one on your numbers.
3. Ask "What needs my attention this week?" to see your biggest problem.

Try first: `/health` (data that needs attention), `/whyprofit` (why profit
moved), `/stockout` (products about to run out), `/fees` (Amazon fee
overcharges) and `/deep` with a question (a fully checked deep answer).
Automations worth opening: `/reorder`, `/adloss` and `/winback`. Type `/go` to
list every other one, and `/setup` to check your connection. Claude shows
these steps the first time it opens, and `/start` brings them back.

## Install

Add Synthesis from Claude's plugin directory. Then sign in: in Claude Code, type
`/mcp`, choose `plugin:synthesis:synthesis`, press Authenticate, and paste your
Synthesis access key, which you make on the Connect your AI page. You see your
brand and nothing else. You need a Synthesis account and a paid Claude plan.

You can also install from a terminal with one line. It installs Claude Code
first if this computer does not have it, and it also installs `synthesis-design`, a second plugin with
design skills for landing pages, banners, design systems and UI:

```
command -v claude >/dev/null 2>&1 || curl -fsSL https://claude.ai/install.sh | bash; export PATH="$HOME/.local/bin:$PATH"; claude plugin marketplace add https://synthesisintelligence.ai/cli/marketplace.json && claude plugin marketplace update axiom-synthesis && claude plugin install synthesis@axiom-synthesis && claude plugin install synthesis-design@axiom-synthesis && claude plugin update synthesis@axiom-synthesis && claude plugin update synthesis-design@axiom-synthesis && (plutil -replace extraKnownMarketplaces.axiom-synthesis.autoUpdate -bool YES ~/.claude/settings.json 2>/dev/null || echo "Updates are off. Ask Claude to turn on auto-update for Synthesis.") && claude mcp login plugin:synthesis:synthesis
```

That line turns on updates too, so you get every new version. If it says
updates are off, tell Claude "Turn on auto-update for the Synthesis plugin"
once. Or update by hand:

```
claude plugin marketplace update axiom-synthesis && claude plugin update synthesis@axiom-synthesis && claude plugin update synthesis-design@axiom-synthesis
```

After an update, run `/reload-plugins` or start a new session.

## Set up

Nothing else is needed once you have signed in through `/mcp`, or if Claude Code
already has the Synthesis connector from your claude.ai account.

**Answer memory is on.** When Claude finishes an answer that used Synthesis,
the plugin sends that answer, the question it answered, and the steps Claude
took with Synthesis to get there. Your brand's memory then grows from what
Claude concluded, not only from what it looked up. The steps are which
Synthesis tools Claude used and what it asked each one. They never include
what those tools sent back, or which other tools and servers you used. An
answer that did not use Synthesis is never sent.

Off on your machine: set `SSI_CAPTURE_DISABLED=1`. Off for the whole brand: an
admin turns off Answer memory on its card in Settings. Nothing saved is deleted.

**`SSI_MCP_TOKEN`** is optional. Set it to your Synthesis access key and the
brand's state is fetched before your first prompt, rather than by Claude on its
first step. It is read from your environment and nowhere else: the plugin never
opens Claude Code's own credential store.

## What leaves your machine, and where it goes

Only to `synthesisintelligence.ai`. The address is pinned in the plugin and
cannot be redirected by an environment variable, a config file, or anything
else on your machine — a request to any other host is refused before it is
made.

- At session start, only if you set `SSI_MCP_TOKEN`: that key, to fetch your
  brand's context.
- With each Synthesis call Claude makes: a fingerprint of a random code the
  plugin keeps on your machine, one per session. It ties that code to your
  sign-in, so the plugin can save answers without ever holding your access
  key. The code itself stays in `~/.synthesis/keys`, readable only by you. It
  can save answers to your brand and nothing else, and it stops working six
  hours after your last Synthesis call.
- On each answer that used Synthesis: the answer, its question, and the
  Synthesis steps behind it (which tools and what was asked, not what they
  returned). Plus one yes or no: whether anything in this session read Google
  data (Analytics, Ads, Search Console or Sheets). If it did, that answer is
  kept out of anything we use to improve Synthesis for all customers, as
  Google's terms require.
- Otherwise: nothing.

## What you get

**Your data.** Every source you have connected — marketplace, store,
subscriptions, email, ads, finance — reachable as tools Claude can call while
it answers.

**Operating know-how, in eleven groups.** Paid media, marketplace, store,
customer and cohort work, retail, creators, supply chain, financial modelling,
reporting, and the layer that reads across all of them. Each group is a short
routing page; when a question needs one, Claude fetches the method for it from
your account as it answers, so what you read is always the current version.

**The corrections that matter.** Platform numbers are not neutral. A return
figure from an ad platform cannot see marketplace sales, so scaling on it
loses money at exactly the moment it looks best. Results carry that context
with them rather than leaving you to remember it.

## What it does not do

It does not change anything and holds no login to your ad or store accounts. It reads, it reasons, and it hands you an exact list of changes.
Your own Claude can apply that list in your browser, signed in as you, one change at a time with your yes. Spending decisions stay yours.

## Support

andre@synthesisintelligence.ai
