# 类变量：
# 直接定义在类体中的变量，被所有实例共享
# 实例变量：
# 在__init__方法中定义的变量，每个实例都有自己的副本，不共享
# 类变量和实例变量的区别：
# 类变量在类定义时创建，所有实例共享；实例变量在实例创建时创建，每个实例独立。
# 当访问一个变量时，Python会先查找实例变量，如果没有找到，再查找类变量，最后查找父类的类变量。
class Animal:
    species = "动物"  # 类变量

    def __init__(self, name):
        self.name = name  # 实例变量


class Dog(Animal):
    species = "狗"  # 类变量


class Cat(Animal):
    species = "猫"  # 类变量


class Bird(Animal):
    pass  # 没有定义species类变量，继承自Animal类的species类变量


dog1 = Dog("旺财")
dog2 = Dog("狗子")
cat1 = Cat("咪咪")
bird1 = Bird("小鸟")
print("---类变量和实例变量的区别---")
print(dog1.species)  # 狗
print(dog2.species)  # 狗
print(cat1.species)  # 猫
print(bird1.species)  # 动物
print(Dog.species)  # 狗
print(Animal.species)  # 动物

dog2.species = "小狗"  # 为dog2实例创建一个新的实例变量species，覆盖了类变量。查找顺序：实例变量 -> 类变量 -> 父类的类变量
print(dog1.species)  # 狗
print(dog2.species)  # 小狗


# 类方法：
# 使用@classmethod装饰器定义的方法，第一个参数是cls，表示类本身
# 类方法可以访问和修改类变量，但不能访问实例变量
# 类方法可以通过类名调用，也可以通过实例调用
class Person:
    population = 0  # 类变量，表示人口数量

    def __init__(self, name):
        self.name = name  # 实例变量，表示个人名字
        Person.population += 1  # 每创建一个实例，人口数量加1

    @classmethod
    def get_population(cls):
        return cls.population  # 返回当前人口数量


person1 = Person("Alice")
person2 = Person("Bob")
print("---类方法---")
print(Person.get_population())  # 2
print(person1.get_population())  # 2
print(person2.get_population())  # 2


# 静态方法：
# 使用@staticmethod装饰器定义的方法，没有默认参数，既不能访问类变量，也不能访问实例变量
# 静态方法通常用于一些与类相关但不需要访问类或实例数据的功能
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print("---静态方法---")
print(MathUtils.add(3, 5))  # 8
print(MathUtils.multiply(3, 5))  # 15


# 属性装饰器@property：
# 使用@property装饰器定义的方法，可以像访问属性一样访问方法，常用于实现只读属性或计算属性
# 类似于javascript中的getter和setter
class Circle:
    def __init__(self, radius):
        self._radius = radius  # 实例变量，表示圆的半径

    # area属性是一个计算属性，根据半径计算圆的面积
    # area属性是只读属性，不能直接赋值，如果需要设置area属性的值，可以定义一个setter方法来计算半径
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("半径不能为负数")
        self._radius = value

    @property
    def area(self):
        import math

        return math.pi * self._radius**2

    @area.setter
    def area(self, value):
        import math

        if value < 0:
            raise ValueError("面积不能为负数")
        self._radius = (value / math.pi) ** 0.5


# 特殊方法：
# 以双下划线开头和结尾的方法，Python内置的特殊方法，用于实现一些特殊的功能，如对象的字符串表示、对象的比较、对象的迭代等
# 常见的特殊方法有：
# __str__(self)：定义对象的字符串表示，使用print()函数打印对象时会调用这个方法
# __repr__(self)：定义对象的官方字符串表示，通常用于调试和开发，在交互式环境中直接输入对象时会调用这个方法
# __eq__(self, other)：定义对象的相等比较，使用==运算符比较对象时会调用这个方法
# __lt__(self, other)：定义对象的大小比较，使用<运算符比较对象时会调用这个方法
# __iter__(self)：定义对象的迭代器，使用for循环遍历对象时会调用这个方法
# __next__(self)：定义迭代器的下一个元素，使用next()函数获取迭代器的下一个元素时会调用这个方法
# __len__(self)：定义对象的长度，使用len()函数获取对象的长度时会调用这个方法
# __getitem__(self, key)：定义对象的索引访问，使用对象[key]访问对象时会调用这个方法
# __setitem__(self, key, value)：定义对象的索引赋值，使用对象[key] = value赋值时会调用这个方法
# __delitem__(self, key)：定义对象的索引删除，使用del对象[key]删除对象时会调用这个方法
# __call__(self, *args, **kwargs)：定义对象的可调用性，使用对象(*args, **kwargs)调用对象时会调用这个方法
# __enter__(self)：定义对象的上下文管理器，使用with语句管理对象时会调用这个方法
# __exit__(self, exc_type, exc_value, traceback)：定义对象的上下文管理器，使用with语句管理对象时会调用这个方法
# 通过定义这些特殊方法，可以让自定义的类具有类似于内置类型的行为，使得代码更加简洁和易读。
#
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


point1 = Point(1, 2)
point2 = Point(1, 2)
print("---特殊方法---")
print(point1)  # Point(1, 2)
print(repr(point1))  # Point(x=1, y=2)
print(point1 == point2)  # True


# 数据类：
# 使用@dataaclass装饰器定义的类，自动生成一些特殊方法，如__init__、__repr__、__eq__等，简化了类的定义和使用
from dataclasses import dataclass


@dataclass
class Square:
    side_length: float  # 定义一个属性，表示正方形的边长

    @property
    def area(self):
        return self.side_length**2  # 计算正方形的面积


square1 = Square(4)
print("---数据类---")
print(square1)  # Square(side_length=4)
print(square1.area)  # 16
print(repr(square1))  # Square(side_length=4)


# 抽象类和抽象方法

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def bark():
        pass


class Cat(Animal):
    def bark(self):
        print("喵--喵--")


print("---抽象类---")
cat1 = Cat()
cat1.bark()
