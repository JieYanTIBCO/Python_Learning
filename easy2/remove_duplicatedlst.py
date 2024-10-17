def remove_duplicate(lst:list)->list:
    seen=set()
    for i in range(len(lst)-1,-1,-1):
        if lst[i] in seen:
            lst.pop(i)
        else: seen.add(lst[i])
    return lst

lst = ["apple", "banana", "cherry", "apple", "banana","apple","banana"]
print(remove_duplicate(lst))