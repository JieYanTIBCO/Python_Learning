a = [-3, -2, 0, 1, 4, -1]

lst1=list(filter(lambda x: not x % 2!=0, a)) # list of even

#square the list
for i in range(len(lst1)):
    lst1[i]*=lst1[i]

print(lst1)