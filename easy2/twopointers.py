def twopointers(list_num, target):
    list_num.sort()
    pointer_a=0
    pointer_b=len(list_num)-1
    while pointer_a < pointer_b: # keep looping if left pointer is less than right pointer
        current_sum=list_num[pointer_a]+list_num[pointer_b]
        if current_sum > target:
            pointer_b-=1
        elif current_sum < target:
            pointer_a+=1
        else:
            return pointer_a,pointer_b #return indices if target is matched.
    return -1,-1 #return -1,-1 if there is no match


print(twopointers([33,45,66,11,27,10, 22, 23, 29, 30, 40],76))