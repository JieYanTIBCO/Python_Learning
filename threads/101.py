import logging
from logging.handlers import RotatingFileHandler
from concurrent.futures import ProcessPoolExecutor


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


def calculate(n):
    return 2*n


if __name__ == "__main__":
    setup_logging(log_level=logging.INFO)
    logger = logging.getLogger(__name__)
    logging.info("test it out")
    number = 10
    WORKERS = 4

    with ProcessPoolExecutor(max_workers=WORKERS) as executor:
        results = executor.map(calculate, range(1, number+1))

    # Log results
    for i, result in enumerate(results, start=1):
        logging.info(f"2**{i} = {result}")
