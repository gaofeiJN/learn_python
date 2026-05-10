# send(value) — 向生成器发送数据
def accumulator():
    total = 0
    while True:
        try:
            value = yield total  # yield返回一个值，并接收外部send的一个值
            total += value
        # except GeneratorExit:
        #     print("生成器关闭")
        except ZeroDivisionError:
            print("发生了除零错误")
            raise
        except BaseException:
            print("发生异常")
            raise


# 调用生成器函数，返回一个生成器
acc = accumulator()
acc.send(None)  # # 必须先启动到第一个 yield，等价于 next(acc)
print(acc.send(10))  # 10
print(acc.send(20))  # 30
print(acc.send(30))  # 60
# acc.close()

# close()
# GeneratorExit 不会向外传播到调用方，也不会打印任何 Traceback。
# 它只是告诉生成器“该结束了”，然后生成器正常终止。
# 如果调用方在 close() 之后继续做其他事，不会有任何异常信息。

# GeneratorExit
# 1. Python 在生成器暂停的 yield 处注入 GeneratorExit
# 2. 生成器中的 except GeneratorExit 捕获它，打印第一次 “生成器关闭”
# 3. 因为没有 raise，异常被“吞掉”，程序继续往下走
# 4. 执行 finally 块，打印第一次 “hello”
# 5. while True 循环继续，再次执行到 value = yield total
#    → 生成器再次暂停，试图交出值
#    → Python 检测到：生成器在 close() 过程中居然又 yield 了！
#    → 立即抛出 RuntimeError: generator ignored GeneratorExit
# 6. 生成器内没有捕获 RuntimeError，异常向上传播
# 7. 传播过程中再次触发 finally 块，打印第二次 “hello”
# 8. 调用方收到 RuntimeError，解释器输出错误信息

# throw(
#   typ: type[BaseException],
#   val: BaseException | object = None,
#   tb: TracebackType | None = None, /)
#   -> (Any | Literal[0])

acc.throw(ZeroDivisionError)
