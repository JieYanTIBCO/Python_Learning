from decoration.log_decoration import log_decoration

@log_decoration
def add(a: int, b: int) -> int:
    """Test function that adds two numbers."""
    return a + b