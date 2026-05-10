"""
ProcessPoolExcutor 提供基于Future的任务管理，将任务提交和结果获取解耦
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import os, math, time


def func1(val):
    print(f"【子进程 {os.getpid()}】开始计算 {val}")
    time.sleep(0.1)

    # val < 0 时抛出异常
    if val < 0:
        raise ValueError(f"负数{val}无实根")
    else:
        return (val, math.sqrt(val), os.getpid())


def add(x: int, y: int) -> tuple[int, int, int, int]:
    print(f"【子进程 {os.getpid()}】开始计算 {x} + {y}")
    time.sleep(0.1)

    return (x, y, x + y, os.getpid())


def test1():
    # 创建ProcessPoolExecutor
    # ProcessPoolExecutor(
    #   max_workers: int | None = None,
    #   mp_context: BaseContext | None = None,
    #   initializer: (() -> object) | None = None,
    #   initargs: tuple[()] = (), *,
    #   max_tasks_per_child: int | None = None)
    #   -> ProcessPoolExecutor

    #   max_workers : 默认值为os.cpu_count()
    #   initializer : 每个工作进程启动时执行的初始化函数
    #   initargs    : 初始化函数的参数
    exec = ProcessPoolExecutor()

    # 提交任务
    # submit(
    #   fn: (**_P@submit) -> _T@submit, /,
    #   **_P@submit)
    #   -> Future[_T@submit]
    # )

    # 返回一个Future对象
    f = exec.submit(func1, -16)

    # Future的方法
    # | 方法                       | 说明                                                          |
    # | ------------------------- | ------------------------------------------------------------  |
    # | `result(timeout=None)`    | 返回任务结果；若任务尚未完成则阻塞等待；若任务抛出异常，则重新引发该异常。  |
    # | `exception(timeout=None)` | 返回任务抛出的异常（如果有），否则返回 `None`；不会重新引发异常。        |
    # | `add_done_callback(fn)`   | 添加一个回调函数，当任务完成时调用 `fn(future)`，回调在添加时的进程/线程中执行。 |
    # | `cancel()`                | 尝试取消任务。如果任务尚未开始执行，可能取消成功并返回 `True`；否则返回 `False`。已开始的任务无法取消。 |
    # | `done()`                  | 返回布尔值，表示任务是否已完成（正常完成或被取消）。                    |
    # | `running()`               | 返回布尔值，表示任务是否正在执行（不应依赖此方法做精确判断）。            |

    # 获取结果与异常处理
    try:
        orig, root, pid = f.result()
        print(f"sqrt({orig}) = {root:.2f} (PID: {pid})")
    except ValueError as e:
        print(f"ValueError : {e}")


def test2():
    # 创建ProcessPoolExecutor
    exec = ProcessPoolExecutor()

    # 提交任务
    origs = [0, 1, 7, 8, -12, 9, 16, -122, 256, 300]
    tasks = [exec.submit(func1, x) for x in origs]

    # 获取结果与异常处理
    # as_completed(fs, timeout=None)：
    # 返回一个迭代器，每当有 Future 完成时就产生该 Future，方便处理“谁先完成就先处理”的场景。
    for task in as_completed(tasks):
        try:
            orig, root, pid = task.result()
            print(f"sqrt({orig}) = {root:.2f} (PID: {pid})")
        except ValueError as e:
            print(f"ValueError : {e}")


def test3():
    # 创建ProcessPoolExecutor
    exec = ProcessPoolExecutor()

    # 提交任务
    origs = [0, 1, 7, 8, -12, 9, 16, -122, 256, 300]
    tasks = [exec.submit(func1, x) for x in origs]

    # 获取结果与异常处理
    # shutdown(
    #   wait: bool = True, *,
    #   cancel_futures: bool = False)   # 值为True时，关闭所有还没执行的任务
    #   -> None

    # 一旦执行 `shutdown`，不能再提交新任务；否则引发 `RuntimeError`
    # `wait=True`（默认）：会阻塞直到所有已提交任务执行完毕
    # `cancel_futures=True`：取消所有尚未开始执行的任务
    exec.shutdown()
    for task in tasks:
        try:
            orig, root, pid = task.result()
            print(f"sqrt({orig}) = {root:.2f} (PID: {pid})")
        except ValueError as e:
            print(f"ValueError : {e}")


def test4():
    # 创建ProcessPoolExecutor
    exec = ProcessPoolExecutor()

    # 提交任务
    # map(
    #   fn: (...) -> _T@map,
    #   *iterables: Iterable[Any],
    #   timeout: float | None = None,
    #   chunksize: int = 1,
    #   buffersize: int | None = None)
    #   -> Iterator[_T@map]

    # 立即返回一个迭代器，惰性地产生结果，保持输入顺序。

    x = [0, 2, 4, 6, 8, 10]
    y = [1, 2, 3, 4, 5, 6]
    results = exec.map(add, x, y)

    # 获取结果
    for res in results:
        x, y, sum, pid = res
        print(f"{x:2d} + {y:2d} = {sum:2d} (PID: {pid:6d})")


def main():
    # test1()
    # test2()
    test3()
    # test4()


if __name__ == "__main__":
    main()
