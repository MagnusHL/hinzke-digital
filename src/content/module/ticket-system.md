---
title: "Smartes Ticketsystem"
description: "Helpdesk mit KI-Unterstützung: Tickets automatisch kategorisieren, priorisieren und dem richtigen Mitarbeiter zuweisen. Auf Wunsch self-hosted, ohne Lizenzkosten."
icon: "ticket"
techStack:
  - "FreeScout (self-hosted, Open Source)"
  - "N8N Webhooks"
benefits:
  - "Kein Ticket geht mehr verloren oder bleibt unbeantwortet"
  - "Effektive Team-Kollaboration mit klarer Zuständigkeit"
  - "Self-hosted bedeutet volle Datenkontrolle"
  - "Open Source und kostenfrei -- keine Lizenzgebühren"
  - "Automatische Eskalation und Priorisierung"
useCases:
  - "Kundenservice und Support-Anfragen"
  - "IT-Support und Systemstörungen"
  - "Reklamationen und Beschwerden"
  - "Interne Anfragen zwischen Abteilungen"
order: 2
relatedModules:
  - "support-chat"
  - "email-assistent"
  - "reporting"
faq:
  - question: "Was kostet FreeScout im Vergleich zu Zendesk?"
    answer: "FreeScout ist Open Source und kostenlos. Bei Zendesk zahlst du ab 49 EUR pro Agent und Monat. Bei einem Team von 5 Agents sparst du mit FreeScout also knapp 3.000 EUR pro Jahr -- bei vergleichbarem Funktionsumfang."
  - question: "Wo werden die Daten gespeichert?"
    answer: "FreeScout läuft auf deiner eigenen Infrastruktur oder auf einem von uns verwalteten Server in Deutschland. Deine Kundendaten verlassen nie den europäischen Raum."
  - question: "Kann ich mein bestehendes E-Mail-System weiter nutzen?"
    answer: "Ja. FreeScout verbindet sich über IMAP/SMTP mit deinem bestehenden Mailserver. E-Mails an support@deinefirma.de landen automatisch als Tickets im System, ohne dass Kunden etwas merken."
  - question: "Wie aufwändig ist die Einrichtung?"
    answer: "Die Grundeinrichtung dauert 2-3 Werktage. Das umfasst Server-Setup, E-Mail-Anbindung, Benutzer anlegen und die wichtigsten Automatisierungen. Danach kann dein Team sofort loslegen."
highlights:
  - icon: "shield"
    title: "Self-hosted, volle Datenkontrolle"
    text: "FreeScout läuft auf deiner eigenen Infrastruktur. Keine Daten bei US-Anbietern, kein Vendor-Lock-in, DSGVO-konform ab Tag eins."
  - icon: "zap"
    title: "Automatische Zuweisung und Eskalation"
    text: "N8N-Webhooks sorgen dafür, dass Tickets automatisch kategorisiert, priorisiert und dem richtigen Mitarbeiter zugewiesen werden. Nach drei Tagen ohne Antwort greift die Eskalation."
  - icon: "trending-up"
    title: "Keine Lizenzkosten"
    text: "Zendesk kostet ab 49 EUR pro Agent/Monat. FreeScout ist Open Source und kostenlos. Bei 5 Agents sparst du knapp 3.000 EUR pro Jahr."
steps:
  - title: "Server aufsetzen und E-Mail anbinden"
    description: "Wir installieren FreeScout auf deiner Infrastruktur und verbinden es über IMAP/SMTP mit deinem bestehenden Mailserver. E-Mails landen automatisch als Tickets."
  - title: "Team und Regeln konfigurieren"
    description: "Benutzer anlegen, Zuständigkeiten definieren, automatische Regeln für Kategorisierung, Priorisierung und Eskalation einrichten."
  - title: "Workflows automatisieren"
    description: "N8N-Webhooks verbinden das Ticket-System mit deinen anderen Tools: Kontaktformular, Chat, CRM. Alles fließt in eine zentrale Inbox."
problem:
  heading: "E-Mail-Chaos kostet Kunden"
  text: "Kundenanfragen landen in verschiedenen Postfächern, werden weitergeleitet, in CC gesetzt oder vergessen. 23 % aller Anfragen werden ohne Ticket-System verspätet oder gar nicht beantwortet. Die durchschnittliche Antwortzeit liegt bei 12 Stunden -- Kunden erwarten unter 4 Stunden. Bei einem Team von 5 Leuten gehen 5-10 Stunden pro Woche allein für Abstimmung verloren."
solution:
  heading: "Struktur statt Chaos -- jede Anfrage hat einen Verantwortlichen"
  text: "FreeScout gibt jeder Kundenanfrage eine Nummer, einen Status und einen Verantwortlichen. Shared Inbox, Kollisionserkennung, interne Notizen und automatische Regeln sorgen für klare Prozesse. Über N8N-Webhooks werden Kontaktformulare, E-Mails und Chat-Anfragen automatisch zu Tickets. Die KI kategorisiert, priorisiert und liefert Antwortvorschläge -- dein Team gibt nur noch frei."
---
