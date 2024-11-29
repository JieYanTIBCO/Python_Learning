import re
from datetime import datetime

LogLocation = r"C:\Build\Python_Learning\RegularExpress\test.log"
# 2024-11-24 21:45:00 - INFO - [Thread-3] - User login successful.


# Adjusted pattern and added re.MULTILINE flag
log_pattern = re.compile(
    r"(?P<Datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) - (?P<Level>[A-Z]+) - \[(?P<Thread>[\w-]+)\] - (?P<message>.+)"
)


def abc(loglocation, threshold_datetime):

    with open(LogLocation, "r", encoding="utf-8") as logfile:
        reader = logfile.readlines()  # Read the entire file as a single string
        list_matchdict = []
        for line in reader:
            match = log_pattern.match(line)
            if match:
                log_datetime = datetime.strptime(match.groupdict()["Datetime"], "%Y-%m-%d %H:%M:%S.%f")
                if log_datetime <= threshold_datetime:
                    list_matchdict.append(match.groupdict())

    return list_matchdict


threshold_datetime = datetime.strptime(
    "2024-11-24 21:45:00.456", "%Y-%m-%d %H:%M:%S.%f")

for i in abc(LogLocation,threshold_datetime):
    print(i)


