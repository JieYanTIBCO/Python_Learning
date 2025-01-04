import json

x = '{"name":"jackie","age":30,"gender":"male"}'

y = json.loads(x)


print(y['age'])

print(json.dumps(y, indent=3))
