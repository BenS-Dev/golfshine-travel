#!/usr/bin/env python3
"""Generate redesign/golf/{country}/{course}.html for each matched course in COURSE_MAP.csv.

Course prose is copied verbatim from sitepro/{N}.php's <h1 class="wb-stl-heading1"> blocks.
No paraphrasing. No invented content.
"""
import csv
import html as html_lib
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REDESIGN = ROOT / "redesign"
SITEPRO = ROOT / "sitepro"
CSV_PATH = REDESIGN / "docs" / "COURSE_MAP.csv"
GOLF_DIR = REDESIGN / "golf"

H1_RE = re.compile(r'<h1 class="wb-stl-heading1"[^>]*>(.*?)</h1>', re.S)


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s)


def legacy_bodies(n: str) -> list[str]:
    php = SITEPRO / f"{n}.php"
    src = php.read_text(encoding="utf-8", errors="ignore")
    out = []
    for raw in H1_RE.findall(src):
        text = html_lib.unescape(strip_tags(raw)).strip()
        text = re.sub(r"\s+", " ", text)
        if len(text) >= 30:
            out.append(text)
    return out


def esc(s: str) -> str:
    """Escape for HTML text content / attributes."""
    return html_lib.escape(s, quote=True)


def url_inquiry(course_name: str) -> str:
    """Build ?inquiry=... value. Spaces → +, &/special → URL encoded."""
    from urllib.parse import quote_plus
    return quote_plus(course_name)


PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{course} Golf | Wingolf Travel</title>
  <meta name="description" content="{meta_desc}" />
  <link rel="canonical" href="https://www.wingolftravel.com/golf/{country_slug}/{course_slug}.html" />
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{course} Golf | Wingolf Travel" />
  <meta property="og:description" content="{meta_desc}" />
  <meta property="og:url" content="https://www.wingolftravel.com/golf/{country_slug}/{course_slug}.html" />
  <meta property="og:image" content="https://www.wingolftravel.com/assets/images/golf/courses/{image_name}" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../css/base.css" /><link rel="stylesheet" href="../../css/layout.css" /><link rel="stylesheet" href="../../css/components.css" /><link rel="stylesheet" href="../../css/pages.css" /><link rel="stylesheet" href="../../css/responsive.css" />
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"TouristDestination","name":"{course}","description":"{meta_desc}","image":"https://www.wingolftravel.com/assets/images/golf/courses/{image_name}","url":"https://www.wingolftravel.com/golf/{country_slug}/{course_slug}.html","touristType":"Golf"}}</script>
</head>
<body>

<a class="sr-only" href="#main">Skip to content</a>

<header class="site-header" id="siteHeader">
  <div class="container site-header__inner">
    <a href="../../index.html" class="brand" aria-label="Wingolf Travel home">
      <img class="brand__mark" src="../../assets/images/logo/gulfshine-logo.png" alt="" />
      <span class="brand__text"><span class="brand__name">Gulfshine</span><span class="brand__tag">Travel · Wingolf</span></span>
    </a>
    <nav class="nav" aria-label="Primary">
      <ul class="nav__list" id="primaryNav">
        <li><a class="nav__link" href="../../index.html">Home</a></li>
        <li><a class="nav__link" href="../../visit-argentina.html">Argentina</a></li>
        <li><a class="nav__link" href="../../golf.html" aria-current="page">Golf</a></li>
        <li><a class="nav__link" href="../../destinations.html">Destinations</a></li>
        <li><a class="nav__link" href="../../journeys.html">Journeys</a></li>
      </ul>
      <a class="btn btn--ghost nav__cta" href="../../contact.html">Plan Your Trip</a>
      <button class="nav-toggle" type="button" aria-controls="primaryNav" aria-expanded="false" aria-label="Toggle navigation"><span class="nav-toggle__lines"></span></button>
    </nav>
  </div>
</header>

<main id="main">

  <section class="page-header">
    <div class="page-header__media"><img src="../../assets/images/golf/courses/{image_name}" alt="" loading="eager" decoding="async" /></div>
    <div class="container page-header__inner">
      <span class="crumbs"><span><a href="../../index.html">Home</a></span><span><a href="../../golf.html">Golf</a></span><span><a href="../{country_slug}.html">{country_name}</a></span><span>{course}</span></span>
      <h1>{course}</h1>
      <p class="page-header__lede">{region} · {country_name}</p>
    </div>
  </section>

  <section class="section section--cream">
    <div class="container container--narrow">
{body_html}
      <p style="margin-top: var(--space-xl); font-size: 0.85rem; color: var(--text-dark-muted);">Suggested hotel: {hotel}</p>
    </div>
  </section>

  <section class="cta-banner">
    <div class="cta-banner__media"><img src="../../assets/images/golf/courses/{image_name}" alt="" loading="lazy" decoding="async" /></div>
    <div class="cta-banner__inner">
      <span class="eyebrow eyebrow--light">Plan With Us</span>
      <h2>Design a {course} golf trip.</h2>
      <p>Send a short note and we'll come back with a draft itinerary.</p>
      <a class="btn btn--primary btn--lg" href="../../contact.html?inquiry={inquiry}">Plan This Trip</a>
    </div>
  </section>

</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand"><img src="../../assets/images/logo/gulfshine-logo.png" alt="" /><strong>Gulfshine Travel</strong></div>
        <p class="footer-blurb">A private travel design house — luxury journeys across Argentina, the Americas, Europe and the world's great golf coastlines.</p>
      </div>
      <div><h4>Explore</h4><ul><li><a href="../../visit-argentina.html">Visit Argentina</a></li><li><a href="../../golf.html">Golf Travel</a></li><li><a href="../../destinations.html">Destinations</a></li><li><a href="../../journeys.html">Featured Journeys</a></li></ul></div>
      <div><h4>Company</h4><ul><li><a href="../../contact.html">Contact</a></li><li><a href="../../contact.html">Plan a Trip</a></li></ul></div>
      <div><h4>Reach Us</h4><ul><li><a href="mailto:contact@gulfshineservices.us">contact@gulfshineservices.us</a></li><li><a href="tel:+15619853886">(561)985-3886</a></li></ul></div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Gulfshine Services Inc. All rights reserved.</span>
      <span class="footer-bottom__legal">Fla. Seller of Travel Ref. No. ST46553.</span>
    </div>
  </div>
</footer>

<script src="../../js/main.js" defer></script>
</body>
</html>
"""


def render_body(bodies: list[str]) -> str:
    if not bodies:
        return ""
    lines = []
    lines.append(f'      <p class="lead">{esc(bodies[0])}</p>')
    for p in bodies[1:]:
        lines.append(f'      <p>{esc(p)}</p>')
    return "\n".join(lines)


def main():
    count = 0
    courses_dir = REDESIGN / "assets" / "images" / "golf" / "courses"
    with CSV_PATH.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row["status"] != "matched":
                continue
            bodies = legacy_bodies(row["legacy_php"])
            if not bodies:
                print(f"  skip (no bodies): {row['country_slug']}/{row['course_slug']}")
                continue
            # Find whichever extension actually exists on disk (extract_hero_images may have
            # written the country-fallback image with a different extension than the legacy).
            stem = f"{row['country_slug']}-{row['course_slug']}"
            candidates = sorted(courses_dir.glob(f"{stem}.*"))
            if not candidates:
                print(f"  skip (no image): {row['country_slug']}/{row['course_slug']}")
                continue
            image_name = candidates[0].name

            meta = bodies[0][:155].rstrip()
            if len(bodies[0]) > 155:
                meta = meta.rsplit(" ", 1)[0] + "…"
            page = PAGE_TEMPLATE.format(
                course=esc(row["course_name"]),
                meta_desc=esc(meta),
                country_slug=row["country_slug"],
                country_name=row["country_name"],
                course_slug=row["course_slug"],
                region=esc(row["region"]),
                hotel=esc(row["hotel"]),
                image_name=image_name,
                inquiry=url_inquiry(row["course_name"]),
                body_html=render_body(bodies),
            )
            out_dir = GOLF_DIR / row["country_slug"]
            out_dir.mkdir(parents=True, exist_ok=True)
            out = out_dir / f"{row['course_slug']}.html"
            out.write_text(page, encoding="utf-8")
            count += 1

    print(f"Generated {count} detail pages.")


if __name__ == "__main__":
    main()
