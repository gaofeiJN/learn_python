"""
守护进程：主进程结束后，守护进程也自动结束
"""

import os
import time
from multiprocessing import Process


def monitor():
    # 守护进程的代码放入一个无限循环中
    while True:
        try:
            with open("./log.txt", "r", encoding="utf-8") as f:
                lines = sum(1 for _ in f)
        except FileNotFoundError:
            lines = 0

        print(f"【子进程 {os.getpid()}】文件目前写入了{lines}行")
        time.sleep(1)


def main():
    # daemon=True : 守护进程，主进程结束后，守护进程也自动结束
    # 如果不指定daemon=True，则主进程代码执行结束后会等待子进程结束，而子进程是无限循环，从而导致主进程无法退出
    p1 = Process(target=monitor, daemon=True)
    p1.start()

    # 主进程：写入文件
    with open("./log.txt", "w", encoding="utf-8") as log:
        for x in range(10):
            log.write(f"第{x}行\n")

            # 使用flush()方法立刻将缓冲区的内容落盘
            log.flush()

            time.sleep(1)

    # 不要对无限循环的守护进程调用 p1.join()

    print("【主进程】代码结束")


if __name__ == "__main__":
    main()
