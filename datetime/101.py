from datetime import datetime, timedelta

# Parse string to datetime
date_str = "2024-11-23 14:30:00"
date1 = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").weekday()
date2 = datetime.strptime("2024-11-23", "%Y-%m-%d")
print(date1)
print(type(date1))

print(date2)
print(type(date2))
