# Server Failover Switcher

Автоматическое переключение между серверами на основе доступности и ping 🧠

## Структура:
- `scripts/checker.py` — пингует список серверов и выбирает лучший
- `config/servers.json` — список серверов
- `haproxy.cfg` — пример балансира

## Установка

```bash
chmod +x install.sh
./install.sh
