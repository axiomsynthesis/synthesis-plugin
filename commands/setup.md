---
description: "Check your Synthesis connection and turn on automatic updates"
disable-model-invocation: true
---

# Set up Synthesis

Do these four things in order. Report each one in a single plain sentence, and
change nothing beyond what step 2 says.

1. **Connection.** Use the Synthesis tool `brand_context_frame`. If it answers,
   say which brand this Claude is connected to. If the Synthesis tools are
   missing or ask for a sign-in, tell the person to type /mcp, choose
   synthesis, and sign in with their Synthesis access key, then run this
   shortcut again. Stop there.

2. **Automatic updates.** Open the person's Claude Code settings file,
   `~/.claude/settings.json`. Look under `extraKnownMarketplaces` for the
   `axiom-synthesis` entry.
   - If it already has `"autoUpdate": true`, say updates are already automatic.
   - If it does not, say in one sentence what you are about to change, then add
     `"autoUpdate": true` to that one entry. Keep every other setting in the
     file exactly as it is.
   - If there is no `axiom-synthesis` entry at all, add this under
     `extraKnownMarketplaces` and change nothing else:
     `"axiom-synthesis": {"source": {"source": "url", "url": "https://synthesisintelligence.ai/cli/marketplace.json"}, "autoUpdate": true}`

   Then say: Synthesis now updates itself each time Claude Code starts.

3. **Answer memory.** Say: answers that use Synthesis are saved to your brand's
   memory, so it learns from what Claude concludes. To switch that off on this
   computer, set `SSI_CAPTURE_DISABLED=1` in your shell. For the whole brand, an
   admin turns off Answer memory on the brand's card in Settings, under Brands.

4. **Shortcuts.** Say: you can run a ready-made job by typing one word. Try
   these first, then type / to see the rest:
   - /fees checks for Amazon fees that went up for no reason
   - /stockout warns before a product runs out
   - /whyprofit explains why profit moved this month
   - /reorder drafts a reorder plan
   Then say: any other automation runs with /go and its name, like
   /go win-back list.
