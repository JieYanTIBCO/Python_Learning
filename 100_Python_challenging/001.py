# 2000-3200 both included
# are divisible by 7  n % 7 == 0
# but are not a multiple of 5 which mean n % 5 != 0
# output single line and separated by , how about last one?

# def return_last(a,b):
#     for m in range(b,a-1,-1):
#         if m % 7 == 0 and  m % 5 != 0:
#             print(f"last value is : {m}")
#             return m

# a= 2000
# b= 3200
# if a<=b:
#     pass
# else: a,b=b,a
# last = return_last(a,b)

# for n in range(a,b+1):
#     if n % 7 == 0 and  n % 5 != 0:
#         print(n, end=", " if n != last else "")


# a= 2000
# b= 3200
# if a<=b:
#     pass
# else: a,b=b,a
# result=[]

# result=[str(n) for n in range(a,b+1) if n % 7 == 0 and n % 5 != 0]

# print(", ".join(result))

# a=2000
# b=3200

# lst=[n for n in range(a,b+1)]
# result=list(filter(lambda n: n%7 == 0 and n%5 != 0, lst))
# result_str=map(str,result)
# print(",".join(result_str))

a = int(input("Please input a integer value a:"))
b = int(input("Please input a integer value b:"))

if a <= b:
    pass
else:
    a, b = b, a

result = [n for n in range(a, b + 1) if n % 7 == 0 and n % 5 != 0]

# Use the unpacking operator (*) and print all in one line with ", " as separator
print(*result, sep=", ")
