import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from datetime import timezone as dt_timezone


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


def setup_logging(
    log_level=logging.DEBUG,
    log_file="application.log",
    max_bytes=25 * 1024 * 1024,
    backup_count=7
):
    """
    Configure the logging system.
    :param log_level: The logging level, e.g., DEBUG, INFO, etc.
    :param log_file: The log file name.
    :param max_bytes: Maximum size of the log file before rotation.
    :param backup_count: Number of backup log files to keep.
    """
    try:
        # Define custom formatter with local timezone
        formatter = TimezoneFormatter(
            fmt="%(asctime)s - %(levelname)s - [%(threadName)s] - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S %Z"
        )

        # Handlers
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        # Configure logging
        logging.basicConfig(
            level=log_level,
            handlers=[file_handler, stream_handler]
        )

        # Convert max_bytes to MB
        max_size_mb = max_bytes / (1024 * 1024)

        # Log configuration details
        logging.info("""
===============================
    Logging Configuration
===============================
Level        : {}
Log File     : {}
Max File Size: {:.2f} MB
Backup Count : {}
Timezone     : {}
===============================
""".format(
            logging.getLevelName(log_level),
            file_handler.baseFilename,
            max_size_mb,
            backup_count,
            datetime.now().astimezone().tzinfo
        ))

    except Exception as e:
        print(f"Failed to configure logging: {e}")
        raise


def get_logger(name=__name__, log_level=logging.DEBUG, log_file="application.log", max_bytes=25 * 1024 * 1024, backup_count=7):
    """
    Simplified function to set up logging and return a logger instance.
    :param name: Name of the logger.
    :param log_level: Logging level.
    :param log_file: Log file name.
    :param max_bytes: Max size of log file before rotation.
    :param backup_count: Number of rotated backups to keep.
    :return: Configured logger instance.
    """
    setup_logging(log_level=log_level, log_file=log_file,
                  max_bytes=max_bytes, backup_count=backup_count)
    return logging.getLogger(name)


# Example Usage
if __name__ == "__main__":
    logger = get_logger()
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
