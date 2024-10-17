thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
    print(x, end='=')
    print(thisdict[x])

for y in thisdict.values():
    print(y)

for i in thisdict.keys():
  print(i)



print(type(thisdict.keys()))

for x,y in thisdict.items():
   print(x,y,sep='=')
   