import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import pytz
import os


def setup_logging(log_level=logging.DEBUG, log_file="application.log"):
    """
    Configure the logging system with timezone support.
    :param log_level: The logging level, e.g., DEBUG, INFO, etc.
    :param log_file: The log file name.
    """

    class TimezoneFormatter(logging.Formatter):
        """
        Custom logging formatter to include timezone-aware timestamps.
        """

        def __init__(self, fmt=None, datefmt=None, timezone=None):
            super().__init__(fmt=fmt, datefmt=datefmt)
            self.timezone = timezone

        def formatTime(self, record, datefmt=None):
            dt = datetime.fromtimestamp(record.created, tz=self.timezone)
            if datefmt:
                return dt.strftime(datefmt)
            return dt.isoformat()

    try:
        # Get the local timezone from the operating system
        # Default to EDT (New York)
        local_tz = pytz.timezone(os.environ.get("TZ", "America/New_York"))

        # Define the log format with timezone-aware timestamps
        log_format = "%(asctime)s - %(levelname)s - [%(threadName)s] - %(message)s"

        # Set up the custom formatter
        formatter = TimezoneFormatter(fmt=log_format, timezone=local_tz)

        # Configure handlers
        file_handler = RotatingFileHandler(
            log_file, maxBytes=25 * 1024 * 1024, backupCount=7)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        # Configure the logging system
        logging.basicConfig(level=log_level, handlers=[
                            file_handler, stream_handler])

        logging.info(
            "Logging has been successfully configured with timezone support.")
    except Exception as e:
        print(f"Failed to configure logging: {e}")
        raise

# Uncomment the lines below to test the logging configuration
# if __name__ == "__main__":
#     setup_logging(log_level=logging.DEBUG)
#     logger = logging.getLogger(__name__)
#     logger.info("This is an info message.")
#     logger.warning("This is a warning message.")
#     logger.error("This is an error message.")
