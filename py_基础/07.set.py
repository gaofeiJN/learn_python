# set 类型
# set 是一个无序的、可变的、不可重复的数据类型，使用大括号 {} 定义。
# set 中的元素必须是不可变类型，如数字、字符串、元组等，但不能是列表、字典等可变类型。
# set 支持数学上的集合操作，如交集、并集、差集等。

# set 的常用方法：
# add(elem)：向集合添加元素 elem。

# update(*others)：向集合添加多个元素，可以是一个可迭代对象或多个可迭代对象。
# 参数可以是一个可迭代对象，如列表、元组、集合等，也可以是多个可迭代对象，使用逗号分隔。
# list 中的元素会被逐个添加到集合中。
list_for_set = [1, 2, 3, 4]
set_from_list = set()
set_from_list.update(list_for_set)  # list 中的元素会被逐个添加到集合中。
print(set_from_list)  # 输出：{1, 2, 3, 4}

# set 中的元素会被直接添加到集合中，重复的元素会被自动去除。
# tuple 中的元素会被逐个添加到集合中，重复的元素会被自动去除。
# dict 中的元素会被逐个添加到集合中，重复的元素会被自动去除。dict中的键会被添加到集合中，值会被忽略。
# dict 中的键是不可变类型，可以作为集合的元素。值是可变类型，不能作为集合的元素。
dict_for_set = {"a": 1, "b": 2, "c": 3, "d": 4}
set_from_dict = set()
set_from_dict.update(dict_for_set)  # dict中的键会被添加到集合中，值会被忽略。
print(set_from_dict)  # 输出：{'d', 'b', 'a', 'c'}

# remove(elem)：从集合中删除元素 elem，如果 elem 不存在会引发 KeyError。
# discard(elem)：从集合中删除元素 elem，如果 elem 不存在不会引发错误。
# pop()：随机删除并返回集合中的一个元素，如果集合为空会引发 KeyError。
# clear()：清空集合中的所有元素。
# union(other_set)：返回当前集合与 other_set 的并集。
# intersection(other_set)：返回当前集合与 other_set 的交集。
# difference(other_set)：返回当前集合与 other_set 的差集。
# symmetric_difference(other_set)：返回当前集合与 other_set 的对称差集。

# set 的常用操作：
# len(s)：返回集合 s 中元素的个数。
# elem in s：判断元素 elem 是否在集合 s 中。
# for elem in s：遍历集合 s 中的元素。
