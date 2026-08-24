import socket
import argparse
import threading
import concurrent.futures
import json
import time
from unittest import result
from urllib.parse import _ResultMixinStr

#host = "37.99.26.101"
#port = 80
#ports = 22, 80, 443 # 22 - SSH, 80 - HTTP, 443 - HTTPS

host = input("Enter host: ")
portOne = 22 #Ssh
portTwo = 80 #Http
portThree = 443 #Https
ports = [portOne, portTwo, portThree]

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
                return f"Port {port}: open"
            else:
                return f"Port {port}: closed"
    except Exception as e:
        return f"Port {port}: error ({e})"
    
# Working version scan ports

def scan_ports(host, ports):
    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda port: scan_port(host, port), ports))
    return results
print("Starting port scan...")
for result in scan_ports(host, ports):
    print(result)
# Временно print("Scanning ports:", scan_ports(testhost, ports))
print("Port scan completed.")
