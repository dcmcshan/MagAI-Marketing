#!/usr/bin/env python3
"""Capture Magisterium MagAI pages with Playwright for visual + content review."""
from __future__ import annotations

import json
import re
from pathlib import Path

from playwright.sync_api import sync_playwright

BASE = "https://magisterium.castalia.institute"
PAGES: list[tuple[str, str]] = [
    ("01-magai-hub", f"{BASE}/magai/"),
    ("02-marketing-home", f"{BASE}/magai/marketing/"),
    ("03-marketing-catalog", f"{BASE}/magai/marketing/catalog"),
    ("04-program-overview", f"{BASE}/magai/marketing/program-overview"),
]

OUT = Path(__file__).resolve().parent.parent / "playwright-review"


def extract_outline(page) -> dict:
    """Headings and key metrics for content review."""
    return page.evaluate(
        """() => {
          const hs = [...document.querySelectorAll('h1, h2, h3')].map(
            (el) => ({ tag: el.tagName, text: el.innerText.trim().slice(0, 200) })
          );
          const title = document.title;
          const metaDesc = document.querySelector('meta[name="description"]')?.content || '';
          const wordCount = document.body?.innerText?.split(/\\s+/).filter(Boolean).length ?? 0;
          return { title, metaDesc, wordCount, headings: hs.slice(0, 40) };
        }"""
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    report: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
            device_scale_factor=1,
        )
        page = context.new_page()
        page.set_default_timeout(60_000)

        for slug, url in PAGES:
            entry: dict = {"slug": slug, "url": url, "ok": False, "error": None}
            try:
                resp = page.goto(url, wait_until="domcontentloaded")
                entry["http_status"] = resp.status if resp else None
                page.wait_for_timeout(2500)
                entry["outline"] = extract_outline(page)
                png = OUT / f"{slug}-desktop.png"
                page.screenshot(path=str(png), full_page=True)
                entry["screenshot"] = str(png.relative_to(OUT.parent))
                entry["ok"] = True
            except Exception as e:
                entry["error"] = str(e)
            report.append(entry)

        # Mobile pass — marketing home only
        mctx = browser.new_context(
            viewport={"width": 390, "height": 844},
            device_scale_factor=2,
        )
        mp = mctx.new_page()
        try:
            mp.goto(PAGES[1][1], wait_until="domcontentloaded")
            mp.wait_for_timeout(2500)
            mp.screenshot(path=str(OUT / "02-marketing-home-mobile.png"), full_page=True)
        finally:
            mctx.close()

        context.close()
        browser.close()

    (OUT / "report.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
