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
list every other one, and `/setup` to check your connection. `/start` brings
these steps back.

## Install

Add Synthesis from Claude's plugin directory. Then sign in: in Claude Code, type
`/mcp`, choose `plugin:synthesis:synthesis`, press Authenticate, and paste your
Synthesis access key, which you make on the Connect your AI page. You see your
brand and nothing else. You need a Synthesis account and a paid Claude plan.

You can also install from a Mac terminal with one line. It installs Claude Code first if needed, and
`synthesis-design`, a second plugin with design skills for landing pages, banners, design systems and UI:

```
command -v claude >/dev/null 2>&1 || curl -fsSL https://claude.ai/install.sh | bash; export PATH="$HOME/.local/bin:$PATH"; claude plugin marketplace add https://synthesisintelligence.ai/cli/marketplace.json && claude plugin marketplace update axiom-synthesis && claude plugin install synthesis@axiom-synthesis && claude plugin install synthesis-design@axiom-synthesis && claude plugin update synthesis@axiom-synthesis && claude plugin update synthesis-design@axiom-synthesis && (plutil -replace extraKnownMarketplaces.axiom-synthesis.autoUpdate -bool YES ~/.claude/settings.json 2>/dev/null || echo "Updates are off. Ask Claude to turn on auto-update for Synthesis.") && claude mcp login plugin:synthesis:synthesis
```

That line turns on updates too. If it says updates are off, tell Claude "Turn on auto-update for the
Synthesis plugin" once. Or update by hand, then run `/reload-plugins` or start a new session:

```
claude plugin marketplace update axiom-synthesis && claude plugin update synthesis@axiom-synthesis && claude plugin update synthesis-design@axiom-synthesis
```

On Windows, paste this into PowerShell instead, then ask Claude to turn on auto-update:
```
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) { irm https://claude.ai/install.ps1 | iex }; $env:Path = "$env:USERPROFILE\.local\bin;$env:Path"; claude plugin marketplace add https://synthesisintelligence.ai/cli/marketplace.json; claude plugin marketplace update axiom-synthesis; claude plugin install synthesis@axiom-synthesis; claude plugin install synthesis-design@axiom-synthesis; claude plugin update synthesis@axiom-synthesis; claude plugin update synthesis-design@axiom-synthesis; claude mcp login plugin:synthesis:synthesis
```

## Set up

Nothing else is needed once you have signed in through `/mcp`, or if Claude
already has the Synthesis connector from your claude.ai account.

Answer memory is on. When Claude finishes an answer that used Synthesis, it
saves that answer and the question it answered to your brand's memory, so the
memory grows from what Claude concluded. An admin can turn it off for the
whole brand on its card in Settings.

## What leaves your machine, and where it goes

This plugin ships no scripts. It is written instructions for Claude and a
connection to `https://synthesisintelligence.ai/mcp`. Everything it sends goes
there, through that connection: the questions Claude asks Synthesis, and the
answers Claude saves to your brand's memory.

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
