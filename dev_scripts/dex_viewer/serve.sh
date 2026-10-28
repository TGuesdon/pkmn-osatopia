#!/usr/bin/env bash
# Serves the repo root so the dex viewer can read the C sources directly.
# Usage: ./dev_scripts/dex_viewer/serve.sh [port]
set -e
PORT="${1:-8642}"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"

# Falls back to the next free port if the requested one is taken.
while lsof -iTCP:"$PORT" -sTCP:LISTEN >/dev/null 2>&1; do PORT=$((PORT + 1)); done

URL="http://localhost:$PORT/dev_scripts/dex_viewer/"
echo "Dex viewer: $URL  (Ctrl+C pour arrêter)"
( sleep 1 && (open "$URL" 2>/dev/null || xdg-open "$URL" 2>/dev/null || true) ) &
exec python3 -m http.server "$PORT" --bind 127.0.0.1 --directory "$ROOT"
