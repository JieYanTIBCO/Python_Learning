import csv
from datetime import datetime, timedelta
from dateutil import parser
import json
import logging

csv_file = r"C:\Users\Jackie\Employee_export.csv"
json_file = r"C:\Users\Jackie\Employee_export1.json"

# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Set log level
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %z"
)

formats = [
    "%Y-%m-%d",
    "%m/%d/%Y",
    "%d %b %Y",
    "%Y-%m-%d %H:%M:%S",
    "%m/%d/%Y %H:%M:%S"
]


def parse_date(value):
    if value is None:  # Handle None
        return None
    for fmt in formats:
        try:
            return str(datetime.strptime(value, fmt).date())
        except ValueError:
            continue
    return None  # Return None if no format matches


with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
    for row in data:
        logging.info("Before transform datetime:"+str(row["HireDate"]))
        row["HireDate"] = parse_date(str(row["HireDate"]))
        # row["HireDate"] = datetime.strptime(str(row["HireDate"]), "%Y-%m-%d %H:%M:%S").date()
        logging.info("After transform datetime:"+str(row["HireDate"]))

with open(json_file, "w", encoding="utf-8") as jfile:
    json.dump(data, jfile, indent=4)
