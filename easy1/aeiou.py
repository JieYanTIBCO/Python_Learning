




def count_vowel(input_str):
    #convert str to list
    input_list=list(input_str.lower())

    vowel={"a","e","i","o","u"}
    counter = 0
    #for loop to check each characters and calculate the number.
    for char in input_list:
        if char in vowel:
            counter+=1
    return counter

#input words and check validation

input_str=input("Please input the string:")
#print result.
print(count_vowel(input_str))