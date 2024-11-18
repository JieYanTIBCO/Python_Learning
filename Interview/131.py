import csv
from genericpath import exists
import json
import xmltodict
import xml
from pydantic import BaseModel, ValidationError
import sys
import re
import os

filelocation = "C:\Build\SRs\\02309066\EBXLogs\\1.txt"

with open(filelocation, "r") as file:
    log_data = file.read()
    size = sys.getsizeof(log_data)
    MB_size = round(size/(1024*1024), 2)
    print(f"{MB_size}MB")


log_pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"             # Date
    r"(?P<time>\d{2}:\d{2}:\d{2},\d{3})\s+"       # Time
    r"(?P<timezone>[A-Z]+)\s+"                    # Timezone
    r"(?P<logging_level>\w+)\s+"                  # Logging level
    r"(?P<logger_name>\w+\.\w+)\s+"               # Logger name
    r"(?P<version>\d+:\d+)\s+"                    # Version
    r"\[(?P<thread>[^\]]+)\]\s+"                  # Thread
    r"(?P<message>.+)"                            # Message (initial line)
)

# List to store parsed log entries
parsed_logs = []
current_entry = None

# Process each line, handling multi-line messages
for line in log_data.splitlines():
    match = log_pattern.match(line)
    if match:
        # If there's an existing entry, add it to parsed_logs
        if current_entry:
            parsed_logs.append(current_entry)

        # Start a new log entry
        current_entry = match.groupdict()
        # Strip leading/trailing whitespace
        current_entry["message"] = current_entry["message"].strip()
    elif current_entry:
        # If line does not match the start of a new log entry, it’s part of the current message
        # Append line to message, stripping leading spaces
        current_entry["message"] += "\n" + line.strip()

# Add the last entry if it exists
if current_entry:
    parsed_logs.append(current_entry)

# Display parsed logs
for log in parsed_logs:
    log_json = json.dumps(log, indent=4)
    print(log_json)


with open("C:\Build\SRs\\02309066\EBXLogs\\2.txt", "w", encoding="utf-8") as outputfile:
    json.dump(parsed_logs, outputfile, indent=4)
    if os.path.exists("C:\Build\SRs\\02309066\EBXLogs\\2.txt"):
        print("successfully generated output json file!!")
