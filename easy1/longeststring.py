# function to take a list and return the first longest string
def longeststring(list_str):
    #define str_length
    str_length=0
    max_length_str =""
    for str in list_str:            #iterate all str
        if len(str) > str_length:   # if current str is longer than previous longest
            str_length = len(str)   # set a new longest string length
            max_length_str = str    # set the longest string
    return max_length_str

test=["aaa","bbbb","ccccccccc","dddd","eeeeeee"]
print(longeststring(test))