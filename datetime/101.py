from datetime import datetime, timedelta

# Parse string to datetime
date_str = "2024-11-23 14:30:00"
# dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").date()
dt = datetime.strptime(date_str, "%Y-%m-%d")
print(dt)



