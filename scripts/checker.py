import json
import subprocess
import time

CONFIG_FILE = "config/servers.json"
BEST_SERVER_FILE = "config/best_server.txt"

def ping_server(host):
    try:
        output = subprocess.check_output(["ping", "-c", "3", host], stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def load_servers():
    with open(CONFIG_FILE) as f:
        return json.load(f)["servers"]

def save_best_server(ip):
    with open(BEST_SERVER_FILE, "w") as f:
        f.write(ip)

def main():
    servers = load_servers()
    for server in servers:
        if ping_server(server["ip"]):
            print(f"[+] Server {server['ip']} is up. Selecting as best.")
            save_best_server(server["ip"])
            return
    print("[-] No servers available!")

if __name__ == "__main__":
    main()