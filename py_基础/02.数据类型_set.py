# set 类型
# set 是一个无序的、可变的、不可重复的数据类型，使用大括号 {} 定义。
# set 中的元素必须是不可变类型，如数字、字符串、元组等，但不能是列表、字典等可变类型。
# set 支持数学上的集合操作，如交集、并集、差集等。

# 创建集合
#   - 字面量 注意{}为字典，不是集合
#   - set()，frozenset()构造函数
#   - 集合推导式 {表达式 for 变量 in 可迭代对象 if 条件}
set1: set = {1, 2, 2, 3, 4}
set2: set = set("hello")
set3: set = frozenset([0, 1, 2, 2, 3, 3, 4])
print("---创建集合---")
print(f"set1 = {set1}")  # set1 = {1, 2, 3, 4}
print(f"set2 = {set2}")  # set2 = {'e', 'o', 'h', 'l'}
print(f"set3 = {set3}")  # set3 = frozenset({0, 1, 2, 3, 4})

# 添加元素
# `add(element)`: 添加单个元素
# `update(iterable)`: 添加多个元素，参数可以是列表、元组、集合等。
set1.add(5)
set2.update("world")
print("---添加元素---")
print(f"set1 = {set1}")  # set1 = {1, 2, 3, 4, 5}
print(f"set2 = {set2}")  # set2 = {'l', 'h', 'o', 'e', 'r', 'd', 'w'}

# set 中的元素会被直接添加到集合中，重复的元素会被自动去除。
# tuple 中的元素会被逐个添加到集合中，重复的元素会被自动去除。
# dict 中的元素会被逐个添加到集合中，重复的元素会被自动去除。dict中的键会被添加到集合中，值会被忽略。
# dict 中的键是不可变类型，可以作为集合的元素。值是可变类型，不能作为集合的元素。
dict_for_set = {"a": 1, "b": 2, "c": 3, "d": 4}
set_from_dict = set()
set_from_dict.update(dict_for_set)  # dict中的键会被添加到集合中，值会被忽略。
print(set_from_dict)  # 输出：{'d', 'b', 'a', 'c'}

# 删除元素
# remove(element)：从集合中删除元素 element， element 不存在会引发 KeyError。
# discard(element)：从集合中删除元素 element， element 不存在不会引发错误。
# pop()：随机删除并返回集合中的一个元素，如果集合为空会引发 KeyError。
# clear()：清空集合中的所有元素。
# set1.remove(0) # KeyError: 0
set1.remove(1)
set2.discard("a")  # 不报错
set2.discard("o")
val = set2.pop()
print("---删除元素---")
print(f"set1 = {set1}")  # set1 = {2, 3, 4, 5}
print(f"set2 = {set2}")  # set2 = {'w', 'r', 'l', 'e', 'h'}
print(f"val = {val}")  # val = d

# 集合运算
# union(other_set)：返回当前集合与 other_set 的并集。
# intersection(other_set)：返回当前集合与 other_set 的交集。
# difference(other_set)：返回当前集合与 other_set 的差集。
# symmetric_difference(other_set)：返回当前集合与 other_set 的对称差集，即两个集合中不重复的元素（去掉交集）。
seta: set = {1, 2, 3, 4, 5, 6}
setb: set = {3, 4, 7, 8}
setc1 = seta | setb
setc2 = seta.union(setb)
setc3 = seta & setb
setc4 = seta.intersection(setb)
setc5 = seta - setb
setc6 = seta.difference(setb)
setc7 = seta ^ setb
setc8 = seta.symmetric_difference(setb)
print("---集合运算---")
print(f"setc1 = {setc1}")  # {1, 2, 3, 4, 5, 6, 7, 8}
print(f"setc2 = {setc2}")  # {1, 2, 3, 4, 5, 6, 7, 8}
print(f"setc3 = {setc3}")  # {3, 4}
print(f"setc4 = {setc4}")  # {3, 4}
print(f"setc5 = {setc5}")  # {1, 2, 5, 6}
print(f"setc6 = {setc6}")  # {1, 2, 5, 6}
print(f"setc7 = {setc7}")  # {1, 2, 5, 6, 7, 8}
print(f"setc8 = {setc8}")  # {1, 2, 5, 6, 7, 8}

# 原地修改版本
# seta |= setb  # seta.update(setb)
# seta &= setb  # seta.intersection_update(setb)
# seta -= setb  # seta.difference_update(setb)
# seta ^= setb  # seta.symmetric_difference_update(setb)

# 关系判断
# A.issubset(B)    : 判断A是否是B的子集
# A.issuperset(B)  : 判断A是否是B的超集
# A.isdisjoint(B)  : 判断两个集合是否没有交集
setd1 = {1, 2, 3, 4}
setd2 = {1, 2, 3, 4}
setd3 = {1, 2, 3, 4, 5, 6}
setd4 = {5, 6, 7, 8}
print("---关系判断---")
print(f"setd1.issubset(setd2) : {setd1.issubset(setd2)}")  # True
print(f"setd1 <= setd2 : {setd1<=setd2}")  # True
print(f"setd1 < setd2 : {setd1<setd2}")  # 真子集 # False
print(f"setd1 < setd3 : {setd1<setd3}")  # 真子集 # True
print(f"setd3.issuperset(setd1) : {setd3.issuperset(setd1)}")  # True
print(f"setd3 >= setd1 : {setd3>=setd1}")  # True
print(f"setd3 > setd1 : {setd3>setd1}")  # 真超集 # True
print(f"setd2 > setd1 : {setd2>setd1}")  # 真超集 # False
print(f"setd1.isdisjoint(setd4) : {setd1.isdisjoint(setd4)}")  # 没有交集 # True


# set 的常用操作：
# len(s)：返回集合 s 中元素的个数。
# elem in s：判断元素 elem 是否在集合 s 中。
# for elem in s：遍历集合 s 中的元素。

# 集合和列表的效率对比
import time

print("---集合和列表的效率对比---")

# 成员检测：集合 O(1) vs 列表 O(n)
big_list = list(range(1000000))
big_set = set(big_list)

# 列表查找（慢）
start = time.time()
999999 in big_list  # 0.00938058s ~10ms
print(f"列表: {time.time() - start:.8f}s")

# 集合查找（快）
start = time.time()
999999 in big_set  # 0.00000167s ~0.001ms
print(f"集合: {time.time() - start:.8f}s")
