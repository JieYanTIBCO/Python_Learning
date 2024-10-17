tuple1=("test")
print(tuple1)
print(type(tuple1))

tuple2=("aaa","bbb","aaa","ccc","ddd","eee","fff")

print(tuple([items for items in tuple2]))

def get_person():
    return "Alice", 30, "Designer"

person_info = get_person()
print(person_info)  # Output: ('Alice', 30, 'Designer')

x,y=10,20

print(x,y)

print(tuple2[-3:-1])

print("cccd" in tuple2)

list2=list(tuple2)
list2.append('zzz') # type: ignore
tuple2=tuple(list2)
print(tuple2)