def reversestr(input_str):
    reverselist=[]
    for i in range(len(input_str)):
        reverselist.append(input_str[len(input_str)-i-1])
    return ''.join(reverselist)
print(reversestr("oiqueioqueoiqueioquoie"))