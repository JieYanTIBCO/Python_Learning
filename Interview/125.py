employees = [
    (201, 'Alice', 29, 'HR'),
    (202, 'Bob', 25, 'Engineering'),
    (203, 'Charlie', 28, 'HR'),
    (204, 'David', 32, 'Marketing'),
    (205, 'Eve', 24, 'Engineering'),
    (206, 'Frank', 30, 'HR'),
    (207, 'Grace', 26, 'Marketing')
]


sorted_employees= sorted(employees, key=lambda x: (x[3], -x[2]), reverse=True)

print(sorted_employees)