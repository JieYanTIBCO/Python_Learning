from sys import exception

# define file location
URL="C:/Build/tmp/demofile.txt"

#read the file from URL:
try: 
    with open(URL,"r") as f:
        content =f.read()       #no need to close the file
        print(content)          #print it out for test
except FileNotFoundError:
    print(f"file not found at {URL}")
    exit()

#cast it as string type list including , . ! ""
result_list = content.split()
result_list = result_list
print(f"Before sorting:{result_list}")
#sort the list
result_list.sort()
print(f"After sorting:{result_list}")

#Initialize word count dictionary
word_count={}

#count the number and find the maximum
for word in result_list:
    word = word.lower() # convert to lower case, optional
    word = word.strip(",./?!\"'")
    if word in word_count:
        word_count[word]+=1 # count++ for repeated word
    else:
        word_count[word]=1

max_key = max(word_count, key= word_count.get)    # type: ignore # get max key
max_value = word_count[max_key]                 # get max value
print(f"Max key:{max_key}, and Max count:{max_value}")

