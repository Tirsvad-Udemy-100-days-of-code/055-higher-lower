**English** · [Dansk](Run-and-Test-da) · [Bahasa Melayu](Run-and-Test-ms)

# Run and test

## Create and use `.venv`

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Activate the environment first: `.venv\Scripts\Activate.ps1` on Windows (PowerShell) or `source .venv/bin/activate` on Linux and macOS. Leave it with `deactivate`.

## Run the game

```bash
python server.py
```

Open `http://127.0.0.1:5000/` and then a guess such as `http://127.0.0.1:5000/3`.

## Run the tests

```bash
python -m pytest
```

## What we gained

- A repeatable setup that does not touch the global Python.
- One command to start the site and one to prove it works.
