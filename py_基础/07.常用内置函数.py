# map(
#   func: (_T1@__new__) -> _S@map,
#   iterable: Iterable[_T1@__new__], /, *,
#   strict: bool = False)
#   -> map[_S@map]
# 返回值是一个迭代器对象
nums = [0, 1, 2, 3, 4, 5]
nums2 = map(lambda x: x * 2, nums)

# map()的返回值是一个迭代器
print(nums2)  # <map object at 0x000001602734E700>

print(str(nums2))  # <map object at 0x0000026933E9E700>
print(list(nums2))  # [0, 2, 4, 6, 8, 10]

# 在list(nums2)之后，迭代器中的值已经全部取出，此时再遍历nums2结果为空
for num in nums2:
    print(num)


# filter(
#   function: None,
#   iterable: Iterable[_T@filter | None], /)
#   -> filter[_T@filter]
# 返回值是一个迭代器对象
nums3 = filter(lambda x: x > 2, nums)
print(nums3)  # <filter object at 0x0000014204737340>
print(list(nums3))  # [3, 4, 5]


from functools import reduce

# reduce(
#   function: (_T@reduce, _S@reduce) -> _T@reduce,
#   iterable: Iterable[_S@reduce], /,
#   initial: _T@reduce)
#   -> _T@reduce
#
sum = reduce(lambda x, y: x + y, nums, 3)
print(sum)  # 18

# print(
#   *values: object,
#   sep: str | None = " ",
#   end: str | None = "\n",
#   file: SupportsWrite[str] | None = None,
#   flush: Literal[False] = False)
#   -> None
# file  : 输出目标，默认sys.stdout
# flush : Python 输出通常先进入缓冲区，`flush=True` 立即将内容写入流，做实时输出。

import sys

print("abc", "def", sep="-", file=sys.stdout)
with open("print.txt", "w") as f:
    print("hello world", end="\nhaha\n", file=f)

import time

# 打印进度条 方法一
for _ in range(1, 21):
    print(".", end="", flush=True)
    time.sleep(0.3)
print()

# 打印进度条 方法二
# 转义字符 \r : (Carriage Return)光标回到当前行的行首。
for i in range(1, 21):
    print(f"\r进度：{i * 5}%", end="", flush=True)
    time.sleep(0.3)
