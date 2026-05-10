# 手写for循环
lsta = [0, 1, 2, 3, 4, 5, 6, 7]

# 获取迭代器Iterator
it = iter(lsta)

# 循环调用迭代器的__next__方法，直到捕捉到StopIteration异常
print("---手写for循环---")
while True:
    try:
        val = next(it)
        print(val)
    except StopIteration:
        break

# 判断是否为可迭代对象，迭代器对象
from collections.abc import Iterable, Iterator

print("---判断是否为可迭代对象，迭代器对象---")
print(f"isinstance(lsta,Iterable) ： {isinstance(lsta,Iterable)}")
print(f"isinstance(it,Iterator) ： {isinstance(it,Iterator)}")


# 自定义迭代器，可迭代对象
class MyIterator:
    def __init__(self, data: MyIterable):
        self.data = data
        self.count = data.num

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.count -= 1
            return self.data.data[self.count]
        else:
            raise StopIteration


class MyIterable:
    def __init__(self, num):
        self.num = num
        self.data = []
        for x in range(num):
            self.data.append(x**2)

    def __iter__(self):
        return MyIterator(self)


print("---自定义迭代器，可迭代对象---")
mydata = MyIterable(9)
myiter = mydata.__iter__()

while True:
    try:
        val = myiter.__next__()
        print(val)
    except StopIteration:
        import traceback

        print(traceback.format_exc())
        break
