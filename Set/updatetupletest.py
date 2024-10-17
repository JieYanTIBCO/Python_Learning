thisset = {"apple", "banana", "cherry"}
thistuple=("pear","kiwi")

thisset.update(thistuple)
print(thisset)

thisset.difference_update(thistuple)
print(thisset)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)