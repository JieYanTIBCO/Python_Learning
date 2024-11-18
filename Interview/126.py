from numpy import average


data = [
    {'id': 1, 'name': 'Alice', 'scores': (
        88, 92, 95), 'department': 'Engineering'},
    {'id': 2, 'name': 'Bob', 'scores': (78, 85, 80), 'department': 'HR'},
    {'id': 3, 'name': 'Charlie', 'scores': (
        95, 90, 100), 'department': 'Engineering'},
    {'id': 4, 'name': 'Diana', 'scores': (
        85, 87, 90), 'department': 'Marketing'},
    {'id': 5, 'name': 'Eve', 'scores': (70, 75, 85), 'department': 'HR'},
]

for dict1 in data:
    dict1['average_score'] = round(float(average(dict1['scores'])), 2)

sorted_data = sorted(data, key=lambda x: (
    x['department'], -x['average_score']))

print(sorted_data)


# 示例代码
data = [1, 2, 3, 4]
avg = average(data)
print(type(avg))  # 输出：2.5