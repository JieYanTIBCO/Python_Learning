class Solution:
    def permute(self, nums: list[int]) -> tuple[list[list[int]], int]:
        result = []
        count = 0  # Initialize the count

        def dfs(path):
            nonlocal count  # Declare count as nonlocal to modify the outer variable
            if len(path) == len(nums):
                # If the length matches, add the path into the result list
                result.append(path.copy())
                return  # Ensure no further recursion when a permutation is complete

            for n in nums:
                count += 1  # Increment the count for each iteration
                if n not in path:
                    path.append(n)  # Choose the current number
                    dfs(path)       # Recurse
                    path.pop()      # Backtrack

        dfs([])  # Start DFS with an empty path
        return result, count  # Return the result and the count


# Test the solution
s = Solution()
permutations, operation_count = s.permute([1, 2, 3])
print("Permutations:", permutations)
print("Operation Count:", operation_count)
