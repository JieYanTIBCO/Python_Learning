numbers = [2, 4, 6, "5", (1, 2), None]

for number in numbers:
    print(f"{number}: {isinstance(number, (int, float))}")
