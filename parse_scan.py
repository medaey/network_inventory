# parse_scan.py

import xml.etree.ElementTree as ET
import csv
import sys
import os

# Lire les chemins passés en argument
if len(sys.argv) != 3:
    print("Usage: python3 parse_scan.py <input_xml> <output_csv>")
    sys.exit(1)

xml_path = sys.argv[1]
csv_path = sys.argv[2]

# Parser le XML
tree = ET.parse(xml_path)
root = tree.getroot()

with open(csv_path, 'w', newline='') as csvfile:
    fieldnames = ['ip', 'hostname', 'os', 'ports']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for host in root.findall('host'):
        status = host.find('status').attrib.get('state', '')
        if status != 'up':
            continue

        addr = host.find("address[@addrtype='ipv4']")
        ip = addr.attrib['addr'] if addr is not None else ''

        hostname = ''
        hostnames = host.find('hostnames')
        if hostnames is not None and len(hostnames) > 0:
            hn = hostnames.find('hostname')
            if hn is not None:
                hostname = hn.attrib.get('name', '')

        os_match = ''
        os_elem = host.find('os')
        if os_elem is not None:
            osmatch = os_elem.find('osmatch')
            if osmatch is not None:
                os_match = osmatch.attrib.get('name', '')

        ports = []
        ports_elem = host.find('ports')
        if ports_elem is not None:
            for port in ports_elem.findall('port'):
                state = port.find('state').attrib.get('state', '')
                if state == 'open':
                    portid = port.attrib.get('portid', '')
                    protocol = port.attrib.get('protocol', '')
                    ports.append(f"{portid}/{protocol}")

        writer.writerow({
            'ip': ip,
            'hostname': hostname,
            'os': os_match,
            'ports': ','.join(ports)
        })

print(f"[✓] Rapport exporté dans : {csv_path}")
