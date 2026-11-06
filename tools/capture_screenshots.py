"""Capture one screenshot per lecture step with a headless browser.

@brief Runs inside the Docker container started by `tools/capture_screenshots.sh`,
so the host desktop is never used (framework/process/gui-testing.md).
Each lecture app is served on its own port; Chromium writes PNG files to the
folder given as the first argument.
"""

import logging
import sys
import threading
from collections.abc import Callable
from pathlib import Path

from flask import Flask
from playwright.sync_api import sync_playwright
from werkzeug.serving import make_server

from higher_lower.presentation.lectures import (
    step_02_url_paths,
    step_03_html,
    step_04_decorators,
    step_05_authenticated,
)
from higher_lower.presentation.web.app import create_app

SECRET_NUMBER = 5
VIEWPORT = {"width": 900, "height": 520}

## File name, application factory and URL path of every screenshot.
SHOTS: list[tuple[str, Callable[[], Flask], str]] = [
    ("lecture-1-goals.png", lambda: create_app(SECRET_NUMBER), "/"),
    ("lecture-2-url-paths.png", step_02_url_paths.create_app, "/username/Angela"),
    ("lecture-3-html.png", step_03_html.create_app, "/"),
    ("lecture-4-decorators.png", step_04_decorators.create_app, "/bye"),
    ("lecture-5-authenticated.png", step_05_authenticated.create_app, "/"),
    ("lecture-6-too-low.png", lambda: create_app(SECRET_NUMBER), "/3"),
    ("lecture-6-too-high.png", lambda: create_app(SECRET_NUMBER), "/7"),
    ("lecture-6-correct.png", lambda: create_app(SECRET_NUMBER), "/5"),
]


def main(out_dir: Path) -> int:
    """Serve each application and save its screenshot.

    @param out_dir Folder that receives the PNG files.
    @return Process exit code; 0 when every screenshot was written.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    out_dir.mkdir(parents=True, exist_ok=True)
    port = 5100
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT)
        for name, factory, path in SHOTS:
            port += 1
            server = make_server("127.0.0.1", port, factory())
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                page.goto(f"http://127.0.0.1:{port}{path}", wait_until="networkidle")
                page.screenshot(path=str(out_dir / name))
                logging.info("wrote %s", name)
            finally:
                server.shutdown()
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1] if len(sys.argv) > 1 else "docs/screenshots")))
