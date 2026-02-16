---
title: "Newsletter-Autopilot"
description: "Newsletter ohne Mailchimp-Kosten: KI-generierte Inhalte, auf Wunsch self-hosted, volle Datenkontrolle. DSGVO-konform ab 0 EUR/Monat."
icon: "send"
techStack:
  - "Listmonk (self-hosted, Go + PostgreSQL)"
  - "Resend SMTP"
  - "Reacher (E-Mail-Validierung)"
benefits:
  - "Keine monatlichen Abo-Kosten für Newsletter-Tools"
  - "Volle Datenkontrolle auf eigener Infrastruktur"
  - "DSGVO-konform ohne Drittanbieter-Abhängigkeit"
  - "Professionelle Analytics und Bounce-Management"
  - "E-Mail-Validierung vor dem Versand"
useCases:
  - "Kunden-Newsletter regelmäßig versenden"
  - "Produkt-Updates und Neuheiten kommunizieren"
  - "Event-Einladungen an Zielgruppen"
  - "Bestandskunden-Aktivierung"
order: 13
relatedModules:
  - "social-media"
  - "lead-qualifizierung"
  - "buchungsmodul"
faq:
  - question: "Was kostet das Newsletter-System im Betrieb?"
    answer: "Die Software (Listmonk) ist kostenlos. Kosten fallen nur für den E-Mail-Versand über Resend an: 3.000 Mails pro Monat sind gratis, danach ab 1 USD pro 1.000 Mails. Bei 5.000 Abonnenten und einem Newsletter pro Woche sind das unter 20 USD im Monat."
  - question: "Kann ich meine bestehenden Kontakte importieren?"
    answer: "Ja. CSV-Import mit beliebigen Feldern. Vor dem Import validiert Reacher alle E-Mail-Adressen -- ungültige und riskante Adressen werden aussortiert, damit deine Absender-Reputation geschützt bleibt."
  - question: "Ist das DSGVO-konform?"
    answer: "Ja. Die Daten liegen auf deinem eigenen Server in Deutschland. Kein Transfer an US-Dienste. Double-Opt-In, Abmeldelink und Impressum werden automatisch in jede Mail integriert."
  - question: "Kann ich verschiedene Newsletter für verschiedene Zielgruppen versenden?"
    answer: "Ja. Listmonk unterstützt beliebig viele Listen und Segmente. Du kannst nach Branche, Interesse, Kaufhistorie oder jedem anderen Kriterium segmentieren."
---

Professionelle Newsletter versenden ohne Mailchimp, Brevo oder CleverReach -- und ohne monatliche Abo-Kosten, die mit jeder neuen Adresse steigen. Das Newsletter-System basiert auf Listmonk und Resend: Open Source, self-hosted, DSGVO-konform. Du zahlst nur für tatsächlich versendete E-Mails.

## Das Problem

70 % der KMU versenden ihre Newsletter unregelmäßig oder gar nicht. Der Grund ist fast nie fehlende Inhalte -- es ist der Aufwand. Mailchimp-Abo verwalten, Templates bauen, Listen pflegen, Bounces bearbeiten, DSGVO-Abmahnungen vermeiden. Und dann die Kosten: Bei 5.000 Kontakten zahlst du bei Mailchimp 75 USD pro Monat. Bei 10.000 Kontakten sind es 115 USD. Für ein Tool, das du einmal pro Woche nutzt.

Dazu kommt die Abhängigkeit: Deine Kontaktliste liegt bei einem US-Unternehmen. Preiserhöhung? Schluck und zahl. Account gesperrt? Viel Spaß beim Export. DSGVO-Audit? Viel Spaß bei der Erklärung, warum deine Kundendaten auf US-Servern liegen.

## So funktioniert's

Das Newsletter-System besteht aus drei Komponenten:

**Listmonk** ist die Newsletter-Plattform. Open Source, geschrieben in Go, extrem schnell und ressourcensparsam. Sie läuft auf deinem eigenen Server und bietet alles, was du brauchst: Kampagnen erstellen, Templates verwalten, Listen segmentieren, Abonnenten pflegen, Analytics auswerten. Die Oberfläche ist schlank und intuitiv -- kein Vergleich zu den überladenen Interfaces der kommerziellen Anbieter.

**Resend** ist der SMTP-Provider, der die Mails zuverlässig zustellt. Gute Zustellraten, faire Preise, einfache Anbindung. 3.000 Mails pro Monat sind im Free Tier inklusive. Für die meisten KMU reicht das für den Anfang. Bei Wachstum skaliert der Preis moderat: 1 USD pro 1.000 Mails.

**Reacher** validiert deine E-Mail-Adressen vor dem Versand. Syntax-Check, DNS-Lookup, SMTP-Verification -- in drei Schritten wird geprüft, ob eine Adresse existiert und erreichbar ist. Das schützt deine Absender-Reputation und verhindert, dass du an tote Adressen versendest. Auch Reacher ist self-hosted -- keine Daten an Dritte.

Der typische Ablauf: Du schreibst deinen Newsletter in Listmonk (oder lässt die KI einen Entwurf erstellen), wählst die Zielgruppe, planst den Versand und klickst "Senden". Listmonk übergibt an Resend, Resend stellt zu. Danach siehst du in Listmonk: Öffnungsrate, Klickrate, Bounces, Abmeldungen. Alles auf deinem Server, alles unter deiner Kontrolle.

## Für wen?

- **Handwerksbetriebe**: Saisonale Angebote, Tipps zur Pflege oder Wartung, Projektvorstellungen -- ein monatlicher Newsletter hält dich bei Bestandskunden in Erinnerung. Mit dem [Buchungsmodul](/module/buchungsmodul) lässt sich direkt ein Terminlink einbauen.
- **Dienstleister und Berater**: Expertise zeigen durch regelmäßige Fachbeiträge. Wer monatlich wertvollen Content liefert, wird als Experte wahrgenommen -- und bekommt die Anfragen, wenn der Bedarf da ist. Ein IT-Dienstleister, der monatlich über Sicherheitstipps schreibt, positioniert sich als vertrauenswürdiger Ansprechpartner.
- **Handel und E-Commerce**: Produktneuheiten, Rabattaktionen, Restposten -- direkt in den Posteingang deiner Kunden. Keine Algorithmus-Abhängigkeit wie bei Social Media. Du erreichst deine Zielgruppe direkt.

## Kombiniert mit

Das Newsletter-System wird in Kombination mit anderen Modulen zum echten Marketing-Kanal. Zusammen mit dem [Social Media Autopilot](/module/social-media) entsteht ein Content-Kreislauf: Newsletter-Themen werden zu Social-Media-Posts, gut performende Posts werden zum Newsletter-Inhalt. Einmal erstellen, überall verwenden.

Die [Lead-Qualifizierung](/module/lead-qualifizierung) liefert neue Abonnenten automatisch: Kalte Leads, die noch nicht kaufbereit sind, landen im Newsletter-Funnel und werden mit relevanten Inhalten aufgewärmt. Wenn sie bereit sind, kennen sie dich bereits.

Und das [Buchungsmodul](/module/buchungsmodul) macht Newsletter messbar: Ein Terminbuchungs-Link direkt im Newsletter zeigt, welche Themen wirklich Interesse wecken -- und generiert direkt Gespräche.

Du brauchst erst mal eine professionelle Website mit Newsletter-Anmeldeformular? Schau dir unsere [Webseiten-Pakete](/webseiten) an -- das Anmeldeformular ist in jedem Paket enthalten.

## Was kostet das Newsletter-System im Betrieb?

Die Software (Listmonk) ist kostenlos -- Open Source, keine Lizenzgebühren. Kosten fallen nur für den E-Mail-Versand über Resend an: 3.000 Mails pro Monat sind gratis, danach ab 1 USD pro 1.000 Mails. Rechenbeispiel: Bei 5.000 Abonnenten und einem Newsletter pro Woche (20.000 Mails/Monat) zahlst du ca. 17 USD. Bei Mailchimp wären das 75 USD -- jeden Monat, auch wenn du keinen Newsletter versendest.

## Kann ich meine bestehenden Kontakte importieren?

Ja. Listmonk unterstützt CSV-Import mit beliebigen Feldern -- Name, E-Mail, Firma, Branche, was auch immer du hast. Vor dem Import validiert Reacher alle Adressen automatisch. Ungültige, nicht erreichbare und riskante Adressen werden aussortiert. So startest du mit einer sauberen Liste und schützt deine Absender-Reputation von Tag eins.

## Ist das DSGVO-konform?

Ja. Alle Daten liegen auf deinem eigenen Server in Deutschland (oder einem EU-Standort deiner Wahl). Kein Transfer an US-Dienste. Double-Opt-In für neue Abonnenten, Abmeldelink in jeder Mail, Impressum automatisch eingefügt -- Listmonk macht das alles out of the box. Bei einem DSGVO-Audit kannst du exakt nachweisen, wo die Daten liegen und wer Zugriff hat.

## Kann ich verschiedene Newsletter für verschiedene Zielgruppen versenden?

Ja. Listmonk unterstützt beliebig viele Listen und Segmente. Du kannst nach Branche, Interesse, Kaufhistorie, Region oder jedem anderen Kriterium segmentieren. Ein Handwerksbetrieb bekommt andere Inhalte als ein E-Commerce-Unternehmen. Personalisierung funktioniert über Template-Variablen: "Hallo {{Vorname}}" ist nur der Anfang. Du kannst auch Inhaltsblöcke dynamisch ein- und ausblenden, basierend auf den Attributen deiner Abonnenten. So bekommt jeder Empfänger genau die Inhalte, die für ihn relevant sind.

Klingt interessant? [Lass uns in 20 Minuten besprechen](/kontakt), wie das Newsletter-System für dein Unternehmen aussehen könnte.
