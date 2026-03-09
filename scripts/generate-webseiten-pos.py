#!/usr/bin/env python3
"""
POS-Visuals fuer Webseiten-Pakete (Web Start, Web Business, Web Pro).
3 Pakete x 2 Formate = 6 Bilder. Generiert via Gemini, Post-Processing
mit Resize + QR-Overlay, dann Kopie nach shopware2pos.

Verwendung:
  python scripts/generate-webseiten-pos.py                    # Alle 6 Bilder
  python scripts/generate-webseiten-pos.py --paket start      # Nur Web Start
  python scripts/generate-webseiten-pos.py --landscape-only   # Nur Querformat
  python scripts/generate-webseiten-pos.py --portrait-only    # Nur Hochformat
  python scripts/generate-webseiten-pos.py --dry-run          # Nur Prompts anzeigen
  python scripts/generate-webseiten-pos.py --force            # Bestehende ueberschreiben
  python scripts/generate-webseiten-pos.py --no-copy          # Nicht nach shopware2pos kopieren
"""

import argparse
import shutil
import sys
import time
from pathlib import Path

# Post-Processing und API-Funktionen aus dem bestehenden POS-Script importieren
import importlib.util

SCRIPT_DIR = Path(__file__).parent
_spec = importlib.util.spec_from_file_location(
    "generate_pos_visuals", SCRIPT_DIR / "generate-pos-visuals.py"
)
_pos = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_pos)

LANDSCAPE_SIZE = _pos.LANDSCAPE_SIZE
PORTRAIT_SIZE = _pos.PORTRAIT_SIZE
QR_SIZE_LANDSCAPE = _pos.QR_SIZE_LANDSCAPE
QR_SIZE_PORTRAIT = _pos.QR_SIZE_PORTRAIT
create_qr_image = _pos.create_qr_image
generate_image_bytes = _pos.generate_image_bytes
get_api_key = _pos.get_api_key
postprocess_image = _pos.postprocess_image

try:
    import qrcode  # noqa: F401
except ImportError:
    qrcode = None

# --- Konfiguration ---

PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = PROJECT_ROOT / "public" / "images" / "pos"

# Ziel-Verzeichnisse in shopware2pos
POS_APP_ROOT = Path.home() / "Documents" / "git" / "shopware2pos" / "public" / "static"
POS_LANDSCAPE_DIR = POS_APP_ROOT / "pos-quer"
POS_PORTRAIT_DIR = POS_APP_ROOT / "pos-hoch"

# Pause zwischen API-Calls (Sekunden)
DELAY_BETWEEN_CALLS = 5

# Basis-Stil (angelehnt an bestehende POS-Visuals)
STYLE_PREFIX = (
    "Clean digital signage graphic for professional business display. "
    "European business style, understated and sophisticated. "
    "Ultra-sharp, high-resolution rendering. No people, no photographs. "
    "Brand color: electric blue #137EDE. "
    "Light, bright, airy feel -- white or light gradient background. "
    "Do NOT render physical screen frames or bezels. "
    "Do NOT render 'hinzke.digital' as a styled logo or wordmark -- only as clean plain sans-serif text. "
)

# --- Paket-Prompts ---

# Web Start (1.690 EUR)
_START_COMMON = (
    "A single floating browser window showing a clean, simple website with minimal navigation. "
    "Large headline text: 'Web Start' in dark sans-serif. "
    "Prominent price: '1.690 EUR' in bold, electric blue #137EDE -- must be readable from 3 meters. "
    "Small subline: 'Responsive Design | Basis-SEO'. "
    "Bottom corner: 'hinzke.digital' as clean dark sans-serif text + 'Webseiten fuer den Mittelstand' smaller below. "
    "Overall: minimal, entry-level feel. Lots of white space. "
)

START_LANDSCAPE = STYLE_PREFIX + _START_COMMON + (
    "Landscape orientation, browser window centered with slight perspective tilt. "
    "Subtle geometric accents (dots, thin lines) in blue #137EDE. "
)

START_PORTRAIT = STYLE_PREFIX + _START_COMMON + (
    "Portrait/vertical orientation, browser window in upper half. "
    "Subtitle and branding in lower third. Clean vertical layout. "
    "Subtle geometric accents (dots, thin lines) in blue #137EDE. "
)

# Web Business (2.890 EUR) -- Meistgewaehlt
_BUSINESS_COMMON = (
    "A website preview browser window plus a small floating SEO dashboard widget showing keyword rankings and a bar chart. "
    "Large headline text: 'Web Business' in dark sans-serif. "
    "Prominent price: '2.890 EUR' in bold, electric blue #137EDE -- must be readable from 3 meters. "
    "A small badge or ribbon: 'Beliebteste Wahl' in blue #137EDE. "
    "Small subline: 'Corporate Design | SEO + KI'. "
    "Bottom area: 'hinzke.digital' as clean dark sans-serif text + 'Webseiten fuer den Mittelstand' smaller below. "
    "Slight blue glow accent around the main card. "
)

BUSINESS_LANDSCAPE = STYLE_PREFIX + _BUSINESS_COMMON + (
    "Landscape orientation, main browser window left-center, SEO widget floating right. "
    "Subtle geometric accents. Premium but not over-the-top. "
)

BUSINESS_PORTRAIT = STYLE_PREFIX + _BUSINESS_COMMON + (
    "Portrait/vertical orientation, browser window in upper portion, SEO widget below it. "
    "Badge positioned near the headline. Clean vertical layout. "
    "Subtle geometric accents. "
)

# Web Pro (ab 3.990 EUR) -- Premium
_PRO_COMMON = (
    "Multiple floating elements: a website preview, an analytics chart widget, and a small AI badge with sparkle icon. "
    "Large headline text: 'Web Pro' in dark sans-serif. "
    "Prominent price: 'ab 3.990 EUR' in bold, electric blue #137EDE -- must be readable from 3 meters. "
    "Small subline: 'Individuelles Design | Full SEO + AIO'. "
    "Bottom area: 'hinzke.digital' as clean dark sans-serif text + 'Webseiten fuer den Mittelstand' smaller below. "
    "Premium white space, sophisticated layout. Most premium tier. "
)

PRO_LANDSCAPE = STYLE_PREFIX + _PRO_COMMON + (
    "Landscape orientation, three floating elements arranged with depth and shadows. "
    "Website preview largest in center, analytics left, AI badge right. "
    "Subtle geometric accents, premium spacing. "
)

PRO_PORTRAIT = STYLE_PREFIX + _PRO_COMMON + (
    "Portrait/vertical orientation, floating elements stacked vertically with overlap. "
    "Website preview at top, analytics middle, AI badge lower. "
    "Clean vertical layout, premium spacing. "
)

# Paket-Definitionen
PAKETE = {
    "start": {
        "name": "Web Start",
        "landscape_prompt": START_LANDSCAPE,
        "portrait_prompt": START_PORTRAIT,
    },
    "business": {
        "name": "Web Business",
        "landscape_prompt": BUSINESS_LANDSCAPE,
        "portrait_prompt": BUSINESS_PORTRAIT,
    },
    "pro": {
        "name": "Web Pro",
        "landscape_prompt": PRO_LANDSCAPE,
        "portrait_prompt": PRO_PORTRAIT,
    },
}


def process_variant(paket_key: str, orientation: str, prompt: str,
                    aspect_ratio: str, target_size: tuple,
                    qr_size: int, qr_position: str,
                    api_key: str, force: bool, dry_run: bool,
                    qr_cache: dict | None = None) -> str:
    """Generiert und verarbeitet eine Variante. Gibt 'generated', 'skipped' oder 'failed' zurueck."""
    filename = f"webseiten-pos-{orientation}-{paket_key}.png"
    final_path = OUTPUT_DIR / filename

    print(f"\n  [{PAKETE[paket_key]['name']} {orientation.upper()} {aspect_ratio}]")

    if dry_run:
        print(f"  Prompt:\n  {prompt[:200]}...")
        return "skipped"

    if final_path.exists() and not force:
        print(f"  SKIP: {final_path} existiert bereits")
        return "skipped"

    # Bild generieren
    print("  Generiere via Gemini...")
    raw_bytes = generate_image_bytes(prompt, aspect_ratio, api_key)

    if raw_bytes is None:
        return "failed"

    raw_size_kb = len(raw_bytes) / 1024
    print(f"  Gemini-Response: {raw_size_kb:.0f} KB")

    # Post-Processing: Resize + QR
    print(f"  Post-Processing: Resize auf {target_size[0]}x{target_size[1]} + QR-Overlay...")
    success = postprocess_image(raw_bytes, final_path, target_size, qr_size, qr_position, qr_cache)

    if not success:
        return "failed"

    final_size_kb = final_path.stat().st_size / 1024
    print(f"  OK: {final_path} ({final_size_kb:.0f} KB, {target_size[0]}x{target_size[1]})")
    return "generated"


def copy_to_pos_app(dry_run: bool, no_copy: bool) -> int:
    """Kopiert generierte Bilder nach shopware2pos. Gibt Anzahl kopierter Dateien zurueck."""
    if dry_run or no_copy:
        return 0

    if not POS_APP_ROOT.exists():
        print(f"\n  WARNUNG: shopware2pos nicht gefunden ({POS_APP_ROOT})")
        return 0

    copied = 0
    for f in sorted(OUTPUT_DIR.glob("webseiten-pos-*.png")):
        if "landscape" in f.name:
            dest = POS_LANDSCAPE_DIR / f.name
        elif "portrait" in f.name:
            dest = POS_PORTRAIT_DIR / f.name
        else:
            continue

        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, dest)
        print(f"  Kopiert: {f.name} -> {dest}")
        copied += 1

    return copied


def main():
    parser = argparse.ArgumentParser(
        description="Generiert POS-Visuals fuer Webseiten-Pakete (Start/Business/Pro).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("--force", action="store_true", help="Bestehende Bilder ueberschreiben")
    parser.add_argument("--dry-run", action="store_true", help="Nur Prompts anzeigen")
    parser.add_argument("--landscape-only", action="store_true", help="Nur Querformat")
    parser.add_argument("--portrait-only", action="store_true", help="Nur Hochformat")
    parser.add_argument("--no-copy", action="store_true", help="Nicht nach shopware2pos kopieren")
    parser.add_argument(
        "--paket",
        choices=["start", "business", "pro"],
        help="Nur ein bestimmtes Paket generieren",
    )

    args = parser.parse_args()

    if args.landscape_only and args.portrait_only:
        print("ERROR: --landscape-only und --portrait-only schliessen sich gegenseitig aus.")
        sys.exit(1)

    # API-Key pruefen
    api_key = ""
    if not args.dry_run:
        api_key = get_api_key()

    # Pakete bestimmen
    paket_keys = [args.paket] if args.paket else ["start", "business", "pro"]

    # Varianten aufbauen
    variants = []
    for key in paket_keys:
        paket = PAKETE[key]
        if not args.portrait_only:
            variants.append({
                "paket_key": key,
                "orientation": "landscape",
                "prompt": paket["landscape_prompt"],
                "aspect_ratio": "16:9",
                "target_size": LANDSCAPE_SIZE,
                "qr_size": QR_SIZE_LANDSCAPE,
                "qr_position": "bottom-right",
            })
        if not args.landscape_only:
            variants.append({
                "paket_key": key,
                "orientation": "portrait",
                "prompt": paket["portrait_prompt"],
                "aspect_ratio": "9:16",
                "target_size": PORTRAIT_SIZE,
                "qr_size": QR_SIZE_PORTRAIT,
                "qr_position": "bottom-right",
            })

    # Header
    mode = "DRY-RUN" if args.dry_run else "GENERIERUNG"
    paket_info = PAKETE[args.paket]["name"] if args.paket else "Alle 3 Pakete"
    print(f"\n{'#' * 60}")
    print(f"  Webseiten-POS-Generierung -- {mode}")
    print(f"  Pakete: {paket_info}")
    print(f"  Bilder: {len(variants)}")
    print(f"  Output: {OUTPUT_DIR}")
    if args.force:
        print("  Force: Bestehende Bilder werden ueberschrieben")
    if args.no_copy:
        print("  Copy: Deaktiviert")
    print(f"{'#' * 60}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # QR-Cache vorab erstellen
    qr_cache = {}
    if not args.dry_run and qrcode is not None:
        print("\n  QR-Code vorab generieren...")
        for size in {QR_SIZE_LANDSCAPE, QR_SIZE_PORTRAIT}:
            qr_cache[size] = create_qr_image(size)
        print(f"  QR-Cache: {len(qr_cache)} Groessen")

    # Varianten verarbeiten
    stats = {"generated": 0, "skipped": 0, "failed": 0}

    for i, variant in enumerate(variants):
        result = process_variant(
            paket_key=variant["paket_key"],
            orientation=variant["orientation"],
            prompt=variant["prompt"],
            aspect_ratio=variant["aspect_ratio"],
            target_size=variant["target_size"],
            qr_size=variant["qr_size"],
            qr_position=variant["qr_position"],
            api_key=api_key,
            force=args.force,
            dry_run=args.dry_run,
            qr_cache=qr_cache,
        )
        stats[result] += 1

        # Rate-Limiting
        if not args.dry_run and result == "generated" and i < len(variants) - 1:
            print(f"\n  Warte {DELAY_BETWEEN_CALLS}s (Rate-Limiting)...")
            time.sleep(DELAY_BETWEEN_CALLS)

    # Nach shopware2pos kopieren
    if stats["generated"] > 0 or (not args.dry_run and not args.no_copy):
        print(f"\n{'=' * 60}")
        print("Kopiere nach shopware2pos...")
        print(f"{'=' * 60}")
        copied = copy_to_pos_app(args.dry_run, args.no_copy)
        if copied:
            print(f"  {copied} Dateien kopiert")

    # Zusammenfassung
    print(f"\n{'#' * 60}")
    print("  FERTIG")
    print(f"  Generiert: {stats['generated']}")
    print(f"  Uebersprungen: {stats['skipped']}")
    print(f"  Fehlgeschlagen: {stats['failed']}")
    print(f"{'#' * 60}")

    # Dateien auflisten
    print(f"\n  Webseiten-POS-Dateien in {OUTPUT_DIR}:")
    if OUTPUT_DIR.exists():
        for f in sorted(OUTPUT_DIR.glob("webseiten-pos-*.png")):
            size_kb = f.stat().st_size / 1024
            print(f"    {f.name} ({size_kb:.0f} KB)")
    print()

    if stats["failed"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
