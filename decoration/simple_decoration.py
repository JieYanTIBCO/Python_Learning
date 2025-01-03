from functools import wraps


def simple_decoration(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("started:")
        func(*args, **kwargs)
        print("ended.")
    return wrapper


@simple_decoration
def sum(a, b):
    print(a + b)
    return a + b


sum(2, 2)
