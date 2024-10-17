class Animal:
    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        return cls(name)

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"

# 使用类方法创建不同的子类对象
dog = Dog.create("Buddy")
cat = Cat.create("Kitty")

print(dog.speak())  # 输出: Buddy says woof!
print(cat.speak())  # 输出: Kitty says meow!
