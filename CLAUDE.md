# Hinzke Digital

Digitale Produkte & Beratung von Magnus Hinzke. Eigenständiges Geschäftsfeld neben dem Druckerei-Kerngeschäft (hinzke.de / Folger Hinzke GmbH).

## Projektüberblick

- **Was**: Website zum Verkauf digitaler Produkte (Webseiten-Pakete) und Modul-Übersicht für KI/Digitalisierung
- **Zielgruppe**: KMU / Mittelstand, bestehende Hinzke-Druckkunden, Neukunden
- **Herkunft**: Inhalte von l3dynamics.de (wird eingestellt) werden übernommen und erweitert
- **Abrechnung**: Erstmal über Folger Hinzke GmbH, später ggf. trennbar
- **Kein Login/Auth**: Kein Account-System, keine User-Daten

## Design

- **Primary Color**: #137EDE (Blau, übernommen von L3 Dynamics)
- **Secondary**: #000000 (Schwarz)
- **Background**: Weiß
- **Stil**: Clean, professionell, Grid-basiert, responsive
- **Referenz**: https://l3dynamics.de/ (Design-Richtung)

## Tech Stack (Website)

| Bereich | Tool | Details |
|---------|------|---------|
| **Framework** | Astro 5 (Hybrid) | SSR nur für /api/* Routes, Rest statisch vorgerendert |
| **Styling** | Tailwind CSS | Utility-first |
| **Hosting** | Dokploy | Self-hosted PaaS auf eigenem VPS |
| **Payments** | Stripe | Checkout Sessions + Webhooks, nur für Webseiten-Pakete |
| **Termine** | Cal.com Cloud | Ersetzt Microsoft Bookings, Free Tier, Embed-Widget |
| **Email (transaktional)** | Resend | Bestätigungsmails, Kontaktformular |
| **Email (Newsletter)** | Listmonk (self-hosted) | Go + PostgreSQL, Resend als SMTP |
| **Email-Validierung** | Reacher (self-hosted) | Syntax/DNS/SMTP Check vor Kampagnenversand |
| **Content** | Claude Code | Alle Texte, Produktbeschreibungen, SEO |
| **Analytics** | Matomo (self-hosted) | DSGVO-konform, eigene Instanz |
| **Domain** | TBD | Eigene Domain, l3dynamics.de → 301 Redirect |

> **Infrastruktur-Hinweis**: Resend, Listmonk, Reacher, Dokploy und Matomo werden in einem separaten Projekt verwaltet. Setup und Konfiguration dieser Services sind dort dokumentiert. Hier nur als Abhängigkeiten referenziert.

## Produkte

### Webseiten (3 Pakete) → direkt kaufbar über Stripe

Klassisches Paket-Pricing für KMU:
- **Starter** - Einfache Webpräsenz
- **Business** - Erweiterte Features
- **Premium** - Full-Service

CTA: **"Jetzt buchen"** → Stripe Checkout

### Module (Beratungsprodukte) → individuell

Digitale Bausteine, die zeigen was mit KI und Automatisierung möglich ist. Kunden wissen oft gar nicht, was digitalisiert werden kann - die Module machen das sichtbar und greifbar.

**Kein Stripe-Checkout für Module.** Jedes Modul hat nur Beratungs-CTAs:
- **"Beratungsgespräch buchen"** → Cal.com
- **"Individuell anfragen"** → Kontaktformular

Jedes Modul hat eine eigene Produktseite unter `/module/[slug]`. Neue Module = neue Markdown-Datei in der Content Collection.

| # | Modul | Slug | Was es macht | Tech dahinter |
|---|-------|------|-------------|---------------|
| 1 | Online Support Chat | `support-chat` | KI-Chatbot auf Kunden-Website, trainiert auf Firmendaten (FAQ, Produkte) | N8N + OpenAI/Claude + RAG (Vektordatenbank) |
| 2 | Ticket-System | `ticket-system` | Helpdesk & Shared Inbox für Kundenservice-Teams | FreeScout (self-hosted, Open Source) + N8N Webhooks |
| 3 | Buchungsmodul | `buchungsmodul` | Terminbuchung / Reservierungen für Kunden-Webseiten | Cal.com White-Label oder Custom |
| 4 | Buchhaltung | `buchhaltung` | LexOffice-Anbindung, automatisierte Belegverarbeitung, Rechnungsflows | N8N + LexOffice API + KI |
| 5 | Controlling | `controlling` | Liquiditätsplanung, Cashflow-Analyse, Szenarien, Echtzeit-Dashboard | Tidely (ab 45 EUR/Monat, 5000+ Bankanbindungen) + Beratung |
| 6 | KI E-Mail Assistent | `email-assistent` | Posteingang kategorisieren, Antwortvorschläge generieren, tägliche Zusammenfassung | N8N + OpenAI/Claude + IMAP/Gmail |
| 7 | Bewertungs-Management | `bewertungen` | Google Reviews automatisch beantworten, Sentiment-Analyse, Alerts bei negativen Bewertungen | N8N + Google Business API + KI |
| 8 | Social Media Autopilot | `social-media` | Content-Generierung aus Firmennews, automatisches Posten auf LinkedIn/Instagram/Facebook | N8N + KI + Social Media APIs |
| 9 | Dokumenten-KI | `dokumenten-ki` | Rechnungen/Lieferscheine/Anfragen automatisch erkennen, Daten extrahieren, ablegen | N8N + Vision AI + OCR |
| 10 | Angebots-Generator | `angebots-generator` | Aus Kundenanfrage automatisch Angebot erstellen (mit Preislisten, Vorlagen) | N8N + KI + Templates |
| 11 | Lead-Qualifizierung | `lead-qualifizierung` | Website-Besucher bewerten, automatisch CRM-Eintrag + Follow-up Mail | N8N + KI + CRM-Anbindung |
| 12 | Reporting Dashboard | `reporting` | Automatische Berichte aus verschiedenen Datenquellen (Umsatz, Social, Website) | N8N + Daten-APIs + KI-Zusammenfassung |
| 13 | Newsletter-System | `newsletter` | Self-hosted Newsletter ohne Mailchimp, volle Datenkontrolle, Analytics, Bounce-Management | Listmonk (self-hosted) + Resend SMTP |
| 14 | Allgemeine Beratung | `beratung` | Prozessoptimierung, Digitalisierungs-Strategie, KI-Readiness-Assessment | Persönliche Beratung + Analyse |

## Tech-Stack (auf der Website gezeigt)

Kompetenz-Übersicht als Logo-Grid. Kategorisiert, mit Hover-Tooltips.
Kuratiert aus L3 Dynamics + allen Git-Repos von Magnus.

### KI & Automatisierung
OpenAI, Azure AI, Claude/Anthropic, N8N, Cursor

### Frameworks & Web
Astro, Next.js, React, SvelteKit, Tailwind CSS, TypeScript

### E-Commerce & CMS
Shopware 6, Medusa.js, Strapi, Meilisearch

### Datenbanken & Backend
PostgreSQL, Redis, Supabase, SQL Server, Prisma

### DevOps & Infrastruktur
Docker, Proxmox, Dokploy, Cloudflare, Playwright

### Payments & Business
Stripe, PayPal, LexOffice, Datev, Tidely, HubSpot

### Produktivität & Tools
FreeScout, Listmonk, Obsidian, Notion, Coda.io, Paperless, Nextcloud, Home Assistant, Matomo

### Sprachen
TypeScript/JavaScript, Python, Go, PHP

## Seitenstruktur

```
[neue-domain.de] — Astro 5 Hybrid auf Dokploy
│
├── /                              Landing Page (Hero, USPs, Überblick)
├── /webseiten                     3 Pakete (Starter/Business/Premium) → Stripe
│
├── /module                        Übersicht aller Module (Grid/Cards)
├── /module/support-chat           ┐
├── /module/ticket-system          │
├── /module/buchungsmodul          │
├── /module/buchhaltung            │
├── /module/controlling            │
├── /module/email-assistent        │ Alle Module: nur Beratungs-CTAs
├── /module/bewertungen            │ (Cal.com + Kontaktformular)
├── /module/social-media           │ Kein Stripe Checkout
├── /module/dokumenten-ki          │
├── /module/angebots-generator     │
├── /module/lead-qualifizierung    │
├── /module/reporting              │
├── /module/newsletter             │
├── /module/beratung               ┘
│
├── /kontakt                       Formular + Cal.com Embed
├── /ueber-mich                    Magnus + Tech-Stack Grid
├── /impressum                     Pflichtseiten
├── /datenschutz                   DSGVO
├── /danke                         Stripe Success-Page (nur Webseiten-Pakete)
│
├── /api/checkout                  POST → Stripe Checkout Session (nur Webseiten)
├── /api/webhook                   POST → Stripe Webhook Handler
└── /api/contact                   POST → Kontaktformular → Resend
```

## Payment Flow (nur Webseiten-Pakete)

```
Webseiten-Paket auswählen → "Jetzt buchen"
  → POST /api/checkout (Produkt-ID, Preis-ID)
  → Stripe Checkout Session erstellen
  → Redirect → Stripe Hosted Checkout
  → Erfolg → /danke + Stripe Webhook feuert
  → Webhook → Resend: Bestätigungsmail an Kunden + Benachrichtigung an Magnus
```

## Modul-Anfragen (individuelle Beratung)

```
Modul-Seite besuchen → Interesse geweckt
  → "Beratungsgespräch buchen" → Cal.com Buchungswidget
  → ODER "Individuell anfragen" → Kontaktformular → Resend Mail an Magnus
```

## Bestandskunden-Aktivierung

### Ziel
Bestehende Hinzke-Druckkunden (< 2000 Adressen aus CSV) informieren: "Magnus macht jetzt auch digital" → auf Hinzke Digital verweisen.

### Flow
1. CSV mit E-Mail + Ansprechpartner importieren
2. Reacher: Alle Adressen validieren → Ungültige rausfiltern
3. Bereinigte Liste in Listmonk importieren
4. Personalisiertes E-Mail-Template ("Hallo {{Vorname}}")
5. Kampagne senden über Resend SMTP
6. Listmonk trackt: Opens, Clicks, Bounces
7. Bounces automatisch entfernen

### DSGVO
- Bestandskunden dürfen über ähnliche eigene Produkte informiert werden (§ 7 Abs. 3 UWG)
- Abmeldelink + Impressum in jeder Mail (Listmonk automatisch)

> **Infrastruktur-Hinweis**: Reacher- und Listmonk-Setup sind im separaten Infrastruktur-Projekt dokumentiert.

## Migration von L3 Dynamics

- l3dynamics.de → 301 Redirect auf neue Domain
- Beratungsinhalte → Modul "Allgemeine Beratung"
- Case Studies / Referenzen übernehmen
- Prozess-Methodik (6 Schritte) übernehmen
- Tech-Stack aktualisiert und erweitert
- Design-Richtung (Blau #137EDE) übernommen

## Projekt-Setup (Reihenfolge)

1. Astro 5 Projekt initialisieren (TypeScript, Tailwind, Hybrid, Node-Adapter)
2. Komponenten (Layout, Header, Footer, Paket-Cards, Modul-Cards, Tech-Stack Grid)
3. Content Collection für Module (Schema + Markdown pro Modul)
4. Content erstellen via Claude Code (Landing, Pakete, 14 Modul-Seiten, Über mich, SEO)
5. Stripe (Products/Prices nur für 3 Webseiten-Pakete, /api/checkout, /api/webhook)
6. Cal.com Cloud (Account, Eventtypen, Embed-Widget auf /kontakt + Modul-Seiten)
7. Resend, Listmonk, Reacher, Dokploy, Matomo → separates Infrastruktur-Projekt
8. Verlinkung von hinzke.de (Banner/Link im Shopware-Shop)
9. l3dynamics.de → 301 Redirect
10. E-Mail-Kampagne (CSV validieren → Listmonk → senden)

## Trennbarkeit / Zukunftssicherheit

- Eigene Domain → jederzeit auf andere GmbH übertragbar
- Stripe-Account unabhängig vom Druckerei-Business
- Cal.com Cloud-Account personengebunden
- Module als Content Collection → beliebig erweiterbar ohne Code-Änderung
- N8N Workflows reproduzierbar → einmal bauen, oft verkaufen
- Open-Source Stack (FreeScout, Listmonk, N8N, Cal.com) → kein Vendor-Lock-in
- Kein Auth-Layer = keine User-Daten = weniger DSGVO-Aufwand
