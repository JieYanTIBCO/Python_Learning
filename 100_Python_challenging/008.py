# Question 8
# Level 2

# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words
# in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def sort_str(input_string):
    input_list = [word.strip() for word in input_string.split(",")]
    input_list = sorted(input_list)
    return ",".join(input_list)


input_string = input("please input a comma separated sequence of words:")

print(sort_str(input_string))
