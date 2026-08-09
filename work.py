import socket
import argparse
import threading
import concurrent.futures
import json
import time

host = "37.99.26.101"
port = 80
testhost = "https://github.com/Dimeisi/Port-Scanner"

# First version scan port
def scan_port(host, port):
    pass

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

print(scan_port(host, port))