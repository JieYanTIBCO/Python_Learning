import logging
from logging.handlers import RotatingFileHandler
from concurrent.futures import ThreadPoolExecutor
import random
import string


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


def convert_to_upper(s: str):
    logging.info(f"{s}")
    return s.upper()


def generate_lowercase_strings(count, length):
    """
    Generate a list of random lowercase strings.
    :param count: Number of strings to generate.
    :param length: Length of each string.
    :return: List of random lowercase strings.
    """
    return [
        ''.join(random.choices(string.ascii_lowercase, k=length)) for _ in range(count)
    ]


def square_num(num):
    logging.info(f"{num}'s square = {num**2}")
    return num**2


if __name__ == "__main__":
    setup_logging(log_level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    workers = 4
    chunksize = 5  # Specify chunksize
    numbers = range(1, 21)
    # str_list = ["abd", "bcd", "aaa", "ccc", "eeee"]
    str_list = generate_lowercase_strings(count=100, length=5)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        #     futures = [executor.submit(convert_to_upper, string1)
        #                for string1 in str_list]
        # for index, s in enumerate(futures, start=1):
        #     logging.info(f"index{index} string= {s.result()}")
        # results = executor.map(convert_to_upper, str_list, chunksize=10)
        # logging.info([result for result in results])
        results = executor.map(square_num, numbers, chunksize=chunksize)

        logging.info(f"Results: {[result for result in results]}")
