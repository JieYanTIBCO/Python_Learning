def sortnum(list_num):
    n=len(list_num)
    for i in range(n-1):
        for j in range(0,n-1-i):
            if list_num[j] > list_num[j+1]:
                temp = list_num[j]
                list_num[j]=list_num[j+1]
                list_num[j+1]=temp

    return list_num


print(sortnum([7,6,5,4,3,2,1]))

