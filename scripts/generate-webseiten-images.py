#!/usr/bin/env python3
"""
Bildgenerierung fuer die Webseiten-Seite (hinzke-digital).
Generiert Problem- und Solution-Bilder via Gemini 3 Pro.

Verwendung:
  python scripts/generate-webseiten-images.py           # Generieren
  python scripts/generate-webseiten-images.py --dry-run  # Nur Prompts anzeigen
  python scripts/generate-webseiten-images.py --force     # Bestehende ueberschreiben
"""

import argparse
import importlib.util
import sys
import time
from pathlib import Path

# generate_image und Konstanten aus dem Modul-Script importieren (Dateiname hat Bindestriche)
_spec = importlib.util.spec_from_file_location(
    "generate_module_images",
    Path(__file__).parent / "generate-module-images.py",
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)

generate_image = _mod.generate_image
get_api_key = _mod.get_api_key
STYLE_PREFIX = _mod.STYLE_PREFIX
DELAY_BETWEEN_CALLS = _mod.DELAY_BETWEEN_CALLS

PROJECT_ROOT = Path(__file__).parent.parent
OUTPUT_DIR = PROJECT_ROOT / "public" / "images"

IMAGES = [
    {
        "filename": "webseiten-problem.png",
        "prompt": (
            "Outdated ugly business website from 2010 displayed in browser, slow loading spinner, "
            "not mobile responsive, broken layout on phone screen preview, PageSpeed score showing "
            "red 23/100, poor design with cluttered navigation"
        ),
    },
    {
        "filename": "webseiten-solution.png",
        "prompt": (
            "Modern clean business website in browser window, fast loading with green PageSpeed "
            "score 98/100, responsive design previews on desktop tablet and phone, minimal "
            "professional layout, clean navigation"
        ),
    },
]


def main():
    parser = argparse.ArgumentParser(
        description="Generiert Problem- und Solution-Bilder fuer die Webseiten-Seite via Gemini 3 Pro.",
    )
    parser.add_argument("--force", action="store_true", help="Bestehende Bilder ueberschreiben")
    parser.add_argument("--dry-run", action="store_true", help="Nur Prompts anzeigen")
    args = parser.parse_args()

    api_key = ""
    if not args.dry_run:
        api_key = get_api_key()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    generated = 0
    skipped = 0
    failed = 0

    for img in IMAGES:
        output_path = OUTPUT_DIR / img["filename"]
        print(f"\n  [{img['filename']}]")

        if args.dry_run:
            print(f"  Prompt: {STYLE_PREFIX}{img['prompt']}")
            skipped += 1
            continue

        if output_path.exists() and not args.force:
            print(f"  SKIP: Datei existiert bereits ({output_path})")
            skipped += 1
            continue

        print(f"  Generiere...")
        success = generate_image(img["prompt"], output_path, api_key)

        if success:
            size_kb = output_path.stat().st_size / 1024
            print(f"  OK: {output_path} ({size_kb:.0f} KB)")
            generated += 1
        else:
            failed += 1

        time.sleep(DELAY_BETWEEN_CALLS)

    print(f"\n  FERTIG -- Generiert: {generated}, Uebersprungen: {skipped}, Fehlgeschlagen: {failed}")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
