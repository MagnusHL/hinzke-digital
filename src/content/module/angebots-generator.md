---
title: "KI-Angebotsgenerator"
description: "Aus Kundenanfragen automatisch Angebote erstellen -- KI nutzt deine Preislisten und Vorlagen. Schneller als jeder Vertrieb."
icon: "clipboard-list"
techStack:
  - "N8N"
  - "OpenAI / Claude"
  - "PDF-Templates"
  - "E-Mail-Automatisierung"
benefits:
  - "Angebote in Minuten statt Stunden"
  - "Einheitliches, professionelles Design"
  - "Preislisten-Integration für korrekte Kalkulation"
  - "Automatische Nachverfolgung offener Angebote"
  - "Weniger verlorene Aufträge durch schnelle Reaktionszeit"
useCases:
  - "Handwerker-Angebote schnell erstellen"
  - "Dienstleistungsangebote kalkulieren"
  - "Projektkalkulationen automatisieren"
  - "Angebots-Follow-up per E-Mail"
order: 10
relatedModules:
  - "buchhaltung"
  - "lead-qualifizierung"
  - "dokumenten-ki"
faq:
  - question: "Kann der Generator mit meinen bestehenden Preislisten arbeiten?"
    answer: "Ja. Deine Preislisten werden einmalig importiert und danach automatisch für die Kalkulation verwendet. Preisänderungen pflegst du an einer Stelle, und alle neuen Angebote nutzen automatisch die aktuellen Preise."
  - question: "Wie sehen die generierten Angebote aus?"
    answer: "Professionell. Das Template wird einmalig an dein Corporate Design angepasst -- Logo, Farben, Schriften, Textbausteine. Jedes Angebot sieht aus, als hätte es dein bester Mitarbeiter erstellt."
  - question: "Was passiert, wenn der Kunde nicht reagiert?"
    answer: "Der Workflow verfolgt offene Angebote automatisch nach. Nach einer konfigurierbaren Frist (z.B. 5 Tage) geht eine freundliche Erinnerung raus. Die Anzahl und Frequenz der Follow-ups bestimmst du."
  - question: "Funktioniert das auch für komplexe Angebote?"
    answer: "Der Generator eignet sich besonders für standardisierbare Angebote. Bei hochkomplexen Projekten liefert er einen soliden Entwurf, den du manuell anpasst -- immer noch schneller als bei null anzufangen."
---

Eine Kundenanfrage kommt rein, und dann passiert -- erstmal nichts. Der Vertrieb ist im Termin, die Preisliste liegt irgendwo auf dem Server, das Angebots-Template ist veraltet. Der Angebots-Generator verkürzt den Weg von der Anfrage zum versandfertigen Angebot auf Minuten statt Stunden oder Tage.

## Das Problem

Laut einer Studie von Harvard Business Review sinkt die Chance auf einen Abschluss um den Faktor 10, wenn das Angebot erst nach 24 Stunden statt innerhalb einer Stunde rausgeht. Trotzdem dauert es in den meisten KMU 2-3 Tage, bis ein Angebot beim Kunden landet. Die Gründe sind immer die gleichen: Preislisten müssen zusammengesucht werden, das Template muss angepasst werden, der Chef muss drüberschauen, und dann ist Freitagnachmittag und es wird Montag.

In der Zwischenzeit hat der Kunde bei zwei Wettbewerbern angefragt, die schneller waren. Nicht weil sie besser sind -- sondern weil sie schneller waren.

Dazu kommt die Inkonsistenz. Jeder Mitarbeiter erstellt Angebote etwas anders. Andere Formulierungen, andere Struktur, manchmal sogar andere Preise. Das wirkt unprofessionell und führt zu internen Korrekturschleifen, die noch mehr Zeit kosten. Der Chef muss jedes Angebot gegenlesen, bevor es rausgeht -- ein Flaschenhals, der den ganzen Prozess weiter verlangsamt.

## So funktioniert's

Der Angebots-Generator ist ein N8N-Workflow, der die Angebotserstellung in vier Schritten automatisiert:

**Schritt 1 -- Anfrage analysieren**: Die KI (OpenAI oder Claude) liest die Kundenanfrage -- egal ob E-Mail, Kontaktformular oder telefonische Notiz -- und identifiziert, was der Kunde braucht. Produkte, Mengen, Sonderwünsche, Liefertermine.

**Schritt 2 -- Positionen zusammenstellen**: Aus deiner hinterlegten Preisliste werden die passenden Positionen automatisch zugeordnet. Die KI erkennt auch Varianten ("das Gleiche wie letztes Mal, aber in größer") und schlägt die richtigen Positionen vor.

**Schritt 3 -- Angebot generieren**: Ein professionelles PDF wird aus deinem Template erstellt. Mit Logo, Anschreiben, Positionsliste, Gesamtpreis und AGB. Der Angebotsentwurf geht zur Freigabe an dich oder direkt raus -- je nach Konfiguration.

**Schritt 4 -- Nachverfolgung**: Offene Angebote werden automatisch getrackt. Keine Antwort nach 5 Tagen? Eine freundliche Erinnerung geht automatisch raus. Nach 14 Tagen eine zweite. Die Frequenz und Formulierung bestimmst du.

## Für wen?

- **Handwerksbetriebe**: Der Meister ist auf der Baustelle und kann nicht ans Angebot. Mit dem Generator reicht eine kurze Notiz ("Kunde Müller, 3 Fenster, Altbau, EG") und das Angebot geht raus, bevor der Meister vom Dach gestiegen ist. Kein Laptop nötig, kein Bürobesuch -- eine Sprachnachricht oder kurze E-Mail reicht als Input.
- **Dienstleister und Berater**: Projektangebote mit Stundensätzen, Paketen und optionalen Zusatzleistungen. Die KI strukturiert das Angebot so, dass der Kunde sofort versteht, was er bekommt und was es kostet.
- **Handel und Großhandel**: Anfragen mit vielen Positionen und Staffelpreisen. Der Generator kalkuliert automatisch Mengenrabatte und erstellt ein übersichtliches Angebot -- auch bei 50+ Positionen in Sekunden.

## Kombiniert mit

Der Angebots-Generator wird besonders stark in Kombination mit anderen Modulen. Die [Dokumenten-KI](/module/dokumenten-ki) erkennt eingehende Anfragen automatisch und liefert die extrahierten Daten direkt an den Generator -- so startet die Angebotserstellung, bevor du die Anfrage überhaupt gelesen hast.

Mit dem [Buchhaltungsmodul](/module/buchhaltung) schließt sich der Kreis: Wird ein Angebot angenommen, fließen die Daten direkt in die Rechnungsstellung. Gleiche Positionen, gleiche Preise, kein erneutes Abtippen.

Und die [Lead-Qualifizierung](/module/lead-qualifizierung) priorisiert eingehende Anfragen vor der Angebotserstellung. Heiße Leads bekommen ihr Angebot in Minuten, weniger dringende Anfragen werden automatisch beantwortet und für später eingetaktet.

Du brauchst erst mal eine professionelle Website, über die Anfragen reinkommen? Schau dir unsere [Webseiten-Pakete](/webseiten) an -- der Angebots-Generator lässt sich nahtlos anbinden.

## Kann der Generator mit meinen bestehenden Preislisten arbeiten?

Ja. Deine Preislisten werden einmalig importiert -- aus Excel, CSV oder direkt aus deinem ERP. Danach werden sie automatisch für die Kalkulation verwendet. Preisänderungen pflegst du an einer Stelle, und alle neuen Angebote nutzen automatisch die aktuellen Preise. Keine veralteten Zahlen mehr in Angeboten.

## Wie sehen die generierten Angebote aus?

Professionell und einheitlich. Das Template wird einmalig an dein Corporate Design angepasst -- Logo, Farben, Schriften, Textbausteine. Jedes Angebot sieht aus, als hätte es dein bester Mitarbeiter erstellt. Egal ob es der Chef macht oder der Azubi -- die Qualität ist identisch.

## Was passiert, wenn der Kunde nicht reagiert?

Der Workflow verfolgt offene Angebote automatisch nach. Nach einer konfigurierbaren Frist geht eine freundliche Erinnerung raus. Die Formulierung ist professionell und nicht aufdringlich -- keine "Haben Sie unser Angebot erhalten?"-Mails, sondern echte Follow-ups mit Mehrwert. Die Anzahl und Frequenz der Nachfassmails bestimmst du selbst.

## Funktioniert das auch für komplexe Angebote?

Der Generator eignet sich besonders für standardisierbare Angebote mit bekannten Positionen und Preisen. Bei hochkomplexen Projekten -- Sonderanfertigungen, individuelle Kalkulation, mehrstufige Verhandlungen -- liefert er einen soliden Entwurf als Basis. Den passt du dann manuell an. Das ist immer noch deutlich schneller als bei null anzufangen, weil Kundendaten, Positionen und Formatierung bereits stehen. Die manuelle Anpassung beschränkt sich auf die individuelle Kalkulation.

Klingt interessant? [Lass uns in 20 Minuten besprechen](/kontakt), wie der Angebots-Generator bei dir im Vertrieb aussehen könnte.
