# Automated Daily Subnet Scanner || Nmap + Telegram Alerts

**What it does**: Scheduled Nmap full‑port scan of your /24 subnet, compares with baseline, sends Telegram alert on new devices or open ports.

## Components
- `nmap_scanner.sh` – runs Nmap, saves XML
- `compare_scans.py` – diff logic
- `telegram_alert.py` – sends alerts
- Cron job (hourly)

## Example alert
New device: 192.168.1.105
Open ports: 22/tcp, 8080/tcp
