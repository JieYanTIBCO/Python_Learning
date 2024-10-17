def removeduplicates(nums): #this nums is list of sorted integer
    n=len(nums)
    a=0
    b=1
    while b <= n-1:
        if nums[a] == nums[b]:
            b+=1
        elif nums[a] != nums[b]:
            a+=1
            nums[a]=nums[b]
            b+=1
    return a+1,nums

n,nums=removeduplicates([1, 1, 1, 2, 2, 3, 4, 4, 5, 5])
print(f"{n}, nums={nums}")
