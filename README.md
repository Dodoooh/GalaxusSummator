# GalaxusSummator

Mit diesem Skript kannst du ganz einfach den Gesamtbetrag deiner Galaxus oder Digitec Bestellungen berechnen. Es gibt zwei Versionen des Skripts: `not-grouped.py` und `grouped.py`. 

### not-grouped.py
Dieses Skript berechnet den Gesamtbetrag deiner Bestellungen und zeigt eine Liste aller Produkte mit Mengen, Gesamtpreisen und Daten, ohne die gleichnamigen Artikel zu gruppieren.

### grouped.py
Dieses Skript macht dasselbe wie `not-grouped.py`, gruppiert jedoch gleichnamige Artikel zusammen.

## Benutzung

1. Öffne die Digitec Galaxus Webseite und kopiere den gesamten Text deiner Bestellungen (Strg+A, Strg+C oder Cmd+A, Cmd+C). Unter dem Punkt `Bestellungen`
2. Füge den kopierten Text in die Datei `beträge.txt` ein.
3. Führe das gewünschte Skript aus (`not-grouped.py` oder `grouped.py`).
4. Die Skripte geben den Gesamtbetrag, die Artikelinformationen und das Datum der Bestellungen auf der Konsole aus und exportieren die Ergebnisse als CSV-Datei (`export.csv`).