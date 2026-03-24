# MCP — Marketing Tools in the Mag.AI-M Curriculum

**Castalia Institute — Mag.AI-Marketing**

*Authoritative copy: part of the MyST project (`myst.yml`).*

---

## What MCP is (here)

The **Model Context Protocol (MCP)** is an open standard for connecting AI assistants to **external tools and data** through well-defined servers. In this program, **marketing tools** means any capability you would use in real go-to-market work — analytics, CRM, ad platforms, content systems, search/social APIs, internal spreadsheets — **exposed as MCP servers** (or consumed from approved community servers) so workflows stay **inspectable, scoped, and reproducible**.

We care about MCP because it forces **explicit contracts**: what the model can *do*, with what credentials, and what gets logged — instead of opaque “the AI did something in the browser.”

**Curriculum alignment:** Mag.AI-M **names** major ecosystems students model and may connect: **Meta (Facebook/Instagram)**, **Google (Ads, Analytics/GA4-style, Search/YouTube)**, **Amazon (marketplace + Sponsored Products/Brands + retail media)**—see `CURRICULUM_FULL.md` (*Major platform ecosystems*). MCP servers might wrap **read-only** reporting pulls, creative asset lists, or **synthetic** datasets with the same **schema shape** as production exports.

---

## Build vs leverage

| Mode | What students do |
| --- | --- |
| **Leverage** | Call existing MCP tools from notebooks or agents: pull metrics, draft from templates, query segments — always with **documented** assumptions and evaluation |
| **Build** | Implement or extend **MCP servers** that wrap marketing APIs, data stores, or simulators (including PTAH/iNQspace hooks): define resources, tools, and prompts with **least privilege** |

Courses expect **both**: you must *use* tools well before you *ship* tools others depend on.

---

## How terms use MCP

- **Term I (Audience & Message):** Instrument **personal** and **audience** models with live signals where ethical (e.g. your own site analytics, public trend APIs) via MCP; design tool schemas that map to ontology choices.
- **Term II (Campaign & Growth):** Orchestrate multi-touch workflows; attribute and experiment with **data pulled through MCP**, not screenshots.
- **Term III (Strategy):** Portfolio and automation courses require **governed** MCP surfaces (audit trails, escalation) aligned with AINS-M6205.

Specific course artifacts may require an **MCP appendix**: tools used, servers touched, and failure modes.

---

## Guardrails (non-negotiable)

1. **Consent & ToS** — Only connect accounts and data you are allowed to use for coursework; respect platform policies.
2. **Secrets** — No API keys in Git; use environment / secret stores as required by iNQspace or faculty policy.
3. **Scope** — Tools are **narrowly** described; avoid “full admin” MCP surfaces for class demos.
4. **Measurement** — When MCP feeds a model, **document latency, bias, and missing data** as you would for any sensor.

---

## Access and equity

Not every student has **ad accounts, spend, or employer API access**. Faculty may provide:

- **Shared or faculty-hosted** MCP endpoints with **read-only** or **synthetic** data
- **Paired projects** where one student supplies account access under policy and another builds analysis only
- **Fully synthetic** endpoints that still exercise **tool contracts** and logging

Course artifacts must be **achievable** without self-funding ad spend; live spend is **optional** enhancement, not a hidden prerequisite.

---

## References (external)

- [Model Context Protocol — specification & SDKs](https://modelcontextprotocol.io/)

---

## Legal

> "The Castalia Institute Magisterium confers proprietary credentials based on demonstrated work and evaluation. These credentials are not accredited academic degrees and do not confer professional licensure."
