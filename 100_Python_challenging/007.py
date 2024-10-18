#Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

#input 2 digital number, check, split
def creat_list(m,n):
    return [[i*j for i in range(n)] for j in range(m)]



X,Y=input("Please input two integer separated by comma:").split(",")

print(type(X))
print(Y)

x=int(X)
y=int(Y)

print(creat_list(x,y))

# then create a embeded list with X*Y with each value is i*j
lst=[]

for i in range(0,x):
    sublst=[]
    for j in range(0,y):
        sublst.append(i*j)
    lst.append(sublst)

print(lst)

