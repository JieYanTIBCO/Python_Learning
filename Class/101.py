class helloworld:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello world! Happy {self.age}th birthday {self.name}!!!")



object1 = helloworld("Jackie", 42)

print(object1.name)

object1.greeting()