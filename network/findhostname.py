import os
import socket

# Get ARP table
arp_output = os.popen("arp -a").readlines()


for line in arp_output:
    print(line)
    if "(" in line:  # Extract lines with IP
        ip = line.split("(")[1].split(")")[0]
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Hostname not found"
        print(f"IP: {ip}, Hostname: {hostname}")
