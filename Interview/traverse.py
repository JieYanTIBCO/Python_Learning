def traverse_list(lst:list):
    for i in range(len(lst)):
        if isinstance(lst[i],list):
            traverse_list(lst[i])
        else:
            lst[i]=0
    return lst
c = [7, [-1, 2], 0, [9, [-3, 4]], 6]
a = [1, [2, 3, [4, 5]], [6, 7], 8]

print(traverse_list(c))
print(traverse_list(a))








