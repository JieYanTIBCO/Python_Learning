a = [-3, -2, 0, 1, 4, -1]

lst1=list(map(lambda x: x**2 if x%2==0 else None, a))

print(lst1)

result1 = list(filter(lambda y: y is not None, lst1))

print(result1)