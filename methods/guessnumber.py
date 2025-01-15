import random


def compare(random_num: int, number: int):
    if random_num == number:
        print(f"number: {number} is the correct answer!")
        return 1
    elif random_num > number:
        print(f"number: {number} is less than the answer!")
        return 0
    else:
        print(f"number: {number} is greater than the answer!")
        return 0


def generate_hints(random_num: int, number: int):
    hints = []

    # Check if the random number is a multiple of a smaller number
    for i in range(2, 11):  # Checking multiples between 2 and 10
        if random_num % i == 0:
            hints.append(f"The answer is a multiple of {i}.")
        else:
            hints.append(f"The answer is not a multiple of {i}.")

    # Add a range hint
    if random_num > number:
        hints.append(f"The answer is between {number + 1} and 100.")
    else:
        hints.append(f"The answer is between 0 and {number - 1}.")

    # Add an odd/even hint
    if random_num % 2 == 0:
        hints.append("The answer is an even number.")
    else:
        hints.append("The answer is an odd number.")

    return hints


# Main game logic
random_num = random.randint(0, 100)
input_num = input("Please input an integer between 0 and 100: ")

if not input_num.isdigit() or int(input_num) > 100 or int(input_num) < 0:
    print(f"This {input_num} is not a valid number.")
else:
    hints = generate_hints(random_num, int(input_num))
    random.shuffle(hints)  # Shuffle hints to ensure randomness

    while not compare(random_num, int(input_num)):
        if hints:  # Check if there are hints left
            print("Hint: " + hints.pop(0))  # Display and remove the first hint
        else:
            print("No more hints available!")
        input_num = input("Please input again: ")
