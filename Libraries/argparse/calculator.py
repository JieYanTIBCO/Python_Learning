import argparse


def calculator(number1: int, operator: str, number2: int):
    operations = {
        "+": lambda x, y: x+y,
        "-": lambda x, y: x-y,
        "*": lambda x, y: x*y,
        "/": lambda x, y: x/y if y != 0 else "Division by zero",
        "//": lambda x, y: x//y if y != 0 else "Division by zero",
        "%": lambda x, y: x % y,
        "**": lambda x, y: x ** y,  # Power
    }
    operation = operations.get(operator)
    if operation:
        return operation(float(number1), float(number2))
    else:
        return "Unsupported operator"


parser = argparse.ArgumentParser(
    description="这是一个计算器，第一个参数和三个参数是数字，第二个参数是运算符，用空格隔开")

parser.add_argument("number1", help="The first number")  # 必须参数
parser.add_argument("operatior", help="The Operatior")  # 必须参数
parser.add_argument("number2", help="The second number")  # 必须参数
# parser.add_argument("--age", type=int, help="用户的年龄", default=18)  # 可选参数，带默认值
# parser.add_argument("--verbose", action="store_true", help="是否启用详细模式")  # 布尔开关

args = parser.parse_args()
print(f"The first Number: {args.number1}")
print(f"The operator: {args.operatior}")
print(f"The second Number: {args.number2}")

try:
    result = calculator(args.number1, args.operatior, args.number2)
except ZeroDivisionError as error:
    print(error)
else:
    print(f"{args.number1} {args.operatior} {args.number2} = {result}")
finally:
    print("Print this message anyway, this means the code has been executed!")
