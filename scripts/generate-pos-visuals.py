#!/usr/bin/env python3
"""
POS-Visuals fuer Hinzke Digital -- 3 Motive x 2 Formate = 6 Bilder.
Generiert Bilder via Gemini 3 Pro, skaliert auf exakte Pixelgroessen
und compositet einen echten QR-Code mit abgerundeten Ecken ins Bild.

Verwendung:
  python scripts/generate-pos-visuals.py                    # Alle 6 Bilder
  python scripts/generate-pos-visuals.py --motif 2          # Nur Motiv 2
  python scripts/generate-pos-visuals.py --landscape-only   # Nur Querformat
  python scripts/generate-pos-visuals.py --portrait-only    # Nur Hochformat
  python scripts/generate-pos-visuals.py --dry-run          # Nur Prompts anzeigen
  python scripts/generate-pos-visuals.py --force            # Bestehende ueberschreiben
  python scripts/generate-pos-visuals.py --qr-only          # Nur QR-Code
"""

import argparse
import base64
import io
import json
import os
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("ERROR: requests nicht installiert. Fuehre aus: pip install requests")
    sys.exit(1)

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("ERROR: Pillow nicht installiert. Fuehre aus: pip install Pillow")
    sys.exit(1)

try:
    import qrcode
    from qrcode.image.styledpil import StyledPilImage
    from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
except ImportError:
    qrcode = None

# --- Konfiguration ---

MODEL_ID = "gemini-3-pro-image-preview"
API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = PROJECT_ROOT / "public" / "images" / "pos"

# Pause zwischen API-Calls (Sekunden) -- Rate-Limiting
DELAY_BETWEEN_CALLS = 2

# QR-Code Ziel-URL
QR_URL = "https://hinzke.digital"

# Exakte Pixelgroessen
LANDSCAPE_SIZE = (1920, 1080)
PORTRAIT_SIZE = (1080, 1920)

# QR-Code-Groessen und Positionen
QR_SIZE_LANDSCAPE = 150
QR_SIZE_PORTRAIT = 200
QR_PADDING = 30  # Abstand vom Rand
QR_BG_CORNER_RADIUS = 14  # Abgerundete Ecken fuer QR-Hintergrund

# Basis-Stil fuer alle Visuals
STYLE_PREFIX = (
    "Clean digital graphic for a professional presentation. "
    "European business style, understated and sophisticated -- not American flashy advertising. "
    "Ultra-sharp, high-resolution rendering. No people, no photographs of real humans. "
    "Brand color: electric blue #137EDE. "
    "Do NOT render a physical screen, monitor frame, display device, or bezel around the image. "
    "Do NOT render 'hinzke.digital' or 'Hinzke Digital' as a styled logo, wordmark, or badge -- "
    "only as clean plain sans-serif text if mentioned. "
    "Light, bright, airy feel -- white or very light gradient background only. "
)

# --- Motiv-Prompts ---
# Gemeinsame Elemente fuer alle Motive
_COMMON_LANDSCAPE = (
    "Small decorative geometric elements (dots, thin lines) in blue (#137EDE), very subtle. "
    "Bottom left area: 'hinzke.digital' as clean, plain dark sans-serif text (not a logo, just text). "
    "Below that or nearby: 'Ihre Prozesse. Automatisiert.' as a smaller tagline in gray. "
    "Overall: clean, professional, European tech aesthetic. Muted tones, no loud colors except the brand blue."
)

_COMMON_PORTRAIT = (
    "Small decorative geometric elements (dots, thin lines) in blue (#137EDE), very subtle. "
    "Upper area: 'hinzke.digital' as clean, plain dark sans-serif text (not a logo, just text). "
    "Place 'Ihre Prozesse. Automatisiert.' as a tagline in dark sans-serif at roughly 75% from the top. "
    "The background gradient must continue smoothly all the way to the very bottom -- no dividers, no edges, no panels, no footer blocks. "
    "Do not place ANY text, icons, or decorative elements below the tagline. Just the same continuous background. "
    "Overall: clean, professional, European tech aesthetic. Muted tones, no loud colors except the brand blue."
)

# Motiv 1: Dashboard-Trio
MOTIF_1_LANDSCAPE = (
    "Light gradient background white to cool blue. "
    "Three floating browser windows with depth and shadows: "
    "Left: analytics dashboard, bar chart, green KPI indicators. "
    "Center (largest): AI chat widget with message bubbles. "
    "Right: booking calendar with colored time slots. "
    + _COMMON_LANDSCAPE
)

MOTIF_1_PORTRAIT = (
    "Light gradient background white to cool blue. "
    "Three floating browser windows stacked vertically with overlap and shadows: "
    "Top: analytics dashboard, bar chart, green KPI indicators. "
    "Middle (largest): AI chat widget with message bubbles. "
    "Bottom: booking calendar with colored time slots. "
    + _COMMON_PORTRAIT
)

# Motiv 2: Workflow-Automation
MOTIF_2_LANDSCAPE = (
    "Light gradient background white to cool blue. "
    "Workflow diagram left to right: Email node -> AI brain node -> checkmark node, "
    "connected by curved blue (#137EDE) lines. Rounded rectangle nodes with icons. "
    "Floating widgets: mini bar chart, notification bell, calendar snippet, trend card. "
    + _COMMON_LANDSCAPE
)

MOTIF_2_PORTRAIT = (
    "Light gradient background white to cool blue. "
    "Workflow diagram top to bottom: Email node -> AI brain node -> checkmark node, "
    "connected by curved blue (#137EDE) lines. Rounded rectangle nodes with icons. "
    "Floating widgets on sides: mini bar chart, notification bell, calendar snippet, trend card. "
    + _COMMON_PORTRAIT
)

# Motiv 3: KI-Module-Grid
MOTIF_3_LANDSCAPE = (
    "Light gradient background white to cool blue. "
    "3x2 grid of module cards with shadows and rounded corners: "
    "'Chat' (bubble icon), 'Tickets' (tag icon), 'Kalender' (calendar icon), "
    "'E-Mail' (envelope icon), 'Analytics' (bar chart icon), 'Dokumente' (document icon). "
    "White cards, blue (#137EDE) accent line at top, icons in blue, titles dark gray. Slight perspective tilt. "
    + _COMMON_LANDSCAPE
)

MOTIF_3_PORTRAIT = (
    "Light gradient background white to cool blue. "
    "2x3 grid of module cards centered in the upper 60% of the image, with shadows and rounded corners: "
    "'Chat' (bubble icon), 'Tickets' (tag icon), 'Kalender' (calendar icon), "
    "'E-Mail' (envelope icon), 'Analytics' (bar chart icon), 'Dokumente' (document icon). "
    "White cards, blue (#137EDE) accent line at top, icons in blue, titles dark gray. Slight perspective tilt. "
    + _COMMON_PORTRAIT
)

# Motiv-Definitionen: Nummer -> (Landscape-Prompt, Portrait-Prompt, Kurzname)
MOTIFS = {
    1: (MOTIF_1_LANDSCAPE, MOTIF_1_PORTRAIT, "Dashboard-Trio"),
    2: (MOTIF_2_LANDSCAPE, MOTIF_2_PORTRAIT, "Workflow-Automation"),
    3: (MOTIF_3_LANDSCAPE, MOTIF_3_PORTRAIT, "KI-Module-Grid"),
}


def get_api_key() -> str:
    """Liest den Gemini API-Key aus der Umgebungsvariable."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("ERROR: GEMINI_API_KEY nicht gesetzt.")
        print("Setze die Variable: export GEMINI_API_KEY='dein-key'")
        sys.exit(1)
    return key


def generate_image_bytes(prompt: str, aspect_ratio: str, api_key: str) -> bytes | None:
    """Generiert ein Bild via Gemini 3 Pro und gibt die Roh-Bytes zurueck (kein Datei-Schreiben)."""
    url = f"{API_BASE}/{MODEL_ID}:generateContent"

    full_prompt = STYLE_PREFIX + prompt

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": api_key,
    }

    payload = {
        "contents": [{"parts": [{"text": full_prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE", "TEXT"],
            "imageConfig": {"aspectRatio": aspect_ratio},
        },
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
    except requests.exceptions.RequestException as e:
        print(f"  ERROR: Netzwerkfehler -- {e}")
        return None

    if response.status_code != 200:
        print(f"  ERROR: API-Fehler {response.status_code}")
        print(f"  {response.text[:300]}")
        return None

    data = response.json()

    candidates = data.get("candidates", [])
    if not candidates:
        print("  ERROR: Keine Candidates in Response")
        print(f"  {json.dumps(data, indent=2)[:300]}")
        return None

    parts = candidates[0].get("content", {}).get("parts", [])

    image_data = None
    for part in parts:
        inline_data = part.get("inlineData", {})
        if inline_data.get("mimeType", "").startswith("image/"):
            image_data = inline_data["data"]
            break

    if not image_data:
        print("  ERROR: Kein Bild in Response-Parts gefunden")
        print(f"  {json.dumps(data, indent=2)[:500]}")
        return None

    return base64.b64decode(image_data)


def create_qr_image(size: int) -> Image.Image:
    """Erzeugt einen QR-Code als PIL-Image in der angegebenen Groesse."""
    if qrcode is None:
        raise RuntimeError("qrcode nicht installiert. Fuehre aus: pip install 'qrcode[pil]'")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=2,
    )
    qr.add_data(QR_URL)
    qr.make(fit=True)

    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        fill_color="#0a1628",
        back_color="white",
    )

    pil_img = img.convert("RGBA")
    return pil_img.resize((size, size), Image.LANCZOS)


def generate_standalone_qr() -> bool:
    """Generiert einen standalone QR-Code als separate PNG-Datei."""
    if qrcode is None:
        print("  ERROR: qrcode nicht installiert. Fuehre aus: pip install 'qrcode[pil]'")
        return False

    output_path = OUTPUT_DIR / "qr-hinzke-digital.png"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=2,
    )
    qr.add_data(QR_URL)
    qr.make(fit=True)

    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        fill_color="#0a1628",
        back_color="white",
    )
    img.save(str(output_path))

    size_kb = output_path.stat().st_size / 1024
    print(f"  OK: {output_path} ({size_kb:.0f} KB)")
    return True


def postprocess_image(raw_bytes: bytes, final_path: Path, target_size: tuple,
                      qr_size: int, qr_position: str,
                      qr_cache: dict | None = None) -> bool:
    """
    Post-Processing: Resize auf exakte Groesse und QR-Code mit abgerundeten Ecken compositen.
    qr_position: 'bottom-right' oder 'bottom-center'
    qr_cache: Dict mit vorgenerierten QR-Images nach Groesse (wird in main() befuellt)
    """
    try:
        img = Image.open(io.BytesIO(raw_bytes)).convert("RGBA")
    except Exception as e:
        print(f"  ERROR: Bild konnte nicht geladen werden -- {e}")
        return False

    # Resize auf exakte Pixelgroesse
    img = img.resize(target_size, Image.LANCZOS)

    # QR-Code compositen (aus Cache oder neu erzeugen)
    if qrcode is not None:
        try:
            if qr_cache and qr_size in qr_cache:
                qr_img = qr_cache[qr_size]
            else:
                qr_img = create_qr_image(qr_size)

            # Weissen Hintergrund mit abgerundeten Ecken
            bg_padding = 8
            bg_size = qr_size + bg_padding * 2

            # Maske mit abgerundeten Ecken erstellen
            mask = Image.new("L", (bg_size, bg_size), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.rounded_rectangle(
                [(0, 0), (bg_size - 1, bg_size - 1)],
                radius=QR_BG_CORNER_RADIUS,
                fill=255,
            )

            # Weisser Hintergrund mit Maske anwenden
            qr_bg = Image.new("RGBA", (bg_size, bg_size), (0, 0, 0, 0))
            white_bg = Image.new("RGBA", (bg_size, bg_size), (255, 255, 255, 255))
            qr_bg.paste(white_bg, (0, 0), mask)

            # QR-Code auf den abgerundeten Hintergrund
            qr_bg.paste(qr_img, (bg_padding, bg_padding), qr_img)

            # Position berechnen
            if qr_position == "bottom-right":
                x = target_size[0] - bg_size - QR_PADDING
                y = target_size[1] - bg_size - QR_PADDING
            else:  # bottom-center
                x = (target_size[0] - bg_size) // 2
                y = target_size[1] - bg_size - QR_PADDING

            img.paste(qr_bg, (x, y), qr_bg)
        except Exception as e:
            print(f"  WARNUNG: QR-Code konnte nicht eingebettet werden -- {e}")
    else:
        print("  WARNUNG: qrcode nicht installiert -- kein QR-Overlay")

    # Als PNG speichern (RGBA -> RGB fuer kleinere Datei)
    final_path.parent.mkdir(parents=True, exist_ok=True)
    img_rgb = img.convert("RGB")
    img_rgb.save(str(final_path), "PNG")

    return True


def process_variant(name: str, motif_num: int, prompt: str, aspect_ratio: str,
                    target_size: tuple, qr_size: int, qr_position: str,
                    api_key: str, force: bool, dry_run: bool,
                    qr_cache: dict | None = None) -> str:
    """
    Generiert und verarbeitet eine Variante.
    Gibt 'generated', 'skipped' oder 'failed' zurueck.
    """
    final_path = OUTPUT_DIR / f"pos-{name}-{motif_num}.png"

    print(f"\n  [{name.upper()} Motiv {motif_num} {aspect_ratio}]")

    if dry_run:
        print(f"  Prompt:\n  {STYLE_PREFIX}{prompt}")
        return "skipped"

    # Pruefen ob finale Datei schon existiert
    if final_path.exists() and not force:
        print(f"  SKIP: {final_path} existiert bereits")
        return "skipped"

    # Bild generieren (in-memory)
    print(f"  Generiere via Gemini...")
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


def cleanup_old_files():
    """Loescht alte Dateien aus frueheren Versionen (v1 + v2)."""
    old_patterns = [
        "entwurf-1-*", "entwurf-2-*", "entwurf-3-*",  # v1
        "pos-landscape.png", "pos-portrait.png",         # v2 (ohne Motiv-Nummer)
        "pos-*-raw.png",                                  # v2 Raw-Dateien
    ]
    deleted = []
    for pattern in old_patterns:
        for f in OUTPUT_DIR.glob(pattern):
            f.unlink()
            deleted.append(f.name)
    if deleted:
        print(f"\n  Alte Dateien geloescht: {', '.join(deleted)}")


def main():
    parser = argparse.ArgumentParser(
        description="Generiert POS-Visuals fuer Hinzke Digital via Gemini 3 Pro.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Beispiele:\n"
            "  python scripts/generate-pos-visuals.py                    # Alle 6 Bilder\n"
            "  python scripts/generate-pos-visuals.py --motif 2          # Nur Motiv 2\n"
            "  python scripts/generate-pos-visuals.py --landscape-only   # Nur Querformat\n"
            "  python scripts/generate-pos-visuals.py --portrait-only    # Nur Hochformat\n"
            "  python scripts/generate-pos-visuals.py --dry-run          # Nur Prompts zeigen\n"
            "  python scripts/generate-pos-visuals.py --force            # Ueberschreiben\n"
            "  python scripts/generate-pos-visuals.py --qr-only          # Nur QR-Code\n"
        ),
    )

    parser.add_argument(
        "--force",
        action="store_true",
        help="Bestehende Bilder ueberschreiben",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Nur Prompts anzeigen, keine Bilder generieren",
    )
    parser.add_argument(
        "--qr-only",
        action="store_true",
        help="Nur den QR-Code generieren",
    )
    parser.add_argument(
        "--landscape-only",
        action="store_true",
        help="Nur Querformat (1920x1080) generieren",
    )
    parser.add_argument(
        "--portrait-only",
        action="store_true",
        help="Nur Hochformat (1080x1920) generieren",
    )
    parser.add_argument(
        "--motif",
        type=int,
        choices=[1, 2, 3],
        help="Nur ein bestimmtes Motiv generieren (1=Dashboard-Trio, 2=Workflow-Automation, 3=KI-Module-Grid)",
    )

    args = parser.parse_args()

    if args.landscape_only and args.portrait_only:
        print("ERROR: --landscape-only und --portrait-only schliessen sich gegenseitig aus.")
        sys.exit(1)

    # QR-Only-Modus
    if args.qr_only:
        print("\nGeneriere QR-Code...")
        success = generate_standalone_qr()
        sys.exit(0 if success else 1)

    # API-Key pruefen (ausser bei dry-run)
    api_key = ""
    if not args.dry_run:
        api_key = get_api_key()

    # Motive bestimmen
    motif_nums = [args.motif] if args.motif else [1, 2, 3]

    # Varianten bestimmen: jedes Motiv x jedes Format
    variants = []
    for motif_num in motif_nums:
        landscape_prompt, portrait_prompt, motif_name = MOTIFS[motif_num]

        if not args.portrait_only:
            variants.append({
                "name": "landscape",
                "motif_num": motif_num,
                "motif_name": motif_name,
                "prompt": landscape_prompt,
                "aspect_ratio": "16:9",
                "target_size": LANDSCAPE_SIZE,
                "qr_size": QR_SIZE_LANDSCAPE,
                "qr_position": "bottom-right",
            })
        if not args.landscape_only:
            variants.append({
                "name": "portrait",
                "motif_num": motif_num,
                "motif_name": motif_name,
                "prompt": portrait_prompt,
                "aspect_ratio": "9:16",
                "target_size": PORTRAIT_SIZE,
                "qr_size": QR_SIZE_PORTRAIT,
                "qr_position": "bottom-center",
            })

    # Header
    mode = "DRY-RUN" if args.dry_run else "GENERIERUNG"
    motif_info = f"Motiv {args.motif}" if args.motif else "Alle 3 Motive"
    print(f"\n{'#'*60}")
    print(f"  POS-Visual-Generierung v2.1 -- {mode}")
    print(f"  Modell: {MODEL_ID}")
    print(f"  Motive: {motif_info}")
    print(f"  Bilder: {len(variants)} ({', '.join(f'{v['name']}-{v['motif_num']}' for v in variants)})")
    print(f"  Output: {OUTPUT_DIR}")
    if args.force:
        print(f"  Force: Bestehende Bilder werden ueberschrieben")
    print(f"{'#'*60}")

    # Motiv-Legende
    for num in motif_nums:
        _, _, name = MOTIFS[num]
        print(f"  Motiv {num}: {name}")

    # Output-Verzeichnis erstellen
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Alte Dateien aufraeumen
    cleanup_old_files()

    # QR-Code einmal vorab generieren und cachen
    qr_cache = {}
    if not args.dry_run and qrcode is not None:
        print("\n  QR-Code vorab generieren...")
        for size in {QR_SIZE_LANDSCAPE, QR_SIZE_PORTRAIT}:
            qr_cache[size] = create_qr_image(size)
        print(f"  QR-Cache: {len(qr_cache)} Groessen ({', '.join(f'{s}px' for s in sorted(qr_cache))})")

    # Varianten verarbeiten
    stats = {"generated": 0, "skipped": 0, "failed": 0}

    for i, variant in enumerate(variants):
        result = process_variant(
            name=variant["name"],
            motif_num=variant["motif_num"],
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

        # Rate-Limiting zwischen Calls (nicht nach dem letzten)
        if not args.dry_run and result == "generated" and i < len(variants) - 1:
            print(f"\n  Warte {DELAY_BETWEEN_CALLS}s (Rate-Limiting)...")
            time.sleep(DELAY_BETWEEN_CALLS)

    # Standalone QR-Code generieren (ausser dry-run)
    if not args.dry_run:
        print(f"\n{'='*60}")
        print(f"QR-Code (standalone)")
        print(f"{'='*60}")
        qr_path = OUTPUT_DIR / "qr-hinzke-digital.png"
        if qr_path.exists() and not args.force:
            print(f"  SKIP: QR-Code existiert bereits ({qr_path})")
        else:
            generate_standalone_qr()

    # Zusammenfassung
    print(f"\n{'#'*60}")
    print(f"  FERTIG")
    print(f"  Generiert: {stats['generated']}")
    print(f"  Uebersprungen: {stats['skipped']}")
    print(f"  Fehlgeschlagen: {stats['failed']}")
    print(f"{'#'*60}")

    # Output-Datei-Uebersicht
    print(f"\n  Dateien in {OUTPUT_DIR}:")
    if OUTPUT_DIR.exists():
        for f in sorted(OUTPUT_DIR.iterdir()):
            if f.is_file():
                size_kb = f.stat().st_size / 1024
                print(f"    {f.name} ({size_kb:.0f} KB)")
    print()

    if stats["failed"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
