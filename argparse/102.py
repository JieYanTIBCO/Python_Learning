import argparse
from faker import Faker
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
                RotatingFileHandler(log_file, maxBytes=25 * 1024 * 1024, backupCount=7),
                logging.StreamHandler(),
            ],
        )
        logging.info("Logging has been successfully configured.")
    except Exception as e:
        print(f"Failed to configure logging: {e}")
        raise


fake = Faker()


def name_address_population(n):
    lst = []
    for i in range(0, n):
        lst.append({"name": fake.name(), "address": fake.address()})
    return lst


if __name__ == "__main__":
    setup_logging(log_level=logging.DEBUG)

    parser = argparse.ArgumentParser(
        description="This is command to print fake name with address dictionary!"
    )

    parser.add_argument("-n", "--number", type=int, help="the number of name")
    parser.add_argument("-v", "--verbose", action="store_true", help="是否打印详细信息")
    # parse parameters with -n and -v
    args = parser.parse_args()

    lst_dict = name_address_population(args.number)

    logging.info(f"-n is: {args.number}")

    if args.verbose:
        logging.debug("\n".join(str(d) for d in lst_dict))
