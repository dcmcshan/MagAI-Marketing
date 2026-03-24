#!/usr/bin/env python3
"""Add lectures 02–08 to scaffold courses (AINS-M6002–AINS-M6206 only).

AINS-M6001 is hand-authored and excluded—do not run this against M6001.
Idempotent: re-running overwrites the same lecture filenames and lecture sequence.
"""
from __future__ import annotations

import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT / "courses"

# Same metadata as generate_course_scaffold.py
DATA: list[tuple[str, str, str, str]] = [
    ("AINS-M6002", "Audience Worlds", "Term I", "Populations of agents with heterogeneous attention, trust, and channel habits—emergence from rules, not personas on slides."),
    ("AINS-M6003", "Positioning & Narrative Systems", "Term I", "Positioning and story as mechanisms: claims, categories, and narrative arcs as testable state machines."),
    ("AINS-M6004", "Brand as Dynamic System", "Term I", "Brand as state: awareness, association, trust, and elasticity under shocks."),
    ("AINS-M6005", "Channel & Content Economics", "Term I", "Reach, cost, and conversion across Meta, Google, and Amazon—parallel channel modules."),
    ("AINS-M6006", "Measurement, Privacy & Compliance", "Term I", "Measurement, consent, and compliance as first-class constraints; platform policy as enforceable rules."),
    ("AINS-M6101", "Campaign Orchestration", "Term II", "Multi-touch campaigns as coordinated dynamics across social, Google, and Amazon touchpoints."),
    ("AINS-M6102", "Creative Testing at Scale", "Term II", "Experiment systems: lift, variance, sample size, and when to stop."),
    ("AINS-M6103", "Data-Driven Marketing & Attribution", "Term II", "Attribution and decision workflows; triangulation across Google, Meta, and Amazon metrics."),
    ("AINS-M6104", "Partnerships & Ecosystem", "Term II", "Partners, affiliates, and ecosystems as agents with incentives and leakage."),
    ("AINS-M6105", "Growth Loops & Community", "Term II", "Loops and community as reinforced feedback; social and retail surfaces."),
    ("AINS-M6106", "Crisis & Reputation Stress Tests", "Term II", "Adversarial reputation scenarios and fragility analysis."),
    ("AINS-M6201", "Competitive Narrative Arena", "Term III", "Competing world models: strategic interaction as emergent behavior."),
    ("AINS-M6202", "Strategy as Marketing Policy", "Term III", "Strategy encoded as policy: rules mapping states to actions under uncertainty."),
    ("AINS-M6203", "Budget & Portfolio Allocation", "Term III", "Budget allocation across initiatives under constraints: liquidity, payback, risk of ruin."),
    ("AINS-M6204", "Autonomous Marketing Systems", "Term III", "Self-running marketing subsystems with human-in-the-loop boundaries and monitoring."),
    ("AINS-M6205", "Ethics, Influence & Control", "Term III", "Alignment and governance for influence systems: oversight and legibility."),
    ("AINS-M6206", "Magisterium Thesis (Marketing)", "Term III", "Capstone: real system, simulation validation, measurable outcomes, defense-ready documentation."),
]

# Shared filenames (unique within each course directory)
LECTURE_SPEC: list[tuple[str, str, str]] = [
    ("02_foundations", "Foundations", "Ontology, assumptions, and boundary conditions for this course."),
    ("03_core_mechanisms", "Core mechanisms", "Primary dynamics and formal moves your simulations must encode."),
    ("04_signals_and_measurement", "Signals & measurement", "What you observe, calibrate, and log—closing the loop between model and evidence."),
    ("05_system_integration", "System integration", "Connecting subsystems into one coherent, runnable world."),
    ("06_stress_and_failure_modes", "Stress & failure modes", "Adversarial scenarios, tail risk, and brittleness—before spend gets real."),
    ("07_tools_ethics_and_policy", "Tools, ethics & policy", "MCP surfaces, consent, and governance boundaries for this course’s artifact line."),
    ("08_artifact_synthesis_and_defense", "Artifact synthesis & defense", "Capstone readiness: lineage, documentation, and faculty Q&A."),
]


def lecture_body(code: str, title: str, term: str, slug: str, lect_title: str, one_line: str) -> str:
    return textwrap.dedent(
        f"""\
        ---
        title: "{lect_title} — {code}"
        description: "{lect_title} — {title}"
        ---

        # {lect_title} — {code}: {title}

        **{term}**

        {one_line}

        Read the [course syllabus](../) for outcomes and artifact expectations. Complete work in **iNQspace** with traceable lineage; use **SAMWISE** reflection prompts your faculty assigns; respect **MCP** policy in [MCP & marketing tools](../../docs/MCP_MARKETING.md).

        ## Core moves

        1. Connect this module to the prior lecture’s constructs.
        2. Encode at least one testable hypothesis in your simulation or notebook line.
        3. Document what you simplified and what would break if reality differed.

        ## Bridge

        The next lecture extends this module—keep assumptions and open questions visible.
        """
    ).strip() + "\n"


def syllabus_lecture_block() -> str:
    lines = [
        "## Lecture sequence",
        "",
        "Eight lectures. Each includes **Concept**, **PTAH** work in iNQspace, **SAMWISE** reflection, and **Faculty** challenge as your cohort syllabus specifies.",
        "",
        "- [Course overview](lectures/01_course_overview.md) — scope, outcomes, and how this module connects to your artifact line.",
    ]
    for slug, lect_title, blurb in LECTURE_SPEC:
        lines.append(f"- [{lect_title}](lectures/{slug}.md) — {blurb}")
    lines.append("")
    return "\n".join(lines)


def replace_lecture_sequence(text: str, new_block: str) -> str:
    """Replace from ## Lecture sequence through the next ## heading or EOF."""
    return re.sub(
        r"(?ms)^## Lecture sequence\b.*?(?=^## |\Z)",
        new_block.rstrip() + "\n",
        text,
        count=1,
    )


def main() -> None:
    block = syllabus_lecture_block()
    for code, title, term, _blurb in DATA:
        lec_dir = COURSES / code / "lectures"
        lec_dir.mkdir(parents=True, exist_ok=True)
        for slug, lect_title, one_line in LECTURE_SPEC:
            path = lec_dir / f"{slug}.md"
            path.write_text(lecture_body(code, title, term, slug, lect_title, one_line), encoding="utf-8")
            print("wrote", path.relative_to(ROOT))

        syllabus_path = COURSES / code / "SYLLABUS.md"
        text = syllabus_path.read_text(encoding="utf-8")
        if "## Lecture sequence" not in text:
            raise SystemExit(f"Missing ## Lecture sequence in {syllabus_path}")
        syllabus_path.write_text(replace_lecture_sequence(text, block), encoding="utf-8")
        print("updated", syllabus_path.relative_to(ROOT))


if __name__ == "__main__":
    main()
