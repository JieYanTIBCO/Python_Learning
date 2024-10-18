# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

# string1 = input("Please input a sequence of comma-separated numbers:")

# iterator1 = list(map(str, string1.split(",")))

# print(iterator1)
# print(tuple(iterator1))

values=input()
l=values.split(",")
t=tuple(l)
print(l)
print(t)