#coding=utf-8

""""这是文档字符串"""

# 文件编码：#coding=utf-8，必须放在py文件开始的地方，默认为utf-8
# 文档字符串

# 变量名区分大小写
userName = "gao fei"
UserName = "tao tao"
user_name = "wang jin fei"

print(userName, UserName, user_name)  # gao fei tao tao wang jin fei

# 常量
# python语法中没有常量，只有关于常量的约定，
# 即一个变量的标识符如果全是大写字母的话，就把它当做常量，只赋值一次
MAX_VALUE = 10
MAX_VALUE = 15
print(MAX_VALUE, MAX_VALUE)  # 15 15

"""
python中没有真正意义上的多行注释
多行注释实际上是多行字符串，
只是不把它赋值给标识符
"""

