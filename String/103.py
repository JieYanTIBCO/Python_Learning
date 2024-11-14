def is_anagram(s1: str, s2: str) -> bool:
    # is_anagram("Listen", "Silent")  # Should return True
    # is_anagram("Hello", "World")    # Should return False
    # we want case insensitive: lower case the str.
    s1 = s1.lower()
    s2 = s2.lower()
    # we can not use set, but we can use dictionary with value count?
    dict1 = dict()
    for char1 in s1:
        if char1 not in dict1:
            dict1[char1] = 1
        else:
            dict1[char1] += 1

    for char2 in s2:
        if char2 not in dict1:
            return False
        else:
            dict1[char2] -= 1

    if all(value == 0 for value in list(dict1.values())):
        return True
    else:
        return False

    # then we can scan the s2 to sub the count.
    # if eventually count is 0 for all dictionary, then return true.


print(is_anagram("Listen", "Silent"))
print(is_anagram("Hello", "World"))

# chatGPT
# def is_anagram(s1: str, s2: str) -> bool:
#     s1 = s1.lower()
#     s2 = s2.lower()

#     # Initialize dictionaries to count character occurrences
#     dict1 = {}

#     # Count characters in s1
#     for char in s1:
#         if char.isalpha():  # Filter to include only alphabetic characters
#             dict1[char] = dict1.get(char, 0) + 1

#     # Adjust counts based on s2
#     for char in s2:
#         if char.isalpha():  # Same filter for s2
#             if char not in dict1:
#                 return False
#             dict1[char] -= 1

#     # Return True if all counts are zero
#     return all(value == 0 for value in dict1.values())

# # Test cases
# print(is_anagram("Listen", "Silent"))  # Expected: True
# print(is_anagram("Hello", "World"))    # Expected: False
