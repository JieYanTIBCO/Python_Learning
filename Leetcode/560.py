class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        d = dict()
        d[0] = 1
        running_sum = 0
        for i in range(len(nums)):
            # count running sum
            running_sum += nums[i]
            # running_sum-k is desired value in the previous sums.
            # check how many it occurs in dicitonary and add it to count.
            count += d.get(running_sum-k, 0)
            # record the running sum into directory.
            d[running_sum] = d.get(running_sum, 0)+1
        return count


# Test result:
nums = [0, 2, 1, 0, 0]
k = 3
solution = Solution()
print(solution.subarraySum(nums, k))
