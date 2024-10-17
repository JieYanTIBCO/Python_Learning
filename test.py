fruits = ["honey crysp","pear","apple", "banana", "cherry", "kiwi", "mango"]

#newlist = [x for x in fruits if len(x)>=6]

fruits.sort(key=len)

print(fruits)




squares = [x**2 for x in range(10)]  # Simple and readable
squares.sort(reverse=True)
print(squares)


