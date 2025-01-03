import datetime
import pytz

# Get the current datetime with timezone
tz = pytz.timezone('America/Toronto')  # Replace with your desired timezone
now_with_tz = datetime.datetime.now(tz)

# Format the datetime with the custom format
formatted = now_with_tz.strftime("%Y-%m-%d %H:%M:%S %Z")
print(formatted)
