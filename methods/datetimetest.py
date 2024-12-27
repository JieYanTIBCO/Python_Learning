import datetime
from setup_logging import get_logger

logger = get_logger()
if __name__ == "__main__":
    x = datetime.datetime.now()
    logger.debug(f"time is {x}")
    
    
    logger.debug(f"time %A is {x.strftime("%A")}")