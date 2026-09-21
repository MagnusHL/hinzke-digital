---
title: "Beratung ohne Vertrieb: wie ein Hygiene-Beratungsangebot komplett online buchbar wird"
description: "Case Study hygiene-luebeck.de: Festpreise statt Angebote, Buchung und Bezahlung ohne Telefon, Rechnung aus dem ERP. Warum sich auch klassische Beratung digitalisieren lässt und welche Prozesse dahinter laufen."
publishedAt: 2026-09-21
tags: ["case-study", "prozesse", "digitalisierung", "kmu"]
modulbezug: "buchungsmodul"
---

**Kurzfassung:** Beratung gilt als das Gegenteil von digitalisierbar: Man telefoniert, schreibt ein Angebot, wartet auf die Zusage, vereinbart einen Termin, schreibt hinterher die Rechnung. Bei hygiene-luebeck.de läuft das anders. Der Kunde findet das Angebot, sieht Festpreise, bucht und bezahlt direkt. Termin, Bestätigung und Rechnung laufen im Hintergrund. Niemand muss vorher telefonieren, niemand schreibt ein Angebot. Das Angebot verkauft sich selbst, weil die Prozesse dahinter das zulassen.

Dieser Beitrag zeigt das Konzept: was der Kunde erlebt, was im Hintergrund passiert und welche Entscheidung das Ganze überhaupt erst möglich macht. Die technischen Eckdaten stehen auf der [Projektseite](/projekte/hygiene-luebeck-de/), die Seite selbst unter [hygiene-luebeck.de](https://hygiene-luebeck.de/).

## Die Ausgangslage

Sandra Hinzke startet als Hygienebeauftragte ein Beratungsangebot für Pflegedienste, Arztpraxen, Tattoo- und Kosmetikstudios und die Kindertagespflege. Das Problem ist typisch für jedes neue Dienstleistungsangebot:

- Es gibt noch keine Kunden und keine Empfehlungen.
- Für aktiven Vertrieb (Anrufe, Besuche, Netzwerken) fehlt die Zeit.
- Die Zielgruppe sucht erst, wenn eine Prüfung ansteht. Dann will sie sofort wissen: Was kostet das, und wann geht es los?

Der klassische Weg wäre: Website mit Kontaktformular, dann Telefonat, dann Angebot per E-Mail, dann warten. Jeder Schritt kostet Zeit auf beiden Seiten. Und jeder Schritt ist eine Stelle, an der der Kunde abspringt.

## Die eine Entscheidung, die alles möglich macht: Festpreise

Beratung lässt sich nicht digital buchen, solange jeder Auftrag individuell kalkuliert wird. Der Hebel ist deshalb kein Tool, sondern eine unternehmerische Entscheidung: **Das Angebot wird in feste Bausteine mit festen Preisen zerlegt.**

| Baustein | Preis (netto) |
|---|---|
| Prüfungs-Check: Begehung vor Ort mit Protokoll | 290 EUR |
| Prüfungsvorbereitung in 14 Tagen | 890 EUR |
| Hygiene-Patenschaft, monatlich kündbar | 99 EUR/Monat |
| Studio-Paket | 249 EUR |
| Kindertagespflege-Paket | 149 EUR |
| Alles darüber hinaus | 85 EUR/Stunde |

Anfahrt bis 25 km ist drin. Was nicht in ein Paket passt, läuft über den Stundensatz.

Erst diese Entscheidung macht den Rest möglich. Wer Festpreise hat, braucht kein Angebot. Wer kein Angebot braucht, braucht kein Telefonat davor. Wer kein Telefonat braucht, kann direkt buchen lassen.

## Was der Kunde erlebt

1. **Finden.** Der Pflegedienstleiter googelt "MD-Prüfung Hygiene Checkliste" oder fragt ChatGPT. Er landet auf einem Ratgeber oder einer Fachseite für Pflegedienste.
2. **Verstehen.** Auf jeder Seite steht der wichtigste Satz ganz oben. Danach: was das Angebot ist, was es nicht ist, was es kostet.
3. **Buchen.** Klick auf den Baustein, Bezahlung mit Karte, SEPA oder PayPal. Im Bezahlformular gibt er Einrichtung, Einsatzort und Wunschtermin an.
4. **Bestätigung.** Sofort nach der Zahlung landet er auf einer Danke-Seite. Die Zahlungsbestätigung kommt automatisch per E-Mail.
5. **Termin.** Wer erst reden will, bucht ein kostenloses Erstgespräch von 20 Minuten direkt im Kalender.
6. **Rechnung.** Kommt mit Umsatzsteuerausweis aus der Buchhaltung, nicht aus dem Zahlungsanbieter.

Kein Anruf, kein Angebot, kein Warten. Der ganze Vorgang dauert wenige Minuten und funktioniert auch abends um 22 Uhr.

## Was im Hintergrund läuft

Das Prinzip: **Jeder Schritt, der früher ein Mensch gemacht hat, wird entweder automatisiert oder weggelassen.**

| Früher | Jetzt |
|---|---|
| Anruf entgegennehmen, Bedarf klären | Fachseite je Zielgruppe beantwortet die Standardfragen, FAQ mit 17 Fragen |
| Angebot kalkulieren und schreiben | Entfällt, Festpreise stehen online |
| Auf Zusage warten, nachfassen | Entfällt, Buchung ist die Zusage |
| Termin per E-Mail hin und her | Kunde bucht selbst im Kalender, Bestätigung und Erinnerung automatisch |
| Zahlung anmahnen | Bezahlt wird vor der Leistung |
| Rechnung tippen | Rechnung wird im ERP erstellt, wie jede andere Rechnung der Firma |

Was übrig bleibt, ist die eigentliche Beratung vor Ort. Alles andere läuft ohne Zutun.

**Bezahlung:** Über Zahlungslinks von Stripe. Kein eigener Shop, kein Warenkorb, kein Kundenkonto. Jeder Baustein ist ein Link. Die Patenschaft ist ein Abo, das der Kunde selbst kündigen kann.

**Terminbuchung:** Über einen selbst gehosteten Buchungskalender (Cal.com). Der Kunde sieht freie Slots, bucht, bekommt Bestätigung und Erinnerung. Läuft auf der eigenen Infrastruktur, keine Daten bei Dritten.

**Rechnung:** Stripe kassiert nur. Die Rechnung kommt aus dem ERP, in dem auch alle anderen Rechnungen der Firma entstehen. Buchhaltung bleibt in einem System, Steuerberater sieht keinen Unterschied.

**Kontaktanfragen:** Wer trotzdem eine Frage hat, schreibt über das Formular. Die Anfrage geht ins Firmenpostfach und wird dort wie jede andere Kundenanfrage bearbeitet.

## Gefunden werden, ohne Werbung zu schalten

Ohne Vertrieb muss die Seite von selbst gefunden werden. Und zwar nicht nur bei Google, sondern auch dort, wo Leute inzwischen fragen: ChatGPT, Perplexity, Google AI Overviews.

Dafür ist die Seite so gebaut, dass Suchmaschinen und KI-Systeme sie verstehen und zitieren können:

- **Pro Zielgruppe eine eigene Seite.** Ein Pflegedienst hat andere Fragen als ein Tattoostudio. Jede Seite beantwortet die Fragen ihrer Zielgruppe, mit Quellen (RKI, Infektionsschutzgesetz, Landesverordnung).
- **Ratgeber zu den Momenten, in denen gesucht wird:** MD-Prüfung im Pflegedienst, Praxisbegehung durch das Gesundheitsamt, Hygieneplan für Studios.
- **Der wichtigste Satz steht immer oben.** Wer nur den ersten Absatz liest (oder eine KI, die ihn zitiert), hat die Antwort.
- **Preise, Leistungen und Einzugsgebiet sind maschinenlesbar hinterlegt.** Eine KI, die nach "Hygieneberatung Lübeck Kosten" gefragt wird, findet die Zahl.
- **Alle KI-Crawler dürfen rein.** Viele Seiten sperren sie aus. Hier sind sie ausdrücklich eingeladen.

## Ehrlichkeit als Teil des Angebots

Ein Punkt, der bei der Digitalisierung von Beratung gern untergeht: Ohne Vorgespräch muss die Seite selbst klären, was das Angebot nicht ist. Sonst bucht jemand etwas Falsches.

Deshalb steht auf hygiene-luebeck.de an jeder relevanten Stelle: Sandra Hinzke ist Hygienebeauftragte, keine Hygienefachkraft (das ist eine geschützte Weiterbildung). Keine Beratung für Einrichtungen, die unter die Medizinprodukte-Verordnung fallen. Kein Versprechen, dass eine Prüfung bestanden wird.

Diese Abgrenzung steht in der FAQ, auf den Fachseiten und in den maschinenlesbaren Daten. Wer bucht, weiß, was er bekommt. Das spart hinterher Diskussionen und Rückabwicklungen.

## Was das gekostet hat

- **Keine neuen Abos.** Website und Buchungskalender laufen auf dem vorhandenen Server.
- **Stripe berechnet nur pro Zahlung.** Keine Grundgebühr.
- **Umsetzung: ein Tag.** Möglich, weil auf alles verzichtet wurde, was Pflege braucht: kein Shop, kein CMS, keine Kundenkonten.

## Was das für andere Dienstleister heißt

Das Muster ist nicht auf Hygieneberatung beschränkt. Es funktioniert überall, wo drei Dinge zusammenkommen:

1. Das Angebot lässt sich in **Festpreis-Bausteine** zerlegen.
2. Die Zielgruppe **sucht online**, wenn sie Bedarf hat.
3. Der Anbieter hat **keine Zeit für Vertrieb** und will sie auch nicht haben.

Steuerberatung mit Erstcheck-Paket, Datenschutzbeauftragte, Energieberater, Handwerker mit Wartungspaketen, Coaches: gleiches Prinzip. Die Frage ist nie, ob die Technik das kann. Die Frage ist, ob man sich traut, Preise auf die Website zu schreiben.

## Das Ergebnis

Ein Beratungsangebot, das sich ohne Vertrieb verkauft: Der Kunde findet es, versteht es, bucht und bezahlt. Angebot, Telefonat und Nachfassen entfallen. Was bleibt, ist die Beratung vor Ort und die Rechnung aus dem ERP. Die Zeit, die früher im Vorlauf steckte, geht in die eigentliche Arbeit.

## Häufige Fragen

**Verkauft sich Beratung wirklich ohne Gespräch?**
Standardleistungen ja. Wer erst reden will, bucht das kostenlose Erstgespräch. Der Unterschied: Der Kunde entscheidet, ob er ein Gespräch braucht, nicht der Anbieter.

**Warum Vorkasse?**
Weil es die Zahlungsmoral vom Prozess entkoppelt. Keine Mahnungen, kein Nachfassen. Bei Festpreisen unter 1.000 EUR akzeptieren das die meisten Kunden ohne Diskussion.

**Was passiert, wenn jemand das falsche Paket bucht?**
Das Bezahlformular fragt Einrichtung, Einsatzort und Wunschtermin ab. Passt etwas nicht, ist das vor dem Termin sichtbar und wird geklärt. Die klare Abgrenzung auf der Seite sorgt dafür, dass das selten vorkommt.

**Braucht man dafür einen Online-Shop?**
Nein. Sechs Bausteine mit festem Preis brauchen keinen Warenkorb. Ein Zahlungslink pro Baustein reicht.

**Lässt sich das mit dem bestehenden ERP verbinden?**
Ja, das ist sogar der Punkt. Die Buchung ist nur der Einstieg. Rechnung, Buchhaltung und Kundenstamm bleiben dort, wo sie schon sind.
