class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def from_square(cls, side_length):
        # 使用边长创建一个正方形
        return cls(side_length, side_length)
    
    @classmethod
    def from_test(cls, length):
        return cls(length, length)

    def area(self):
        return self.width * self.height

# 通过不同的方式构造对象
rect1 = Rectangle(10, 20)  # 普通矩形
rect2 = Rectangle.from_square(5)  # 通过类方法创建一个正方形
rect3 = Rectangle.from_test(7)

print(rect1.area())  # 输出: 200
print(rect2.area())  # 输出: 25
print(rect3.area())
