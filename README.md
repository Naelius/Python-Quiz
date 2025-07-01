# Python-Quiz

Ein modernes, flexibles Quiz-Tool mit grafischer Oberfläche (tkinter) für PowerShell, Virtualisierung, VM-Konzepte und Automatisierung. Das Tool eignet sich für Schulungen, Prüfungen oder Selbsttests und bietet eine intuitive Card-Style-Bedienung.

## Features
- Login für Teilnehmer
- Auswahl von Kategorie und Schwierigkeitsgrad (Card-Style)
- Zufällige Fragen pro Durchlauf (z.B. 5 pro Quiz)
- Multiple-Choice mit Card-Style-Antworten und Hover-Effekt
- Sofortiges Feedback nach jeder Antwort
- Auswertung am Ende (inkl. Kategorie & Schwierigkeitsgrad)
- Ergebnisse werden strukturiert in einer JSON-Datei gespeichert
- Moderne, strukturierte Codebasis (Separation of Concerns)
- GUI mit tkinter (klassisch, aber modernisiert)
- Einfache Erweiterbarkeit (neue Fragen, Kategorien, Schwierigkeitsgrade)

## Projektstruktur
```
Python-Quiz/
│
├── data/
│   ├── split/                  # Fragenpools nach Kategorie & Schwierigkeitsgrad
│   │   ├── powershell_leicht.json
│   │   ├── virtualisierung_mittel.json
│   │   └── ... (weitere Pools)
│   └── user_results.json       # Ergebnisse aller Nutzer (wird automatisch erstellt)
│
├── gui/
│   ├── login.py                # Login-Fenster
│   ├── auswahl.py              # Kategorie-/Schwierigkeitsauswahl (Card-Style)
│   ├── quiz.py                 # Quiz-Fenster (Card-Style für Antworten)
│   └── ergebnis.py             # Ergebnis-Fenster
│
├── main.py                     # Hauptprogramm (Startpunkt)
├── utils.py                    # Hilfsfunktionen (Laden/Speichern)
├── README.md                   # Diese Anleitung
```

## Installation
1. Python 3.8+ installieren
2. Abhängigkeiten installieren (nur Standardbibliothek nötig)
3. Projekt klonen oder herunterladen

## Starten
```bash
python main.py
```

## Beispiel für eine Frage in `data/split/powershell_leicht.json`
```json
{
  "frage": "Wie listet man alle Dateien in einem Verzeichnis mit PowerShell auf?",
  "antworten": ["List-Dir", "Show-Files", "Get-ChildItem", "Get-File"],
  "richtig": 2,
  "kategorie": "PowerShell",
  "schwierigkeit": "leicht"
}
```
- Die richtige Antwort steht im Feld `richtig` (Index in der Liste `antworten`).
- Kategorien: PowerShell, Virtualisierung, VM-Konzepte, Automatisierung
- Schwierigkeitsgrade: leicht, mittel, schwer

## Beispiel für ein Ergebnis in `data/user_results.json`
```json
{
  "benutzer": "Max",
  "kategorie": "powershell",
  "schwierigkeit": "mittel",
  "richtig": 4,
  "gesamt": 5,
  "datum": "2024-05-23 18:30:00"
}
```

## Hinweise
- Die Fragenpools liegen in `data/split/` und können beliebig erweitert werden (mehr Fragen, neue Kategorien/Schwierigkeitsgrade).
- Die Datei `data/user_results.json` enthält die Ergebnisse aller Nutzer (wird automatisch angelegt).
- Die Anzahl der Fragen pro Durchlauf ist im Code einstellbar (Standard: 5).
- Die Antworten werden bei jedem Durchlauf zufällig gemischt.
- Das Design (Farben, Schriftgrößen, Card-Style) kann in den GUI-Modulen angepasst werden.

## Mitwirkende
- Initiale Entwicklung: Martin