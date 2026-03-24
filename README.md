# Mag.AI-Marketing

**Castalia Institute — Magister of Artificial Intelligence in Marketing**

> Marketing is a world model with attention, trust, and measurable persuasion.

---

## Source of truth: MyST

**All program narrative, curriculum, public pages, and course sources** are authored in this repo and built with the MyST / Jupyter Book CLI stack from `requirements-docs.txt`. The **program hub** (orientation, docs, catalog) is defined by root [`myst.yml`](myst.yml). **Each course** has its own [`myst.yml`](courses/AINS-M6001/myst.yml) under `courses/AINS-M####/` and builds as a **separate book**. That tree is **canonical**. Everything else **derives** from it:

| Derived surface | Role |
| --- | --- |
| **`myst start` / `myst build`** or **`jupyter-book build --site`** | Static site (HTML in `_build/`) — use `jupyter-book build --site` with **no trailing path** |
| **Slides** | Decks under `slides/` (`+++` frame breaks for export) |
| **Exercises** | `{exercise}` / `{solution}` blocks under `exercises/` |
| **Exports** | PDF, Word, JATS via `jupyter-book build --pdf` (etc.) when needed |
| **iNQspace** | Teaching and execution: notebooks, simulations, lineage — **content** is ingested from these MyST-authored paths; labs run there |
| **MCP** | **Marketing tools:** students **build** and **leverage** [Model Context Protocol](https://modelcontextprotocol.io/) servers for real data/actions — see [`docs/MCP_MARKETING.md`](docs/MCP_MARKETING.md) |
| **This `README.md`** | Orientation and clone/build commands only — **not** a second curriculum. Excluded from the MyST build. |

Edit **`docs/`**, **`pages/`**, **`courses/`**, and **`index.md`**; list hub pages in root **`myst.yml`** → **`project.toc`**, and each course’s pages in that course’s **`myst.yml`**. Regenerate course `myst.yml` files after scaffold changes with `python3 scripts/generate_course_myst.py`. Do not fork wording in the README.

**Entry page for readers:** [`index.md`](index.md) (hub). **Course index:** [`catalog.md`](catalog.md). Each course book is built from `courses/AINS-M####/`.

Completing the credential means leaving with a **full toolbox** — inspectable world models, deployment evidence, **technical AI practice** (eval, grounding, oversight), MCP marketing-tool integration, and publishable artifacts. See [`pages/certificate.md`](pages/certificate.md#graduate-toolbox).

---

## Teach AI (iNQspace) + author content (MyST)

- **iNQspace** — where students run notebooks, simulations, and tracked artifacts.
- **Authoring tree** — syllabi, lectures, program docs, and public pages in the MyST project.
- **Build CLI** — same toolchain produces the public site, slide sources, and exercise banks from this repo.
- **MCP** — courses integrate **marketing tools** (analytics, CRM, ads, CMS, etc.) via Model Context Protocol: **inspectable** tool contracts, not opaque automation.
- **Curriculum principles** — [`docs/CURRICULUM_FULL.md`](docs/CURRICULUM_FULL.md): **AI literacy spine** (eval, RAG, generative QA, scoped tools), **tools-first platform ecosystems** (**Meta**, **Google**, **Amazon**), qualitative grounding, pacing, B2B/B2C and channel modeling notes.

See [`docs/DESIGN.md`](docs/DESIGN.md) and [`docs/MCP_MARKETING.md`](docs/MCP_MARKETING.md) for architecture and tool policy.

---

## Build the books locally

**Program hub** (one build from repo root):

```bash
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-docs.txt
myst start                    # http://localhost:3000 (or next free port)
# myst build                  # static site → _build/
jupyter-book build --site     # hub + catalog; run from repo root (no `.` at end)
```

**Each course book** (18 builds — run from each `courses/AINS-M####/` directory, or use):

```bash
bash scripts/build_all_books.sh   # hub, then every course under courses/AINS-M*/
```

**Canonical public site (Magisterium):** CI in [InquiryInstitute/magisterium](https://github.com/InquiryInstitute/magisterium) should publish the **hub** under **`/magai/marketing/`** and each **course** under **`/magai/marketing/ains-m####/`** (see [`catalog.md`](catalog.md)). See [magisterium/docs/MAG_AI_PROGRAMS.md](https://github.com/InquiryInstitute/magisterium/blob/main/docs/MAG_AI_PROGRAMS.md).

**Local static HTML preview** (same `BASE_URL` as production; set per build for nested paths):

```bash
BASE_URL=/magai/marketing jupyter-book build --html --ci
# open _build/html/index.html (or serve the folder)
```

Or use the magisterium helper (expects this repo as a sibling of `magisterium/`): `../magisterium/scripts/build-magai-marketing-book.sh` — update that script if it still assumes a single root build only.

---

## Repository layout (canonical files)

```
MagAI-Marketing/
├── myst.yml              # Program hub TOC: index, catalog, pages, docs (not course sources)
├── catalog.md            # Links to every course book (slug paths)
├── index.md              # Hub home (MyST)
├── docs/                 # DESIGN, CURRICULUM_FULL, ASSESSMENT, MCP_MARKETING (MyST)
├── pages/                # Public pages (MyST)
├── slides/               # Instructor decks (MyST; +++ frame breaks)
├── exercises/            # {exercise} / {solution} banks (MyST)
├── courses/              # AINS-M####: syllabus, lectures, myst.yml per course (each = own book)
├── scripts/              # generate_course_myst.py, build_all_books.sh
├── requirements-docs.txt # mystmd + jupyter-book
└── README.md             # This file — stub only (excluded from MyST)
```

**Curriculum tables and course detail:** open the built site or the Markdown under `docs/` and `pages/` — do not duplicate here.

---

## Legal

> "The Castalia Institute Magisterium confers proprietary credentials based on demonstrated work and evaluation. These credentials are not accredited academic degrees and do not confer professional licensure."
