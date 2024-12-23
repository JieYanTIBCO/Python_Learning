from typing import List
from collections import deque


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = deque(nums[:k],maxlen=k)
        maxsum = sum(nums[:k])

        for i in nums[k:]: # i=k=4
            window.append(i)
            if sum(window) >maxsum:
                maxsum=sum(window)
        return maxsum/k
    
        window= deque(nums[:k],maxlen(k))
        maxsum= sum(nums[:k])
        for i in nums[k:]:
            window.append(i)
            if sum(window) > maxsum:
                maxsum=sum(window)
        return float(maxsum/k)




def test_max_average_subarray():
    # Create an instance of the Solution class
    solution = Solution()

    # Define test cases
    test_cases = [
        {"input": ([1, 12, -5, -6, 50, 3], 4), "expected": 12.75},
        {"input": ([5], 1), "expected": 5.0},
        # Corrected expected value
        {"input": ([-1, -12, -5, -6, -50, -3], 2), "expected": -5.5},
        {"input": ([7, 7, 7, 7, 7, 7, 7], 3), "expected": 7.0},
        {"input": ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), "expected": 8.0}
    ]

    # Run the tests
    for i, case in enumerate(test_cases, 1):
        nums, k = case["input"]
        expected = case["expected"]
        result = solution.findMaxAverage(nums, k)
        assert abs(
            result - expected) < 1e-5, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed.")


# Run the tests
test_max_average_subarray()
