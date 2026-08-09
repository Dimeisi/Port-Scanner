import socket
import argparse
import threading
import concurrent.futures
import json
import time
from unittest import result
from urllib.parse import _ResultMixinStr

host = "37.99.26.101"
port = 80
ports = 22, 80, 443 # 22 - SSH, 80 - HTTP, 443 - HTTPS
testhost = "https://www.youtube.com/" #Рабочий хост для теста

# First version scan port
def scan_port(host, ports):
    pass

# Second version scan port
def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                return f"Port {port} is open on {host}"
            else:
                return f"Port {port} is closed on {host}"
    except Exception as e:
        return f"Error scanning port {port} on {host}: {e}"
    
# Working version scan ports

def scan_ports(host, ports):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(scan_port, host, port): port for port in ports}
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                results.append(f"Error scanning port {port} on {host}: {e}")
    print("Scanning ports on host:", host)
    print("Scanning ports:", ports)
    print("Port scan completed.")
    return results
print("Starting port scan...")
print("Scanning ports:", scan_ports(host, ports))
# Временно print("Scanning ports:", scan_ports(testhost, ports))
print("Port scan completed.")