from sre_compile import isstring


a = "test"
b = input("prompt message:")
print(f"a is {a} and type a is {type(a)}")

print(f"b is {b} and isstring(b) is {isstring(b)}")
