child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily1=dict(child1=child1,child2=child2,child3=child3)

myfamily2={
    "child1":child1,
    "child2":child2,
    "child3":child3
}

print(myfamily1)
print(myfamily2)

print("name" in myfamily1["child3"].keys())


for keyx,dictx in myfamily1.items():
    print(keyx)
    for keyy in dictx:
        print(keyy + ':', dictx[keyy]) # type: ignore