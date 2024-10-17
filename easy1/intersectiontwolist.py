def intersectiontwolist(list1, list2):
    commonlist=[]
    for num in list1:
        if num in list2:
            commonlist.append(num)
    return commonlist 

print(list(set(intersectiontwolist([1, 2, 3,3, 4], [3, 4, 5, 6]))))

