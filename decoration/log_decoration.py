# log_decoration.py
from functools import wraps
from typing import Callable, Any
from typing_extensions import get_type_hints
from setup_logging import get_logger
import time
import random
import requests  # Example of a network-related library

# 只在这里调用一次 get_logger()
logger = get_logger()


def log_decoration(max_retries: int = 3) -> Callable:
    """
    A decorator that logs function execution using custom setup_logging and retries on failure.

    Args:
        max_retries: Maximum number of retry attempts (default: 3)
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Argument type checking
            type_hints = get_type_hints(func)
            for arg, hint in zip(args, type_hints.values()):
                if not isinstance(arg, hint):
                    raise TypeError(
                        f"Argument {arg} does not match type {hint}")

            attempt = 0
            while attempt <= max_retries:
                try:
                    # Combined start logging
                    logger.debug(f"Starting {func.__name__} | args: {
                                 args} | kwargs: {kwargs}")

                    start_time = time.perf_counter_ns()
                    result = func(*args, **kwargs)
                    elapsed_microseconds = (
                        time.perf_counter_ns() - start_time) / 1000  # Convert to µs

                    # Determine appropriate unit
                    if elapsed_microseconds >= 1_000_000:
                        elapsed_time = f"{
                            elapsed_microseconds / 1_000_000:.2f}s"
                    elif elapsed_microseconds >= 1_000:
                        elapsed_time = f"{elapsed_microseconds / 1_000:.2f}ms"
                    else:
                        elapsed_time = f"{elapsed_microseconds:.2f}µs"

                    # Combined completion logging with elapsed time
                    logger.debug(f"Completed {func.__name__} | return: {
                                 result} | elapsed: {elapsed_time}")
                    return result

                except (requests.ConnectionError, requests.Timeout) as e:
                    attempt += 1
                    logger.error(f"Network error in {func.__name__} on attempt {
                                 attempt}/{max_retries}: {str(e)}")
                    if attempt > max_retries:
                        logger.error(f"Function {func.__name__} failed after {
                                     max_retries} attempts")
                        raise
                    else:
                        logger.debug(f"Retrying {func.__name__} (attempt {
                                     attempt}/{max_retries}) after 10 seconds")
                        time.sleep(10)  # Wait for 10 seconds before retrying

                except Exception as e:
                    attempt += 1
                    logger.error(f"Function {func.__name__} failed on attempt {
                                 attempt}/{max_retries}: {str(e)}")
                    if attempt > max_retries:
                        logger.error(f"Function {func.__name__} failed after {
                                     max_retries} attempts")
                        raise
                    else:
                        logger.debug(f"Retrying {func.__name__} (attempt {
                                     attempt}/{max_retries})")

        return wrapper
    return decorator

# Usage example


@log_decoration(max_retries=3)
def example_function(x, y):
    """Example function that adds two numbers."""
    if x == 0:
        raise requests.ConnectionError("Simulated network error")
    return x + y


if __name__ == "__main__":
    print(example_function(0, 2))
