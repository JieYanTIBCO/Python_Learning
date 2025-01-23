import re
import pytest


def regular_express_test(pattern: str, input_str: str):
    pass


    # Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"^The", txt)
print(x.span())  # type: ignore
print(x.string)  # type: ignore
print(x.group())  # type: ignore
print(x)


result = re.fullmatch(r"\d{3}-\d{2}-\d{4}", "123-45-6789")
print(result.group())  # type: ignore # 输出: 123-45-6789

result = re.fullmatch(r"\d{3}-\d{2}-\d{4}", "123-45-6789")
print(result)  # 输出: None
