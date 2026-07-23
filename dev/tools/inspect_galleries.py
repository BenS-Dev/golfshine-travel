#!/usr/bin/env python3
"""Dump every legacy page's image-hash list so we can find unique images per course."""
import re, pathlib, json, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITEPRO = ROOT / "sitepro"
IMG = re.compile(r'"image":"gallery_gen\\\/([a-f0-9]+)_gallery\.(jpg|png)"')

targets = sys.argv[1:] if len(sys.argv) > 1 else None

for php in sorted(SITEPRO.glob("*.php"), key=lambda p: int(p.stem) if p.stem.isdigit() else 9999):
    n = php.stem
    if targets and n not in targets:
        continue
    src = php.read_text(encoding="utf-8", errors="ignore")
    hashes = [m.group(1) for m in IMG.finditer(src)]
    if not hashes:
        continue
    title = re.search(r"<title>([^<]+)</title>", src)
    print(f"{n}.php ({title.group(1) if title else '?'}): {len(hashes)} images")
    for i, h in enumerate(hashes, 1):
        print(f"    {i}: {h}")
