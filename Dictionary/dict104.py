import random

def find_pair_with_sum(nums:list, target_sum:int)->(int,int):
    # Dictionary to store numbers we've seen and their indices
    seen = {}
    
    # Iterate over the list of numbers
    for num in nums:
        # Calculate the complement that would give the target sum
        complement = target_sum - num
        
        # Check if the complement is already in the dictionary
        if complement in seen:
            return (complement, num)
        
        # Store the current number in the dictionary
        seen[num] = True
    
    # If no pair is found, return None
    return None

# Example usage
nums = [21, 34, 35, 97, 66, 86, 27, 88, 65, 31, 84, 12, 91, 45, 20, 11, 41, 3, 23, 32]
target_sum = 12
pair = find_pair_with_sum(nums, target_sum)
print(f"Pair with sum {target_sum}: {pair}")