from multiprocessing import Process, Value, Array, Lock


def worker(name, v, a, l):
    """
    name: 子进程名字
    v: value
    a: array
    l: lock
    """
    for _ in range(1000):
        # 必须加锁！
        with l:
            v.value += 1

    for x in range(len(a)):
        # 必须加锁！
        with l:
            a[x] += 1


def main():
    # ctypes 类型：'i'=int, 'd'=double, 'c'=char
    v = Value("i", 0)
    a = Array("d", [1.0, 2.0, 3.0])

    l = Lock()

    # 创建子进程
    ps = []
    for x in range(10):
        ps.append(Process(target=worker, args=(f"sub-{x}", v, a, l)))

    # 启动子进程
    for p in ps:
        p.start()

    # 等待子进程结束
    for p in ps:
        p.join()

    #
    print(v.value)
    print(list(a))


if __name__ == "__main__":
    main()
