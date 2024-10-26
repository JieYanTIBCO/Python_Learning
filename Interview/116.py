# Step 1: 定义装饰器
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # 执行传入的原始函数
        print("Something is happening after the function is called.")
    return wrapper

# Step 2: 使用装饰器
@my_decorator  # 等效于 say_hello = my_decorator(say_hello)
def say_hello():
    print("Hello!")

# Step 3: 调用函数
say_hello()



import functools
import datetime

# 定义日志装饰器
def log_function_call(func):
    @functools.wraps(func)  # 保持原函数的元数据，如函数名和文档字符串
    def wrapper(*args, **kwargs):
        # 获取当前时间
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 打印日志信息
        print(f"[{now}] Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        # 执行原函数
        result = func(*args, **kwargs)
        
        # 打印函数的返回值
        print(f"[{now}] {func.__name__} returned: {result}")
        
        return result
    
    return wrapper

# 使用装饰器
@log_function_call
def add(x, y):
    return x + y

@log_function_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# 调用函数，触发日志记录
result1 = add(5, 3)
result2 = greet("Alice")
result3 = greet("Bob", greeting="Hi")
