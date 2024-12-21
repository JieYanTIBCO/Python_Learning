import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from datetime import timezone as dt_timezone
import time


class TimezoneFormatter(logging.Formatter):
    """
    Custom formatter to include timezone-aware timestamps.
    """

    def __init__(self, fmt=None, datefmt=None):
        super().__init__(fmt, datefmt)
        self.local_timezone = datetime.now().astimezone().tzinfo

    def formatTime(self, record, datefmt=None):
        # Use record.created (UNIX timestamp) to create timezone-aware datetime
        local_dt = datetime.fromtimestamp(record.created, self.local_timezone)
        if datefmt:
            return local_dt.strftime(datefmt)
        else:
            return local_dt.isoformat()


def setup_logging(log_level=logging.DEBUG, log_file="application.log"):
    """
    Configure the logging system.
    :param log_level: The logging level, e.g., DEBUG, INFO, etc.
    :param log_file: The log file name.
    """
    try:
        # Define custom formatter with local timezone
        formatter = TimezoneFormatter(
            fmt="%(asctime)s - %(levelname)s - [%(threadName)s] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S %Z"
        )

        # Handlers
        file_handler = RotatingFileHandler(
            log_file, maxBytes=25 * 1024 * 1024, backupCount=7)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        # Configure logging
        logging.basicConfig(
            level=log_level,
            handlers=[file_handler, stream_handler]
        )

        logging.info("Logging has been successfully configured.")
    except Exception as e:
        print(f"Failed to configure logging: {e}")
        raise

# Example Usage
# if __name__ == "__main__":
#     setup_logging(log_level=logging.DEBUG)
#     logger = logging.getLogger(__name__)
#     logger.info("This is an info message.")
#     logger.warning("This is a warning message.")
#     logger.error("This is an error message.")
