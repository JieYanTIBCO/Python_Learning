set1={1, 2, 3}
set2={2, 3, 4}
set3={3, 4, 5}

myset=set1&set2|set2&set3|set1&set3

print(set1-myset|set2-myset|set3-myset)


seta={"apple", "banana"}
setb={"apple", "banana", "cherry", "orange"}

print(seta<=setb, seta<setb)

str="This is a test. This test is simple."

list1=str.split()

set_word=set()

for words in list1:
    words=words.lower()
    words=words.strip('.!?/ ')
    set_word.add(words) # type: ignore

print(set_word)

print(len(set_word))