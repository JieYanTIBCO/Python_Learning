from curses.ascii import isdigit
import random


def compare(random_num: int, number: int):
    if random_num == number:
        print(f"number :{number} is correct answer!")
        return 1
    elif random_num > number:
        print(f"number :{number} is less than answer!")
        return 0
    else:
        print(f"number :{number} is great than answer!")
        return 0


random_num = random.randint(0, 100)
input_num = input("Please input a int 0-100:")
if not input_num.isdigit() or int(input_num) > 100 or int(input_num) < 0:
    print(f"this {input_num} is not a valid number.")
else:
    while not compare(random_num, int(input_num)):
        input_num = input("Please input again:")
