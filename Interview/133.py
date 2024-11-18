def is_valid_ip(ipaddress: str) -> bool:
    if ipaddress:
        parts = ipaddress.split(".")

        if len(parts) != 4:
            return False

        for part in parts:
            if not part.isdigit() or (part[0] == '0' and len(part) > 1):
                return False
            num = int(part)
            if num < 0 or num > 255:
                return False

        return True

    else:
        print("ipaddress is empty!")
        return False


# Test cases
test_ips = [
    "192.168.1.1",
    "255.255.255.255",
    "0.0.0.0",
    "256.100.50.25",
    "192.168.01.1",
    "10.1.243.192",
    "10.0.243.01"  # Additional test case
]

# Print IP addresses and their validation results
for ip in test_ips:
    result = is_valid_ip(ip)
    print(f"{ip}: {result}")