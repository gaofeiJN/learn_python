from multiprocessing import Process, Pipe, current_process
from multiprocessing.connection import PipeConnection
import os


def subp1(cp: PipeConnection):
    print(f"sub process : {os.getpid()}, {current_process().name}")

    res = sum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)

    # 接收主进程的消息
    while True:
        msg = cp.recv()
        print(msg)
        if msg == "close":
            cp.send("子进程收到主进程的终止消息，正在关闭")
            break

    # 传回结果
    cp.send(res)


def test1():
    pp, cp = Pipe()
    subpro1 = Process(target=subp1, name="worker", args=(cp,))
    subpro1.start()

    print("主进程发送信息")
    pp.send("message from parent process : 1")
    pp.send("message from parent process : 2")
    pp.send("message from parent process : 3")

    # 发送终止消息
    pp.send("close")

    # 阻塞直到子进程结束
    subpro1.join()

    # 接收子进程发送的消息
    # 该方法会阻塞直到接收到消息
    print("主进程接收信息")
    res = pp.recv()
    print(res)
    res = pp.recv()
    print(res)


def main():
    test1()


if __name__ == "__main__":
    main()
