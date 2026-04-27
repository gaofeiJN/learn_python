#!/usr/bin/env python

import argparse

# 创建解析器
parser = argparse.ArgumentParser(description='第一个python cli工具')

# 添加参数
# 位置参数，必须
parser.add_argument("name",help='输入名字')

# 选项参数，可选
parser.add_argument("-a","--age",type=int,help="你的年龄")

# 解析参数
args = parser.parse_args()

print("hello,",args.name)
print("你的年龄是",args.age)