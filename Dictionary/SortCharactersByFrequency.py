# Define a function to iterate the string and import characters and frequency into dictionary
# Then sort this dictionary and return it.
import json


def SortCharactersByFrequency(s1: str) -> dict():  # type: ignore
    dict1 = dict()
    for char in s1:
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1
    print(json.dumps(dict1, indent=4))

    # sorting dictionary
    for char_tuple in dict1.items():
        print(char_tuple, type(char))
    return sorted(dict1.items(), key=lambda item: (-item[1], item[0]))


print(SortCharactersByFrequency("aaakldflkwaasjgilelrge"))
