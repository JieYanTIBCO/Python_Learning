
def reverse_string(s1: str) -> str:
    # abcd
    # dcba
    # can not be null, 
    # stack the string like abcd, and then pop() it, so it will become dbca.
    outputstring=""
    if not s1:
        print("s1 is null")
    else:
        stack=[]
        stack=list(s1)
        for i in range(len(stack)):
            outputstring+=stack.pop()
    return outputstring


print(reverse_string("abcde"))


    

