# 创建列表
# - 字面量
# - 构造函数 从可迭代对象创建
# - 列表推导式
# - 乘法初始化（注意浅拷贝问题）
print("---创建列表---")
lst1: list = [1, 2, 3, 4]
lst2: list = list("hello")  # ['h', 'e', 'l', 'l', 'o']
lst3: list = [x**2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]
lst4: list = [1] * 5  # [1, 1, 1, 1, 1]
lst5: list = [[0]] * 3  # [[0], [0], [0]]
lst5[0].append(1)  # [[0, 1], [0, 1], [0, 1]]

print(lst1)
print(lst2)
print(lst3)
print(lst4)
print(lst5)

# 索引和切片
# list[start:stop:step]
# [start,stop)
# 当 step 为正数时，切片从左向右（索引递增方向）选取元素；
# 当 step 为负数时，切片从右向左（索引递减方向）选取元素，并且要求 起始索引 start 必须大于结束索引 stop 才能取到元素。
print("---索引和切片---")
print(lst1[0:-1])  # [1, 2, 3]
print(lst1[-1:0:-1])  # [4, 3, 2]
print(lst1[::-1])  # [4, 3, 2, 1] # 相当于lst1.reverse()
lst1.reverse()  # 原地反转
print(lst1)  # [4, 3, 2, 1]
lst1.sort(reverse=True)  # 根据值的降序排序，和list.reverse()方法不同
print(lst1)
print(sorted(lst1, reverse=True))  # 根据值的降序排序，和list.reverse()方法不同


# 元素的增删改查
lst6: list = [0, 1, 2, 3, 4, 5, 6]
# 插入元素
# list.append(arg) 末尾插入一个元素
# list.extend(arg) 末尾合并另一个列表或可迭代对象，相当于 list += list(arg)
# 列表合并运算符 list + iterable
# list.insert(index,value) 在指定位置插入元素
print("---增删改查---")
lst6.append(7)
lst6.extend([8, 9])
lst6.extend("abc")
lst6 += "def"
lst6 += list("ghi")
lst6.insert(2, "third")
print(
    lst6
)  # [0, 1, 'third', 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

# 删除元素
# list.clear() 清空列表
# list.pop(index) 从指定位置取出元素并将其删除，返回取出的元素，修改原列表
# list.pop() 从末尾取出元素并将其删除，返回取出的元素，修改原列表
# del list[idx]
# del list[start:stop:step]
# list.remove(value) 按值删除（第一个匹配的）
pop1 = lst6.pop(2)
pop2 = lst6.pop()
del lst6[0]
del lst6[0:5:2]
lst6.remove("d")
print(pop1)
print(pop2)
print("lst6=", lst6)  # [2, 4, 6, 7, 8, 9, 'a', 'b', 'c', 'e', 'f', 'g', 'h']

lst7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# del lst7[:] # 清空列表 lst7= []
# del lst7[::-1]  # 清空列表 lst7= []
# del lst7[::2]  # 按照索引递增方向删除，步长为2 lst7= [1, 3, 5, 7, 9]
# del lst7[::-2]  # 按照索引递减方向删除，步长为2 lst7= [0, 2, 4, 6, 8]
# del lst7[2:7:2]  # 按照索引递增方向删除，步长为2 lst7= [0, 1, 3, 5, 7, 8, 9]
del lst7[7:2:-2]  # 按照索引递减方向删除，步长为2 lst7= [0, 1, 2, 4, 6, 8, 9]
print("lst7=", lst7)

# collection.deque
# popleft() 从头部取出元素并将其删除，返回取出的元素，修改原队列
from collections import deque

que8: deque = deque([0, 1, 2, 3, 4, 5])
pop3 = que8.popleft()
print("pop3=", pop3)  # pop3= 0
print("que8=", que8)  # que8= deque([1, 2, 3, 4, 5])


# 查询
# len(list)
# x in list
# list.index(value)
# list.index(value,start,stop)
lst9: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("index ", lst9.index(2))
print("index ", lst9.index(3, 0, 7))


# 排序
# list.sort(key,reverse)
# sorted(iterable,key,reverse) 返回新列表，不修改原列表
# key参数可传入一个函数，用以指定排序的“比较键”

# list.reverse() 原地反转

print("---排序---")
lsta: list = [5, 4, 6, 8, 3, 2, 9, 1, 0]
lsta.reverse()
print("list.reverse() ", lsta)  # [0, 1, 9, 2, 3, 8, 6, 4, 5]
lsta.sort(key=None, reverse=True)
print("list.sort(key=None,reverse=True) ", lsta)  # [9, 8, 6, 5, 4, 3, 2, 1, 0]

lstb = sorted(lsta, key=lambda x: -x, reverse=True)
print("lstb =", lstb)  # [0, 1, 2, 3, 4, 5, 6, 8, 9]

lstc = ["abc", "a", "B", "c", "def", "HELLO", "DE"]
lstc.sort(key=len)  # 先按长度从小到大排序
lstc.sort(key=str.lower)  # 再按字母序排序，不区分大小写
print("lstc =", lstc)  # ['a', 'abc', 'B', 'c', 'DE', 'def', 'HELLO']
print(sorted(lstc))  # ['B', 'DE', 'HELLO', 'a', 'abc', 'c', 'def']


# 列表推导式
# **基本结构**：`[表达式 for 变量 in 可迭代对象 if 条件]`
# 列表推导式会直接生成整个列表，注意内存占用。
# 对于非常大的数据，可考虑生成器表达式（`()` 代替 `[]`），按需产生值。
print("---列表推导式---")
# 嵌套循环（笛卡尔积）
lstd = [(x, y) for x in "ab" for y in "12"]

# 多条件与if-else（注意位置不同）
lste = [x if x > 0 else 0 for x in [-1, 3, -2, 5]]

print("lstd =", lstd)  # lstd = [('a', '1'), ('a', '2'), ('b', '1'), ('b', '2')]
print("lste =", lste)  # lste = [0, 3, 0, 5]

# 生成器表达式
lstf = []
for item in (x**2 for x in range(5)):
    lstf.append(item)
print("lstf =", lstf)  # lstf = [0, 1, 4, 9, 16]

# 多重条件
# lstg = [x for x in range(100) if x % 3 == 0 and x % 5 == 0]  # 既能被 3 整除又能被 5 整除
lstg = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]  # 既能被 3 整除又能被 5 整除
print("lstg =", lstg)  # lstg = [0, 15, 30, 45, 60, 75, 90]

# 推导式嵌套
# 矩阵转置
matrix = [[1, 2, 3], [4, 5, 6]]
lsth = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("lsth =", lsth)  # lsth = [[1, 4], [2, 5], [3, 6]]


# 赋值列表：浅拷贝与深拷贝
# 浅拷贝：
#   - new = old.copy()
#   - new = list(old)
#   - new = old[:]
#   新列表中的元素仍然是原元素的引用（对于可变对象，修改内部状态会相互影响）
# 深拷贝：
#   - new = copy.deepcopy(old)
print("---浅拷贝和深拷贝---")
lsti = [0, 1, 2, [3, 4, 5]]

lstj0 = lsti
lstj0[0] = "a"

lstj1 = lsti.copy()
lstj1[0] = "b"
lstj1[3].append(6)

lstj2 = list(lsti)
lstj2[0] = "c"
lstj2[3].append(7)

import copy

lstj3 = copy.deepcopy(lsti)
lstj3[0] = "d"
lstj3[3].append(8)
print("lsti =", lsti)  # lsti = ['a', 1, 2, [3, 4, 5, 6, 7]]
print("lstj0 =", lstj0)  # lstj0 = ['a', 1, 2, [3, 4, 5, 6, 7]]
print("lstj1 =", lstj1)  # lstj1 = ['b', 1, 2, [3, 4, 5, 6, 7]]
print("lstj2 =", lstj2)  # lstj2 = ['c', 1, 2, [3, 4, 5, 6, 7]]
print("lstj3 =", lstj3)  # lstj3 = ['d', 1, 2, [3, 4, 5, 6, 7, 8]]

# 多列表并行遍历
print("---多列表并行遍历---")
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
# Alice: 25
# Bob: 30


# 内置函数
# filter(function: None, iterable: Iterable[_T@filter | None], /) -> filter[_T@filter]
print("---内置函数---")
lstk = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lstl = list(filter(lambda x: x % 2 == 0, lstk))
print("lstl =", lstl)  # lstl = [0, 2, 4, 6, 8]

# map(func: (_T1@__new__, _T2@__new__) -> _S@map,
#     iterable: Iterable[_T1@__new__],
#     iter2: Iterable[_T2@__new__], /, *,
#     strict: bool = False)
#     -> map[_S@map]
lstm = list(map(lambda x: x + 2, lstk))
print("lstm =", lstm)  # lstm = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# reduce(function: (_T@reduce, _S@reduce) -> _T@reduce,
#        iterable: Iterable[_S@reduce], /,
#        initial: _T@reduce) -> _T@reduce
from functools import reduce

rdc = reduce(lambda x, y: x + y, lstk, 10)
print("rdc =", rdc)  # rdc = 55


# all / any 逻辑运算
print(all([True, 1, "a"]))  # True（所有为真）
print(any([False, 0, ""]))  # False（全为假）
