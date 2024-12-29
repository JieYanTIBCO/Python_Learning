import pytest
from setup_logging import get_logger, logging
# 关键：只从 log_decoration.py 文件中导入 log_decoration 函数
from decoration.log_decoration import log_decoration


@log_decoration
def add(a: int, b: int) -> int:
    """Test function that adds two numbers."""
    return a + b


def test_log_decoration():
    """Test the log decoration functionality."""
    assert add(1, 2) == 3
    assert add(3, 4) == 7
    assert add(0, 5) == 5
    assert add(-1, 1) == 0
    assert add(-2, -3) == -5


if __name__ == "__main__":
    pytest.main(["-v", __file__])
    print(add(4, 5))
    add(1, 2)
    add(3, 4)
    add(0, 5)
    add(-1, 1)
    add(-2, -3)
    add(a=4, b=2)
    logger = get_logger(log_level=logging.INFO)
    logger.info("This is a debug message.")
