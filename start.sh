#!/bin/bash

# === CONFIG ===
NETWORK="192.168.0.0/16"
SCAN_DIR="scans"
REPORT_DIR="reports"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M")
XML_FILE="$SCAN_DIR/scan_$TIMESTAMP.xml"
CSV_FILE="$REPORT_DIR/inventaire_$TIMESTAMP.csv"

# === SETUP ===
mkdir -p "$SCAN_DIR"
mkdir -p "$REPORT_DIR"

# === SCAN ===
echo "[+] Lancement du scan Nmap sur $NETWORK..."
sudo nmap -A -T4 -oX "$XML_FILE" "$NETWORK"
echo "[✓] Scan terminé. Résultat : $XML_FILE"

# === PARSING ===
echo "[+] Conversion en CSV..."
python3 parse_scan.py "$XML_FILE" "$CSV_FILE"

# === FIN ===
echo "[✓] Rapport généré : $CSV_FILE"
