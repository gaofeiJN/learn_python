var1 = "gao fei"
var2 = 39
p1 = {"name": "gao fei", "age": 39, "city": "jinan"}


class Dog:
    def __init__(self):
        self.name = "狗子"
        self.tail = True

    def bark(self):
        print("wang wang!")


def test():
    pass


def main():
    puppy = Dog()
    puppy.bark()

    var3 = var1 + str(var2)
    print(p1)
    print(var3)

    i = 6

    assert i > 0, "i <= 0 !"

    assert p1["age"] > 40, f"{p1}的年龄不到40岁"


if __name__ == "__main__":
    main()
