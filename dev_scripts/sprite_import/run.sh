#!/usr/bin/env bash
# Runs import_sprites.py in its own venv (created on first use). Usage: see import_sprites.py --help
#   ./run.sh fetch <name> [dofus] ...  fetches the artworks from Dofus first (see fetch_dofus.py --help)
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
if [ ! -x "$DIR/.venv/bin/python" ]; then
  python3 -m venv "$DIR/.venv"
  "$DIR/.venv/bin/pip" install -q -r "$DIR/requirements.txt"
fi
if [ "$1" = "fetch" ]; then
  shift
  exec "$DIR/.venv/bin/python" "$DIR/fetch_dofus.py" "$@"
fi
exec "$DIR/.venv/bin/python" "$DIR/import_sprites.py" "$@"
