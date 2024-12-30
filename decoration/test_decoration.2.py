from decoration.log_decoration import log_decoration


@log_decoration(max_retries=3)
def add(a: int, b: int) -> int:
    """Test function that adds two numbers."""
    return a + b

add(1, 2)