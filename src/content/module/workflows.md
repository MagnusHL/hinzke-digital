---
title: "Workflows & Automatisierung"
description: "Produktionsprozesse automatisieren -- von der Druckvorstufe bis zum Versand. Mit n8n und Enfocus Switch werden manuelle Abläufe zu zuverlässigen Workflows."
icon: "repeat"
techStack:
  - "N8N"
  - "Enfocus Switch"
  - "REST APIs"
  - "Webhooks"
benefits:
  - "Weniger manuelle Zwischenschritte in der Produktion"
  - "Fehlerquote sinkt durch automatische Prüfungen"
  - "Durchlaufzeiten verkürzen sich messbar"
  - "Bestehende Software wird über APIs verbunden"
  - "Skaliert mit dem Auftragsvolumen"
useCases:
  - "Druckdaten automatisch prüfen, korrigieren und weiterleiten"
  - "Auftragseingang bis Produktionsfreigabe ohne Medienbruch"
  - "Statusmails und Benachrichtigungen automatisieren"
  - "Systeme verbinden: ERP, Webshop, Vorstufe, Versand"
order: 15
relatedModules:
  - "dokumenten-ki"
  - "angebots-generator"
  - "email-assistent"
faq:
  - question: "Brauche ich Programmierkenntnisse?"
    answer: "Nein. Sowohl n8n als auch Enfocus Switch arbeiten visuell mit Drag-and-Drop. Die Workflows werden gemeinsam aufgebaut und dokumentiert, sodass dein Team sie selbst anpassen kann."
  - question: "Was ist der Unterschied zwischen n8n und Enfocus Switch?"
    answer: "Enfocus Switch ist spezialisiert auf Druckvorstufe und Medienproduktion -- Dateien prüfen, konvertieren, im Workflow weiterleiten. n8n verbindet alles drumherum: E-Mails, APIs, Datenbanken, Benachrichtigungen. Zusammen decken sie den gesamten Prozess ab."
  - question: "Funktioniert das auch ohne Enfocus Switch?"
    answer: "Ja. Wenn du keine Druckdaten verarbeitest, reicht n8n allein für die meisten Automatisierungen -- Auftragsverarbeitung, E-Mail-Workflows, API-Anbindungen. Enfocus Switch kommt nur ins Spiel, wenn Druckdaten im Prozess stecken."
  - question: "Wie lange dauert die Einrichtung?"
    answer: "Ein typischer Workflow ist in 1-2 Wochen produktiv. Komplexere Prozesse mit mehreren Systemen und Sonderfällen brauchen 3-4 Wochen. Der erste Quick Win ist oft schon nach wenigen Tagen sichtbar."
highlights:
  - icon: "printer"
    title: "Gebaut für Druckereien"
    text: "Enfocus Switch ist der Industriestandard in der Druckvorstufe. Preflight, Farbkonvertierung, Ausschießen, Dateiumbenennung -- alles automatisch, alles nachvollziehbar."
  - icon: "zap"
    title: "Alles verbunden"
    text: "n8n verbindet Webshop, ERP, E-Mail, Vorstufe und Versand zu einem durchgängigen Prozess. Kein Copy-Paste zwischen Systemen, keine vergessenen Statusmails."
  - icon: "shield"
    title: "Self-hosted, volle Kontrolle"
    text: "Beide Tools laufen auf deiner eigenen Infrastruktur. Keine Daten bei Drittanbietern, keine monatlichen Pro-User-Gebühren, keine Abhängigkeit von SaaS-Anbietern."
steps:
  - title: "Prozesse aufnehmen"
    description: "Gemeinsam identifizieren wir die zeitfressendsten manuellen Abläufe. Wo wird kopiert, wo wird gewartet, wo passieren Fehler?"
  - title: "Workflows designen"
    description: "Visuell in n8n und Enfocus Switch: Jeder Schritt wird als Baustein angelegt, getestet und dokumentiert. Du siehst genau, was passiert."
  - title: "Systeme anbinden"
    description: "Webshop, ERP, E-Mail, Dateisystem -- alles wird über APIs und Webhooks verbunden. Daten fließen automatisch dorthin, wo sie gebraucht werden."
  - title: "Live und optimieren"
    description: "Der Workflow geht in Produktion. Monitoring zeigt Durchlaufzeiten und Fehler. Nach 2-4 Wochen optimieren wir anhand der echten Daten."
problem:
  heading: "Jeden Tag dieselben Handgriffe"
  text: "In vielen Druckereien und produzierenden Betrieben sieht der Alltag gleich aus: Auftrag kommt per Mail, wird manuell ins System übertragen, Druckdaten werden von Hand geprüft, umbenannt und in den richtigen Ordner geschoben. Statusmails werden per Copy-Paste verschickt, Produktionsfreigaben per Zuruf erteilt. Jeder dieser Schritte kostet Zeit und ist fehleranfällig. Bei 50 Aufträgen am Tag summiert sich das auf Stunden -- und bei Personalwechsel geht das Wissen über den Ablauf verloren."
solution:
  heading: "Vom Auftragseingang bis zum Versand -- automatisch"
  text: "Die Kombination aus n8n und Enfocus Switch automatisiert den gesamten Prozess. Enfocus Switch übernimmt die Druckvorstufe: Dateien prüfen, konvertieren, ausschießen, umbenennen und an die Produktion übergeben -- vollautomatisch nach definierten Regeln. n8n verbindet alles drumherum: Auftragseingang aus dem Webshop, Statusbenachrichtigungen an den Kunden, Übergabe an den Versand. Jeder Schritt ist protokolliert, jeder Fehler wird sofort gemeldet. Das Ergebnis: schnellere Durchlaufzeiten, weniger Fehler und ein Prozess, der auch funktioniert, wenn jemand krank ist."
---
