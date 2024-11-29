import re

# Example plain text logs
log_content = """
2024-11-24 21:45:00 - INFO - [Thread-3] - User login successful.
2024-11-24 21:45:00 - DEBUG - [Thread-1] - Cache miss for key: user123
2024-11-24 21:45:00 - WARNING - [Thread-5] - Memory usage exceeds threshold.
2024-11-24 21:45:00 - ERROR - [Thread-2] - Request timed out.
2024-11-24 21:45:00 - CRITICAL - [Thread-3] - System reboot initiated.
"""

# Regex pattern without verbose mode
log_pattern = re.compile(
    r"(?P<Datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) - (?P<Level>[A-Z]+) - \[(?P<Thread>[\w-]+)\] - (?P<message>.+)"
)

# Normalize log content
log_content = log_content.strip()

# Match and print results
matches = log_pattern.finditer(log_content)
has_match = False
for match in matches:
    print(match.groupdict())
    has_match = True

if not has_match:
    print("No matches found. Check your log file format and regex pattern.")
