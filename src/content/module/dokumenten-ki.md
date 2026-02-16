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
highlights:
  - icon: "brain"
    title: "KI versteht Kontext"
    text: "Die Vision-KI erkennt nicht nur Text, sondern versteht Zusammenhänge. Sie weiß, dass 'Gesamtbetrag' und 'Total' dasselbe bedeuten und unterscheidet Daten von Preisen."
  - icon: "zap"
    title: "Über 95 % Erkennungsrate"
    text: "Bei strukturierten Dokumenten wie Rechnungen und Lieferscheinen werden über 95 % korrekt und vollständig erkannt. Bei Unsicherheit markiert das System den Beleg zur Prüfung."
  - icon: "database"
    title: "Durchsuchbares Archiv"
    text: "Alle Dokumente werden in Paperless-ngx archiviert und sind ab sofort volltextdurchsuchbar. Auf deiner eigenen Infrastruktur, ohne Cloud-Abhängigkeit."
steps:
  - title: "Eingang erkennen"
    description: "Ein Dokument trifft per E-Mail-Anhang, Upload-Ordner oder Scan ein. Der Workflow startet automatisch die Verarbeitung."
  - title: "Klassifizieren und extrahieren"
    description: "Die Vision-KI analysiert den Dokumenttyp, extrahiert Kerndaten wie Absender, Datum, Positionen und Beträge und strukturiert sie als JSON."
  - title: "Weiterleiten und ablegen"
    description: "Extrahierte Daten gehen an das richtige System -- Rechnungen zur Buchhaltung, Anfragen zum E-Mail-Assistenten. Das Original wird in Paperless-ngx archiviert."
problem:
  heading: "150 Stunden pro Jahr nur für Abtippen"
  text: "Deutsche KMU verarbeiten 1.000 bis 5.000 Eingangsbelege pro Jahr. Jede Rechnung wird manuell geöffnet, Rechnungsnummer, Datum, Betrag und Positionen abgetippt -- 3-5 Minuten pro Beleg. Bei 3.000 Belegen sind das über 150 Arbeitsstunden, fast vier Wochen Vollzeitarbeit. Dazu kommen Fehler: Zahlendreher, falsches Datum, Beleg im falschen Ordner. Die Fehlerquote bei manueller Eingabe liegt bei 1-5 % -- bis zu 150 fehlerhafte Einträge pro Jahr."
solution:
  heading: "Vom Posteingang zur Buchung -- automatisch"
  text: "Die Dokumenten-KI nutzt Vision-AI-Modelle, die Dokumente nicht nur lesen, sondern verstehen. Ein N8N-Workflow erkennt eingehende Dokumente automatisch, klassifiziert sie nach Typ, extrahiert die relevanten Daten und leitet sie an das richtige System weiter. Rechnungen gehen direkt zur Buchhaltung, Anfragen zum E-Mail-Assistenten. Das Originaldokument wird in Paperless-ngx archiviert und ist ab sofort durchsuchbar. Die KI lernt mit der Zeit dazu -- je mehr Dokumente verarbeitet werden, desto besser wird die Erkennung."
---
