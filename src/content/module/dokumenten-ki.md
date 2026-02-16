---
title: "Dokumenten-KI"
description: "Rechnungen & Lieferscheine automatisch erkennen und Daten extrahieren. KI-gestützte Dokumentenverarbeitung für KMU."
icon: "file-scan"
techStack:
  - "N8N"
  - "Vision AI (GPT-4o / Claude)"
  - "OCR"
  - "Paperless-ngx"
benefits:
  - "Keine manuelle Dateneingabe mehr"
  - "Schnelle Verarbeitung großer Dokumentenmengen"
  - "Fehlerarm durch KI-gestützte Erkennung"
  - "Durchsuchbares digitales Archiv"
  - "Automatische Klassifizierung nach Dokumenttyp"
useCases:
  - "Rechnungseingang automatisch verarbeiten"
  - "Lieferscheine erfassen und zuordnen"
  - "Verträge digitalisieren und archivieren"
  - "Formulare und Anfragen auslesen"
order: 9
relatedModules:
  - "buchhaltung"
  - "angebots-generator"
  - "email-assistent"
faq:
  - question: "Welche Dokumenttypen werden erkannt?"
    answer: "Rechnungen, Lieferscheine, Angebote, Verträge, Formulare und Anfragen. Das System lernt mit der Zeit neue Dokumenttypen dazu."
  - question: "Wie genau ist die Erkennung?"
    answer: "Bei strukturierten Dokumenten wie Rechnungen liegt die Erkennungsrate bei über 95 %. Bei handschriftlichen oder schlecht gescannten Dokumenten entsprechend niedriger, aber immer noch deutlich schneller als manuelles Abtippen."
  - question: "Funktioniert das auch mit Papierdokumenten?"
    answer: "Ja. Du scannst das Dokument oder fotografierst es mit dem Smartphone. Die KI verarbeitet Scans, Fotos und PDFs gleichermaßen."
  - question: "Wo werden die Daten gespeichert?"
    answer: "Auf deiner eigenen Infrastruktur. Keine Cloud-Abhängigkeit, keine Daten bei Drittanbietern. Optional mit Paperless-ngx als durchsuchbarem Archiv."
---

Jeden Tag treffen Rechnungen, Lieferscheine und Anfragen ein -- per E-Mail, per Post, per Upload. Die Dokumenten-KI erkennt automatisch, um welchen Dokumenttyp es sich handelt, extrahiert die relevanten Daten und leitet sie an die richtige Stelle weiter. Schluss mit Abtippen, Zuordnen und Ablegen von Hand.

## Das Problem

Deutsche KMU verarbeiten im Schnitt 1.000 bis 5.000 Eingangsbelege pro Jahr. Jede Rechnung wird manuell geöffnet, die Daten werden abgetippt -- Rechnungsnummer, Datum, Betrag, Lieferant, Positionen. Das dauert pro Beleg 3-5 Minuten. Bei 3.000 Belegen sind das über 150 Arbeitsstunden im Jahr, die ein Mitarbeiter mit stumpfer Dateneingabe verbringt. Umgerechnet sind das fast vier Wochen Vollzeitarbeit -- nur für Tippen.

Dazu kommen Fehler. Zahlendreher bei der Rechnungsnummer, falsches Datum, Beleg im falschen Ordner abgelegt. Diese Fehler fallen oft erst auf, wenn es zu spät ist -- bei der Steuererklärung, beim Jahresabschluss oder wenn ein Lieferant mahnt. Die Fehlerquote bei manueller Dateneingabe liegt bei 1-5 % -- klingt wenig, aber bei 3.000 Belegen sind das bis zu 150 fehlerhafte Einträge pro Jahr.

## So funktioniert's

Die Dokumenten-KI nutzt einen N8N-Workflow mit Vision-AI-Modellen (GPT-4o oder Claude), die Dokumente nicht nur lesen, sondern verstehen. Der Prozess läuft in drei Schritten:

**Schritt 1 -- Eingang erkennen**: Ein Dokument trifft ein, per E-Mail-Anhang, Upload-Ordner oder Scan. Der Workflow erkennt automatisch, dass ein neues Dokument vorliegt und startet die Verarbeitung.

**Schritt 2 -- Klassifizieren und Extrahieren**: Die Vision-KI analysiert das Dokument. Sie erkennt den Typ (Rechnung, Lieferschein, Angebot, Vertrag), extrahiert die Kerndaten (Absender, Datum, Positionen, Beträge) und strukturiert sie als JSON. Bei mehrseitigen Dokumenten werden alle Seiten analysiert und zusammengeführt.

**Schritt 3 -- Weiterleiten und Ablegen**: Die extrahierten Daten werden an das richtige System weitergeleitet. Rechnungen gehen ans [Buchhaltungsmodul](/module/buchhaltung), Anfragen an den [E-Mail-Assistenten](/module/email-assistent), Angebote ins CRM. Das Originaldokument wird in Paperless-ngx archiviert und ist ab sofort durchsuchbar.

Der Unterschied zu klassischer OCR: Die KI versteht Kontext. Sie weiß, dass "Gesamtbetrag" und "Total" dasselbe bedeuten. Sie erkennt, ob eine Zahl ein Datum, eine Menge oder ein Preis ist. Und sie lernt mit der Zeit dazu -- je mehr Dokumente verarbeitet werden, desto besser und schneller wird die Erkennung.

## Für wen?

- **Handwerksbetriebe**: Eingangsrechnungen von Lieferanten, Materiallieferscheine, Auftragsbestätigungen -- alles automatisch erfasst statt im Aktenordner. Besonders wertvoll, wenn die Buchhaltung nur Teilzeit besetzt ist und jede eingesparte Stunde zählt.
- **Dienstleister und Agenturen**: Verträge, Briefings und Kundenanfragen automatisch erkennen und zuordnen. Nie wieder eine Anfrage im Posteingang übersehen, weil sie als Anhang versteckt war. Die KI erkennt auch komplexe Dokumente wie NDAs oder Rahmenverträge.
- **Handel und E-Commerce**: Lieferscheine mit Bestellungen abgleichen, Rechnungen automatisch kontieren, Retourenbelege verarbeiten. Bei hohem Belegvolumen spart das nicht Stunden, sondern Tage pro Monat. Ein Online-Händler mit 500 Belegen im Monat spart ca. 30 Arbeitsstunden.

## Kombiniert mit

Die Dokumenten-KI ist der ideale Einstiegspunkt für Automatisierung, weil sie an so vielen Stellen andockt. In Kombination mit dem [Buchhaltungsmodul](/module/buchhaltung) fließen extrahierte Rechnungsdaten direkt in LexOffice -- keine manuelle Belegerfassung mehr, vollautomatisch vom Posteingang bis zur Buchung.

Zusammen mit dem [Angebots-Generator](/module/angebots-generator) wird es richtig rund: Eingehende Anfragen werden automatisch erkannt, die Daten extrahiert und als Basis für ein automatisch generiertes Angebot verwendet. Von der Anfrage zum Angebot in Minuten statt Tagen.

Und der [KI E-Mail Assistent](/module/email-assistent) profitiert ebenfalls: Dokumente, die als E-Mail-Anhang eintreffen, werden automatisch klassifiziert und verarbeitet -- der Assistent muss nicht mehr jeden Anhang einzeln prüfen.

Du brauchst erst mal eine professionelle Website? Schau dir unsere [Webseiten-Pakete](/webseiten) an -- die Dokumenten-KI lässt sich nahtlos integrieren.

## Welche Dokumenttypen werden erkannt?

Rechnungen, Lieferscheine, Angebote, Verträge, Formulare und allgemeine Anfragen. Das System ist nicht auf eine feste Liste beschränkt -- neue Dokumenttypen lassen sich jederzeit anlernen. Nach einer kurzen Trainingsphase mit 10-20 Beispieldokumenten erkennt die KI auch branchenspezifische Formate zuverlässig. Ob Speditionsaufträge, technische Zeichnungen mit Maßangaben oder Laborberichte -- die KI passt sich an deine Branche an.

## Wie genau ist die Erkennung?

Bei strukturierten Dokumenten wie Rechnungen und Lieferscheinen liegt die Erkennungsrate bei über 95 %. Das bedeutet: Von 100 Rechnungen werden 95+ korrekt und vollständig erkannt. Bei handschriftlichen oder schlecht gescannten Dokumenten liegt die Rate niedriger, aber selbst dann ist die Verarbeitung schneller als manuelles Abtippen. Und bei Unsicherheit markiert das System den Beleg zur manuellen Prüfung -- so rutscht nichts durch.

## Funktioniert das auch mit Papierdokumenten?

Ja. Papierdokumente werden gescannt oder mit dem Smartphone fotografiert. Die KI verarbeitet Scans, Fotos und PDFs gleichermaßen. Für optimale Ergebnisse empfehlen wir einen Dokumentenscanner mit automatischem Einzug -- so landen Papierbelege in Sekunden im Workflow. Selbst ein Smartphone-Foto eines leicht schiefen Belegs wird zuverlässig erkannt.

## Wo werden die Daten gespeichert?

Auf deiner eigenen Infrastruktur. Die Dokumente liegen in Paperless-ngx auf deinem Server, die extrahierten Daten in deiner Datenbank. Keine Abhängigkeit von Cloud-Diensten, keine Daten bei Drittanbietern. Das ist nicht nur DSGVO-konform, sondern gibt dir die volle Kontrolle über dein Dokumentenarchiv. Und falls du mal den Anbieter wechseln willst: Alles exportierbar, kein Vendor-Lock-in.

Klingt interessant? [Lass uns in 20 Minuten besprechen](/kontakt), wie die Dokumenten-KI in deinem Unternehmen aussehen könnte.
