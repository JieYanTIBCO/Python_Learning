def LongestCommonSubset(set1:set,set2:set)->set:
    #{1, 2, 3, 4, 7, 8, 9, 10}, {2, 3, 4, 7, 8, 9, 10}
    # set1 &set2 ={2,3,4,7,8,9,10} 
    commonlist= sorted(set1&set2) #convert to list and sort
    print(commonlist)
    longlist=[]
    currentlist=[]
    for num in commonlist: # type: ignore
        if not currentlist or num ==currentlist[-1]+1:
            currentlist.append(num)
        else:
            currentlist=[num]
        # then check if new currentlist is longer than longestlist.
        if len(currentlist)>len(longlist):
            longlist=currentlist.copy()
    return set(longlist)


set1={1, 2, 3, 4, 7, 8, 9, 10}
set2={2, 3, 4, 7, 8, 9, 10}
print(LongestCommonSubset(set1,set2))

