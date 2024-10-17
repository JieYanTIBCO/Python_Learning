tuple1 = ("apple", "banana", "cherry", "date", "apple", "banana", "elderberry", "fig")

index_banana = tuple1.index("banana")

tuple2=tuple1[index_banana:]

apple_count=tuple2.count("apple")

concatenate_tuple = tuple1+("grape", "honeydew")

reversed_con= concatenate_tuple[::-1]

print((index_banana,apple_count,*reversed_con))


# Define a function that takes multiple arguments
def describe_fruit(fruit1, fruit2, fruit3):
    print(f"The first fruit is {fruit1}.")
    print(f"The second fruit is {fruit2}.")
    print(f"The third fruit is {fruit3}.")

# A tuple containing fruit names
fruit_tuple = ("apple", "banana", "cherry")

# Use unpacking to pass the tuple elements as arguments to the function
describe_fruit(*fruit_tuple)
