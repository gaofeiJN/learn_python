from multiprocessing import Pool
import os
import time


def func(x):
    print(f"进程{os.getpid():6d}正在运行: func({x})")
    time.sleep(0.1)
    return x**2


def add(x, y):
    print(f"进程{os.getpid():6d}正在运行: add({x},{y})")
    time.sleep(0.1)
    return x + y


if __name__ == "__main__":
    lsta = list(range(20))
    lstb = [x**2 for x in lsta]
    lstc = list(zip(lsta, lstb))

    with Pool(5) as p:
        # map(阻塞，有序返回)
        print("---map---")
        res = p.map(func, lsta)
        print(res)

        # imap(惰性迭代，有序返回)
        print("---imap---")
        for res in p.imap(func, lsta):
            print(res)

        # imap_unordered(惰性迭代，谁先完成谁先返回)
        print("---imap_unordered---")
        for res in p.imap_unordered(func, lsta):
            print(res)

        # apply_async(异步提交单个任务)
        print("---apply_async---")
        res = p.apply_async(func, (12,))
        print(res.get())

        # starmap(多参数)
        print("---starmap---")
        res = p.starmap(add, lstc)
        print(res)
