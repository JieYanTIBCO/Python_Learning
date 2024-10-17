dict1=dict(name="John",age=25)

print(dict1)
print(len(dict1))

dict2={}
print(len(dict2))


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["year"])
print(thisdict.values())

print(list(thisdict.keys()))

print(thisdict.items())

if 'model1' in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
else: print("No, 'model1' is not one of the keys in the thisdict dictionary")

thisdict.update({"color":"blue"})
thisdict["color"]="red"

thisdict["year"]=2024
thisdict.update({"model":"F150"})

thisdict.popitem()
del thisdict["model"]
print(thisdict)
thisdict.clear()
print(thisdict)
del thisdict
