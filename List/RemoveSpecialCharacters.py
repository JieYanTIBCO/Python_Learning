import re


def RemoveSpecialCharacters1(s1: str) -> str:
    return "".join(list(s1.split(" ,~!@#$%^&*()_-=+`[]\\{\\}\\|;':")))


def RemoveSpecialCharacters2(s1: str) -> str:
    return re.sub(r'[^a-zA-Z0-9]', '', s1)


print(RemoveSpecialCharacters1(
    "sjdfo[iqwjf98317y4513ujigeipj-]90rub90w4j5pmteijv8ehv93qr    2"))
print(RemoveSpecialCharacters2(
    "sjdfo[iqwjf98317y4513ujigeipj-]90rub90w4j5pmteijv8ehv93qr    2"))
