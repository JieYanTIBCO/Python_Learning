# Question: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

from collections import defaultdict

import json


input_str = input()

dict1 = defaultdict(int)
for char in input_str:
    if char.isdigit():
        dict1["DIGITS"] += 1
    elif char.isalpha():
        dict1["LETTERS"] += 1
    else:
        pass

print(json.dumps(dict1, indent=4))
