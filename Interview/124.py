data = [
    (101, 'Alice', 25),
    (102, 'Bob', 30),
    (103, 'Charlie', 28),
    (104, 'Diana', 22)
]


for index, (num, name, age) in enumerate(data):
    if name == 'Bob':
        print(index, (num, name, age))
        break

list_above25 = []
for (num, name, age) in data:
    if age > 25:
        list_above25.append(name)

print(list_above25)

data1 = []
# add 1 year for age
for (num, name, age) in data:
    data1.append((num, name, age+1))

print(data1)

sorted_data = sorted(data, key=lambda x: x[2], reverse=False)

print(sorted_data)