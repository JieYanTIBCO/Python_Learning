import math


def calculate_average(numbers: list) -> float:
    """
    Calculate the sum of the numbers in the list,
    and return the average value as a float rounded to two decimal places.

    :param numbers: List of numeric values (int or float).
    :return: Average value as a float, rounded to two decimal places.
    """
    if numbers is None or len(numbers) == 0:
        raise ValueError("The list of numbers cannot be None or empty.")

    # Check if all elements are numeric
    if not all(
        isinstance(number, (int, float)) and not math.isnan(number)
        for number in numbers
    ):
        raise ValueError(
            "All elements must be valid numbers (int or float) and not NaN."
        )

    total = sum(numbers)
    return round(total / len(numbers), 2)


# Sample usage
try:
    result = calculate_average([2, 4, 6, None])
    print("Average:", result)
except ValueError as e:
    print(f"Error: {e}")
