fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

green, *yellow, red = fruits

print(green)
print(yellow)
print(red)

print(type(green))
print(type(yellow))
print(type(red))

tuple1 = (1, 2, 3, 4, 5)
list1 = [1, 2, 3, 4, 5]

print(tuple1.__sizeof__())  # Output: typically smaller
print(list1.__sizeof__())  # Output: typically larger

# print(tuple([item for item in fruits]))

# for i in range(len(fruits)):
#     print(fruits[i], end=" ")

# while i < len(fruits):
#     print(fruits[i])
#     i+=1

tuple1+=fruits
print(tuple1*2)

print((tuple1*2).count("apple"))

print(f"apple's index is:{(tuple1*2).index("apple")}")