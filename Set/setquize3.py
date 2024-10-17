def remove_divisiblen(set1:set,n:int)->set:
    set2=set()
    for num in set1:
        if num%n!=0:
            set2.add(num)
    return set2

def remove_divisiblen2(set1:set,n:int)->set:
    return{num for num in set1 if num%n!=0}

print(remove_divisiblen({1, 2, 3, 4, 5, 6, 7, 8, 9},3))
print(remove_divisiblen2({1, 2, 3, 4, 5, 6, 7, 8, 9},3))