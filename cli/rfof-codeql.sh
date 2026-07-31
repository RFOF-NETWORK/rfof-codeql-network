#!/usr/bin/env bash
set -e

LANGUAGE=${1:-python}
DB_DIR=".codeql-db"

echo "[*] Erstelle CodeQL-Datenbank für Sprache: $LANGUAGE..."
codeql database create "$DB_DIR" \
  --language="$LANGUAGE" \
  --source-root="."

echo "[*] Analysiere Code mit RFOF-Sicherheits-Packs..."
codeql database analyze "$DB_DIR" \
  queries/$LANGUAGE \
  --format=sarif-latest \
  --output=codeql-results.sarif

echo "[*] Analyse abgeschlossen. Ergebnis in: codeql-results.sarif"
