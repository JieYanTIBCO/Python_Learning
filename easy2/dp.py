import pdb
def subset_sum(nums, target):
    # Initialize a DP table with False, where dp[i][j] represents
    # whether we can achieve sum 'j' using the first 'i' elements.
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: You can always form sum 0 by choosing no elements.
    for i in range(n + 1):
        dp[i][0] = True

    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j >= nums[i - 1]:
                # Check if sum 'j' can be formed by:
                # 1. Excluding the current element (dp[i-1][j])
                # 2. Including the current element (dp[i-1][j-nums[i-1]])
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                # If current element is greater than sum 'j', exclude it.
                dp[i][j] = dp[i-1][j]
            


    # Return True if a subset sum equal to target is found, otherwise False
    print(f"After considering element {nums[i-1]} (i={i}, j={j}):")
    for row in dp:
        print(row)
    return dp[n][target]

# Example usage
nums = [2,3,4,5,6,7,8,9,10]
target = 15
result = subset_sum(nums, target)
print(f"Is there a subset that sums to {target}? {result}")
