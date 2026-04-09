#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

if ! python3 -c "import rumps, tomlkit, webview" 2>/dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
fi

exec python3 -m codex_switcher.app
