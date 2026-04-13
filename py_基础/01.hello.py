name = "gao fei"
age = 39
city = "jinan"


def say_hello():
    print("hello world,", name, "at age of ", age, "years old,lives in city ", city)


say_hello()


# 取得当前系统时间并格式化
import time

current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("当前系统时间：", current_time)

# 计算传入的两个整数的和
def sums(int1: int, int2: int) -> int:
    return int1 + int2

print(sums(1, 2))