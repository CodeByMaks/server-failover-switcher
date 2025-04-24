# 🚀 Server Failover Switcher

This project continuously monitors a list of predefined servers and automatically switches to the one with the best performance (lowest latency). It is designed for real-time failover in case of network degradation or server failure.

---

## 📦 Project Structure

### `server_checker.py`
Main script responsible for:
- Loading server list from `servers.json`
- Measuring latency (ping) to each server
- Comparing latencies and determining the optimal server
- Switching to a faster server if needed
- Recording the current active server in `current_server.txt`
- Logging all actions to `/var/log/server_checker.log`

### `servers.json`
Configuration file containing a list of target server IPs or domain names:
```json
{
  "servers": [
    "8.8.8.8",
    "1.1.1.1",
    "9.9.9.9"
  ]
}
```

### `current_server.txt`
Stores the IP or hostname of the currently active server to avoid unnecessary switching.

### `/var/log/server_checker.log`
Log file containing:
- Health check results
- Failover events
- Error messages

Sample log entry:
```
[2025-04-24 12:00:00] Switched to better server: 1.1.1.1 (ping: 24ms)
```

---

## ⚙️ Installation & Usage

### 1. Install dependencies (if needed):
```bash
sudo apt update
sudo apt install python3 git
```

### 2. Clone the repository:
```bash
git clone https://github.com/CodeByMaks/server-failover-switcher.git
cd server-failover-switcher
```

### 3. Manual execution:
```bash
python3 server_checker.py
```

---

## 🔁 Automate via cron

### 1. Edit crontab:
```bash
crontab -e
```

### 2. Add a job to run every 5 minutes:
```bash
*/5 * * * * /usr/bin/python3 /path/to/server_checker.py
```
Replace `/path/to/` with the absolute path to the script.

---

## 💡 Use Case Example
This script is ideal for setups such as VPN gateways, routers, or cloud-based services that require always using the fastest and most stable connection available.

---

## 🛡 Tips
- Add only reliable and low-latency servers in `servers.json`
- Make sure the `cron` user has execution permission for Python and write access to the log file
- Adjust file permissions accordingly when logging to `/var/log`

---

Made with ❤️ for automated resilience and network stability 🙌

_Contributions and improvements are welcome. Feel free to open an Issue or submit a Pull Request!_