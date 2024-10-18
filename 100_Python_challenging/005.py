# Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.

class get_print_string():
    def __init__(self):
        self.s1 = ""

    def getString(self):
        self.s1 = input("please input the string:")

    def printString(self):
        print(self.s1.upper())


obj = get_print_string()
obj.getString()
obj.printString()
