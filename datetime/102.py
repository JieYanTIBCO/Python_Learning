from datetime import datetime

# List of date formats to try
formats = [
    "%Y-%m-%d",
    "%m/%d/%Y",
    "%d %b %Y",
    "%Y-%m-%d %H:%M:%S",
    "%m/%d/%Y %H:%M:%S"
]

# Function to parse dates using multiple formats


def parse_date(value):
    if value is None:  # Handle None
        return None
    for fmt in formats:
        try:
            return str(datetime.strptime(value, fmt).date())
        except ValueError:
            continue
    return None  # Return None if no format matches


date_values = ["2024-11-21", "11/22/2024", "23 Nov 2024",
               None, "2002-08-14 00:00:00", "08/15/2024 15:33:00"]


# Parse the date values
parsed_dates = [parse_date(date) for date in date_values]
print(parsed_dates)

