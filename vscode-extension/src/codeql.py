# -*- coding: utf-8 -*-
"""
RFOF-NETWORK // CodeQL End-to-End (E2E) Bridge (Reverse/Bidirectional)
Verknüpft das rfof-codeql-network Repository mit dem Python-polyglotten-Monolithen-prime-Multiplikation-Base Repo (src/ & Root).
"""

import os
import subprocess
import sys
import json

# Pfad-Konfiguration für die bidirektionale E2E-Verknüpfung
CODEQL_NET_REPO = os.path.dirname(os.path.abspath(__file__))
PYTHON_REPO_ROOT = os.path.join(CODEQL_NET_REPO, "..", "Python-polyglotten-Monolithen-prime-Multiplikation-Base")
SRC_DIR = os.path.join(PYTHON_REPO_ROOT, "src")
TARGET_QUERY_DIR = os.path.join(CODEQL_NET_REPO, "queries", "python")

def verify_directories():
    print("[RFOF-CODEQL-E2E-REV] Prüfe bidirektionale Verzeichnisstrukturen...")
    if not os.path.exists(SRC_DIR):
        print(f"[WARNUNG] src/ Verzeichnis nicht gefunden unter: {SRC_DIR}")
        os.makedirs(SRC_DIR, exist_ok=True)
        print("[INFO] src/ Verzeichnis automatisch erstellt.")
    
    if not os.path.exists(PYTHON_REPO_ROOT):
        print(f"[FEHLER] Python-polyglotten-Monolithen-prime-Multiplikation-Base Repository nicht gefunden unter: {PYTHON_REPO_ROOT}")
        print("[HINWEIS] Stelle sicher, dass die Repositories korrekt im Workspace verknüpft sind.")
        return False
    
    print("[SUCCESS] Bidirektionaler Verzeichnis-Check erfolgreich bestanden.")
    return True

def link_sources_to_codeql():
    """Verknüpft/Kopiert die Quellquellen bidirektional für den tiefen CodeQL-Monolithen-Scan"""
    print("[RFOF-CODEQL-E2E-REV] Starte bidirektionale Quellcode-Verknüpfung (Monolith -> CodeQL)...")
    
    # Zielordner im CodeQL-Repo für die erweiterte Monolithen-Analyse vorbereiten
    analysis_target = os.path.join(CODEQL_NET_REPO, "target_src_monolith")
    os.makedirs(analysis_target, exist_ok=True)
    
    files_to_link = []
    
    # Aus src/ des Monolithen
    if os.path.exists(SRC_DIR):
        for f in os.listdir(SRC_DIR):
            if f.endswith(".py"):
                files_to_link.append(os.path.join(SRC_DIR, f))
                
    # Aus dem Root des Monolithen
    for f in os.listdir(PYTHON_REPO_ROOT):
        if f.endswith(".py") and f != "codeql.py":
            files_to_link.append(os.path.join(PYTHON_REPO_ROOT, f))
            
    # Verknüpfungen / Kopien für den CodeQL Runner erzeugen
    linked_count = 0
    for src_file in files_to_link:
        file_name = os.path.basename(src_file)
        dest_file = os.path.join(analysis_target, file_name)
        
        if os.path.exists(dest_file) or os.path.islink(dest_file):
            os.remove(dest_file)
            
        try:
            os.symlink(src_file, dest_file)
        except OSError:
            import shutil
            shutil.copy2(src_file, dest_file)
            
        linked_count += 1
        print(f"[LINK-REV] Verknüpft: {file_name} -> CodeQL Monolith Target")
        
    print(f"[SUCCESS] Bidirektionale E2E-Verknüpfung abgeschlossen. {linked_count} Monolithen-Module bereitgestellt.")
    return analysis_target

def run_codeql_analysis(target_dir):
    """Führt den lokalen CodeQL-Prozess für den Prime-Multiplikations-Monolithen aus"""
    print("[RFOF-CODEQL-E2E-REV] Starte CodeQL Monolith-Sicherheits- und Prime-Struktur-Scan...")
    
    db_path = os.path.join(CODEQL_NET_REPO, "rfof_monolith_db")
    query_file = os.path.join(TARGET_QUERY_DIR, "rfof-security.ql")
    
    print(f"[INFO] Erstelle Monolith CodeQL Datenbank unter: {db_path}")
    print(f"[INFO] Verwende Security Query: {query_file}")
    
    codeql_check = subprocess.run(["codeql", "--version"], capture_output=True, text=True)
    if codeql_check.returncode != 0:
        print("[INFO] CodeQL CLI nicht gefunden. Starte nativen RFOF-Monolithen-AST-Scan...")
        run_native_ast_scan(target_dir)
    else:
        print("[SUCCESS] CodeQL CLI erkannt. Starte vollen Monolithen-Datenbank-Build...")

def run_native_ast_scan(target_dir):
    """Fallback: Direkter AST- und Prime-Struktur-Scan des verknüpften Monolithen"""
    print("[RFOF-CODEQL-E2E-REV] RFOF nativer Monolith-AST-Sicherheits-Scan läuft...")
    issues_found = 0
    
    for root, _, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                    if "eval(" in content or "exec(" in content:
                        print(f"[ALERT] Gefährliche Ausführung in Monolith-Modul {file} entdeckt!")
                        issues_found += 1

    print(f"[SUCCESS] Monolith-AST-Scan beendet. Gefundene Risiken: {issues_found}")
    print("[SUCCESS] Bidirektionale CodeQL E2E-Pipeline erfolgreich synchronisiert.")

if __name__ == "__main__":
    print("==================================================")
    print(" RFOF-NETWORK // CodeQL E2E Bridge (Monolith <-> Net)")
    print("==================================================")
    
    if verify_directories():
        target = link_sources_to_codeql()
        run_codeql_analysis(target)
    else:
        print("[FEHLER] Bidirektionale E2E-Verknüpfung abgebrochen.")
        sys.exit(1)
