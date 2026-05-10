# 使用yield from和递归对可迭代对象进行扁平化处理
from collections.abc import Iterable


def flatten(nested):
    for item in nested:
        if isinstance(item, Iterable):
            if isinstance(item, str):
                yield item
            else:
                yield from flatten(item)
        else:
            yield item


lsta = [
    0,
    [1, [2, [3, [4, [5, 6]]]]],
    [7, 8, 9],
    "a",
    "b",
    "hello",
    ["world", (10, 20, 30)],
]

gener = flatten(lsta)
flattened = [x for x in gener]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'hello', 'world', 10, 20, 30]
print(flattened)
