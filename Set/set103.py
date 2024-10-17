thisset = {"apple", "banana", "cherry"}

print({item for item in thisset})


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset=set1.union(set2,set3,set4)
print(set1.union(set2,set3,set4))
print(set1|set2|set3|set4)


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2) # type: ignore
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

print(set1&set2)