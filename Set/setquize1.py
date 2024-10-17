def remove_duplicate(list1:list)->set:
    return set(list1)

list1=[1, 2, 3, 2, 1, 4, 5]

print(remove_duplicate(list1))


set1={"apple", "banana", "cherry"}
set2= {"banana", "cherry", "orange"}

print(set1&set2)

set1={1, 2, 3, 4}  

set2= {3, 4, 5, 6}

interset=set1&set2

print(set1-(set1&set2))


set1={10, 20, 30, 40, 50}
set1.pop()
print(set1)