import random
thisset = {"apple", "banana", "cherry"}
thisset.add(("kiwifruit","test")) # type: ignore
tropical = {"pineapple", "mango", "papaya"}

thislist=[1,2,3]

thisset.update(tropical)

thisset.update(thislist) # type: ignore

print(thisset)
print({item for item in thisset})



print("banana" in thisset)
print("kiwifruit" not in thisset)

