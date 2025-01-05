from utils.mytime import MyDateTime
from utils.setup_logging import get_logger

logger = get_logger()
if __name__ == "__main__":
    # logger.debug("test debug")
    print(MyDateTime.now())
