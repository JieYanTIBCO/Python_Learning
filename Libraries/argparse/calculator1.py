import argparse


def calculator(number1: float, operator: str, number2: float):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Error: Division by zero",
        "//": lambda x, y: x // y if y != 0 else "Error: Division by zero",
        "%": lambda x, y: x % y if y != 0 else "Error: Division by zero",
        "**": lambda x, y: x ** y,  # Power
    }
    operation = operations.get(operator)
    if operation:
        return operation(number1, number2)
    else:
        return "Error: Unsupported operator"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A calculator script that performs operations on two numbers.\n"
                    "Supported operators:\n"
                    "  +  : Addition\n"
                    "  -  : Subtraction\n"
                    "  *  : Multiplication\n"
                    "  /  : Division\n"
                    "  // : Integer Division\n"
                    "  %  : Modulus (Remainder)\n"
                    "  ** : Exponentiation (Power)",
        formatter_class=argparse.RawTextHelpFormatter  # Ensures newlines are preserved
    )

    parser.add_argument("number1", type=float,
                        help="The first number (e.g., 10)")
    parser.add_argument("operator", type=str,
                        help="The operator (+, -, *, /, //, %%, **)")
    parser.add_argument("number2", type=float,
                        help="The second number (e.g., 20)")

    args = parser.parse_args()

    try:


    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
