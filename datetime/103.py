import logging
from datetime import datetime
from zoneinfo import ZoneInfo

class LocalTimezoneFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        # Use zoneinfo for Eastern Time
        eastern = ZoneInfo("America/New_York")
        local_time = datetime.fromtimestamp(record.created, tz=eastern)
        if datefmt:
            return local_time.strftime(datefmt)
        return local_time.isoformat()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %z"
)

logging.Formatter.formatTime = LocalTimezoneFormatter.formatTime

# Test logging
logging.info("This is a log message with timezone abbreviation.")
