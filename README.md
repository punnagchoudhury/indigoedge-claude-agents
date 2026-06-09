# IndigoEdge Claude Agents — private plugin marketplace

A **private** Claude Code plugin marketplace for IndigoEdge. It distributes internal AI agents to everyone in the org with one-command install and automatic updates. The first plugin is the **Market Research Agent** (pre-diligence dossiers). Future agents — including DDE-system components — can be added to the same marketplace rather than living in separate silos.

> **Private — internal only.** This repository encodes IndigoEdge's research methodology and connects to internal Notion/Slack data. Host it in a **private** Git repo. Do **not** publish to any public marketplace.

---

## What's in here

```
indigoedge-claude-agents/
├── .claude-plugin/
│   └── marketplace.json                # the catalog (lists the plugins)
└── plugins/
    └── market-research-agent/
        ├── .claude-plugin/
        │   └── plugin.json             # plugin manifest + MCP connector declarations
        ├── skills/
        │   └── market-research-agent/
        │       └── SKILL.md            # the agent's brain (the v9 operating method)
        ├── commands/
        │   └── dossier.md              # /dossier <company> slash command
        ├── reference/
        │   └── playbook.md             # full design doctrine (consulted on demand)
        └── assets/
            ├── IndigoEdge_Dossier_Template.docx   # branded Word template
            └── build_ie_template.py               # regenerates the template
```

When a fellow installs the plugin, Claude Code copies this whole directory into a local cache, so the template, script, and playbook travel with it.

---

## One-time setup (admin)

**Prerequisites:** each fellow needs Claude Code installed and a Claude plan that includes it; the Word deliverable needs `pandoc` on the machine.

### 1. Fill in two placeholders
- In `.claude-plugin/marketplace.json` → `owner.email`.
- Confirm the three MCP endpoint URLs in `plugins/market-research-agent/.claude-plugin/plugin.json` are correct for our tenants (Tracxn / Notion / Slack). These are the remote MCP URLs; each fellow signs in **per-user** (see "Connectors" below), so no shared secret lives in the repo. Adjust or add connectors (Airtable, Google Drive) here as needed.

### 2. Validate before publishing
From this directory:
```bash
claude plugin validate .
```
Fix anything it flags (JSON syntax, kebab-case names, version mismatches).

### 3. Push to a private repo
```bash
git init && git add . && git commit -m "IndigoEdge agents marketplace: Market Research Agent v9"
git remote add origin git@github.com:INDIGOEDGE_ORG/indigoedge-claude-agents.git   # private repo
git push -u origin main
```

### 4. (Recommended) make it org-wide automatically
Instead of asking every fellow to run install commands, push these to the firm's **managed settings** (`managed-settings.json`) or a shared project's `.claude/settings.json`. This registers the marketplace and enables the plugin for everyone, and locks installs to our repo only:

```json
{
  "extraKnownMarketplaces": {
    "indigoedge-agents": {
      "source": { "source": "github", "repo": "INDIGOEDGE_ORG/indigoedge-claude-agents" }
    }
  },
  "enabledPlugins": {
    "market-research-agent@indigoedge-agents": true
  },
  "strictKnownMarketplaces": [
    { "source": "github", "repo": "INDIGOEDGE_ORG/indigoedge-claude-agents" }
  ]
}
```
For background auto-updates from a private repo, set `GITHUB_TOKEN` (read access to the repo) in the environment.

---

## How a fellow uses it

If the admin set up managed settings (step 4), the plugin is already there — skip to "Run it." Otherwise, install once:

```bash
# add the private marketplace (uses your existing GitHub credentials)
/plugin marketplace add INDIGOEDGE_ORG/indigoedge-claude-agents
# install the agent
/plugin install market-research-agent@indigoedge-agents
```

**Connectors (per-user, one time):** run `/mcp` and sign in to Tracxn, Notion, and Slack. Authentication is per-user — fellows only ever reach data they personally have access to, which is the data-governance win of this approach.

**Run it:**
```bash
/dossier Pratilipi  (pratilipi.com)
```
…or just ask in plain language, e.g. *"Run a pre-diligence dossier on Supertails."* The dossier is written to the Notion **Market Research Dossiers** database; ask for the branded Word doc if you want the `.docx`.

---

## Updating the agent (push once, everyone gets it)

This is the payoff of the marketplace. To ship a change (e.g. the pending presentation-standards update — founders table, SWOT 2×2, labelled internal precedents, etc.):

1. Edit the relevant file (usually `skills/market-research-agent/SKILL.md` or `reference/playbook.md`).
2. Bump `"version"` in `plugins/market-research-agent/.claude-plugin/plugin.json` (e.g. `9.0.0` → `9.1.0`). **Bumping the version is what triggers the update for installed users** — if you don't bump it, nothing changes for them. (Alternatively, omit `version` entirely and every commit counts as a new version.)
3. Commit and push.

Fellows pick it up with:
```bash
/plugin marketplace update indigoedge-agents
/plugin update market-research-agent@indigoedge-agents
```
(Or automatically, if managed settings + `GITHUB_TOKEN` are configured.)

---

## Notes
- **Version source of truth:** keep `version` in `plugin.json` only (not also in `marketplace.json`) — the manifest value always wins, and setting it in both is a known footgun.
- **No secrets in the repo:** connectors authenticate per-user via OAuth; nothing here contains credentials.
- **Adding more agents later:** create another folder under `plugins/`, give it its own `plugin.json` + `skills/…/SKILL.md`, and add an entry to `marketplace.json`'s `plugins` array.
