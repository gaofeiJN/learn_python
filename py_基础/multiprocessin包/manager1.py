from multiprocessing import Process, Manager


def worker(wkdict, wklist, wkval):
    wkdict[wkval] = wkval**2
    wklist.append(wkval)


def main():
    # manager
    ma = Manager()

    # 创建共享内存
    shared_dict = ma.dict()
    shared_list = ma.list([0, 1, 2])

    # 创建子进程
    ps = []
    for x in range(10):
        ps.append(Process(target=worker, args=(shared_dict, shared_list, x)))

    # 启动子进程
    for p in ps:
        p.start()

    # 等待子进程结束
    for p in ps:
        p.join()

    # 结果
    print(shared_dict)
    print(shared_list)


if __name__ == "__main__":
    main()
