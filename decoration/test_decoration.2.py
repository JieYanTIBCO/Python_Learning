from functools import wraps, lru_cache
from utils.log_decoration import log_decoration


@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# First call
print(fibonacci(5))
print(fibonacci.cache_info())

# Second call
print(fibonacci(5))
print(fibonacci.cache_info())
