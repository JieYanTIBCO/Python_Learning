import json

print("=======================")
# some JSON:
a = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
b = json.loads(a)

print(b["age"])

print(type(b))

print(json.dumps(b, indent=4))

print("=======================")

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("=======================")

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x, indent=3, separators=(". ", " = ")))
