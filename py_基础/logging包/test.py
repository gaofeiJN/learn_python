import logging
from pathlib import Path

log_path = Path(__file__).resolve().parent / "app.log"

# 创建 logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)-8.8s - %(name)s - %(message)s"
)

# 创建控制台 handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# 创建文件 handler
# file_handler = logging.FileHandler(log_path, encoding="utf-8")
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

logger.debug("这条只会写到文件")
logger.info("这条同时显示在控制台和文件")
