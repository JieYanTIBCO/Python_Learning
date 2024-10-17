import copy

def traverse_list(lst:list):
    for element in lst:
        if isinstance(element,list):
            traverse_list(element)
        else:
            elment=0

c = [7, [-1, 2], 0, [9, [-3, 4]], 6]
a = [1, [2, 3, [4, 5]], [6, 7], 8]


e = c

f = c.copy()

d = copy.deepcopy(c)
print("Before change list c")
print(f"c list now is :{c}")
print(f"d list now is :{d}")
print(f"e list now is :{e}")
print(f"f list now is :{f}")

c[1][0] = 100
for i in range(len(c)):
    c[i]=0

print("After change list c")

print(f"c list now is :{c}")
print(f"d list now is :{d}")
print(f"e list now is :{e}")
print(f"f list now is :{f}")