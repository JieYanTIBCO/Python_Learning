def longestsubstr(mystr):
    

    n=len(mystr)
    substr=""
    win=0
    for x in range(n):
        for i in range(x,n):
            if len(mystr[x:x+win])>len(set(mystr[x:x+win])):
                break
            elif mystr[x+win] not in substr:
                win+=1
                substr=mystr[x:x+win]
    return substr

outcome=longestsubstr("abcdabcbbcdefg")
print(f"{len(outcome)},{outcome}")