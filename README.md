# Server Failover Switcher

This project automates failover between servers based on availability.

## Features
- Checks the availability of servers using ping.
- Automatically selects the best server based on ping response.
- Configurable server list.
- Integrates with HAProxy to load balance.

## Requirements
- Python 3.x
- HAProxy

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/CodeByMaks/server-failover-switcher.git
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the installer:
    ```bash
    ./install.sh
    ```

## Usage

The `server_checker.py` script can be scheduled to run every 5 minutes using `cron`:

```bash
*/5 * * * * /usr/bin/python3 /usr/local/bin/server_checker.py