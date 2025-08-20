# Network Inventory Scanner

Cet outil permet de scanner un réseau local (192.168.0.0/16 par défaut) avec **Nmap**, de générer un fichier XML, puis de le convertir automatiquement en un rapport CSV lisible.

## 📁 Structure des dossiers

- `scans/` : contient les fichiers XML issus des scans Nmap
- `reports/` : contient les rapports CSV générés
- `start.sh` : script principal à exécuter
- `parse_scan.py` : script Python pour convertir le XML en CSV

## 🚀 Utilisation

1. Rendre le script exécutable :
   ```bash
   chmod +x start.sh
   ```

2. Lancer le scan et la génération du rapport :
   ```bash
   sudo ./start.sh
   ```

3. Le rapport CSV final se trouve dans le dossier `reports/`.

> ⚠️ Le scan `192.168.0.0/16` peut prendre du temps : ~65 000 adresses IP.  
> Tu peux modifier la variable `NETWORK` dans `start.sh` pour cibler un sous-réseau plus petit (ex : `192.168.1.0/24`).

## 🔧 Prérequis

- `nmap` installé
- `python3` installé
