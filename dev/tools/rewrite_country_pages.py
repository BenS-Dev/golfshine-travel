#!/usr/bin/env python3
"""Rewrite each redesign/golf/{country}.html: replace the .stack-lg article list with
a .tile image grid. Each tile links to the per-course detail page when one exists,
otherwise to contact.html?inquiry=… .
"""
import csv
import html as html_lib
import re
import unicodedata
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parents[2]
REDESIGN = ROOT / "redesign"
CSV_PATH = REDESIGN / "docs" / "COURSE_MAP.csv"
GOLF_DIR = REDESIGN / "golf"
COURSES_IMG_DIR = REDESIGN / "assets" / "images" / "golf" / "courses"
COUNTRY_FALLBACK_IMG_DIR = REDESIGN / "assets" / "images" / "golf"

# Per-country fallback image for tiles when no course-specific hero exists.
COUNTRY_FALLBACK = {
    "scotland": "scotland-st-andrews.jpg",
    "ireland": "ireland-ballyliffin.jpg",
    "wales": "scotland-st-andrews.jpg",
    "spain": "spain-barcelona.jpg",
    "portugal": "portugal-algarve.jpg",
    "france": "spain-barcelona.jpg",
    "italy": "italy-milan.jpg",
    "netherlands": "netherlands-amsterdam.jpg",
    "germany": "netherlands-amsterdam.jpg",
    "switzerland": "italy-milan.jpg",
    "greece": "greece-costa-navarino.jpg",
    "sweden": "netherlands-amsterdam.jpg",
    "denmark": "netherlands-amsterdam.jpg",
    "norway": "netherlands-amsterdam.jpg",
}


def esc(s: str) -> str:
    return html_lib.escape(s, quote=True)


def tile_html(row: dict) -> str:
    country = row["country_slug"]
    course_slug = row["course_slug"]
    course = row["course_name"]
    region = row["region"]
    country_name = row["country_name"]

    stem = f"{country}-{course_slug}"
    candidates = sorted(COURSES_IMG_DIR.glob(f"{stem}.*"))
    if candidates:
        img_src = f"../assets/images/golf/courses/{candidates[0].name}"
    else:
        img_name = COUNTRY_FALLBACK.get(country, "scotland-st-andrews.jpg")
        img_src = f"../assets/images/golf/{img_name}"

    if row["status"] == "matched":
        href = f"{country}/{course_slug}.html"
    else:
        # image-only and no-detail both link to contact form
        href = f"../contact.html?inquiry={quote_plus(course)}"

    return (
        f'        <a class="tile" href="{esc(href)}">\n'
        f'          <img src="{img_src}" alt="{esc(course)}" loading="lazy" decoding="async" />\n'
        f'          <div class="tile__body"><span class="tile__region">{esc(region)} · {esc(country_name)}</span><h3 class="tile__name">{esc(course)}</h3></div>\n'
        f'        </a>'
    )


STACK_LG_RE = re.compile(
    r'<div class="stack-lg" style="margin-top: var\(--space-2xl\);">.*?</div>',
    re.S,
)
# Existing tile grid (idempotent re-runs).
TILE_GRID_RE = re.compile(
    r'<div class="grid grid--3 grid--gap-sm" style="margin-top: var\(--space-2xl\);">.*?</div>\s*</div>\s*</section>',
    re.S,
)
NARROW_TO_WIDE_RE = re.compile(r'<div class="container container--narrow">')


def main():
    # group rows by country, preserve CSV order
    by_country: dict[str, list[dict]] = {}
    with CSV_PATH.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            by_country.setdefault(row["country_slug"], []).append(row)

    for country, rows in by_country.items():
        page_path = GOLF_DIR / f"{country}.html"
        if not page_path.exists():
            print(f"  skip (page missing): {country}")
            continue
        src = page_path.read_text(encoding="utf-8")

        # build new tile grid
        tiles = "\n".join(tile_html(r) for r in rows)
        new_grid = (
            '<div class="grid grid--3 grid--gap-sm" style="margin-top: var(--space-2xl);">\n'
            + tiles
            + '\n      </div>'
        )

        # Try old stack-lg first; if not present, replace existing tile grid.
        new_src, n = STACK_LG_RE.subn(new_grid, src, count=1)
        if n == 0:
            # Idempotent: replace existing tile grid block (preserving the </div></section> trailer).
            existing_grid = TILE_GRID_RE.search(src)
            if existing_grid:
                new_src = src[:existing_grid.start()] + new_grid + "\n    </div>\n  </section>" + src[existing_grid.end():]
            else:
                print(f"  skip (no grid found): {country}")
                continue

        # widen container for the courses section (only meaningful on first pass)
        new_src = NARROW_TO_WIDE_RE.sub('<div class="container">', new_src, count=1)

        page_path.write_text(new_src, encoding="utf-8")
        print(f"  rewrote {country}: {len(rows)} tiles, {sum(1 for r in rows if r['status']=='matched')} with detail pages")


if __name__ == "__main__":
    main()
