#function to take input as list and sum integer as output

def sumEvenNumber(list_num):
    sum=0
    #for loop to sum even
    for i in list_num:
        if i%2==0:
            sum+=i
    return sum


list_str= input("input the number separate by \",\" :")

list_num= [int(num) for num in list_str.split(",")]

print(list_num)
print(sumEvenNumber(list_num))