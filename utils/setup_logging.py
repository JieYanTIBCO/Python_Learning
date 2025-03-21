# Standard library imports
from datetime import datetime, timezone as dt_timezone
import json
import logging
from logging.handlers import RotatingFileHandler
import os
from typing import Optional, Union


class TimezoneFormatter(logging.Formatter):
    """
    Custom formatter to include timezone-aware timestamps in log messages.

    Args:
        fmt: The format string for the log message
        datefmt: The format string for the timestamp
        timezone: Optional specific timezone to use (defaults to local)

    Example:
        formatter = TimezoneFormatter(
            fmt='%(asctime)s [%(timezone)s] %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    """

    def __init__(
        self,
        fmt: Optional[str] = None,
        datefmt: Optional[str] = None,
        timezone: Optional[dt_timezone] = None
    ) -> None:
        super().__init__(fmt, datefmt)
        self.local_timezone = timezone or datetime.now().astimezone().tzinfo

    def formatTime(self, record: logging.LogRecord, datefmt: Optional[str] = None) -> str:
        try:
            local_dt = datetime.fromtimestamp(
                record.created, self.local_timezone)
            if datefmt:
                return local_dt.strftime(datefmt)
            return local_dt.isoformat()
        except Exception as e:
            # Fallback to basic timestamp if formatting fails
            return str(record.created)

    def format(self, record: logging.LogRecord) -> str:
        # Add timezone name to log record
        record.timezone = str(self.local_timezone)
        return super().format(record)


def setup_logging(
    log_level: int = logging.DEBUG,
    log_file: Optional[str] = None,
    max_bytes: int = 25 * 1024 * 1024,  # 25MB
    backup_count: int = 7,
    console_output: bool = True,
    log_format: Optional[str] = None,
    date_format: Optional[str] = None,
    json_format: bool = False,
    indent: Optional[int] = None  # Add indent parameter
) -> logging.Logger:
    """
    Configure logging system with rotating file handler and optional console output.

    Args:
        log_level: Logging level (default: DEBUG)
        log_file: Log file path (default: application.log or application_log.json if json_format is True)
        max_bytes: Max log file size before rotation (default: 25MB)
        backup_count: Number of backup files to keep (default: 7)
        console_output: Enable console logging (default: True)
        log_format: Custom log format string (optional)
        date_format: Custom date format string (optional)
        json_format: Flag to determine if log format should be JSON (default: False)
        indent: Indentation level for JSON output (default: None)

    Returns:
        logging.Logger: Configured logger instance

    Raises:
        OSError: If log file creation fails
        ValueError: If invalid parameters provided
    """
    try:
        print(f"thread name:{__name__}")
        # Parameter validation
        if max_bytes <= 0:
            raise ValueError("max_bytes must be positive")
        if backup_count < 0:
            raise ValueError("backup_count must be non-negative")
        if indent is not None and not json_format:
            raise ValueError(
                "indent parameter is only valid when json_format is True")

        # Set default log file based on json_format
        if log_file is None:
            log_file = "application_log.json" if json_format else "application.log"

        # Create log directory if needed
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Create logger
        logger = logging.getLogger(__name__)
        logger.setLevel(log_level)

        # Clear existing handlers
        logger.handlers = []

        # Set up formatter
        if json_format:
            formatter = logging.Formatter(json.dumps({
                "time": "%(asctime)s",
                "name": "%(name)s",
                "level": "%(levelname)s",
                "thread": "%(threadName)s",
                "message": "%(message)s"
            }, indent=indent))  # Use indent parameter
        else:
            log_format = log_format or '%(asctime)s [%(levelname)s] [%(threadName)s] %(message)s'
            date_format = date_format or '%Y-%m-%d %H:%M:%S %z'
            formatter = logging.Formatter(log_format, date_format)

        # Set up file handler
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Set up console handler if requested
        if console_output:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

        # Calculate max size in MB for display
        max_size_mb = max_bytes / (1024 * 1024)

        # Get processID for display during initialization
        processID = os.getpid()
        # print(f"processID: {processID}")

        # Log configuration details
        logger.info(f"""
===============================
    Logging Configuration
===============================
Level        : {logging.getLevelName(log_level)}
Log File     : {file_handler.baseFilename}
Max File Size: {max_size_mb:.2f} MB
Backup Count : {backup_count}
Console Out  : {console_output}
Timezone     : {datetime.now().astimezone().tzinfo}
ProcessID    : {processID}
===============================
""")

        return logger

    except Exception as e:
        raise RuntimeError(f"Failed to setup logging: {str(e)}") from e


def get_logger(name=__name__, log_level=logging.DEBUG, log_file=None, max_bytes=25 * 1024 * 1024, backup_count=7, json_format=False, indent=None):
    """
    Simplified function to set up logging and return a logger instance.
    :param name: Name of the logger.
    :param log_level: Logging level.
    :param log_file: Log file name.
    :param max_bytes: Max size of log file before rotation.
    :param backup_count: Number of rotated backups to keep.
    :param json_format: Flag to determine if log format should be JSON.
    :param indent: Indentation level for JSON output.
    :return: Configured logger instance.
    """
    return setup_logging(log_level=log_level, log_file=log_file,
                         max_bytes=max_bytes, backup_count=backup_count, json_format=json_format, indent=indent)


# Example Usage
if __name__ == "__main__":
    try:
        # logger = get_logger(json_format=True, indent=4)
        logger = get_logger()
        logger.info("This is an info message.")
        logger.warning("This is a warning message.")
        logger = get_logger(json_format=True)
        logger.error("This is an error message.")
        logger = get_logger(json_format=True, indent=4)
        logger.critical("This is a critical message.")
    except Exception as e:
        print(f"Error: {str(e)}")
        raise
