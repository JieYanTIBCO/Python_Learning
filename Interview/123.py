
data = [(1, 'apple'), (2, 'banana'), (3, 'cherry'), (1, "pear")]
dict1 = {}
for tuple in data:
    if tuple[0] not in dict1:
        dict1[tuple[0]] = [tuple[1]]
    else:
        dict1[tuple[0]].append(tuple[1])

print(dict1)


for index, (num,fruit) in enumerate(data):
    print(f"Tuple {index} - number:{num},fruit:{fruit}")