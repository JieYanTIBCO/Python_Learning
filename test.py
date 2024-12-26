import setup_logging as sl
import logging

sl.setup_logging()
logger = logging.getLogger(__name__)

logger.info("test")