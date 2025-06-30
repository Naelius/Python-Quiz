# Python-Quiz

Ein interaktives, modernes Quiz-Tool mit GUI für PowerShell, Virtualisierung, VM-Konzepte und Automatisierung. Fragen und Antworten werden aus einer JSON-Datei geladen. Das Tool eignet sich für Schulungen, Prüfungen oder Selbsttests.

## Features
- Login für Teilnehmer
- Auswahl von Kategorie und Schwierigkeitsgrad
- Zufällige Fragen pro Durchlauf (z.B. 5 pro Kategorie/SV)
- Multiple-Choice mit sofortigem Feedback
- Auswertung am Ende (Punkte, Übersicht)
- Ergebnisse werden in einer JSON-Datei gespeichert
- Moderne, strukturierte Codebasis (Separation of Concerns)
- GUI mit tkinter

## Projektstruktur
```
Python-Quiz/
│
├── data/
│   ├── quiz.json            # Fragenpool (editierbar)
│   └── user_results.json    # Ergebnisse (wird automatisch erstellt)
│
├── gui/
│   ├── login.py             # Login-Fenster
│   ├── auswahl.py           # Kategorie-/Schwierigkeitsauswahl
│   ├── quiz.py              # Quiz-Fenster
│   └── ergebnis.py          # Ergebnis-Fenster
│
├── utils.py                 # Hilfsfunktionen (Laden/Speichern)
├── main.py                  # Hauptprogramm (Startpunkt)
├── README.md                # Diese Anleitung
```

## Installation
1. Python 3.8+ installieren
2. Abhängigkeiten installieren (nur Standardbibliothek nötig)
3. Projekt klonen oder herunterladen

## Starten
```bash
python main.py
```

## Beispiel für eine Frage in `data/quiz.json`
```json
{
  "frage": "Wie listet man alle Dateien in einem Verzeichnis mit PowerShell auf?",
  "antworten": ["Get-ChildItem", "Get-File", "List-Dir", "Show-Files"],
  "richtig": 0,
  "kategorie": "PowerShell",
  "schwierigkeit": "leicht"
}
```
- Die richtige Antwort steht im Feld `richtig` (Index in der Liste `antworten`).
- Kategorien: PowerShell, Virtualisierung, VM-Konzepte, Automatisierung
- Schwierigkeitsgrade: leicht, mittel, schwer

## Hinweise
- Die Datei `data/quiz.json` kann beliebig erweitert werden (mehr Fragen, neue Kategorien).
- Die Datei `data/user_results.json` enthält die Ergebnisse aller Nutzer (wird automatisch angelegt).
- Die Anzahl der Fragen pro Durchlauf ist im Code einstellbar (Standard: 5).
- Die Antworten werden bei jedem Durchlauf zufällig gemischt.

## Mitwirkende
- Initiale Entwicklung: Martin