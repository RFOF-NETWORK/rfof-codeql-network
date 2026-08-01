# rfof-codeql-network


```
rfof-codeql-network/
├── .github/
│   └─ workflows/
│       ├── codeql-global.yml   # Globale netzwerkspezifische CodeQL-Analysen
│       ├── codeql-strict.yml   # Strenge Sicherheits- und Syntax-Prüfungen
│       └── publish-extension.yml # Automatisierte Deployment-Pipelines
├── cli/
│   ├── codeql-cli-config.yml   # Konfiguration für den CodeQL-CLI-Runner
│   ├── rfof-codeql.sh          # Lokales Ausführungs-Skript für Scans
│   └── README.md               # Dokumentation der CLI-Befehle
├── queries/
│   ├── python/
│   │   ├── rfof-security.ql    # Spezifische Sicherheitsabfragen für Python
│   │   └── qlpack.yml          # Konfigurationspaket für Python-Queries
│   └── javascript/
│       ├── rfof-security.ql    # Sicherheitsabfragen für JavaScript-Komponenten
│       └── qlpack.yml          # Konfigurationspaket für JS-Queries
├── vscode-extension/
│   ├── package.json            # Manifest und Abhängigkeiten der Extension
│   ├── src/                    # Quellcode der VS Code Extension
│   │   ├── QuellCode.py        # Kern-Quellcode für die CodeQL-Analyse im Netzwerk
│   │   ├── codeql.V1.py           # Bidirektionale E2E-Brücke direkt im src/-Ordner
│   │   ├── pzqqet_master_node.py
│   │   ├── codeql.v2.py 
│   │   └── codeql.v3.py 
│   │
│   │
│   └── rfof.code-workspace     # Nahtlose Workspace-Entwicklungsumgebung
│
├── pzqqet_master_node.py
│
└── docs/
    └── architecture.md         # Architektur- und Sicherheitsdokumentation
```
