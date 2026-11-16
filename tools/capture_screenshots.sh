#!/usr/bin/env bash
# Captures the lecture screenshots in a Docker container (Linux, headless
# Chromium), never on the host desktop. Run from the project root:
#   bash tools/capture_screenshots.sh
# The PNG files are written to docs/screenshots/ through the mounted folder.
set -euo pipefail

IMAGE="mcr.microsoft.com/playwright/python:v1.49.1-noble"

MSYS_NO_PATHCONV=1 docker run --rm \
  -v "$PWD:/work" -w /work \
  -e PYTHONPATH=/work/src \
  "$IMAGE" \
  bash -c "python -m pip install --quiet --root-user-action=ignore flask playwright==1.49.1 && python tools/capture_screenshots.py docs/screenshots"
