# Creating a dictionary
students = {
    "Alice": {"Math": 85, "Science": 90},
    "Bob": {"Math": 78, "Science": 82}
}

students["Smith"] =  {"Math": 70, "Science": 99}

students["Alice"] = {"Math": 85, "Science": 100}

students["Bob"]["Math"]=95

print(students)
print()
print(students.items())