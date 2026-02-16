#!/usr/bin/env python3
"""
Bildgenerierung fuer Modul-Seiten (hinzke-digital).
Generiert Problem- und Solution-Bilder fuer alle 14 Module via Gemini 3 Pro.

Verwendung:
  python scripts/generate-module-images.py                  # Alle Module
  python scripts/generate-module-images.py --module support-chat  # Einzelnes Modul
  python scripts/generate-module-images.py --dry-run        # Nur Prompts anzeigen
  python scripts/generate-module-images.py --force           # Bestehende ueberschreiben
"""

import argparse
import base64
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

# --- Konfiguration ---

MODEL_ID = "gemini-3-pro-image-preview"
API_BASE = "https://generativelanguage.googleapis.com/v1beta/models"

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUT_DIR = PROJECT_ROOT / "public" / "images" / "module"

# Pause zwischen API-Calls (Sekunden) -- Rate-Limiting
DELAY_BETWEEN_CALLS = 5

# Basis-Stil fuer konsistente Bildsprache
STYLE_PREFIX = (
    "Realistic UI screenshot mockup, floating browser window, clean minimal background, "
    "modern SaaS design, subtle drop shadow, rounded corners, no people, no cartoon. "
)

# --- Modul-Definitionen mit Prompts ---

MODULES = [
    {
        "slug": "support-chat",
        "name": "KI-Support-Chat",
        "problem": (
            "Overflowing email inbox showing 999+ unread messages, cluttered helpdesk interface, "
            "multiple browser tabs with unanswered customer tickets, red notification badges, "
            "chaotic and overwhelming"
        ),
        "solution": (
            "Clean modern chat widget embedded in a professional business website, "
            "AI chatbot conversation showing helpful instant response, green online indicator, "
            "minimal and organized interface"
        ),
    },
    {
        "slug": "ticket-system",
        "name": "Ticket-System",
        "problem": (
            "Messy project management tool with overdue tasks everywhere, red warning icons, "
            "unassigned tickets piling up, cluttered sidebar with hundreds of unread notifications, "
            "multiple overlapping modal windows"
        ),
        "solution": (
            "Clean helpdesk dashboard with organized ticket list, color-coded status badges showing "
            "open, in-progress and resolved, shared inbox with team assignments, smooth minimal interface"
        ),
    },
    {
        "slug": "buchungsmodul",
        "name": "Buchungsmodul",
        "problem": (
            "Paper desk calendar with crossed-out appointments, double bookings marked in red, "
            "sticky notes everywhere, phone ringing icon, old-school scheduling chaos on screen"
        ),
        "solution": (
            "Elegant online booking calendar interface showing available time slots in green, "
            "automatic confirmation email preview, clean weekly view with smooth drag-and-drop scheduling"
        ),
    },
    {
        "slug": "buchhaltung",
        "name": "Buchhaltung",
        "problem": (
            "Spreadsheet nightmare with hundreds of rows of manual bookkeeping entries, "
            "formula errors highlighted in red, multiple Excel windows open, receipt photos "
            "scattered across desktop"
        ),
        "solution": (
            "Modern accounting dashboard with automatic receipt scanning, AI-detected invoice data "
            "auto-filling fields, clean transaction list with smart categorization, green checkmarks "
            "for verified entries"
        ),
    },
    {
        "slug": "controlling",
        "name": "Controlling",
        "problem": (
            "Multiple outdated Excel spreadsheets with confusing pivot tables, broken chart "
            "visualizations, copy-paste errors between files, overwhelming wall of numbers "
            "with no clear insights"
        ),
        "solution": (
            "Real-time financial dashboard with cashflow charts, trend lines, liquidity forecast "
            "graph, traffic-light health indicators in green, clean data visualization with KPI cards"
        ),
    },
    {
        "slug": "email-assistent",
        "name": "KI E-Mail Assistent",
        "problem": (
            "Overflowing email inbox with 2,847 unread messages, no folder structure, spam mixed "
            "with important client emails, red notification badges on every folder, search returning "
            "too many results"
        ),
        "solution": (
            "Smart email dashboard with AI-categorized inbox sections: Urgent, Clients, Newsletter, "
            "Internal. Auto-generated reply suggestions shown as cards, daily summary panel with "
            "key action items"
        ),
    },
    {
        "slug": "bewertungen",
        "name": "Bewertungs-Management",
        "problem": (
            "Google Business profile showing declining star rating from 4.5 to 3.2, unanswered "
            "negative reviews stacking up, angry review notifications, no response management "
            "system visible"
        ),
        "solution": (
            "Review management dashboard showing all Google reviews in real-time, AI-suggested "
            "response drafts, sentiment analysis chart trending upward, alert badges for new reviews, "
            "star rating recovering to 4.6"
        ),
    },
    {
        "slug": "social-media",
        "name": "Social Media Autopilot",
        "problem": (
            "Empty social media profiles on a screen, last post date showing 6 months ago, "
            "zero engagement metrics, dusty neglected analytics dashboard with flat-line graphs"
        ),
        "solution": (
            "Social media management dashboard with content calendar grid, auto-generated posts "
            "queued for LinkedIn and Instagram, rising engagement charts, follower growth metrics, "
            "scheduled post previews"
        ),
    },
    {
        "slug": "dokumenten-ki",
        "name": "Dokumenten-KI",
        "problem": (
            "Desktop cluttered with unsorted PDF files, invoices and delivery notes mixed together, "
            "file explorer showing hundreds of unnamed documents, no folder structure, search "
            "returning nothing useful"
        ),
        "solution": (
            "Document AI processing interface showing automatic document classification: Invoice "
            "detected, data fields extracted and highlighted, clean digital filing system with "
            "smart search, organized folder tree"
        ),
    },
    {
        "slug": "angebots-generator",
        "name": "Angebots-Generator",
        "problem": (
            "Word document with manual quote being typed, printed price list lying beside keyboard, "
            "slow and error-prone process visible, customer email asking 'where is my quote?' "
            "showing 3 days old"
        ),
        "solution": (
            "Automatic quote generator interface showing professional PDF quote created in seconds "
            "from customer inquiry, price positions auto-filled, one-click PDF export button, "
            "clean and fast workflow"
        ),
    },
    {
        "slug": "lead-qualifizierung",
        "name": "Lead-Qualifizierung",
        "problem": (
            "Website analytics showing high visitor count but near-zero conversion rate, bounce "
            "rate at 89%, no contact forms filled, potential customers leaving without action, "
            "missed opportunity indicators"
        ),
        "solution": (
            "CRM dashboard with lead scoring system, qualified leads ranked by engagement score, "
            "automated follow-up email sequences shown, sales pipeline funnel filling up, "
            "visitor-to-customer conversion flow"
        ),
    },
    {
        "slug": "reporting",
        "name": "Reporting Dashboard",
        "problem": (
            "Multiple browser tabs open with different analytics tools, manual copy-paste into "
            "a messy Excel report, outdated charts from last month, time-consuming and error-prone "
            "manual reporting process"
        ),
        "solution": (
            "Unified real-time reporting dashboard pulling data from multiple sources: revenue, "
            "social media, website traffic, customer service. AI-generated summary panel with "
            "key insights and trend arrows"
        ),
    },
    {
        "slug": "newsletter",
        "name": "Newsletter-System",
        "problem": (
            "Mailchimp pricing page showing expensive monthly plans, limited features warning, "
            "US-hosted data concerns badge, GDPR compliance question marks, vendor lock-in "
            "warning indicators"
        ),
        "solution": (
            "Self-hosted newsletter dashboard with full data control, campaign analytics showing "
            "opens and clicks, professional template editor, bounce management panel, zero monthly "
            "fees indicator, GDPR-compliant badge"
        ),
    },
    {
        "slug": "beratung",
        "name": "Allgemeine Beratung",
        "problem": (
            "Whiteboard covered in question marks and unstructured sticky notes, too many digital "
            "tool logos scattered around with no clear connection, overwhelmed planning interface "
            "with no strategy visible"
        ),
        "solution": (
            "Clean consulting roadmap interface showing structured digitalization plan with "
            "milestones, clear step-by-step phases on a timeline, connected tool ecosystem "
            "diagram, progress tracking dashboard"
        ),
    },
]


def get_api_key() -> str:
    """Liest den Gemini API-Key aus der Umgebungsvariable."""
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("ERROR: GEMINI_API_KEY nicht gesetzt.")
        print("Setze die Variable: export GEMINI_API_KEY='dein-key'")
        sys.exit(1)
    return key


def generate_image(prompt: str, output_path: Path, api_key: str) -> bool:
    """Generiert ein Bild via Gemini 3 Pro und speichert es als PNG."""
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
            "imageConfig": {"aspectRatio": "16:9"},
        },
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
    except requests.exceptions.RequestException as e:
        print(f"  ERROR: Netzwerkfehler -- {e}")
        return False

    if response.status_code != 200:
        print(f"  ERROR: API-Fehler {response.status_code}")
        print(f"  {response.text[:300]}")
        return False

    data = response.json()

    # Bild aus Response extrahieren
    candidates = data.get("candidates", [])
    if not candidates:
        print("  ERROR: Keine Candidates in Response")
        print(f"  {json.dumps(data, indent=2)[:300]}")
        return False

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
        return False

    # Speichern
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(base64.b64decode(image_data))

    return True


def process_module(module: dict, api_key: str, force: bool, dry_run: bool) -> dict:
    """Generiert Problem- und Solution-Bild fuer ein Modul. Gibt Statistik zurueck."""
    slug = module["slug"]
    name = module["name"]
    stats = {"generated": 0, "skipped": 0, "failed": 0}

    print(f"\n{'='*60}")
    print(f"Modul: {name} ({slug})")
    print(f"{'='*60}")

    for image_type, prompt_key in [("problem", "problem"), ("solution", "solution")]:
        filename = f"{slug}-{image_type}.png"
        output_path = OUTPUT_DIR / filename
        prompt = module[prompt_key]

        print(f"\n  [{image_type.upper()}] {filename}")

        if dry_run:
            print(f"  Prompt: {STYLE_PREFIX}{prompt}")
            stats["skipped"] += 1
            continue

        if output_path.exists() and not force:
            print(f"  SKIP: Datei existiert bereits ({output_path})")
            stats["skipped"] += 1
            continue

        print(f"  Generiere...")
        success = generate_image(prompt, output_path, api_key)

        if success:
            size_kb = output_path.stat().st_size / 1024
            print(f"  OK: {output_path} ({size_kb:.0f} KB)")
            stats["generated"] += 1
        else:
            stats["failed"] += 1

        # Rate-Limiting: Pause vor dem naechsten Call
        print(f"  Warte {DELAY_BETWEEN_CALLS}s (Rate-Limiting)...")
        time.sleep(DELAY_BETWEEN_CALLS)

    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Generiert Problem- und Solution-Bilder fuer Modul-Seiten via Gemini 3 Pro.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Beispiele:\n"
            "  python scripts/generate-module-images.py                      # Alle Module\n"
            "  python scripts/generate-module-images.py --module support-chat # Einzelnes Modul\n"
            "  python scripts/generate-module-images.py --dry-run             # Nur Prompts zeigen\n"
            "  python scripts/generate-module-images.py --force               # Ueberschreiben\n"
        ),
    )

    parser.add_argument(
        "--module",
        type=str,
        help="Slug eines einzelnen Moduls (z.B. support-chat)",
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

    args = parser.parse_args()

    # API-Key pruefen (ausser bei dry-run)
    api_key = ""
    if not args.dry_run:
        api_key = get_api_key()

    # Module filtern
    if args.module:
        modules = [m for m in MODULES if m["slug"] == args.module]
        if not modules:
            available = ", ".join(m["slug"] for m in MODULES)
            print(f"ERROR: Modul '{args.module}' nicht gefunden.")
            print(f"Verfuegbar: {available}")
            sys.exit(1)
    else:
        modules = MODULES

    # Header
    mode = "DRY-RUN" if args.dry_run else "GENERIERUNG"
    print(f"\n{'#'*60}")
    print(f"  Modul-Bildgenerierung -- {mode}")
    print(f"  Modell: {MODEL_ID}")
    print(f"  Module: {len(modules)}")
    print(f"  Bilder: {len(modules) * 2}")
    print(f"  Output: {OUTPUT_DIR}")
    if args.force:
        print(f"  Force: Bestehende Bilder werden ueberschrieben")
    print(f"{'#'*60}")

    # Output-Verzeichnis erstellen
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Module verarbeiten
    total = {"generated": 0, "skipped": 0, "failed": 0}

    for module in modules:
        stats = process_module(module, api_key, args.force, args.dry_run)
        for key in total:
            total[key] += stats[key]

    # Zusammenfassung
    print(f"\n{'#'*60}")
    print(f"  FERTIG")
    print(f"  Generiert: {total['generated']}")
    print(f"  Uebersprungen: {total['skipped']}")
    print(f"  Fehlgeschlagen: {total['failed']}")
    print(f"{'#'*60}\n")

    if total["failed"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
