import pytest
from typing import Tuple
from collections import Counter

# Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


def count_case(sentence: str) -> Tuple[int, int]:
    """
    Count the number of uppercase and lowercase letters in a sentence.

    Args:
        sentence: Input string to analyze

    Returns:
        Tuple containing (uppercase_count, lowercase_count)

    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")

    counts = Counter(sentence)
    upper_count = sum(1 for c in sentence if c.isupper())
    lower_count = sum(1 for c in sentence if c.islower())

    return upper_count, lower_count


def test_count_case():
    assert count_case("Hello World!") == (2, 8)
    assert count_case("") == (0, 0)
    assert count_case("ABC123abc") == (3, 3)
    assert count_case("!@#$%^") == (0, 0)


def test_invalid_input():
    with pytest.raises(TypeError):
        count_case(None)
    with pytest.raises(TypeError):
        count_case(123)


def test_special_cases():
    assert count_case("     ") == (0, 0)
    assert count_case("HELLO") == (5, 0)
    assert count_case("hello") == (0, 5)


def main() -> None:
    try:
        sentence = input("Enter a sentence: ").strip()
        upper, lower = count_case(sentence)
        print(f"UPPER CASE {upper}")
        print(f"LOWER CASE {lower}")
    except (EOFError, KeyboardInterrupt):
        print("\nProgram terminated.")


if __name__ == "__main__":
    main()
    test_count_case()
    test_invalid_input()
    test_special_cases()
