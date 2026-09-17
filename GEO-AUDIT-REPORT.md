# GEO Audit Report: Hinzke Digital

**Audit-Datum:** 2026-03-27
**URL:** https://hinzke.digital
**Business Type:** Agency/Services (Digitale Produkte & Beratung fuer KMU)
**Seiten analysiert:** 26 (Sitemap) / 8 tiefenanalysiert
**Framework:** Astro 5.17.2 (SSG) auf Dokploy/Hetzner

---

## Executive Summary

**Overall GEO Score: 42/100 (Poor)**

Die technische Basis ist solide: Astro SSG liefert blitzschnelles, crawler-freundliches HTML, alle AI-Crawler haben Zugang, llms.txt existiert, und die Schema-Architektur ist erweiterbar. Aber: Die Seite ist fuer AI-Systeme praktisch unsichtbar. Es fehlt zitierbarer Content (kein einziger Blog-Artikel mit Substanz, keine Case Studies), die Marke "Hinzke Digital" existiert als Entity in keinem AI-System, und das Schema.org Markup ist unvollstaendig (null sameAs-Links, fehlende Kontaktdaten). Die 40-jaehrige Unternehmensgeschichte und 2.000+ Kunden sind ein massiver ungenutzter Hebel.

### Score Breakdown

| Kategorie | Score | Gewicht | Gewichtet |
|---|---|---|---|
| AI Citability | 47/100 | 25% | 11,75 |
| Brand Authority | 18/100 | 20% | 3,60 |
| Content E-E-A-T | 47/100 | 20% | 9,40 |
| Technical GEO | 73/100 | 15% | 10,95 |
| Schema & Structured Data | 28/100 | 10% | 2,80 |
| Platform Optimization | 38/100 | 10% | 3,80 |
| **Overall GEO Score** | | | **42/100** |

---

## Critical Issues (Sofort beheben)

### 1. Datenschutzerklaerung ist ein Entwurf
- **Seite:** /datenschutz
- **Problem:** Die Datenschutzerklaerung ist explizit als Entwurf markiert ("wird vor dem Launch durch eine vollstaendige, rechtlich gepruefte Version ersetzt"). Matomo-Tracking laeuft aber bereits.
- **Impact:** Rechtliches Risiko (DSGVO) und sofortiger Vertrauens-Killer fuer Besucher und AI-Systeme.
- **Fix:** Rechtlich finalisierte Datenschutzerklaerung einsetzen. Entwurfs-Hinweis entfernen.

### 2. Security Headers fehlen komplett
- **Seite:** Alle (Server-Level)
- **Problem:** Kein HSTS, kein CSP, kein X-Frame-Options, kein X-Content-Type-Options, kein Referrer-Policy, kein Permissions-Policy. Score: 15/100.
- **Impact:** Reales Sicherheitsrisiko + fehlendes Trust-Signal fuer Suchmaschinen.
- **Fix:** Traefik Middleware in Dokploy konfigurieren:
  ```
  stsSeconds=31536000
  frameDeny=true
  contentTypeNosniff=true
  referrerPolicy=strict-origin-when-cross-origin
  permissionsPolicy=camera=(), microphone=(), geolocation=()
  ```

### 3. Schema.org ohne sameAs -- Entity Linking fehlt komplett
- **Seite:** Alle (Layout.astro)
- **Problem:** ProfessionalService-Schema hat null sameAs-Links, keine Telefonnummer, keine E-Mail, keine vollstaendige Adresse, kein Logo. AI-Modelle koennen "Hinzke Digital" nicht als Entity verifizieren.
- **Impact:** Die Marke existiert fuer AI-Systeme schlicht nicht.
- **Fix:** ProfessionalService in Layout.astro erweitern um: vollstaendige Adresse (Kanalstr. 62, 23552 Luebeck), telephone, email, logo, sameAs (LinkedIn, hinzke.de).

---

## High Priority Issues (Diese Woche)

### 4. Null zitierbarer Content
- **Problem:** Blog hat 1 Post (185 Woerter Willkommenstext). Keine Case Studies. Keine eigenen Daten/Studien. Kein einziger Content-Block erreicht 70/100 Citability Score.
- **Impact:** AI-Systeme haben keinen Grund, diese Seite als Antwortquelle zu verwenden.
- **Fix:** Mindestens 3 substanzielle Artikel veroeffentlichen:
  - "Was kostet eine KMU-Webseite 2026?" (mit eigenen Preisdaten)
  - "Von der Druckerei zum Digital-Dienstleister: 40 Jahre Hinzke" (Unique Story)
  - Case Study zur eigenen Druckerei-Digitalisierung (Vorher/Nachher, konkrete Zahlen)

### 5. Person Schema fehlt auf /ueber-mich
- **Problem:** Magnus Hinzke hat kein Person-Schema. LinkedIn ist im HTML, aber nicht strukturiert. Kein eigenstaendiges Person-Schema mit jobTitle, worksFor, sameAs.
- **Fix:** Person-Schema mit @id auf /ueber-mich implementieren.

### 6. FAQPage Schema fehlt auf Modul-Seiten
- **Problem:** Modul-Detailseiten (z.B. /module/support-chat) haben FAQ-Inhalte im HTML, aber kein FAQPage-Schema. Nur /webseiten hat FAQPage-Schema.
- **Fix:** FAQPage-Schema auf allen Modul-Seiten mit FAQ-Sektionen ergaenzen.
- **Update:** Laut Code-Analyse ist das FAQPage-Schema in [...slug].astro implementiert und wird automatisch generiert wenn FAQs vorhanden sind. Ggf. pruefen ob alle Modul-Content-Dateien FAQs enthalten.

### 7. Trailing-Slash-Inkonsistenz (Duplicate Content)
- **Problem:** `trailingSlash` ist nicht explizit konfiguriert. Sitemap-URLs haben Trailing-Slash, Canonical-Tags teilweise nicht. Beide URL-Varianten liefern 200 OK = 50 duplizierte Seiten.
- **Fix:** In `astro.config.mjs` explizit `trailingSlash: 'always'` setzen.

### 8. Homepage Title doppelter Brand-Name
- **Problem:** "Weniger Handarbeit, mehr Ergebnis -- Hinzke Digital | Hinzke Digital" (73 Zeichen, Brand doppelt).
- **Fix:** Auf "Weniger Handarbeit, mehr Ergebnis | Hinzke Digital" kuerzen (50 Zeichen).

### 9. Sitemap ohne lastmod Dates
- **Problem:** Alle 25 URLs in sitemap-0.xml ohne `<lastmod>`. Crawler wissen nicht, welche Seiten aktuell sind.
- **Fix:** Astro Sitemap-Plugin mit `serialize` Callback konfigurieren fuer lastmod.

### 10. llms.txt Fehler und Luecken
- **Problem:** Link-Format falsch (sollte `- [Title](url): Description` sein), Paketnamen inkonsistent ("Starter/Business/Premium" statt "Web Start/Web Business/Web Pro"), 2 Module fehlen, kein llms-full.txt.
- **Fix:** llms.txt korrigieren und llms-full.txt erstellen.

---

## Medium Priority Issues (Innerhalb 30 Tage)

### 11. Null externe Brand Presence
- Kein Wikipedia/Wikidata-Eintrag
- Kein YouTube-Kanal
- Kein Reddit-Praesenz
- Kein Google Business Profile
- Keine Bewertungen auf Google, Trustpilot oder ProvenExpert fuer hinzke.digital
- LinkedIn: Nur persoenliches Profil, keine Company Page fuer "Hinzke Digital"

### 12. Keine Testimonials oder Bewertungen
- Referenz-Kunden (VfB Luebeck, VfL Luebeck-Schwartau, THW Kiel) nur als Text-Mentions
- Keine Case Studies, keine Ergebniszahlen, keine Kundenzitate

### 13. Kontaktseite ohne Telefon/Adresse
- Telefonnummer und Adresse nur im Impressum, nicht auf /kontakt sichtbar
- Keine Google Maps Integration

### 14. Keine Kompression / Browser-Caching
- HTML wird unkomprimiert ausgeliefert (22 KB)
- `cache-control: public, max-age=0` -- kein Browser-Caching
- Assets mit Content-Hashes koennten `immutable` sein

### 15. IndexNow nicht implementiert
- Kein IndexNow-Protokoll fuer Bing
- Keine Bing Webmaster Tools Verifikation

### 16. Cross-Domain-Verknuepfung hinzke.de <-> hinzke.digital fehlt
- Keine gegenseitige Verlinkung
- Keine sameAs-Verbindung im Schema
- 40 Jahre Domain-Autoritaet von hinzke.de wird nicht transferiert

### 17. OG-Images identisch auf allen Seiten
- Alle Seiten nutzen `/og-default.png`
- Keine seitenspezifischen Social-Preview-Bilder

---

## Low Priority Issues (Optimieren wenn moeglich)

### 18. Hero-Image fetchpriority
- `fetchpriority="auto"` statt `fetchpriority="high"` auf dem LCP-Element

### 19. speakable Property fehlt
- Keine Markierung fuer AI-Assistenten-Konsum in Schema

### 20. WebSite Schema fehlt auf Homepage
- Kein WebSite-Schema mit Publisher-Referenz

### 21. robots.txt ohne explizite AI-Crawler-Direktiven
- Funktional korrekt, aber keine bewusste AI-Crawler-Strategie erkennbar

### 22. CTA-Formulierungen repetitiv
- "Bereit fuer deinen naechsten Schritt?" auf jeder Seite identisch
- Leichtes AI-Content-Signal

---

## Category Deep Dives

### AI Citability (47/100)

**Staerkste Passage** (62/100): Support-Chat Statistiken -- "80% aller Kundenanfragen sind Wiederholungen. 82% der Kunden erwarten Antwort innerhalb von 10 Minuten."
Problem: Branchentypische Benchmarks ohne Quellenangabe, nicht als Hinzke-eigene Daten zitierbar.

**Zweitstaerkste** (55/100): Preistabelle auf /webseiten -- konkrete Zahlen, gut strukturiert, aber nur relevant wenn jemand explizit nach "Hinzke Digital Preise" sucht.

**Keine einzige Passage erreicht 70/100** (Citation-Ready Schwelle).

**Kernproblem:** Die Seite hat keine Inhalte, die eine konkrete Frage besser beantworten als alles andere im Netz. Der Blog ist leer, es gibt keine Case Studies, keine eigenen Daten, keine Thought-Leadership-Artikel.

**Crawler Access** (80/100): Alle AI-Crawler erlaubt, Sitemap referenziert, llms.txt vorhanden. Technisch gut.

**llms.txt** (55/100): Vorhanden, aber falsches Link-Format, inkonsistente Paketnamen, 2 Module fehlen, kein llms-full.txt.

---

### Brand Authority (18/100)

| Plattform | Status | Score |
|---|---|---|
| Wikipedia | Absent | 0/30 |
| Reddit | Absent | 0/20 |
| YouTube | Absent | 0/15 |
| LinkedIn | Persoenliches Profil vorhanden (397 Kontakte) | 6/10 |
| Branchenquellen | Trustpilot fuer hinzke.de (270 Reviews, 5 Sterne), Gelbe Seiten (Druckerei) | 12/25 |

**Kernproblem:** "Hinzke Digital" existiert als Entity in keinem AI-System. Die Reputation der Druckerei (hinzke.de) strahlt nicht auf hinzke.digital ab -- keine strukturierte Verbindung.

---

### Content E-E-A-T (47/100)

| Dimension | Score | Kernbefund |
|---|---|---|
| Experience | 9/25 | 40+ Jahre behauptet, null belegt. Keine Case Studies, keine Vorher/Nachher |
| Expertise | 13/25 | Detaillierter Tech-Stack, gute Modul-Tiefe, aber keine Zertifizierungen |
| Authoritativeness | 10/25 | GmbH seit 1984, aber null externe Validierung |
| Trustworthiness | 14/25 | Impressum vollstaendig, Matomo statt GA. Aber: Datenschutz als Entwurf, null Bewertungen |

**Ehrliche Einordnung:** Du verkaufst Erfahrung und Praxis -- aber zeigst sie nicht. Die Druckerei-Digitalisierung, die Sportverein-Projekte, die eigene Shopware-Automatisierung: das ist alles echtes Material, das kein Wettbewerber kopieren kann. Es muss nur aufgeschrieben werden.

---

### Technical GEO (73/100)

| Kategorie | Score | Status |
|---|---|---|
| Server-Side Rendering | 100/100 | Astro SSG -- perfekt fuer AI-Crawlability |
| Mobile Optimization | 90/100 | Responsive, Touch-optimiert, Viewport korrekt |
| Core Web Vitals Risk | 80/100 | Sehr schnell (88ms TTFB), minimales JS |
| Crawlability | 70/100 | Sitemap OK, aber Trailing-Slash-Problem und fehlende lastmod |
| URL Structure | 65/100 | Saubere URLs, aber Trailing-Slash-Ambiguitaet |
| Meta Tags | 62/100 | OG + Twitter Cards vorhanden, aber Title-Duplikat |
| Security Headers | 15/100 | 0/6 Security Headers -- kritisch |

**Staerke:** Astro SSG ist der Best-Case fuer GEO. 100% HTML server-rendered, kein JS-Rendering noetig.
**Schwaeche:** Security Headers komplett absent, Trailing-Slash-Duplicate-Content.

---

### Schema & Structured Data (28/100)

| Schema | Vorhanden | Qualitaet |
|---|---|---|
| ProfessionalService | Ja (alle Seiten) | Minimal -- fehlen: sameAs, telephone, email, logo, vollstaendige Adresse |
| FAQPage | Ja (/webseiten, Modulseiten) | Syntaktisch valide |
| Service | Ja (Modulseiten) | Minimal -- fehlen: offers, serviceType, areaServed |
| BreadcrumbList | Ja (Unterseiten) | Korrekt |
| BlogPosting | Ja (Blog-Posts) | Teilweise -- fehlen: image, publisher.logo, inLanguage |
| Person | **Nein** | Komplett fehlend |
| Organization | **Nein** | Nur ProfessionalService |
| WebSite | **Nein** | Fehlend |
| sameAs | **Null Links** | Kritisch |
| speakable | **Nein** | Fehlend |
| Offer/Pricing | **Nein** | Trotz klarer Preise auf /webseiten |

---

### Platform Optimization (38/100)

| Platform | Score | Status |
|---|---|---|
| Google AI Overviews | 52/100 | Fair -- FAQ-Struktur gut, aber fehlende Query-Headings |
| Bing Copilot | 35/100 | Poor -- kein IndexNow, kein Bing Webmaster Tools |
| ChatGPT Web Search | 33/100 | Poor -- Entity nicht erkannt |
| Google Gemini | 30/100 | Poor -- null Google-Oekosystem-Praesenz |
| Perplexity AI | 28/100 | Poor -- null Community-Validation |

**Staerkste Platform:** Google AI Overviews (dank FAQ-Schema und Vergleichstabelle)
**Schwaechste:** Perplexity (null externe Signale)

---

## Quick Wins (Diese Woche umsetzbar)

1. **Schema.org in Layout.astro erweitern** -- sameAs, telephone, email, vollstaendige Adresse hinzufuegen. Effort: 30 Min. Impact: +8 Schema Score, +5 Platform Score.

2. **Person Schema auf /ueber-mich** -- Magnus Hinzke als Entity strukturieren mit LinkedIn sameAs. Effort: 20 Min. Impact: +10 Schema Score.

3. **Trailing-Slash in astro.config.mjs fixen** -- `trailingSlash: 'always'` setzen. Effort: 5 Min. Impact: 50 duplizierte URLs eliminiert.

4. **Homepage Title kuerzen** -- Brand-Duplikat entfernen. Effort: 5 Min.

5. **Security Headers in Traefik** -- Middleware konfigurieren. Effort: 15 Min. Impact: +50 Security Score.

6. **llms.txt korrigieren** -- Link-Format fixen, Paketnamen angleichen, fehlende Module ergaenzen. Effort: 20 Min. Impact: +15 llms.txt Score.

7. **Datenschutzerklaerung finalisieren** -- Entwurfs-Hinweis entfernen. Effort: Variable (braucht rechtliche Pruefung).

---

## 30-Tage Action Plan

### Woche 1: Technische Grundlagen
- [ ] Security Headers in Traefik konfigurieren
- [ ] Schema.org erweitern (sameAs, Adresse, Telefon, Logo)
- [ ] Person Schema auf /ueber-mich
- [ ] Trailing-Slash-Problem fixen
- [ ] Homepage Title korrigieren
- [ ] llms.txt Fehler beheben
- [ ] Datenschutzerklaerung finalisieren
- [ ] Sitemap lastmod aktivieren

### Woche 2: Entity Building
- [ ] Google Business Profile anlegen (Kanalstr. 62, 23552 Luebeck)
- [ ] LinkedIn Company Page fuer "Hinzke Digital" erstellen
- [ ] IndexNow fuer Bing implementieren
- [ ] Bing Webmaster Tools einrichten
- [ ] Cross-Link hinzke.de <-> hinzke.digital einrichten
- [ ] Telefon + Adresse auf Kontaktseite anzeigen

### Woche 3: Content-Maschine starten
- [ ] Case Study #1: Eigene Druckerei-Digitalisierung (Vorher/Nachher mit Zahlen)
- [ ] Blog-Artikel: "Was kostet eine KMU-Webseite 2026?" (mit eigenen Preisdaten)
- [ ] Referenz-Kunden mit konkreten Ergebnissen unterlegen
- [ ] Statistiken auf Modulseiten mit Quellen versehen

### Woche 4: Social Proof & Verbreitung
- [ ] 3-5 Testimonials/Bewertungen sammeln und einbinden
- [ ] Google Reviews von bestehenden Kunden anfragen
- [ ] Blog-Artikel: "Von der Druckerei zum Digital-Dienstleister" (Unique Story)
- [ ] Offer-Schema fuer Webseiten-Pakete implementieren
- [ ] BlogPosting-Schema erweitern (image, publisher.logo, speakable)

---

## Erwartete Score-Entwicklung

| Zeitpunkt | GEO Score | Aenderung |
|---|---|---|
| Jetzt | 42/100 | -- |
| Nach Woche 1 (Technik) | ~52/100 | +10 |
| Nach Woche 2 (Entity) | ~58/100 | +6 |
| Nach Woche 4 (Content + Proof) | ~65-70/100 | +7-12 |
| Nach 3 Monaten (Content-Flywheel) | ~75-80/100 | +10-15 |

---

## Appendix: Seiten analysiert

| URL | Titel | GEO Issues |
|---|---|---|
| / | Weniger Handarbeit, mehr Ergebnis | 4 (Title doppelt, Schema minimal, kein WebSite-Schema, Hero fetchpriority) |
| /webseiten | Webseiten-Pakete | 2 (Kein Offer-Schema, Trailing-Slash) |
| /module | Digitale Module | 2 (Kein ItemList-Schema, duenner Content) |
| /module/support-chat | KI-Support-Chat | 1 (Statistiken ohne Quellen) |
| /ueber-mich | Ueber mich | 3 (Kein Person-Schema, Foto-Alt generisch, Tech-Stack unfokussiert) |
| /blog | Blog | 1 (Nur 1 Post) |
| /blog/willkommen | Digitalisierung fuer KMU | 3 (185 Woerter, kein image im BlogPosting, Thin Content) |
| /kontakt | Kontakt | 3 (Keine Telefonnr, keine Adresse, kein ContactPage-Schema) |
| /impressum | Impressum | 0 (Vollstaendig) |
| /datenschutz | Datenschutz | 1 (Entwurf!) |
| /module/* (14 weitere) | Modul-Detailseiten | Je 1-2 (Service-Schema minimal, Statistiken ohne Quellen) |

---

## Technische Details

### Infrastruktur
- **Server:** Hetzner Cloud (ubuntu-dokploy-hinzke)
- **IPv4:** 46.225.141.104 / **IPv6:** 2a01:4f8:1c19:98a6::1
- **Reverse Proxy:** Traefik (via Dokploy)
- **SSL:** Let's Encrypt, TLSv1.3, gueltig bis 2026-05-17
- **HTTP/2 + H3:** Ja
- **TTFB:** 88ms (exzellent)
- **DNS:** Cloudflare (DNS-only, kein Proxy)
- **Analytics:** Matomo (self-hosted, DSGVO-konform)

### robots.txt
```
User-agent: *
Allow: /
Disallow: /api/
Sitemap: https://hinzke.digital/sitemap-index.xml
```
Keine AI-Crawler blockiert. Keine expliziten AI-Direktiven.

### llms.txt
Vorhanden (200 OK). Format-Fehler bei Links, Inkonsistenzen bei Paketnamen, 2 Module fehlen.

---

*Generiert mit Claude Code GEO Audit -- 2026-03-27*
