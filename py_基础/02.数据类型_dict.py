# dict类型
# dict 是一个无序的、可变的、键值对的数据类型，使用大括号 {} 定义。
# dict 中的键必须是不可变类型，如数字、字符串、元组等，但不能是列表、字典等可变类型。
# dict 中的值可以是任意类型，可以是可变类型，也可以是不可变类型。
# dict 支持通过键访问对应的值，也支持添加、修改和删除键值对。

# 创建字典
#   - 字面量
#   - 构造函数
#       d2 = dict(name='Bob', age=25, city='Shanghai')  # 关键字参数
#       d3 = dict([('name', 'Charlie'), ('age', 35)])   # 从键值对序列
#       d4 = dict(zip(keys, values))                    # zip 组合
#   - dict.fromkeys(
#       iterable: Iterable[_T@fromkeys],
#       value: None = None, /)
#       -> dict[_T@fromkeys, Any | None]
#       批量创建相同值（值是可变对象时共享引用）
d1 = dict.fromkeys(["a", "b"], [])  # 两个键指向同一个列表！

# dict 的常用方法：
# get(key, default=None)：返回指定键 key 对应的值，如果键不存在则返回 default。


# keys()：返回一个包含 dict 中所有键的视图对象。
# values()：返回一个包含 dict 中所有值的视图对象。
# items()：返回一个包含 dict 中所有键值对的视图对象，每个键值对以元组的形式表示。


# update(other_dict)：将 other_dict 中的键值对添加到当前 dict 中，如果有重复的键，则覆盖原有的值。
# setdefault(key, default=None)：
#   如果键 key 不存在于 dict 中，则将 key 和 default 添加到 dict 中，并返回 default；
#   如果键 key 已经存在，则返回对应的值。

# pop(key, default=None)：删除 dict 中指定键 key 的键值对，并返回对应的值，如果键不存在则返回 default。
# popitem()：随机删除并返回 dict 中的一个键值对，以元组的形式表示，如果 dict 为空则引发 KeyError。

# clear()：清空 dict 中的所有键值对。

# dict 的常用操作：
# len(d)：返回 dict d 中键值对的个数。
# key in d：判断键 key 是否在 dict d 中。
# for key in d：遍历 dict d 中的键。

# dict 的赋值
my_dict = {"a": 1, "b": 2, "c": 3}
my_dict["d"] = 4  # 添加新的键值对
my_dict["a"] = 10  # 修改已有的键值对
# my_dict["e"] += 5  # 如果键 "e" 不存在，则会引发 KeyError
print(my_dict)  # 输出：{'a': 10, 'b': 2, 'c': 3, 'd': 4}


# collections 模块中的 defaultdict 类可以用来创建一个具有默认值的 dict，当访问不存在的键时会返回默认值，而不是引发 KeyError。
from collections import defaultdict

default_dict = defaultdict(int)  # 创建一个默认值为 0 的 defaultdict
default_dict["a"] += 1  # 访问不存在的键 "a"，会返回默认值 0，并将其加 1，结果为 1
print(default_dict)  # 输出：defaultdict(<class 'int'>, {'a': 1})
