---
title: "Buchbare Beratungswebsite an einem Tag: wie hygiene-luebeck.de entstanden ist"
description: "Case Study: Statische Astro-5-Website mit Festpreisen über Stripe Payment Links, Terminbuchung über Cal.com und GEO-first-Aufbau. 15 Commits, 93 Minuten von Grundgerüst bis Schema, kein eigener Checkout."
publishedAt: 2026-09-21
tags: ["case-study", "geo", "astro", "stripe", "kmu"]
modulbezug: "buchungsmodul"
---

**Kurzfassung:** hygiene-luebeck.de ist eine statische Website für ein neues Beratungsangebot (Hygienebeauftragte für Pflegedienste, Praxen, Studios und Kindertagespflege). Kunden finden das Angebot, sehen Festpreise und bezahlen direkt, ohne dass vorher jemand telefoniert oder ein Angebot schreibt. Es gibt keinen eigenen Checkout, kein CMS und keine Nutzerkonten. Bezahlung läuft über Stripe Payment Links, Termine über ein selbst gehostetes Cal.com. Vom ersten bis zum letzten Commit vergingen 93 Minuten. Die ganze Seite ging an einem Tag live.

Dieser Beitrag zeigt, welche Entscheidungen das möglich gemacht haben, was konkret gebaut wurde und was noch offen ist. Die Eckdaten stehen auch auf der [Projektseite](/projekte/hygiene-luebeck-de/).

## Ausgangslage

- Ein Beratungsangebot startet bei null: keine Website, keine Kunden, keine Sichtbarkeit.
- Für aktiven Vertrieb ist keine Zeit. Das Angebot muss sich selbst verkaufen.
- Die Zielgruppe (Pflegedienste, Arztpraxen, Tattoo- und Kosmetikstudios, Kindertagespflege) sucht, wenn eine Prüfung ansteht. Dann will sie einen Preis und einen Termin, keine Kontaktanfrage mit drei Tagen Wartezeit.
- Budget: kein neues Abo, kein neues Tool. Alles auf der vorhandenen Infrastruktur.

## Die vier Entscheidungen, die den Tag möglich gemacht haben

**1. Kein eigener Checkout.** Bezahlen heißt: ein Link zu Stripe. Kein Warenkorb, keine Zahlungslogik, keine PCI-Fragen, nichts zu warten.

**2. Kein CMS.** Astro 5, statisch gebaut. Inhalte liegen in Markdown und einer einzigen Config-Datei. Kein Admin-Login, keine Plugin-Updates, keine Angriffsfläche.

**3. Keine Integration mit Script oder iFrame.** Stripe und Cal.com sind reine Links. Die Content Security Policy bleibt hart: `script-src 'self'`, sonst nichts. Ist ein Link in der Config leer, gibt es den Button nicht.

**4. Eine Quelle für alle Fakten.** Preise, Leistungen, FAQ, Einzugsgebiet und Quellen stehen in `src/config.ts`. Daraus entstehen Preistabelle, JSON-LD, llms.txt, robots.txt, Footer und Sitemap. Ein Preis ändert sich an einer Stelle, alles andere zieht nach.

## Was gebaut wurde

**Seitenstruktur (15 Routen):**

- Startseite als One-Pager mit Sprungmarken (Zielgruppen, Leistungen, Über mich, FAQ, Kontakt)
- 4 Fachseiten je Zielgruppe: Pflegedienst, Arztpraxis, Kosmetik/Tattoo/Fußpflege, Kindertagespflege
- 3 Ratgeber mit je rund 750 Wörtern (MD-Prüfung, Praxisbegehung Gesundheitsamt, Hygieneplan Studios nach Landesverordnung SH)
- Leistungen, FAQ mit 17 Fragen, Kontakt, Impressum, Datenschutz, Danke-Seite als Stripe-Redirect-Ziel
- Generiert: llms.txt, llms-full.txt, robots.txt, Sitemap

**Festpreise (netto zzgl. 19 % USt):**

| Baustein | Preis |
|---|---|
| Prüfungs-Check (2 bis 3 Stunden Begehung mit Protokoll) | 290 EUR |
| Prüfungsvorbereitung in 14 Tagen | 890 EUR |
| Hygiene-Patenschaft (monatlich kündbar) | 99 EUR/Monat |
| Studio-Paket | 249 EUR |
| Kindertagespflege-Paket | 149 EUR |
| Stundensatz | 85 EUR/h |

Brutto wird nie hart eingetippt, sondern aus dem Nettopreis berechnet. Anfahrt bis 25 km inklusive.

## Bezahlen ohne Checkout: Stripe Payment Links

Ein Skript mit rund 100 Zeilen legt über die Stripe-API Produkte, Preise und Payment Links an. Es ist idempotent: mehrfach ausführen ändert nichts, was schon existiert.

- Zahlungsarten: Karte, SEPA, PayPal
- Die Patenschaft ist ein Abo, der Rest Einmalzahlung
- 3 Pflichtfelder im Stripe-Formular: Einrichtung, Anschrift Einsatzort, Wunschtermin
- Telefonnummer und Rechnungsadresse sind Pflicht
- Nach Zahlung Redirect auf die Danke-Seite

Die Rechnung mit Umsatzsteuerausweis kommt nicht aus Stripe, sondern aus dem ERP (Obility). Stripe kassiert nur. Das hält die Buchhaltung in einem System.

## Terminbuchung: Cal.com, selbst gehostet

Vorgesehen ist ein kostenloses Erstgespräch von 20 Minuten. Cal.com läuft auf dem eigenen Dokploy-Server, der Datenschutz-Abschnitt ist vorbereitet. Ehrlich gesagt: Der Buchungslink ist zum Zeitpunkt dieses Beitrags noch nicht eingetragen. Solange die Config leer ist, führen alle Termin-Buttons auf das Kontaktformular. Das ist der Vorteil von Slots statt Integrationen: Die Seite ist live und funktioniert, der Baustein kommt dazu, wenn er fertig ist.

## GEO-first konkret

GEO heißt hier: Die Seite soll von ChatGPT, Claude, Perplexity und Google AI Overviews zitiert werden können. Was dafür eingebaut ist:

- **Answer-first-Absatz** direkt unter der H1 auf jeder Seite. Bei Ratgebern steht er im Frontmatter, damit er auch in llms.txt und JSON-LD landet.
- **JSON-LD als @graph** auf jeder Seite: ProfessionalService (mit Angeboten als UnitPriceSpecification, Umsatzsteuer explizit als nicht enthalten), Person, Article, FAQPage, BreadcrumbList, SpeakableSpecification.
- **llms.txt** nach llmstxt.org mit Kurzprofil, Festpreisen, Einzugsgebiet und der Abgrenzung, was das Angebot nicht ist. Dazu **llms-full.txt** mit allen Seitentexten.
- **robots.txt** mit `Allow: /` für alle und 20 explizit erlaubten KI-Crawlern (GPTBot, ClaudeBot, PerplexityBot, Google-Extended und weitere).
- **Quellen-Komponente** auf den Fachseiten: RKI, IfSG, Landesverordnung SH, MD-Bund. Regel: keine geratenen Deep-Links.
- **Entity-Hygiene:** Kein `sameAs` mit leerem Array. Lieber weglassen als leer.

Die Abgrenzung ist dabei bewusst Teil des Contents: Sandra Hinzke ist Hygienebeauftragte, keine Hygienefachkraft (das ist eine geschützte Weiterbildung). Keine Einrichtungen nach MedIpVO, kein Prüfungsversprechen. Dieser Satz steht wortgleich in Config, FAQ, llms.txt und JSON-LD. Ein Sprachmodell, das die Seite zitiert, zitiert damit auch die Grenze.

## Deployment und Sicherheit

- Docker in drei Stufen: Node 22 für Dependencies und Build, nginx:alpine als Runtime
- nginx mit CSP (`default-src 'self'; script-src 'self'`), X-Frame-Options DENY, Referrer-Policy, Permissions-Policy, nosniff
- Assets unter `/_astro/` ein Jahr immutable gecacht
- 301 von www auf die Hauptdomain
- Kein Tracking, keine Cookies, keine externen Ressourcen. Das OG-Bild wird beim Build aus SVG und Portrait gerendert.

**Das eine Learning, das Zeit gekostet hat:** Astro inlinet kleine Scripts standardmäßig ins HTML. Die harte CSP blockiert Inline-Scripts, und zwar still. Die Navigation sah fertig aus und tat nichts. Fix: `assetsInlineLimit: 0` in der Vite-Config, dazu ein Build-Check, der zählt, ob `<script type="module">` im HTML vorkommt. Muss null sein. Die Navigation funktioniert seitdem auch komplett ohne JavaScript.

## Zeitleiste aus der Git-History

| Uhrzeit | Stand |
|---|---|
| 20:05 | Grundgerüst mit GEO-Elementen |
| 20:38 | Buchbar über Stripe |
| 21:07 | Mobil fertig (Burger-Menü, Preiskarten) |
| 21:31 | Rechtliche Korrekturen nach Prüfung |
| 21:38 | Schema angereichert, letzter Commit |

15 Commits, zwei kurze Feature-Branches, alles am selben Abend.

## Was das für KMU bedeutet

Die Frage ist nicht, ob eine Website an einem Tag geht. Die Frage ist, was man dafür weglässt.

- **Weglassen:** eigener Checkout, CMS, Nutzerkonten, Tracking, Integrationen per Script.
- **Behalten:** Festpreise, direkte Bezahlung, ehrliche Abgrenzung, Inhalte, die eine konkrete Frage beantworten.
- **Kosten:** Hosting auf dem vorhandenen Server, Stripe nur pro Transaktion. Keine monatlichen Lizenzen.

Wer ein Angebot hat, das sich in Festpreisen beschreiben lässt, braucht keinen Shop. Ein Link reicht.

## Was noch offen ist

- Cal.com-Link eintragen
- Kontaktformular an n8n-Webhook hängen (aktuell mailto)
- IndexNow-Lauf für die erste Indexierung
- LinkedIn und Google Business Profile für die Entity-Verknüpfung
- 6 weitere Ratgeber für die Zielgruppen

Sichtbarkeit ist im Aufbau. Ob die GEO-Bausteine greifen, zeigt sich erst über die nächsten Monate. Wenn es Zahlen gibt, gibt es hier ein Update.

## Häufige Fragen

**Warum kein Shopsystem?**
Sechs Bausteine mit Festpreis brauchen keinen Warenkorb. Stripe Payment Links decken Karte, SEPA, PayPal und Abos ab, ohne dass etwas entwickelt oder gewartet werden muss.

**Warum statisch statt WordPress?**
Kein Login, keine Plugin-Updates, keine Datenbank. Die Seite besteht aus HTML-Dateien hinter nginx. Angriffsfläche und Betriebskosten sind minimal.

**Was kostet der Betrieb?**
Der Container läuft auf dem vorhandenen Dokploy-Server. Stripe berechnet Gebühren nur pro Zahlung. Es gibt kein monatliches Abo.

**Lässt sich das auf andere Beratungsangebote übertragen?**
Ja, wenn das Angebot in Festpreisen beschreibbar ist und die Zielgruppe online sucht. Steuerberatung, Coaching, Handwerker-Checks, Datenschutzberatung: gleiches Muster, andere Config.
