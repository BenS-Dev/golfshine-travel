#!/usr/bin/env python3
"""Build COURSE_MAP.csv from current state of redesign/golf/{country}.html.

Parses EITHER the original stack-lg `<article>` Course/Hotel blocks OR the rewritten
tile grid (so the script is idempotent across re-runs). Hotel info is carried forward
from the previous CSV when available (since tile HTML doesn't include it).

Strict seed-only legacy mapping. Courses not in SEED → status=no-detail.
"""
import csv
import html
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REDESIGN = ROOT / "redesign"
SITEPRO = ROOT / "sitepro"
OUT_CSV = REDESIGN / "docs" / "COURSE_MAP.csv"

COUNTRY_PAGES = [
    "scotland", "ireland", "wales", "spain", "portugal", "france", "italy",
    "netherlands", "germany", "switzerland", "greece", "sweden", "denmark", "norway",
]

COUNTRY_NAME = {
    "scotland": "Scotland", "ireland": "Ireland", "wales": "Wales", "spain": "Spain",
    "portugal": "Portugal", "france": "France", "italy": "Italy",
    "netherlands": "Netherlands", "germany": "Germany", "switzerland": "Switzerland",
    "greece": "Greece", "sweden": "Sweden", "denmark": "Denmark", "norway": "Norway",
}

# Old format: stack-lg article blocks.
ARTICLE_RE = re.compile(
    r"<article>\s*<h2>(?P<region>[^<]+)</h2>\s*"
    r"<ul class=\"stack\">\s*"
    r"<li><strong>Course:</strong>\s*(?P<course>[^<]+)</li>\s*"
    r"<li><strong>Hotel:</strong>\s*(?P<hotel>[^<]+)</li>\s*"
    r"</ul>\s*</article>",
    re.IGNORECASE,
)

# New format: tile grid <a class="tile">…<span class="tile__region">REGION · COUNTRY</span><h3 class="tile__name">COURSE</h3>
TILE_RE = re.compile(
    r'<a class="tile" href="[^"]*">\s*'
    r'<img[^>]*>\s*'
    r'<div class="tile__body">\s*'
    r'<span class="tile__region">(?P<region>[^<]+?) · [^<]+</span>\s*'
    r'<h3 class="tile__name">(?P<course>[^<]+)</h3>\s*'
    r'</div>\s*</a>',
    re.IGNORECASE,
)

# Image-only mapping: legacy pages with usable gallery imagery but minimal prose.
# Used for hero image only; tile still links to contact form (no detail page).
IMAGE_ONLY_SEED = {
    # Scotland
    "Fairmont St. Andrews": "90",
    # Spain
    "Sitges Terramar Golf Club": "108",
    "Llavaneras Golf Club": "109",
    "Campo de Golf El Saler": "110",
    # Portugal
    "Oitavos Dunes Golf Course": "113",
    "Praia D'El Rey Golf & Beach Resort": "114",
    # France
    "Evian Golf Club": "152",
    # Italy
    "Pevero Golf Club": "121",
    "Gardagolf Country Club": "118",
    "Circolo Golf Villa d'Este": "119",
    "Circolo del Golf di Roma": "122",
    "Argentario Golf & Wellness Resort": "117",
    # Netherlands
    "The International": "163",
    "Koninklijke Haagsche Golf & Country Club": "164",
    "Golf & Country Club Lauswolt": "165",
    # Germany
    "Golf and Country Club Berlin-Wannsee e.V.": "169",
    "Golfclub München Eichenried": "168",
    # Sweden
    "Halmstad Golfklubb and Hotel Resort": "157",
    # Wales
    "Royal Porthcawl Golf Club": "156",
}

# Hand-curated mapping — only courses with real legacy prose.
SEED = {
    # Scotland
    "St. Andrews Links — Old Course": "91",
    "Fairmont St. Andrews": None,
    "Cabot Highlands": "92",
    "Royal Dornoch Championship Course": "94",
    "Royal Aberdeen Golf Club": "100",
    "Trump International": "98",
    "The Bruntsfield Links": "93",
    "Gullane Golf Club": "95",
    # Ireland
    "Killarney G.C. Killen": "86",
    "Ballyliffin Golf Club": "85",
    "Royal Portrush Golf Club — Dunluce Links": "77",
    "Tralee Golf Club": "87",
    "Portmarnock Golf Club (Old)": "88",
    "Carton House Golf Club": "89",
    # Wales
    "Golf at the Vale Resort": "155",
    "Celtic Manor Golf Club": "154",
    "Royal Porthcawl Golf Club": None,
    # Spain
    "Los Naranjos Golf Club": "106",
    "Los Monteros Golf": "105",
    "Real Club La Herrería": "104",
    "Rio Real Golf & Hotel": "107",
    "Sitges Terramar Golf Club": None,
    "Llavaneras Golf Club": None,
    "Campo de Golf El Saler": None,
    # Portugal
    "Vale do Lobo Golf Club": "111",
    "Troia Golf": "112",
    "Oitavos Dunes Golf Course": None,
    "Praia D'El Rey Golf & Beach Resort": None,
    "Palmares Ocean Living & Golf": "115",
    "Oporto Golf Club": "116",
    # France
    "Le Golf Terre Blanches": "153",
    "Evian Golf Club": None,
    "Golf du Medoc": "144",
    # Italy
    "Pevero Golf Club": None,
    "Gardagolf Country Club": None,
    "Circolo Golf Villa d'Este": None,
    "Circolo del Golf di Roma": None,
    "Royal Park Roveri": "123",
    "Argentario Golf & Wellness Resort": None,
    # Netherlands
    "The International": None,
    "Koninklijke Haagsche Golf & Country Club": None,
    "Golf & Country Club Lauswolt": None,
    # Germany
    "Golf and Country Club Berlin-Wannsee e.V.": None,
    "Golfclub München Eichenried": None,
    "Das Achental Golf": "166",
    # Switzerland
    "Golf Club de Geneve": "173",
    "Golf Club Thunersee": "172",
    "Crans-sur-Sierre Golf Club": "171",
    # Greece
    "The Bay Course": "133",
    "The Dunes Course": "131",
    "Glyfada Golf Club of Athens": "136",
    "Corfu Golf Club": "145",
    # Sweden
    "Halmstad Golfklubb and Hotel Resort": None,
    "PGA of Sweden National": "160",
    "Bro Hof Slott Golf Club": "161",
    # Denmark
    "Lübker Golf Resort": "158",
    "Kokkedal Golf Club": "159",
    "Himmerland Golf & Spa Resort": "162",
    # Norway
    "Stavanger Golfklubb": "126",
    "Drøbak Golfklubb": "130",
    "Losby Golfklubb": "125",
    "Bergen Golfklubb": "128",
    "Trondheim Golfklubb": "127",
    "Vestfold Golf Club": "129",
}

# Minimum body paragraphs required to qualify as a detail page.
MIN_BODIES = 2

# Hotel-name corrections (display only; doesn't affect slugs).
HOTEL_CORRECTIONS = {
    "Malmoison Edinburgh": "Malmaison Edinburgh",
    "Malmoison Aberdeen": "Malmaison Aberdeen",
}

H1_RE = re.compile(r'<h1 class="wb-stl-heading1"[^>]*>(.*?)</h1>', re.S)
TITLE_RE = re.compile(r"<title>([^<]+)</title>", re.I)
IMG_JSON_RE = re.compile(r'"image":"gallery_gen\\\/([a-f0-9]+)_gallery\.(jpg|png)"')


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s)


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = text.lower()
    text = text.replace("&", " and ")
    text = re.sub(r"&[a-z]+;", " ", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def parse_country_page(country_slug: str):
    """Yield (region, course) dicts. Tries new tile grid first, then old stack-lg."""
    path = REDESIGN / "golf" / f"{country_slug}.html"
    if not path.exists():
        return
    src = path.read_text(encoding="utf-8")
    tiles = list(TILE_RE.finditer(src))
    if tiles:
        for m in tiles:
            region = html.unescape(m.group("region")).strip()
            course = html.unescape(m.group("course")).strip()
            yield {
                "country_slug": country_slug,
                "country_name": COUNTRY_NAME[country_slug],
                "region": region,
                "course": course,
                "course_slug": slugify(course),
            }
        return
    for m in ARTICLE_RE.finditer(src):
        region = html.unescape(m.group("region")).strip()
        course = html.unescape(m.group("course")).strip()
        hotel = html.unescape(m.group("hotel")).strip()
        yield {
            "country_slug": country_slug,
            "country_name": COUNTRY_NAME[country_slug],
            "region": region,
            "course": course,
            "hotel": hotel,
            "course_slug": slugify(course),
        }


def load_previous_hotels() -> dict:
    """Return {(country_slug, course_slug_normalised_to_slug_of_fixed_name): hotel}.
    We index by (country_slug, slug-of-current-course-name) when possible, else by
    (country_slug, region) as fallback.
    """
    out_by_slug: dict[tuple[str, str], str] = {}
    out_by_region: dict[tuple[str, str], str] = {}
    if not OUT_CSV.exists():
        return {"by_slug": out_by_slug, "by_region": out_by_region}
    with OUT_CSV.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            slug = row.get("course_slug", "")
            region = row.get("region", "")
            hotel = row.get("hotel", "")
            country = row.get("country_slug", "")
            if hotel:
                out_by_slug[(country, slug)] = hotel
                out_by_region[(country, region)] = hotel
    return {"by_slug": out_by_slug, "by_region": out_by_region}


def legacy_page_info(n: str) -> dict:
    php = SITEPRO / f"{n}.php"
    if not php.exists():
        return {"hero_hash": "", "hero_ext": "jpg", "bodies": [], "title": "", "all_hashes": ""}
    src = php.read_text(encoding="utf-8", errors="ignore")
    bodies = []
    for raw in H1_RE.findall(src):
        txt = html.unescape(strip_tags(raw)).strip()
        txt = re.sub(r"\s+", " ", txt)
        if len(txt) >= 30:
            bodies.append(txt)
    title_match = TITLE_RE.search(src)
    title = html.unescape(title_match.group(1)).strip() if title_match else ""
    matches = IMG_JSON_RE.findall(src)
    hero_hash = matches[0][0] if matches else ""
    hero_ext = matches[0][1] if matches else "jpg"
    all_hashes = "|".join(f"{h}:{ext}" for h, ext in matches)
    return {"hero_hash": hero_hash, "hero_ext": hero_ext, "bodies": bodies, "title": title, "all_hashes": all_hashes}


def main():
    prev = load_previous_hotels()

    rows = []
    seen = set()
    for country in COUNTRY_PAGES:
        for entry in parse_country_page(country):
            slug_key = (entry["country_slug"], entry["course_slug"])
            if slug_key in seen:
                continue
            seen.add(slug_key)

            hotel = entry.get("hotel") or prev["by_slug"].get(slug_key) or prev["by_region"].get((entry["country_slug"], entry["region"])) or ""
            hotel = HOTEL_CORRECTIONS.get(hotel, hotel)

            seed_php = SEED.get(entry["course"])
            all_hashes = ""
            php, hero, hero_ext, status, bodies = "", "", "", "no-detail", 0

            if seed_php is not None:
                info = legacy_page_info(seed_php)
                bodies = len(info["bodies"])
                if bodies >= MIN_BODIES:
                    php = seed_php
                    hero, hero_ext = info["hero_hash"], info["hero_ext"]
                    all_hashes = info["all_hashes"]
                    status = "matched"

            # Image-only: status stays no-detail, but we record imagery from a legacy page.
            if status == "no-detail":
                img_php = IMAGE_ONLY_SEED.get(entry["course"])
                if img_php:
                    info = legacy_page_info(img_php)
                    if info["hero_hash"]:
                        hero, hero_ext = info["hero_hash"], info["hero_ext"]
                        all_hashes = info["all_hashes"]
                        php = img_php  # used by extract script
                        status = "image-only"

            rows.append({
                "country_slug": entry["country_slug"],
                "country_name": entry["country_name"],
                "region": entry["region"],
                "course_name": entry["course"],
                "course_slug": entry["course_slug"],
                "hotel": hotel,
                "legacy_php": php,
                "legacy_bodies": bodies,
                "hero_hash": hero,
                "hero_ext": hero_ext,
                "all_hashes": all_hashes,
                "status": status,
            })

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    by_status: dict[str, list] = {}
    for r in rows:
        by_status.setdefault(r["status"], []).append(r)
    print(f"Total courses: {len(rows)}")
    for s, items in by_status.items():
        print(f"  {s}: {len(items)}")
    print(f"\nWrote {OUT_CSV}")


if __name__ == "__main__":
    main()
