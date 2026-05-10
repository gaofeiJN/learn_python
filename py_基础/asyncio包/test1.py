#

import asyncio


async def worker(x):
    print(f"worker-{x}开始执行")
    await asyncio.sleep(1 - x / 10)
    return x**2


async def test1():
    # create_task(
    #   coro: _CoroutineLike[_T@create_task], *,
    #   name: str | None = None,
    #   context: Context | None = None)
    #   -> Task[_T@create_task]

    # 创建一个task并将其放入事件循环
    task1 = asyncio.create_task(worker(1))
    task2 = asyncio.create_task(worker(2))
    task3 = asyncio.create_task(worker(3))
    task4 = asyncio.create_task(worker(4))
    task5 = asyncio.create_task(worker(5))

    # gather(
    #   coro_or_future1: _FutureLike[_T1@gather], /, *,
    #   return_exceptions: Literal[False] = False)
    #   -> Future[tuple[_T1@gather]]

    # 并发运行多个协程或 Task，返回结果列表
    results = await asyncio.gather(
        task1, task2, task3, task4, task5, return_exceptions=True
    )
    print(results)


async def test2():
    # gather(
    #   coro_or_future1: _FutureLike[_T1@gather], /, *,
    #   return_exceptions: Literal[False] = False)
    #   -> Future[tuple[_T1@gather]]

    # 并发运行多个协程或 Task，返回结果列表
    coroutines = [worker(i) for i in range(1, 6)]
    results = await asyncio.gather(*coroutines, return_exceptions=True)
    print(results)


async def test3():
    # as_completed(
    #   fs: Iterable[_FutureLike[_T@as_completed]], *,
    #   timeout: float | None = None)
    #   -> _SyncAndAsyncIterator[Future[_T@as_completed]]

    # 返回一个迭代器，每当有任务完成就立即产出结果，方便处理“谁先完成就先处理”的情形。
    tasks = [asyncio.create_task(worker(i)) for i in range(1, 6)]
    for t in asyncio.as_completed(tasks):
        result = await t
        print(result)


async def main():
    # await test1()
    # await test2()
    await test3()


# asyncio.run()
# 是最高层级的入口，只能调用一次，负责创建事件循环、运行协程、完成清理。
asyncio.run(main())
