def letterCombinations(digits: str) -> list[str]:
    letterMap = [
        "",     # 0
        "",     # 1
        "abc",  # 2
        "def",  # 3
        "ghi",  # 4
        "jkl",  # 5
        "mno",  # 6
        "pqrs", # 7
        "tuv",  # 8
        "wxyz"  # 9
    ]

    result = []

    # Base case: If input is empty, return an empty list
    if not digits:
        return []
    
    # Define the recursive function for backtracking
    def backtrack(index: int, current_str: str):
        # When the current combination has reached the length of digits
        if index == len(digits):
            result.append(current_str)
            return
        
        # Get the letters corresponding to the current digit
        digit = int(digits[index])
        letters = letterMap[digit]
        
        # Recursively build each combination
        for letter in letters:
            backtrack(index + 1, current_str + letter)
    
    # Start the recursive process
    backtrack(0, "")
    
    return result

# Testing
print(letterCombinations("234"))
