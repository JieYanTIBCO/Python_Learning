# function with list of numbers as inpurt and list of squared number as output

def squared_list(list_num):
    list_squared=[]
    for num in list_num:
        list_squared.append(num*num)
    return list_squared