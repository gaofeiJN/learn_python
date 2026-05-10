from multiprocessing import Process
from threading import Thread
import os
import time


def worker(name):
    print(f"{name}正在运行, pid: {os.getpid()}, 父进程: {os.getppid()}")
    sum = 0
    for x in range(10_000_000):
        sum += x**2
    print(f"{name}执行完毕")


def test1():
    # 单线程
    print("---单线程---")
    start = time.time()
    for x in range(os.cpu_count()):
        worker(f"func-{x}")
    print(f"---单线程--- {time.time()-start:8,.2f} s")  # 4.98 s

    # 多线程
    # 由于全局解释器锁GIL的限制，多线程不能加速cpu密集任务，由于线程切换开销反而可能需要更多时间
    print("---多线程---")
    start = time.time()
    ts = []
    for x in range(os.cpu_count()):
        t = Thread(target=worker, args=(f"Thread-{x}",))
        t.start()
        ts.append(t)

    for t in ts:
        t.join()

    print(f"---多线程--- {time.time()-start:8,.2f} s")  # 4.93 s

    # Process(
    #   group: None = None,
    #   target: ((...) -> object) | None = None,
    #   name: str | None = None,
    #   args: Iterable[Any] = (),
    #   kwargs: Mapping[str, Any] = {}, *,
    #   daemon: bool | None = None)
    #   -> Process
    # )
    print("---多进程---")
    start = time.time()
    ps = []
    for x in range(os.cpu_count()):
        p = Process(target=worker, args=(f"Worker-{x}",))
        p.start()
        ps.append(p)

    for p in ps:
        p.join()

    print(f"---多进程--- {time.time()-start:8,.2f} s")  # 1.22 s


def info(title):
    print("----------")
    print(f"{title} : {__name__}")
    print(f"parent process : {os.getppid()}")
    print(f"pid : {os.getpid()}")


# 子进程函数调用其他函数的例子
def subp2(name):
    info(name)
    print(f"hello world from {name}")


def test2():
    info("main process")

    p = Process(target=subp2, args=("sub process 1",))
    p.start()
    p.join()


# 主进程的代码要放到`if __name__ == "__main__"`代码块中，防止子进程也执行创建进程的命令
if __name__ == "__main__":
    # test1()
    test2()
