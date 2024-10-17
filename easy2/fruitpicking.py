# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].

# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
        # define the total fruits, index, and sublist
#import pdb


def totalFruit(fruites):
    n=len(fruites)
    total=0
    basketlist=[]
    for i in range(n):
        sublist=[]
        for j in fruites[i:n]:
            if (j not in sublist and len(set(sublist))<=1) or (j in sublist):
                sublist.append(j)
                if len(sublist)> total:
                    total+=1
                    basketlist=sublist
            else: break
    print(basketlist)
    return total

print(totalFruit([3, 3, 3, 1, 2]))