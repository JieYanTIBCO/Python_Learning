# Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
# n = 1001 // 100

# # if n:
# print(n)

def all_even_digits(number):
    return all(int(digit) % 2 == 0 for digit in str(number))


lst = [str(num) for num in range(1000, 3001) if all_even_digits(num)]

print(",".join(lst))


# lst = []


# for num in range(1000, 3001):
#     if all([num // 10 % 2 == 0, num % 2 == 0, num // 100 % 2 == 0, num // 1000 % 2 == 0]):
#         lst.append(num)

# print("".join(str(lst)))
