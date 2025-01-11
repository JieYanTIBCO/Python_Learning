from functools import wraps
from typing import Callable, Any, Tuple
from typing_extensions import get_type_hints
import time
import random
import requests  # Example of a network-related library
from utils.setup_logging import get_logger
import traceback
import json
# Initialize logger once
logger = get_logger()


def log_decoration(
    max_retries: int = 3,
    retry_delay: int = 10,
    type_check: bool = True,
    exceptions_to_catch: Tuple[Exception, ...] = (
        requests.ConnectionError, requests.Timeout)  # type: ignore
) -> Callable:
    """
    A decorator that logs function execution using custom logging and retries on failure.

    Args:
        max_retries: Maximum number of retry attempts (default: 3).
        retry_delay: Initial delay (in seconds) between retries (default: 10).
        type_check: Whether to enforce type checking based on function hints (default: True).
        exceptions_to_catch: Tuple of exceptions to catch and retry upon.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Argument type checking
            if type_check:
                type_hints = get_type_hints(func)
                for arg, hint in zip(args, type_hints.values()):
                    if not isinstance(arg, hint):
                        raise TypeError(
                            f"Argument {arg} does not match type {hint}"
                        )
                for key, value in kwargs.items():
                    if key in type_hints and not isinstance(value, type_hints[key]):
                        raise TypeError(
                            f"Keyword argument '{key}' with value {
                                value} does not match type {type_hints[key]}"
                        )

            attempt = 0
            current_retry_delay = retry_delay
            while attempt <= max_retries:
                try:
                    logger.debug(
                        json.dumps({
                            "event": "function_call",
                            "function": func.__name__,
                            "args": args,
                            "kwargs": kwargs
                        }, indent=4)
                    )

                    start_time = time.perf_counter_ns()
                    result = func(*args, **kwargs)
                    elapsed_microseconds = (
                        time.perf_counter_ns() - start_time) / 1000  # Convert to µs

                    # Format elapsed time with correct unit
                    if elapsed_microseconds >= 1_000_000:
                        elapsed_time = f"{
                            elapsed_microseconds / 1_000_000:.2f}s"
                    elif elapsed_microseconds >= 1_000:
                        elapsed_time = f"{elapsed_microseconds / 1_000:.2f}ms"
                    else:
                        # Use microseconds symbol
                        elapsed_time = f"{elapsed_microseconds:.2f}µs"

                    logger.debug(
                        json.dumps({
                            "event": "function_complete",
                            "function": func.__name__,
                            "result": result,
                            "elapsed_time": elapsed_time
                        }, indent=4, ensure_ascii=False)
                    )
                    return result

                except exceptions_to_catch as e:  # type: ignore
                    attempt += 1
                    logger.error(
                        json.dumps({
                            "event": "function_error",
                            "function": func.__name__,
                            "attempt": attempt,
                            "max_retries": max_retries,
                            "error": str(e),
                            "traceback": traceback.format_exc()
                        }, indent=4)
                    )
                    if attempt > max_retries:
                        logger.error(f"Function {func.__name__} failed after {
                                     max_retries} attempts")
                        raise
                    else:
                        time.sleep(current_retry_delay)
                        # Exponential backoff, capped at 60 seconds
                        current_retry_delay = min(current_retry_delay * 2, 60)

                except Exception as e:
                    logger.error(
                        json.dumps({
                            "event": "function_failure",
                            "function": func.__name__,
                            "attempt": attempt,
                            "max_retries": max_retries,
                            "error": str(e),
                            "traceback": traceback.format_exc()
                        }, indent=4)
                    )
                    raise

        return wrapper
    return decorator


# Usage example
@log_decoration(max_retries=3, retry_delay=1, type_check=True)
def example_function(x: int, y: int) -> int:
    """Example function that adds two numbers."""
    if x == 0:
        raise requests.ConnectionError("Simulated network error")
    return x + y


if __name__ == "__main__":
    try:
        print(f"example_function(0,1)'s result is :{
              example_function(0, 1)}")  # Simulates a network error
    except Exception as e:
        print(f"Final exception caught: {e}")
