import logging
from logging.handlers import RotatingFileHandler


def setup_logging(log_level=logging.DEBUG, log_file="application.log"):
    """
    Configure the logging system.
    :param log_level: The logging level, e.g., DEBUG, INFO, etc.
    :param log_file: The log file name.
    """
    try:
        logging.basicConfig(
            level=log_level,
            format="%(asctime)s - %(levelname)s - [%(threadName)s] - %(message)s",
            handlers=[
                RotatingFileHandler(log_file, maxBytes=25 *
                                    1024 * 1024, backupCount=7),
                logging.StreamHandler()
            ]
        )
        logging.info("Logging has been successfully configured.")
    except Exception as e:
        print(f"Failed to configure logging: {e}")
        raise

# if __name__ == "__main__":
#     setup_logging(log_level=logging.DEBUG)
#     logger = logging.getLogger(__name__)
#     logger.info("This is an info message.")
#     logger.warning("This is a warning message.")
#     logger.error("This is an error message.")
