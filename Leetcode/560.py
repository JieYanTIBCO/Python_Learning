class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        d = dict()
        d[0] = 1
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            count += d.get(running_sum-k, 0)
            d[running_sum] = d.get(running_sum, 0)+1
        return count


# Test result:
nums = [0, 2, 1, 0, 0]
k = 3
solution = Solution()
print(solution.subarraySum(nums, k))
