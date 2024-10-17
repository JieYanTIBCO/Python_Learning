set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
print(set1)
print(set2)

set3 = set1.intersection(set2)


print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

print(set1.intersection(set2))


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)
print(set2)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(f"This is ^ operator for twe sets: {set3}")

print(set1.symmetric_difference(set2))


set2={"apple"}
print(set2.issubset(set1))