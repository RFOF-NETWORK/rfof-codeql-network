# -*- coding: utf-8 -*-
"""
RFOF-NETWORK QuellCode - Verknüpfung zum externen Python-Repo
"""

import sys
import os

# Fügt den temporär geklonten Monolithen zum Python-Suchpfad hinzu
monolith_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'external-monolith'))
if os.path.exists(monolith_path):
    sys.path.insert(0, monolith_path)

# Direkter Import der Logik aus dem Python-Repo
try:
    from app_silent import *
    from dev_system import *
    from net_krypto import *
    print("[RFOF-NETWORK] Python-Monolith erfolgreich via CodeQL-Brücke geladen.")
except ImportError as e:
    print(f"[RFOF-NETWORK] Hinweis: Lokaler Fallback aktiv ({e})")

def run_bridge():
    print("RFOF-NETWORK CodeQL Bridge & Python Core operational.")

if __name__ == "__main__":
    run_bridge()
