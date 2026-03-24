---
title: AINS-M6001 — MCP tool design
description: Map marketing actions to MCP tools (build + leverage)
---

# AINS-M6001 — MCP & marketing tools

Read `docs/MCP_MARKETING.md` first. Complete one **leverage** exercise and one **build** sketch.

```{exercise}
:label: ex-mcp-leverage

**Leverage:** Pick **one** marketing workflow you already use (e.g. check weekly analytics, draft a post from a template, export a subscriber segment). List **three concrete operations** an AI assistant would need (read metric X, list pages Y, …). For each operation, name an **MCP-shaped** tool (existing server or hypothetical) and **one way** the tool could be misused if scope were too broad.
```

```{exercise}
:label: ex-mcp-build

**Build:** Sketch (bullet list is enough) a minimal **MCP server** that exposes **two tools** and **one resource** supporting your personal influence model from the notebooks — e.g. `get_last_week_content_hours`, `append_reflection_log`, resource `profile://influence-state`. State **least-privilege** credentials you would require and what you would **never** expose.
```

```{solution} ex-mcp-leverage
:label: sol-mcp-leverage

Strong answers name **observable** operations (not vibes), separate **read** vs **write**, and name misuse (e.g. exfiltrating PII, posting without confirmation, deleting data).
```

```{solution} ex-mcp-build
:label: sol-mcp-build

Strong answers keep the server **narrow**, separate **test** vs **prod**, and align tools with entities already in the student’s PTAH-style ontology.
```
