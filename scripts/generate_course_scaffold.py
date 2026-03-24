#!/usr/bin/env python3
"""Generate AINS-M6002–AINS-M6206 syllabus + lecture 01 overview.

After running, execute `scripts/scaffold_eight_lectures.py` to add lectures 02–08
and replace the lecture sequence in each syllabus. (AINS-M6001 is authored separately.)
"""
from __future__ import annotations

import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = ROOT / "courses"

# (code, title, term_label, one_line description from curriculum)
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


def syllabus(code: str, title: str, term: str, blurb: str) -> str:
    slug = code.lower().replace("—", "-")
    return textwrap.dedent(
        f"""\
        ---
        title: "{code}: {title}"
        description: "{title} — Mag.AI-Marketing"
        ---

        # {code}: {title}

        **{term} — Mag.AI-Marketing**  
        **Castalia Institute**

        Authoritative program text. Full program context and prerequisites appear in the [full curriculum](/curriculum-full).

        ---

        ## Course overview

        {blurb}

        For complete learning objectives, artifacts, AI systems, and prerequisites, see the corresponding section in [Full curriculum](/curriculum-full).

        ---

        ## Course structure

        The course is organized into **eight lectures**; run `scripts/scaffold_eight_lectures.py` after this generator to create lectures 02–08 and the full sidebar list.

        ---

        ## Lecture sequence

        - [Course overview](lectures/01_course_overview) — scope, outcomes, and how this module connects to your artifact line.

        *(Lectures 02–08 are added by `scripts/scaffold_eight_lectures.py`.)*
        """
    ).strip() + "\n"


def lecture(code: str, title: str, term: str) -> str:
    return textwrap.dedent(
        f"""\
        ---
        title: "Course overview — {code}"
        description: "Introduction and module map for {title}"
        ---

        # Course overview — {code}: {title}

        **{term}**

        This module sets the scope for **{code}**. Read the [course syllabus](../) for the full artifact expectations, prerequisite chain, and how PTAH, SAMWISE, AI Faculty, and MCP show up in this course.

        ## What you will build

        The required artifact for this course is defined in the [full curriculum](/curriculum-full) under your course heading. Your job is to produce a runnable, documented system that meets the minimum viable artifact criteria your faculty publishes for the cohort.

        ## How to proceed

        1. Align your ontology and assumptions with the syllabus.  
        2. Implement in **iNQspace** with traceable lineage.  
        3. Reflect with **SAMWISE** and defend against **AI Faculty** challenges.  
        4. Where policy allows, connect **MCP** tool surfaces and document scope and limits.

        Next lectures in this course will appear here as they are released.
        """
    ).strip() + "\n"


def main() -> None:
    for code, title, term, blurb in DATA:
        d = COURSES / code
        lec = d / "lectures"
        lec.mkdir(parents=True, exist_ok=True)
        (d / "SYLLABUS.md").write_text(syllabus(code, title, term, blurb), encoding="utf-8")
        (lec / "01_course_overview.md").write_text(lecture(code, title, term), encoding="utf-8")
        print("wrote", d)


if __name__ == "__main__":
    main()
