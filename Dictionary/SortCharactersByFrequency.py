# Define a function to iterate the string and import characters and frequency into dictionary
# Then sort this dictionary and return it.


def SortCharactersByFrequency(s1:str)->dict(): # type: ignore
    dict1=dict()
    for i in s1:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    #sorting dictionary
    for i in dict1.items():
        print(i,type(i))
    return sorted(dict1.items(), key = lambda item: (-item[1], item[0]))



print(SortCharactersByFrequency("aaakldflkwaasjgilelrge"))