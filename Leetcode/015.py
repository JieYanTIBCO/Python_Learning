# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
# 注意： 答案中不可以包含重复的三元组。
# 示例：
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为： [ [-1, 0, 1], [-1, -1, 2] ]

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                current_sum = nums[i]+nums[left]+nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i]+nums[left]+nums[right] > 0:
                    right -= 1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left += 1

        return result


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4,0,0]))
