import sys, xml.etree.ElementTree as ET, requests, os

def parse_nmap(xml_file):
    hosts = {}
    tree = ET.parse(xml_file)
    for host in tree.findall('host'):
        addr = host.find('address').get('addr')
        ports = []
        for port in host.findall('ports/port'):
            if port.find('state').get('state') == 'open':
                ports.append(port.get('portid')+"/"+port.get('protocol'))
        hosts[addr] = ports
    return hosts

def send_telegram(msg):
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    chat = os.getenv('TELEGRAM_CHAT_ID')
    requests.post(f"https://api.telegram.org/bot{token}/sendMessage", json={'chat_id': chat, 'text': msg})

if __name__ == '__main__':
    current = parse_nmap(sys.argv[2])
    previous = parse_nmap(sys.argv[4])
    for ip, ports in current.items():
        if ip not in previous:
            send_telegram(f"🚨 New device: {ip} with ports {ports}")
        else:
            new_ports = set(ports) - set(previous[ip])
            if new_ports:
                send_telegram(f"⚠️ {ip} opened new ports: {new_ports}")