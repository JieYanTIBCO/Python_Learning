class Dog:
    count = 0  # 类属性，所有实例共享

    def __init__(self, name):
        self.name = name
        Dog.count += 1

    def print_count(self):
        print(f"There are {Dog.count} dogs.")

    @classmethod
    def total_dogs(cls):  # 类方法
        return f"There are {cls.count} dogs."

dog1 = Dog("Buddy")
dog2 = Dog("Max")



print(Dog.total_dogs())  # 输出: There are 2 dogs.
dog3 = Dog("Cathy")

dog1.print_count()