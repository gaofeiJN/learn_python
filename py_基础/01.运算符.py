#!/usr/bin/env python3


# 布尔运算符
def bool_demo():
    # 布尔运算 or 和 and 会返回操作数
    # x or y : x为真则返回x，否则返回y
    print("-----布尔预算： x or y-----")
    print("True or False:", True or False)  # 输出: True
    print("False or True:", False or True)  # 输出: True
    print("False or False:", False or False)  # 输出: False

    print("'' or 'hello':", "" or "hello")  # 输出: 'hello'
    print("0 or 42:", 0 or 42)  # 输出: 42
    print("None or 'default':", None or "default")  # 输出: 'default'
    print("[] or [1, 2, 3]:", [] or [1, 2, 3])  # 输出: [1, 2, 3]

    # x and y : x为假值则返回x，否则返回y
    print("-----布尔预算： x and y-----")
    print("True and False:", True and False)  # 输出: False
    print("False and True:", False and True)  # 输出: False
    print("False and False:", False and False)  # 输出: False

    print("'' and 'hello':", "" and "hello")  # 输出: ''
    print("0 and 42:", 0 and 42)  # 输出: 0
    print("None and 'default':", None and "default")  # 输出: None
    print("[] and [1, 2, 3]:", [] and [1, 2, 3])  # 输出: []

    # not x : x为假值则返回True，否则返回False
    print("-----布尔预算： not x -----")
    print("not True:", not True)  # 输出: False
    print("not False:", not False)  # 输出: True

    print("not 'hello':", not "hello")  # 输出: False
    print("not '':", not "")  # 输出: True
    print("not 42:", not 42)  # 输出: False
    print("not 0:", not 0)  # 输出: True
    print("not None:", not None)  # 输出: True
    print("not []:", not [])  # 输出: True


# 比较运算符
def compare_demo():
    print("-----比较运算符-----")

    # >
    # >=
    # <
    # <=
    # ==
    # !=
    # is : 对象标识
    # is not : 否定的对象标识

    # 对象相等的比较 ： 具有不同标识的类的实例比较结果通常为不相等，除非类定义了 __eq__() 方法。

    # 对象的排序 ：
    # 一个类的实例不能与相同类的其他实例或其他类型的对象进行排序，除非定义该类定义了足够多的方法，
    # 包括 __lt__(), __le__(), __gt__() 以及 __ge__()
    # (而如果你想实现常规意义上的比较操作，通常只要有 __lt__() 和 __eq__() 就可以了)。


# in运算符
# in, not in
# 它们被 iterable 或实现了 __contains__() 方法的类型所支持。
def in_demo():
    print("-----in运算符-----")
    t = (1, 2, 3)
    s = "hello world"
    l = ["jinan", "beijing", "hanzhou"]
    a = set([1, 3, 5, 5, 3, 7, 9])

    print(1 in t)  # 输出：True
    print(9 in t)  # 输出：Fasle
    print("z" not in s)  # 输出：True
    print("xian" in l)  # 输出：Fasle
    print(11 in a)  # 输出：Fasle


# 其他运算符


if __name__ == "__main__":
    # bool_demo()
    compare_demo()
    in_demo()
