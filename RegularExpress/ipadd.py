import re

# Your provided regex (corrected for Python compatibility)
# pattern = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])){3}"
pattern = r"((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
# Test cases
test_cases = [
    "192.168.1.1",   # Valid
    "10.0.0.255",    # Valid
    "255.255.255.255", # Valid
    "256.256.256.256", # Invalid
    "192.168.1",     # Invalid
    "192.168.01.1",  # Invalid (leading zeros)
    "127.0.0.1",     # Valid
    "0.0.0.0",       # Valid
    "1.1.1",         # Invalid
    "192.168.1.999", # Invalid (out of range)
]

# Run tests
for ip in test_cases:
    if re.fullmatch(pattern, ip):
        print(f"{ip} is VALID")
    else:
        print(f"{ip} is INVALID")

