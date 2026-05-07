"""
logging包
"""

import logging
from pathlib import Path

log_path = Path(__file__).resolve().parent / "logs" / "app.log"

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)-8.8s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(), logging.FileHandler(log_path, encoding="utf-8")],
)


def main():
    logger = logging.getLogger(__name__)
    logger.critical("this is a critical msg")

    # logger.exception(msg) 等价于 logger.error(msg, exc_info=True)，它的设计意图是在 except 块内自动记录当前异常信息。
    # 如果在没有活动异常时调用（即没有执行 except 块或在 try 之外），exc_info=True 会强制记录一个“空”的异常信息，输出显示为 NoneType: None。
    # 正确使用方法：只在 except 块内使用 logger.exception，让它自动捕获并打印当前异常的堆栈信息。
    try:
        x = 1 / 0
    except:
        logger.exception("this is a exception msg")

    logger.error("this is a error msg")
    logger.info("this is a info msg")
    logger.debug("this is a debug msg")

    import sub1
    import sub2

    sub1.run()
    sub2.run()


if __name__ == "__main__":
    main()
