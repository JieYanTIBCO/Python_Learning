class CallCounter:
    def __init__(self, func):
        self.func = func  # 将被装饰的函数存储在实例变量中
        self.count = 0  # 初始化计数器，作为实例变量

    def __call__(self, *args, **kwargs):
        self.count += 1  # 每次调用时，计数器加1
        print(f"Function called {self.count} times")
        return self.func(*args, **kwargs)  # 调用原始函数


@CallCounter
def say_hello():
    print("Hello!")


say_hello()  # 第一次调用，count = 1
say_hello()  # 第二次调用，count = 2
