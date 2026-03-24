#!/usr/bin/env zsh
# Build the program hub (repo root) and every course book.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "==> Program hub (repo root)"
jupyter-book build --site

for d in "$ROOT"/courses/AINS-M*/; do
  code=$(basename "$d")
  echo "==> Course book: $code"
  (cd "$d" && jupyter-book build --site)
done

echo "Done. Hub: $ROOT/_build/  ·  Each course: $ROOT/courses/AINS-MXXXX/_build/"
