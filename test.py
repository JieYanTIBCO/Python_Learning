import logging
import setup_logging as sl
from logging.handlers import RotatingFileHandler
from datetime import datetime
import pytz
import os
import sys

if __name__ == "__main__":
    print("\nChanging timezone to Asia/Tokyo...")
    os.environ["TZ"] = "Asia/Tokyo"
    logger = logging.getLogger(__name__)
    sl.setup_logging()
    logger.info("Asia/Tokyo timezone log entry.")
