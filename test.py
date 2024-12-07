import logging
from logging.handlers import RotatingFileHandler


# Logging Configuration
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[RotatingFileHandler('loggingtest.log', maxBytes=5 * 1024 * 1024, backupCount=3),  # 5 MB per file, keep 3 backups
                              logging.StreamHandler()  # Log to the console
                              ])
logger = logging.getLogger(__name__)


# Log messages at different levels
logging.debug("This is a DEBUG message for detailed diagnostic information.")
logging.info("This is an INFO message for general information.")
logging.warning("This is a WARNING message for potential issues.")
logging.error("This is an ERROR message for serious issues.")
logging.critical("This is a CRITICAL message for severe errors.")
