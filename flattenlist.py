def flattenlist(lst:list)->list:
    result_list=[]
    for n in range(len(lst)):
        for m in range(len(lst[n])):
            result_list.append(lst[n][m])
    return result_list


def flattenlist2(lst:list)->list:
    return [item 
            for sublist in lst # loop list for finding sublists
            for item in sublist # loop sublists for finding items
            ]

lst = [[1, 2, 3], [4, 5], [6, 7, 8]]

print(flattenlist2(lst))