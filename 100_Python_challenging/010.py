# Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world

# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. We use set container to remove duplicated data automatically and then use sorted() to sort the data.


def cleanup_string(org_str: str):
    words = [word.lower() for word in org_str.split(" ")]
    print(" ".join(sorted(list(set(words)))))


str1 = "hello world and practice makes perfect and hello world again Then"

cleanup_string(str1)
