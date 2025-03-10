# Question: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24

import math

# this is for getting the formula: Q = Square root of [(2 * C * D)/H]


def Q(D: int):
    C = 50
    H = 30
    return str(round(math.sqrt(2*C*D/H)))


# This wil convert the input into list and separate it by comma
# If non-valid str input, the int(x) will throw exception
lst = input("Please input a  comma-separated sequence:").split(",")

# This is use map and lambda to invoke the function Q to calculate and return a list of str
# Then covert the list to a single line string separated by comma.
print(",".join(list(map(lambda x: Q(int(x)), lst))))
