
from curses.ascii import isalpha, isdigit, ispunct, isspace


str1 = r"% hello world! 123^&*()"

for char in str1:
    if isdigit(char):
        print(f"digit:{char}")
    elif isalpha(char):
        print(f"alpha:{char}")
    elif isspace(char):
        print(f"space:{char}")
    elif ispunct(char):
        print(f"punct:{char}")
    else:
        pass
