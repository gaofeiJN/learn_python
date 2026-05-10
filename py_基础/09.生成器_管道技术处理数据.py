# 使用生成器组成管道处理数据


# 生成数字
def numbers(n):
    num = 0
    while num <= n:
        yield num
        num += 1


# 平方
def squares(source):
    for x in source:
        yield x**2


# 加1
def addone(source):
    for x in source:
        yield x + 1


nums = [x for x in addone(squares(numbers(9)))]
print(nums)  # [1, 2, 5, 10, 17, 26, 37, 50, 65, 82]
