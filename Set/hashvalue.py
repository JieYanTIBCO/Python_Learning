# Let's compute the hash value for the string "apple" using Python's built-in hash() function.
hash_value = hash("apple")
print(hash_value)
print(type(hash_value))


myset = {"apple", "banana"}
myset.add("pear")
print(myset)

# Print the hash values for each element in the set
for item in myset:
    print(f"Hash of '{item}': {hash(item)}")
