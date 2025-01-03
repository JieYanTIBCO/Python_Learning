from setup_logging import get_logger


def vowel_count(input_str):
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for character in input_str.lower():
        if character in vowel_set:
            count += 1
    return count


logger = get_logger()
if __name__ == "__main__":
    count = vowel_count(
        "If you have subdirectories in /Users/jieyan/VScode, add an empty __init__.py file in each subdirectory. This allows Python to treat them as packages, enabling imports like")
    logger.debug(f"count is {count}")
