# Input: [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
def productex(list_int):
    list_pro=[]
    for i in range(len(list_int)):
        total_product=1
        for j in range(len(list_int)):
            if j != i:
                total_product*=list_int[j]
        list_pro.append(int(total_product))
    return list_pro

print(productex([1, 2, 3, 4]))