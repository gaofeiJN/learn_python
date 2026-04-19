# 整数
print("----整数---")
print(type(123))  # <class 'int'>
print(isinstance(123, int))  # True

print(123)
print(12_000_000_000)  # 对于较大的数字，可以使用下划线分隔 # 12000000000
print(0x10)  # 十六进制 # 16
print(0x1BDF_A091)  # 十六进制 # 46856961
print(0o10)  # 八进制 # 8
print(0b10010101)  # 二进制 # 149

print("----整数的除法运算---")
# 整数的除法运算会返回一个浮点数
print(10 / 3)  # 3.3333333333333335
# 整数的地板除法运算会返回一个整数，结果向下取整
print(10 // 3)  # 3
# 整数的取模运算会返回一个整数，结果是除法运算的余数
print(10 % 3)  # 1

print("----整数的幂运算---")
# 整数的幂运算会返回一个整数
print(2**3)  # 8

print("----整数的位运算---")
# 整数的位运算
print(0b1010 & 0b1100)  # 位与 # 0b1000 # 8
print(0b1010 | 0b1100)  # 位或 # 0b1110 # 14
print(0b1010 ^ 0b1100)  # 位异或 # 0b0110 # 6

# 位运算的优先级高于算术运算
# ~x 等价于数学公式 -x - 1（这个规则对所有整数都成立）
print(~0b1010)  # 位取反 # -0b1011 # -11

print(0b1010 << 2)  # 位左移 # 0b101000 # 40
print(0b1010 >> 2)  # 位右移 # 0b10 # 2


# 布尔值
# 布尔值只有两个：True和False
# 布尔值是整数的子类，True的值为1，False的值为0
print("----布尔值---")
print(type(True))  # <class 'bool'>
print(isinstance(True, bool))  # True
print(isinstance(True, int))  # True

print(True)  # True
print(False)  # False
print(True + True)  # 2
print(False + False)  # 0
print(True + False)  # 1
print(True * 10)  # 10
print(False * 10)  # 0
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(True or True)  # True
print(True or False)  # True
print(False or False)  # False
print(not True)  # False
print(not False)  # True

# 浮点数
print("----浮点数---")
print(type(3.14))  # <class 'float'>
print(isinstance(3.14, float))  # True

print(3.14)
print(1e-3)  # 科学计数法 # 0.001
print(1e6)  # 科学计数法 # 1000000.0
print(0.1 + 0.2)  # 浮点数的精度问题 # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # 浮点数的精度问题 # False

# 字符串
print("----字符串---")
print(type("hello world"))  # <class 'str'>
print(isinstance("hello world", str))  # True

print("hello world")
print("hello world")
print("hello 'world'")  # 字符串中包含单引号
print('hello "world"')  # 字符串中包含双引号
print("hello\nworld")  # 换行
print("hello\tworld")  # 制表符

# r-string 原始字符串，不会转义
print(r"hello\nworld")  # 原始字符串，不会转义
print("hello\\nworld")  # 转义字符，输出hello\nworld
print("hello\nworld")  # 转义字符，输出hello换行world

# f-string 格式化字符串 类似于javascript中的模板字符串
name = "gao fei"
age = 18
print(f"我的名字是{name}，今年{age}岁")  # 输出：我的名字是gao fei，今年18岁

# None
print("----None---")
print(None)  # None
print(type(None))  # <class 'NoneType'>
print(isinstance(None, type(None)))  # True

# type
# type是一个内置函数，用于返回对象的类型
# type也是一个元类，所有的类都是type的实例
print("----type---")
print(type(str))  # <class 'type'>
print(type(int))  # <class 'type'>
print(type(float))  # <class 'type'>
print(type(bool))  # <class 'type'>
print(type(None))  # <class 'NoneType'>
print(type(type))  # <class 'type'>
print(isinstance(str, type))  # True
print(isinstance(int, type))  # True
