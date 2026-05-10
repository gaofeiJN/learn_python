import time
import os
from multiprocessing import Process, Queue


def worker(name: str, task: Queue, result: Queue):
    """
    name: 子进程名字
    task: 任务队列
    result: 结果队列
    """
    # 从任务队列获取任务
    while not task.empty():
        t = task.get()

        # 处理任务
        time.sleep(0.1)

        # 向结果队列中写入结果
        result.put(f"{name} 完成了任务: {t}")

    #
    result.put(f"{name} 完成了所有任务,正在关闭")


def test1():
    # 创建队列
    task = Queue()
    result = Queue()

    # 创建子进程
    processes = []
    for x in range(os.cpu_count()):
        p = Process(target=worker, args=(f"sub-{x}", task, result))
        p.start()
        processes.append(p)

    # 向任务队列中写入任务
    for x in range(os.cpu_count() * 5):
        task.put(f"task{x}")

    # 等待所有子进程结束
    for p in processes:
        p.join()

    # 从结果队列取出结果
    while not result.empty():
        res = result.get()
        print(res)


def main():
    test1()


if __name__ == "__main__":
    main()
