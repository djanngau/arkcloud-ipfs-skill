# ARKCloud IPFS Skill

ARKCloud IPFS skill for OpenClaw, CowAgent, and other agents that support `SKILL.md`.

This skill uploads files to the ARKCloud/IPFS upload API at `https://file.arklink.hk`, returns the resulting CID, short URL, credit usage, and duplicate status, and provides optional helpers for listing or deleting uploads when a client session is available.

## Install

From a GitHub repo:

```text
/skill install ARK-Interlink/arkcloud-ipfs-skill#skills/arkcloud-ipfs
```

Terminal form:

```bash
cow skill install ARK-Interlink/arkcloud-ipfs-skill#skills/arkcloud-ipfs
```

From a release zip:

```text
/skill install https://github.com/ARK-Interlink/arkcloud-ipfs-skill/releases/latest/download/arkcloud-ipfs.zip
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

