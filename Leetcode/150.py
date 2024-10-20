# scan the list, and push into stack
# whenever the +-*/ found, pop integer A, and B, B operation A.
# after calculation, append the result into stack
# continue to scan.
# we expect the result is one integer in stack and return it.

from collections import deque


def RPN(lst: list) -> int:
    stack = deque()

    for i in lst:
        if i == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif i == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif i == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        elif i == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(i))
    return stack.pop()


print(RPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

print(RPN(["4", "13", "5", "/", "+"]))

print(RPN(["2", "1", "+", "3", "*"]))


