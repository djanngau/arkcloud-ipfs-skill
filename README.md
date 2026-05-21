# ARKCloud IPFS Skill for OpenClaw

ARKCloud IPFS OpenClaw skill for OpenClaw, CowAgent, Claude Code, and other agents that support `SKILL.md`.

This skill uploads files to the ARKCloud/IPFS upload API at `https://file.arklink.hk`, returns the resulting CID, access link, credit usage, and duplicate status, and provides optional helpers for listing or deleting uploads when a client session is available. Upload responses show the CID and access link, and agents should prompt users to open the link when they want to view or share the uploaded file.

Keywords: `arkcloud`, `ARKCloud`, `arkcloud-ipfs`, `ARK Cloud`, `openclaw-skill`, `cowagent-skill`, `claude-code-skill`, `ipfs`, `cid`, `file.arklink.hk`, `decentralized-storage`.

## Install

From a GitHub repo:

```text
/skill install djanngau/arkcloud-ipfs-skill#skills/arkcloud-ipfs
```

Terminal form:

```bash
cow skill install djanngau/arkcloud-ipfs-skill#skills/arkcloud-ipfs
```

From a release zip:

```text
/skill install https://github.com/djanngau/arkcloud-ipfs-skill/releases/latest/download/arkcloud-ipfs.zip
```

## Configure

Set an upload token before using the upload helper:

```bash
export ARKCLOUD_UPLOAD_TOKEN="<token>"
```

Optional:

```bash
export ARKCLOUD_BASE_URL="https://file.arklink.hk"
```

For list/delete helpers, provide a logged-in client session cookie and CSRF token:

```bash
export ARKCLOUD_CLIENT_COOKIE="<cookie header>"
export ARKCLOUD_CSRF_TOKEN="<csrf>"
```

Never commit real tokens, cookies, admin secrets, wallet private keys, or `.env` files.
