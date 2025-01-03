# Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the following input is supplied to the program: 9 Then, the output should be: 11106

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


num = input("Enter a number: ")

try:
    num = int(num)
    if num < 0 or num > 9:
        raise ValueError("Number must be positive")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit()


total = 0
for i in range(1, 5):
    total += int(str(num) * i)
print(total)
