import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import pytz
import os
import sys


def setup_logging(log_level=logging.DEBUG, log_file="application.log"):
    class TimezoneFormatter(logging.Formatter):
        def __init__(self, fmt=None, datefmt=None, timezone=None):
            super().__init__(fmt=fmt, datefmt=datefmt)
            self.timezone = timezone

        def formatTime(self, record, datefmt=None):
            dt = datetime.fromtimestamp(record.created, tz=self.timezone)
            if datefmt:
                return dt.strftime(datefmt)
            return dt.strftime("%Y-%m-%d %H:%M:%S %Z")

    try:
        tz_name = os.environ.get("TZ", "America/New_York")
        try:
            local_tz = pytz.timezone(tz_name)
        except pytz.UnknownTimeZoneError:
            local_tz = pytz.timezone("UTC")
            print(f"Unknown timezone '{tz_name}', defaulting to UTC.")

        log_format = "%(asctime)s - %(levelname)s - [%(threadName)s] - [%(module)s.%(funcName)s] - %(message)s"
        formatter = TimezoneFormatter(fmt=log_format, timezone=local_tz)

        max_log_size = 25 * 1024 * 1024
        backup_count = 7
        file_handler = RotatingFileHandler(
            log_file, maxBytes=max_log_size, backupCount=backup_count)
        file_handler.setFormatter(formatter)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logging.basicConfig(level=log_level, handlers=[
                            file_handler, stream_handler])

        config_details = f"""
        ============================
        Logging Configuration Details
        ============================
        Log File       : {log_file}
        Logger Level   : {logging.getLevelName(log_level)}
        Max File Size  : {max_log_size / (1024 * 1024)} MB
        Backup Count   : {backup_count}
        Timezone       : {local_tz.zone}
        ============================
        """
        print(config_details)

        logging.info("Testing logging setup...")
        logging.debug("Debug level logs are enabled.")
        logging.warning("Warning level logs are enabled.")
        logging.error("Error level logs are enabled.")

    except Exception as e:
        print(f"Failed to configure logging: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    os.environ["TZ"] = "Europe/London"
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Default timezone log entry.")

    # os.environ["TZ"] = "Europe/London"
    # setup_logging()
    # logger.info("Europe/London timezone log entry.")

    # os.environ["TZ"] = "Asia/Tokyo"
    # setup_logging()
    # logger.info("Asia/Tokyo timezone log entry.")

    # os.environ["TZ"] = "Invalid/Timezone"
    # setup_logging()
    # logger.info("Fallback to UTC timezone log entry.")
