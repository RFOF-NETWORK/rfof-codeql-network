# pzqqet_master_node.py
import os
import json

class PzqqetMasterNode:
    def __init__(self, repo_type):
        self.repo_type = repo_type.lower()
        self.root_dir = os.path.dirname(os.path.abspath(__file__))
        self.src_dir = os.path.join(self.root_dir, 'src')
        os.makedirs(self.src_dir, exist_ok=True)

    def deploy(self):
        print(f"[PZQQET MASTER] Starte Bereitstellung für Node-Typ: .{self.repo_type}")
        
        # Root-Konfiguration basierend auf Typ (.net, .dev oder .app)
        root_config = os.path.join(self.root_dir, f'{self.repo_type}_config.json')
        with open(root_config, 'w') as f:
            json.dump({"node": self.repo_type, "status": "ACTIVE", "prai_axiom": "PRAI"}, f, indent=4)
            
        # Src-Logik initialisieren
        src_file = os.path.join(self.src_dir, f'{self.repo_type}_ledger.json')
        with open(src_file, 'w') as f:
            json.dump([{"action": "INITIALIZE", "state": "PERPETUAL"}], f, indent=4)
            
        print(f"[PZQQET MASTER] Repository .{self.repo_type} erfolgreich synchronisiert.")

if __name__ == '__main__':
    # Beispielhafter Start (kann auf 'net', 'dev' oder 'app' gesetzt werden)
    node = PzqqetMasterNode(repo_type="net")
    node.deploy()
