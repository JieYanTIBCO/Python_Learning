import random
import string
import logging
from logging.handlers import RotatingFileHandler
import setup_logging as sl


def generate_password(length, ratio=(6, 3, 1)):
    """
    Generate a random password.

    :param length: Total length of the password
    :param ratio: A tuple of three integers representing the ratio of letters, digits, and special characters
    :return: A randomly generated password string
    """
    sl.setup_logging(log_level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    if len(ratio) != 3 or any(r < 0 for r in ratio):
        raise ValueError(
            "Ratio must be a tuple of three non-negative integers.")

    total_ratio = sum(ratio)
    if total_ratio == 0:
        raise ValueError("The ratio values cannot all be zero.")

    # Calculate counts for each type based on the ratio
    num_letters = length * ratio[0] // total_ratio
    num_digits = length * ratio[1] // total_ratio
    num_specials = length - num_letters - num_digits

    # Generate characters for each category
    letters = random.choices(string.ascii_letters, k=num_letters)
    digits = random.choices(string.digits, k=num_digits)
    specials = random.choices(string.punctuation, k=num_specials)

    logger.info(f"the number of letter:{
                num_letters} and the list of letter:{''.join(letters)}")
    logger.info(f"the number of letter:{
                num_digits} and the list of letter:{''.join(digits)}")
    logger.info(f"the number of letter:{
                num_specials} and the list of letter:{''.join(specials)}")
    # Combine and shuffle
    password_chars = letters + digits + specials
    random.shuffle(password_chars)

    return ''.join(password_chars)


if __name__ == "__main__":
    sl.setup_logging(log_level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    # test_num = random.random()
    # logger.info(f"{test_num}")

    # test_dice = random.randint(1, 6)
    # logging.info(f"{test_dice}")

    # random.seed(22)
    # test_num22 = random.random()
    # logger.info(f"{test_num22}")

    # for _ in range(0, 10):
    #     test_uniform = round(random.uniform(3, 6), 2)
    #     logger.info(f"{test_uniform}")

    # Example usage
    password = generate_password(20, (0, 0, 1))
    print(password)
