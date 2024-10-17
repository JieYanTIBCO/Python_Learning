class solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergelist = []
        # loop times with min length of word1 or word2
        for i in range(min(len(word1), len(word2))):
            mergelist.append(word1[i])
            mergelist.append(word2[i])
        # there is only one word left, or all gone if length is equal.
        if len(word1) > len(word2):  # if word1 left
            mergelist.append(word1[i+1:])
        elif len(word1) < len(word2):  # if word2 left
            mergelist.append(word2[i+1:])
        return ''.join(mergelist)


# Create an instance of the Solution class
sol = solution()

# Take input from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Call the mergeAlternately function and print the result
result = sol.mergeAlternately(word1, word2)
print("Merged result:", result)
