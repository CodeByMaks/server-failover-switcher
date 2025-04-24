#!/bin/bash

echo "[*] Installing HAProxy..."
sudo apt update && sudo apt install -y haproxy

echo "[*] Creating service for checker..."
sudo cp scripts/checker.py /usr/local/bin/server_checker.py
sudo chmod +x /usr/local/bin/server_checker.py

echo "[*] Done! Add to crontab or systemd to run periodically."