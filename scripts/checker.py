import json
import subprocess
import logging

# Настройка логирования
logging.basicConfig(filename='/var/log/server_checker.log', level=logging.INFO, format='%(asctime)s - %(message)s')

CONFIG_FILE = "config/servers.json"
BEST_SERVER_FILE = "config/best_server.txt"

def ping_server(host):
    try:
        output = subprocess.check_output(["ping", "-c", "3", host], stderr=subprocess.DEVNULL)
        logging.info(f"[+] Server {host} is reachable.")
        return True
    except subprocess.CalledProcessError:
        logging.warning(f"[-] Server {host} is unreachable.")
        return False

def load_servers():
    try:
        with open(CONFIG_FILE) as f:
            return json.load(f)["servers"]
    except Exception as e:
        logging.error(f"Error loading servers from {CONFIG_FILE}: {e}")
        raise

def save_best_server(ip):
    try:
        with open(BEST_SERVER_FILE, "w") as f:
            f.write(ip)
        logging.info(f"[+] Best server {ip} saved.")
    except Exception as e:
        logging.error(f"Error saving best server: {e}")
        raise

def main():
    servers = load_servers()
    for server in servers:
        if ping_server(server["ip"]):
            logging.info(f"[+] Server {server['ip']} is up. Selecting as best.")
            print(f"[+] Server {server['ip']} is up. Selecting as best.")
            save_best_server(server["ip"])
            return
    logging.warning("[-] No servers available!")
    print("[-] No servers available!")

if __name__ == "__main__":
    main()