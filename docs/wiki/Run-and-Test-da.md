[English](Run-and-Test) · **Dansk** · [Bahasa Melayu](Run-and-Test-ms)

# Kør og test

## Opret og brug `.venv`

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Aktivér først miljøet: `.venv\Scripts\Activate.ps1` på Windows (PowerShell) eller `source .venv/bin/activate` på Linux og macOS. Forlad det med `deactivate`.

## Kør spillet

```bash
python server.py
```

Åbn `http://127.0.0.1:5000/` og derefter et gæt som `http://127.0.0.1:5000/3`.

## Kør testene

```bash
python -m pytest
```

## Det lærte vi

- En gentagelig opsætning, der ikke rører den globale Python.
- Én kommando til at starte sitet og én til at bevise, at det virker.
