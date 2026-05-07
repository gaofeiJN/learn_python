import logging.config
import json

with open("logging.json", "r") as f:
    config = json.load(f)
    logging.config.dictConfig(config)

# 使用
logger = logging.getLogger(__name__)
logger.debug("调试信息")
logger.info("普通信息")
logger.warning("警告信息")
