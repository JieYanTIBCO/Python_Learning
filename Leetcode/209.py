# use sliding window, the size of window from 1 to len of list
# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2

def min_sub_str(s: int, lst: list) -> int:
    left=0
    min_len=float('inf')
    current_sum =0
    for right in range(len(lst)):
        current_sum+=lst[right]

        while current_sum>=s:
            min_len=min(min_len, right-left+1)
            current_sum-=lst[left]
            left+=1
        
    return min_len if min_len != float('inf') else 0 # type: ignore


print(min_sub_str(7, [2, 3, 1, 2, 4, 3]))