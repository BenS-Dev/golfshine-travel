#!/usr/bin/env python3
"""Build COURSE_MAP.csv mapping redesign country-page courses to legacy sitepro detail files.

Strict seed-only mapping — no fuzzy fallbacks. Any course not listed in SEED becomes
status=no-detail (tile links to contact form). This prevents fabricated content per the
user's primary constraint.
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

ARTICLE_RE = re.compile(
    r"<article>\s*<h2>(?P<region>[^<]+)</h2>\s*"
    r"<ul class=\"stack\">\s*"
    r"<li><strong>Course:</strong>\s*(?P<course>[^<]+)</li>\s*"
    r"<li><strong>Hotel:</strong>\s*(?P<hotel>[^<]+)</li>\s*"
    r"</ul>\s*</article>",
    re.IGNORECASE,
)

# Hand-curated mapping from current-redesign course names → legacy sitepro file number.
# Only courses with real prose in the legacy file appear here. Built by reading every
# wb-stl-heading1 first-paragraph snippet in sitepro/ and matching to redesign content.
SEED = {
    # Scotland
    "St. Andrews Links — Old Course": "91",
    "Fairmont St. Andrews": None,
    "Cabot Highlands": "92",
    "Royal Dornich Championship Course": "94",  # Royal Dornoch
    "Royal Aberdeen Golf Club": "100",
    "Trump International": "98",
    "The Bruntsflield Links": "93",
    "Gullane Golf Club": "95",
    # Ireland
    "Killarney G.C. Killen": "86",
    "Ballyliffin Golf Club": "85",
    "Royal Portrush Golf Club — Dunlance Links": "77",
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
    "Real Club La Herreria": "104",
    "Rio Real Golf & Hotel": "107",
    "Sitges Terramar Golf Club": None,
    "Llavaneras Golf Club": None,
    "Campo de Golf El Saler": None,
    # Portugal
    "Vale do Lobo Golf Club": "111",
    "Troia Golf": "112",
    "Oitavos Dunes Golf Course": None,  # 113 is empty
    "Praia D'El Rey Golf & Beach Resort": None,  # 114 reuses Troia text (junk)
    "Palmares Ocean Living & Golf": "115",
    "Oporto Golf Club": "116",
    # France
    "Le Golf Terre Blanches": "153",
    "Evian Golf Club": None,  # 152 is empty
    "Golf du Medoc": "144",
    # Italy
    "Pevero Golf Club": None,
    "Garrdagolf Country Club": None,
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
    "Glufada Golf Club of Athens": "136",  # 136 is actually Porto Carras (legacy title says ATHENS but content is Porto Carras)
    "Corfu Golf Club": "145",
    # Sweden
    "Halmstad Golfklubb and Hotel Resort": None,  # 157 empty
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

# ---------- Legacy scan ----------

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
    path = REDESIGN / "golf" / f"{country_slug}.html"
    if not path.exists():
        return
    src = path.read_text(encoding="utf-8")
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


def legacy_page_info(n: str) -> dict:
    """Read sitepro/{n}.php and return {hero_hash, bodies, title}. bodies are stripped text."""
    php = SITEPRO / f"{n}.php"
    if not php.exists():
        return {"hero_hash": "", "bodies": [], "title": ""}
    src = php.read_text(encoding="utf-8", errors="ignore")
    bodies = []
    for raw in H1_RE.findall(src):
        txt = html.unescape(strip_tags(raw)).strip()
        if len(txt) >= 30:
            bodies.append(txt)
    title_match = TITLE_RE.search(src)
    title = html.unescape(title_match.group(1)).strip() if title_match else ""
    hash_match = IMG_JSON_RE.search(src)
    hero_hash = hash_match.group(1) if hash_match else ""
    hero_ext = hash_match.group(2) if hash_match else "jpg"
    return {"hero_hash": hero_hash, "hero_ext": hero_ext, "bodies": bodies, "title": title}


def main():
    rows = []
    seen_slugs = set()
    for country in COUNTRY_PAGES:
        for entry in parse_country_page(country):
            seed_php = SEED.get(entry["course"])
            if seed_php is None:
                php, hero, hero_ext, status, bodies = "", "", "", "no-detail", 0
            else:
                info = legacy_page_info(seed_php)
                bodies = len(info["bodies"])
                if bodies < 3:
                    php, hero, hero_ext, status = "", "", "", "no-detail"
                else:
                    php, hero, hero_ext, status = seed_php, info["hero_hash"], info["hero_ext"], "matched"

            # dedupe duplicate (region, course) rows — e.g. Greece has The Dunes Course twice
            slug_key = (entry["country_slug"], entry["course_slug"])
            if slug_key in seen_slugs:
                continue
            seen_slugs.add(slug_key)

            rows.append({
                "country_slug": entry["country_slug"],
                "country_name": entry["country_name"],
                "region": entry["region"],
                "course_name": entry["course"],
                "course_slug": entry["course_slug"],
                "hotel": entry["hotel"],
                "legacy_php": php,
                "legacy_bodies": bodies,
                "hero_hash": hero,
                "hero_ext": hero_ext,
                "status": status,
            })

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    by_status = {}
    for r in rows:
        by_status.setdefault(r["status"], []).append(r)
    print(f"Total courses: {len(rows)}")
    for s, items in by_status.items():
        print(f"  {s}: {len(items)}")
    print(f"\nWrote {OUT_CSV}")

    print("\nmatched details:")
    for r in rows:
        if r["status"] == "matched":
            print(f"  {r['country_slug']:12s}  {r['course_name']:50s}  → sitepro/{r['legacy_php']}.php  (hero={r['hero_hash'][:8]})")


if __name__ == "__main__":
    main()
