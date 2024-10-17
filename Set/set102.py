import random
thisset = {"apple", "banana", "cherry"}
thisset.add(("kiwifruit","test")) # type: ignore
tropical = {"pineapple", "mango", "papaya"}

thisset.remove(("kiwifruit","test"))
thisset2=thisset.copy()
print(len(thisset))
print(thisset)
#thisset.pop()
ramitem=random.choice(list(thisset))
print(f"This is generated random number based on set length:{ramitem}")
thisset.discard(ramitem)
print(thisset)
print(len(thisset))
print({item for item in thisset2 if item not in thisset})

thisset.clear()
thisset2.clear()
thisset.update(thisset2)
print(thisset)
print(thisset2)
del thisset, thisset2
