name = input("请输入名字： \n")

if name == "gao fei":
    print(f"欢迎，{name}")
elif name == "tao tao":
    print("吃肉肉")
else:
    print("hello world")


age = int(input("请输入年龄： \n"))
if age >= 18:
    print("你已经成年了")
else:
    print("你还未成年")

# 练习：输入一个数字，判断这个数字是正数、负数还是零
num = float(input("请输入一个数字： \n"))
if num > 0:
    print("这个数字是正数")
elif num < 0:
    print("这个数字是负数")
else:
    print("这个数字是零")

# 练习：输入一个年份，判断这个年份是否是闰年
year = int(input("请输入一个年份： \n"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")
