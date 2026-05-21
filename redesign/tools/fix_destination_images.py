#!/usr/bin/env python3
"""Extract unique hero images for every tile in redesign/destinations.html.

Maps destination tile name → legacy sitepro PHP page → first unclaimed gallery image.
Saves images to redesign/assets/images/destinations/{slug}.jpg and rewrites the tile
<img src=…> references in destinations.html in place.
"""
import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REDESIGN = ROOT / "redesign"
SITEPRO = ROOT / "sitepro"
GALLERY = SITEPRO / "gallery_gen"
DEST_HTML = REDESIGN / "destinations.html"
DEST_IMG_DIR = REDESIGN / "assets" / "images" / "destinations"
COUNTRY_GOLF_DIR = REDESIGN / "assets" / "images" / "golf"

# tile_name_text  →  (slug, legacy_php)
# legacy_php is the sitepro/{N}.php whose gallery is most representative.
# None = leave unchanged (keep existing image — e.g., Argentina tiles already correct).
DEST_MAP: dict[str, tuple[str, str | None]] = {
    # Argentina — already use Argentina-specific images, skip
    "Buenos Aires": ("argentina-buenos-aires", None),
    "Bariloche": ("argentina-bariloche", None),
    "El Calafate": ("argentina-el-calafate", None),
    "Iguazú": ("argentina-iguazu", None),
    "Puerto Madryn": ("argentina-puerto-madryn", None),
    "Salta": ("argentina-salta", None),
    "Ushuaia": ("argentina-ushuaia", None),
    "Mendoza": ("argentina-mendoza", None),

    # Caribbean
    "Punta Cana": ("caribbean-punta-cana", "75"),
    "Cancun": ("caribbean-cancun", "83"),         # Rivera Maya / Mexico
    "Rivera Maya": ("caribbean-rivera-maya", "84"),
    "Puerto Rico": ("caribbean-puerto-rico", "74"),
    "Bahamas": ("caribbean-bahamas", "76"),
    "Los Cabos": ("caribbean-los-cabos", "82"),

    # USA
    "Daytona": ("usa-daytona", "52"),
    "Miami": ("usa-miami", "53"),
    "Miami — Trump": ("usa-miami-trump", "58"),
    "Naples": ("usa-naples", "54"),
    "Tampa": ("usa-tampa", "56"),
    "Orlando": ("usa-orlando", "57"),
    "Palm Beach": ("usa-palm-beach", "55"),
    "St Augustine": ("usa-st-augustine", "59"),
    "Ponte Vedra Beach": ("usa-ponte-vedra", "60"),
    "Palm Springs": ("usa-palm-springs", "68"),
    "Pebble Beach": ("usa-pebble-beach", "140"),
    "Rancho Santa Fe": ("usa-rancho-santa-fe", "66"),
    "Myrtle Beach": ("usa-myrtle-beach", "50"),
    "Kiawah Island": ("usa-kiawah-island", "49"),
    "Phoenix": ("usa-phoenix", "71"),
    "Tucson": ("usa-tucson", "72"),
    "Las Vegas": ("usa-las-vegas", "64"),
    "Mesquite": ("usa-mesquite", "65"),
    "Ocean City": ("usa-ocean-city", "73"),

    # UK & Ireland — pull from each country's leading course gallery
    "Scotland": ("scotland", "91"),        # St Andrews Old
    "England": ("england", "147"),         # The Belfry / Birmingham
    "Ireland": ("ireland", "85"),          # Ballyliffin
    "Wales": ("wales", "154"),             # Celtic Manor

    # Europe — pull leading-course gallery per country
    "Spain": ("spain", "106"),             # Los Naranjos / Marbella
    "Portugal": ("portugal", "111"),       # Vale do Lobo
    "France": ("france", "144"),           # Médoc / Bordeaux
    "Italy": ("italy", "121"),             # Pevero / Sardinia
    "Netherlands": ("netherlands", "163"), # Amsterdam / The International
    "Germany": ("germany", "166"),         # Das Achental / Grassau
    "Switzerland": ("switzerland", "171"), # Crans-sur-Sierre
    "Greece": ("greece", "131"),           # Costa Navarino Dunes

    # Scandinavia
    "Sweden": ("scandinavia-sweden", "160"),  # PGA of Sweden National / Malmö
    "Denmark": ("scandinavia-denmark", "158"),# Lübker / Nimtofte
    "Norway": ("scandinavia-norway", "125"),  # Losby / Oslo
}

IMG_JSON_RE = re.compile(r'"image":"gallery_gen\\\/([a-f0-9]+)_gallery\.(jpg|png)"')


def legacy_gallery(n: str) -> list[tuple[str, str]]:
    php = SITEPRO / f"{n}.php"
    if not php.exists():
        return []
    src = php.read_text(encoding="utf-8", errors="ignore")
    return IMG_JSON_RE.findall(src)


def main():
    DEST_IMG_DIR.mkdir(parents=True, exist_ok=True)

    claimed: set[str] = set()
    # Process in legacy_php numeric order so lower-numbered pages get their first
    # image; later pages walk past shared prefixes.
    rows = [(name, slug, php) for name, (slug, php) in DEST_MAP.items() if php is not None]
    rows.sort(key=lambda r: int(r[2]))

    name_to_dest_path: dict[str, str] = {}

    for name, slug, php in rows:
        hashes = legacy_gallery(php)
        chosen = None
        source = "unique"
        for h, ext in hashes:
            if h in claimed:
                continue
            src = GALLERY / f"{h}_gallery.{ext}"
            if not src.exists():
                continue
            chosen = (h, ext, src)
            break

        # Fully-shared gallery: reuse the first available image (visual duplicate).
        if not chosen and hashes:
            for h, ext in hashes:
                src = GALLERY / f"{h}_gallery.{ext}"
                if src.exists():
                    chosen = (h, ext, src)
                    source = "shared"
                    break

        if chosen:
            h, ext, src = chosen
            # Claim entire gallery so siblings walk past.
            for hh, _ in hashes:
                claimed.add(hh)
            dest_name = f"{slug}.{ext}"
            shutil.copyfile(src, DEST_IMG_DIR / dest_name)
            name_to_dest_path[name] = f"assets/images/destinations/{dest_name}"
            tag = "" if source == "unique" else " (shared gallery, visual duplicate)"
            print(f"  {name:32s} sitepro/{php}.php → {dest_name}{tag}")
        else:
            print(f"  {name:32s} sitepro/{php}.php — no usable gallery, skipping")

    # Rewrite destinations.html tile-by-tile. Splitting on `<a class="tile"` keeps each
    # rewrite scoped to a single tile so we never spill into a neighbour.
    src = DEST_HTML.read_text(encoding="utf-8")
    parts = re.split(r'(<a class="tile"[^>]*>.*?</a>)', src, flags=re.S)
    replaced = 0
    name_variants = {v: new_path for name, new_path in name_to_dest_path.items()
                                    for v in (name, html.escape(name))}
    name_re = re.compile(r'<h3 class="tile__name">([^<]+)</h3>')
    img_re = re.compile(r'<img src="[^"]+"')
    for i, chunk in enumerate(parts):
        if not chunk.startswith('<a class="tile"'):
            continue
        m = name_re.search(chunk)
        if not m:
            continue
        tile_name = m.group(1).strip()
        new_path = name_variants.get(tile_name)
        if not new_path:
            continue
        new_chunk, n = img_re.subn(f'<img src="{new_path}"', chunk, count=1)
        if n:
            parts[i] = new_chunk
            replaced += 1

    DEST_HTML.write_text("".join(parts), encoding="utf-8")
    print(f"\nReplaced {replaced} <img src> in destinations.html")


if __name__ == "__main__":
    main()
