from typing import List, Any


def sort_list_reverse(list1: list[Any]) -> list[Any]:
    return sorted(list1,key=lambda x: x[0], reverse = True)


position = [10,8,0,5,3]
speed = [2,4,"fast",1,"slow"]
list1 = []
for j in range(len(position)):
    list1.append([position[j],speed[j]])
    
print(list1)
print(sort_list_reverse(list1))

