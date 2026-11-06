[English](Run-and-Test) · [Dansk](Run-and-Test-da) · **Bahasa Melayu**

# Jalankan dan uji

## Cipta dan gunakan `.venv`

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[test]"
```

Aktifkan persekitaran dahulu: `.venv\Scripts\Activate.ps1` pada Windows (PowerShell) atau `source .venv/bin/activate` pada Linux dan macOS. Keluar dengan `deactivate`.

## Jalankan permainan

```bash
python server.py
```

Buka `http://127.0.0.1:5000/` dan kemudian tekaan seperti `http://127.0.0.1:5000/3`.

## Jalankan ujian

```bash
python -m pytest
```

## Apa yang kami perolehi

- Persediaan yang boleh diulang dan tidak menyentuh Python global.
- Satu arahan untuk memulakan laman dan satu lagi untuk membuktikan ia berfungsi.
